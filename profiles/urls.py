from django.urls import path

from .views import profile, profiles_index


app_name = "profiles"

urlpatterns = [
    path('profiles/', profiles_index, name='index'),
    path('profiles/<str:username>/', profile, name='profile'),
]
