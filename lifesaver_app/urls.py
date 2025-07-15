from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('donors/', views.donor_list, name='donor_list'),
    path('donors/new/', views.donor_create, name='donor_create'),
    path('receivers/', views.receiver_list, name='receiver_list'),
    path('receivers/new/', views.receiver_create, name='receiver_create'),
    path('community/', views.community, name='community'),
    path('mobile-friendly/', views.mobile_friendly, name='mobile_friendly'),
    path('trusted-network/', views.trusted_network, name='trusted_network'),
    path('track-impact/', views.track_impact, name='track_impact'),
    path('safe-donation/', views.safe_easy_donation, name='safe_easy_donation'),
    path('donors/edit/<int:pk>/', views.donor_edit, name='donor_edit'),
    path('donors/delete/<int:pk>/', views.donor_delete, name='donor_delete'),]
