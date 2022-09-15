from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse
import pytest

from profiles.models import Profile

CLIENT = Client()


@pytest.fixture
def user(db) -> User:
    data = {
        "password": "pbkdf2_sha256$180000$zjnQu4LiqMAT$Qxom08ahzw11iPlX6kYyySa94yJXdjrptta6Qzx8HWE=",
        "username": "HeadlinesGazer",
        "first_name": "Jamie",
        "last_name": "Lal",
        "email": "jssssss33@acee9.live",
    }
    return User.objects.create(**data)


@pytest.fixture
def profile(db, user) -> Profile:
    data = {
        "user": user,
        "favorite_city": "Buenos Aires"
    }
    return Profile.objects.create(**data)


@pytest.mark.django_db
def test_profiles_route():

    url = reverse('profiles:index')
    response = CLIENT.get(url)

    assert url == "/profiles/"
    assert response.status_code == 200

    assert b"<title>Profiles</title>" in response.content

    assert len(response.templates) == 1
    template_used = response.templates[0].name
    assert template_used == "profiles/index.html"


def test_detail_profile_route(db, user, profile):

    url = reverse('profiles:profile', kwargs={'username': user.username})
    response = CLIENT.get(url)

    assert url == f"/profiles/{user.username}/"
    assert response.status_code == 200

    title = user.username
    assert f"<title>{title}</title>" in response.content.decode()

    assert len(response.templates) == 1
    template_used = response.templates[0].name
    assert template_used == "profiles/profile.html"
