from django.urls import include
from django.urls import path

urlpatterns = [
    path("", include("django_simple_docs.urls")),
]
