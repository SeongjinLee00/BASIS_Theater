from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie, Vote
from .serializers import MovieListSerializer, MovieDetailSerializer, VoteSerializer
from rest_framework import status
import random
from pprint import pprint
from django.db.models import Q
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
    before_vote = Vote.objects.filter(movie_id=movie_pk, user_id=request.user.pk)

    if request.data['rate']==0: # 0점 보내면 삭제
        if len(before_vote)>=1:
            before_vote.delete()
        else:
            pass
        return Response({'message' : 'record has deleted'})

    elif len(before_vote)==0: # 0점 안보냈을 때, 기존에 없으면 create
        serializer = VoteSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    elif len(before_vote)>=1: # 0점 안보냈을 때, 기존에 있으면 delete 후 create
        before_vote.delete()
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

@api_view(['GET'])
def recommendations(request):
    user = request.user
    movies = Movie.objects.all().values('id', 'genre_ids')
    votes = Vote.objects.filter(user_id=user.pk).values('movie_id')
    # 액션(1), 애니메이션(3), 코미디(4), 드라마(7), 공포(11), 로맨스(14)
    movie_ids=set()
    action_ids=set()
    animation_ids=set()
    comedy_ids=set()
    drama_ids=set()
    horror_ids=set()
    romance_ids=set()
    for movie in movies:
        movie_ids.add(movie['id'])
        if movie['genre_ids']==1:
            action_ids.add(movie['id'])
        if movie['genre_ids']==3:
            animation_ids.add(movie['id'])
        if movie['genre_ids']==4:
            comedy_ids.add(movie['id'])
        if movie['genre_ids']==7:
            drama_ids.add(movie['id'])
        if movie['genre_ids']==11:
            horror_ids.add(movie['id'])
        if movie['genre_ids']==14:
            romance_ids.add(movie['id'])
    vote_ids=set()
    for vote in votes:
        vote_ids.add(vote['movie_id'])
    overall_len=len(movie_ids)
    action_len=len(action_ids)
    animation_len=len(animation_ids)
    comedy_len=len(comedy_ids)
    drama_len=len(drama_ids)
    horror_len=len(horror_ids)
    romance_len=len(romance_ids)

    overall_cnt=0
    action_cnt=0
    animation_cnt=0
    comedy_cnt=0
    drama_cnt=0
    horror_cnt=0
    romance_cnt=0

    for num in vote_ids:
        overall_cnt+=1
        if num in action_ids:
            action_cnt+=1
            action_ids.remove(num)
        if num in animation_ids:
            animation_cnt+=1
            animation_ids.remove(num)
        if num in comedy_ids:
            comedy_cnt+=1
            comedy_ids.remove(num)
        if num in drama_ids:
            drama_cnt+=1
            drama_ids.remove(num)
        if num in horror_ids:
            horror_cnt+=1
            horror_ids.remove(num)
        if num in romance_ids:
            romance_cnt+=1
            romance_ids.remove(num)

    power_dict = {
        'action_power' : action_cnt/action_len*100,
        'animation_power' : animation_cnt/animation_len*100,
        'comedy_power' : comedy_cnt/comedy_len*100,
        'drama_power' : drama_cnt/drama_len*100,
        'horror_power' : horror_cnt/horror_len*100,
        'romance_power' : romance_cnt/romance_len*100,
        }

    lowest=''
    lowest_val=100
    message=''
    for key, value in power_dict.items():
        if value<lowest_val:
            lowest=key
            lowest_val=value

    if lowest=='action_power':
        sample=random.sample(action_ids,3)

        action_movies = Movie.objects.filter(Q(id=sample[0])|Q(id=sample[1])|Q(id=sample[2]))
        serializer = MovieDetailSerializer(action_movies, many=True)
        message = '박진감이 부족한 당신에게 추천하는 근본 액션 영화'
    
    elif lowest=='animation_power':
        sample=random.sample(animation_ids,3)

        animation_movies = Movie.objects.filter(Q(id=sample[0])|Q(id=sample[1])|Q(id=sample[2]))
        serializer = MovieDetailSerializer(animation_movies, many=True)
        message = '순수함이 부족한 당신에게 추천하는 근본 애니메이션 영화'

    elif lowest=='comedy_power':
        sample=random.sample(comedy_ids,3)

        comedy_movies = Movie.objects.filter(Q(id=sample[0])|Q(id=sample[1])|Q(id=sample[2]))
        serializer = MovieDetailSerializer(comedy_movies, many=True)
        message = '웃을일이 부족한 당신에게 추천하는 근본 코미디 영화'

    elif lowest=='drama_power':
        sample=random.sample(drama_ids,3)

        drama_movies = Movie.objects.filter(Q(id=sample[0])|Q(id=sample[1])|Q(id=sample[2]))
        serializer = MovieDetailSerializer(drama_movies, many=True)
        message = '감동이 부족한 당신에게 추천하는 근본 드라마'

    elif lowest=='horror_power':
        sample=random.sample(horror_ids,3)

        horror_movies = Movie.objects.filter(Q(id=sample[0])|Q(id=sample[1])|Q(id=sample[2]))
        serializer = MovieDetailSerializer(horror_movies, many=True)
        message = '오싹함이 필요한 당신에게 추천하는 근본 공포 영화'

    elif lowest=='romance_power':
        sample=random.sample(romance_ids,3)

        romance_movies = Movie.objects.filter(Q(id=sample[0])|Q(id=sample[1])|Q(id=sample[2]))
        serializer = MovieDetailSerializer(romance_movies, many=True)
        message = '로맨스가 필요한 당신에게 추천하는 근본 로맨스 영화'

    power_dict['overall_power'] = overall_cnt/overall_len*100
    if max(list(power_dict.values()))<5:
        return Response({
            'recommended_movies' : [],
            'powers' : power_dict,
            'message' : '평가를 좀 더 해주셔야 영화를 추천드릴 수 있어요ㅠ'
            })
    return Response({
        'recommended_movies' : serializer.data,
        'powers' : power_dict,
        'message' : message
        })