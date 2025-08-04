from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # for http://127.0.0.1:8000/
    path('projects/', views.projects, name='projects'),
    path('publications/', views.publications, name='publications'),
    path('teaching/', views.teaching, name='teaching'),
    path('awards/', views.awards, name='awards'),
    path('contact/', views.contact, name='contact'),
]