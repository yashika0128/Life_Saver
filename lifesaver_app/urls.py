from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lifesaver_app.urls')),  # ✅ include app-level routes
]
