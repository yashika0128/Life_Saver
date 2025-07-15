from django.urls import path
from . import views

urlpatterns = [
    # Home / Landing Page
    path('', views.index, name='index'),

    # Donor URLs
    path('donors/', views.donor_list, name='donor_list'),
    path('donors/new/', views.donor_create, name='donor_create'),
    path('donors/<int:pk>/edit/', views.donor_edit, name='donor_edit'),
    path('donors/<int:pk>/delete/', views.donor_delete, name='donor_delete'),

    # Receiver URLs
    path('receivers/', views.receiver_list, name='receiver_list'),
    path('receivers/new/', views.receiver_create, name='receiver_create'),

    # Static/Informational Pages
    path('community/', views.community, name='community'),
    path('mobile-friendly/', views.mobile_friendly, name='mobile_friendly'),
    path('trusted-network/', views.trusted_network, name='trusted_network'),
    path('track-impact/', views.track_impact, name='track_impact'),
    path('safe-donation/', views.safe_easy_donation, name='safe_easy_donation'),
]
