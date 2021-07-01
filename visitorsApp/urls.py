from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.home, name='home'),
    path('visitors/', views.visitors, name='visitors'),
    path('meeting/', views.meeting, name='meeting'),
    path('logout/', views.logout, name='logout'),
    path('record/', views.record, name='record'),
    path('allRecord/', views.allRecord, name='allRecord'),
    path('allMeeting/', views.allMeeting, name='allMeeting'),
    path('emrecord/', views.emrecord, name='emrecord'),


    path('', views.login, name='login'),
]