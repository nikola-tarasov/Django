from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # added the word 'specifics'
    path("specifics/<int:question_id>/", views.detail, name="detail"),
]
