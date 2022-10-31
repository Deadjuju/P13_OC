from django.contrib import admin
from django.urls import path, include


# def trigger_error(request):
#     division_by_zero = 1 / 0


urlpatterns = [
    # path('sentry-debug/', trigger_error),
    path('', include("lettings.urls")),
    path('', include("profiles.urls")),
    path('', include("home.urls")),
    path('admin/', admin.site.urls),
]
