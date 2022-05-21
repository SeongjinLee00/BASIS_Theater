from .serializers import ProfileSerializer
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response

User = get_user_model
# Create your views here.
@api_view(['GET'])
@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    serializer = ProfileSerializer(user)
    print(serializer)
    return Response(serializer.data)