from rest_framework import serializers
from .models import Movie, Vote, Genre

class GenreNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

class MovieDetailSerializer(serializers.ModelSerializer):

    genre_ids = GenreNameSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'

class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        fields = '__all__'
        read_only_fields = ('movie', 'user',)