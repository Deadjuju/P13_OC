from django.urls import path

from .views import profile, profiles_index


urlpatterns = [
    path('profiles/', profiles_index, name='profiles_index'),
    path('profiles/<str:username>/', profile, name='profile'),
]
