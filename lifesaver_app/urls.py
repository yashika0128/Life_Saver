from django.urls import path
from . import views

urlpatterns = [
    path('donors/', views.donor_list, name='donor_list'),
    path('donors/new/', views.donor_create, name='donor_create'),
    path('receivers/', views.receiver_list, name='receiver_list'),
    path('receivers/new/', views.receiver_create, name='receiver_create'),
]
