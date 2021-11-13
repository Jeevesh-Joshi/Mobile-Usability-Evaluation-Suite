from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path("dashboard", views.dashboard, name='dashboard'),
    path("testing", views.testing, name='testing'),
    path("recording", views.recording, name='recording'),
]