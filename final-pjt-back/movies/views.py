from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie, Vote
from .serializers import MovieListSerializer, MovieDetailSerializer, VoteSerializer
from rest_framework import status
import random
from pprint import pprint
# Create your views here.

@api_view(['GET'])
# 장르별로 10개나 20개정도 주는거어때?
# 액션(1), 애니메이션(3), 코미디(4), 드라마(7), 공포(11), 로맨스(14)
# [0:10]     [10:20]      [20:30]    [30:40]   [40:50]  [50:60]
def movie_list(request):
    movies1 = Movie.objects.filter(genre_ids=1)
    serializer1 = MovieListSerializer(movies1, many=True)
    movies2 = Movie.objects.filter(genre_ids=3)
    serializer2 = MovieListSerializer(movies2, many=True)
    movies3 = Movie.objects.filter(genre_ids=4)
    serializer3 = MovieListSerializer(movies3, many=True)
    movies5 = Movie.objects.filter(genre_ids=7)
    serializer5 = MovieListSerializer(movies5, many=True)
    movies6 = Movie.objects.filter(genre_ids=11)
    serializer6 = MovieListSerializer(movies6, many=True)
    movies7 = Movie.objects.filter(genre_ids=14)
    serializer7 = MovieListSerializer(movies7, many=True)

    return Response({ 
        'actions' : random.sample(serializer1.data,10),
        'animations' : random.sample(serializer2.data,10),
        'comedys' : random.sample(serializer3.data,10),
        'dramas' : random.sample(serializer5.data,10),
        'horrors' : random.sample(serializer6.data,10),
        'romances' : random.sample(serializer7.data,10),
     })
    # return Response(random.sample(serializer1.data,10)+random.sample(serializer2.data,10)+random.sample(serializer3.data,10)+random.sample(serializer5.data,10)+random.sample(serializer6.data,10)+random.sample(serializer7.data,10))

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)

@api_view(['POST'])
def create_vote(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    user = request.user
    print(request.data)
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