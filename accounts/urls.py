from django.urls import path
from . import views
from accounts import views

urlpatterns = [
    path('boosters-list/',views.BoostersList.as_view()),
]
