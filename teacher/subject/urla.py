from django.urls import path
from .views import subject, teacher


urlpatterns = [
    path("subject/", subject, name="subject"),
    path("Teacher/", Teacher, name="Teacher"),
]