from django.urls import path
from . import views


## can be changed
urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('users/', views.getUsers, name="users"),
    path('user/<str:pk>', views.getUser, name="user"),
    path('exercise/', views.exerciseList, name="exercise-list"),
    path('dailyExercises/', views.dailyExercises, name="daily-exercises"),
    
    # path('users/<str:pk>/', views.getUserById, name="user"),
    # path('users/register/', views.registerUser, name="register"),
    # path('users/login/', views.MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    # path('users/profile/', views.getUserProfile, name="users-profile"),
    # path('users/profile/update/', views.updateUserProfile, name="users-profile-update"),
    # path('users/<str:pk>/update/', views.updateUser, name="user-update"),
    # path('users/<str:pk>/delete/', views.deleteUser, name="user-delete"),
    
    # path('exercises/', views.getExercises, name="exercises"),
    # path('exercises/<str:pk>/', views.getExerciseById, name="exercise"),
    # path('exercises/create/', views.createExercise, name="exercise-create"),
    # path('exercises/<str:pk>/update/', views.updateExercise, name="exercise-update"),
    # path('exercises/<str:pk>/delete/', views.deleteExercise, name="exercise-delete"),
    
    # path('workouts/', views.getWorkouts, name="workouts"),
    # path('workouts/<str:pk>/', views.getWorkoutById, name="workout"),
    # path('workouts/create/', views.createWorkout, name="workout-create"),
    # path('workouts/<str:pk>/update/', views.updateWorkout, name="workout-update"),
    # path('workouts/<str:pk>/delete/', views.deleteWorkout, name="workout-delete"),
    
    # path('workoutsets/', views.getWorkoutSets, name="workoutsets"),
    # path('workoutsets/<str:pk>/', views.getWorkoutSetById, name="workoutset"),
    # path('workoutsets/create/', views.createWorkoutSet, name="workoutset-create"),
    # path('workoutsets/<str:pk>/update/', views.updateWorkoutSet, name="workoutset-update"),
]