from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path("user_register", views.user_register, name='user'),
    path('load-ptasks', views.load_ptasks, name='ajax_load_tasks'),
    path("project_register", views.project_register, name='project'),
    path("testing", views.testing, name='testing'),
    path("recording", views.recording, name='recording'),
]