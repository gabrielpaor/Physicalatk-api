from rest_framework.serializers import ModelSerializer
from .models import *

class UserSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class ExerciseSerializer(ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'