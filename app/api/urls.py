from django.urls import path
from .views import health, hello, version

urlpatterns = [
    path('health/', health),
    path('hello/', hello),
    path('version/', version),
]