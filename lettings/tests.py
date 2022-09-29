from django.test import Client
from django.urls import reverse
import pytest

from lettings.models import Address, Letting


CLIENT = Client()


@pytest.fixture
def address(db) -> Address:
    data = {
        "number": 7217,
        "street": "Bedford Street",
        "city": "Brunswick",
        "state": "GA",
        "zip_code": 31525,
        "country_iso_code": "USA"
    }
    return Address.objects.create(**data)


@pytest.fixture
def letting(db, address: Address) -> Letting:
    data = {
        "title": "Joshua Tree Green Haus /w Hot Tub",
        "address": address
    }
    return Letting.objects.create(**data)


@pytest.mark.django_db
def test_lettings_route():
    """
    GIVEN a URL containing the lettings,
    WHEN the user tries to access this url",
    THEN template used and url name are correct.
    """

    url = reverse('lettings:index')
    response = CLIENT.get(url)

    assert url == "/lettings/"
    assert response.status_code == 200

    assert b"<title>Lettings</title>" in response.content

    assert len(response.templates) == 1
    template_used = response.templates[0].name
    assert template_used == "lettings/index.html"


def test_detail_letting_route(db, address, letting):
    """
    GIVEN a URL containing a letting detail,
    WHEN the user tries to access this url",
    THEN template used and url name are correct.
    """

    letting_id = letting.pk
    url = reverse('lettings:letting', kwargs={'letting_id': letting_id})
    response = CLIENT.get(url)

    assert url == f"/lettings/{letting_id}/"
    assert response.status_code == 200

    title = letting.title
    assert f"<title>{title}</title>" in response.content.decode()

    assert len(response.templates) == 1
    template_used = response.templates[0].name
    assert template_used == "lettings/letting.html"
