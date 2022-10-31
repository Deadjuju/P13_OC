# from django.test import Client
# from django.urls import reverse
# import pytest
#
#
# CLIENT = Client()
#
#
# @pytest.mark.django_db
# def test_lettings_route():
#     """
#     GIVEN a URL for index page,
#     WHEN a user tries to access this url",h
#     THEN template used and url name are correct.
#     """
#
#     url = reverse('home:index')
#     response = CLIENT.get(url)
#
#     assert url == "/"
#     assert response.status_code == 200
#
#     assert len(response.templates) == 1
#     template_used = response.templates[0].name
#     assert template_used == "index.html"
#
#     assert b"<title>Holiday Homes</title>" in response.content
