from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie, Vote
from .serializers import MovieListSerializer, MovieDetailSerializer, VoteSerializer
from rest_framework import status
# Create your views here.

@api_view(['GET'])
# 장르별로 10개나 20개정도 주는거어때?
# 액션, 애니메이션, 코미디, 다큐멘터리, 드라마, 공포, 로맨스
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)

@api_view(['POST'])
def create_vote(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    user = request.user
    serializer = VoteSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=user, movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['DELETE', 'PUT'])
def update_or_delete_vote(request, movie_pk, vote_pk):
    vote = Vote.objects.get(pk=vote_pk)
    
    if request.method=='DELETE':
        vote.delete()
        data = {
            "delete": f"vote {vote_pk} is deleted"
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method=='PUT':
        serializer = VoteSerializer(vote, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)