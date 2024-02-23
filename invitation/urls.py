from django.urls import path
from . import views

urlpatterns = [
    path('', views.invitation, name='index'),
    path('engagementpics/', views.engagementpics, name='engagementpics'),
    path('engagementpics_upload/', views.engagementpics_upload, name='engagementpics_upload'),

]
