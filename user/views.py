from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from .models import UserProfile as User

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/users/',
        {
        'Endpoint': 'api/users/register/',
        'method': 'POST',
        'body': {'username': '', 'email': '', 'password': ''},
        'description': 'Creates a new user'
        },
        {
        'Endpoint': 'api/users/login/',
        'method': 'POST',
        'body': {'username': '', 'password': ''},
        'description': 'Returns a token to authenticate a user'
        },
        'api/users/profile/',
        'api/users/profile/update/',
        'api/users/<str:pk>/update/',
        'api/users/<str:pk>/delete/',
        
        'api/exercises/',
        'api/exercises/<str:pk>/',
        'api/exercises/create/',
        'api/exercises/<str:pk>/update/',
        'api/exercises/<str:pk>/delete/',
        
        'api/workouts/',
        'api/workouts/<str:pk>/',
        'api/workouts/create/',
        'api/workouts/<str:pk>/update/',
        'api/workouts/<str:pk>/delete/',
        
        'api/workoutsets/',
        'api/workoutsets/<str:pk>/',
        'api/workoutsets/create/',
        'api/workoutsets/<str:pk>/update/',
    ]

    return Response(routes)

@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUser(request, pk):
    user = User.objects.get(user_id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)