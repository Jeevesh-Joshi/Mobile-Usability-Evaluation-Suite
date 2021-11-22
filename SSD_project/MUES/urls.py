from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path("user_register", views.user_register, name='user'),
    path('load-ptasks', views.load_ptasks, name='ajax_load_tasks'),

    path("project_register", views.project_register, name='project'),
    path("testing", views.testing, name='testing'),
    path('load_videos', views.load_videos, name='ajax_load_videos'),
    path("recording", views.recording, name='recording'),
    path('load_utasks', views.load_utasks, name='ajax_load_utasks'),

    path("camera", views.camera, name='camera'),
    path("record_status", views.record_status, name='record_status'),
    path("video_viewer", views.video_viewer, name='video_viewer'),
]