"""eventex URL Configuration
"""
from django.contrib import admin
from django.urls import path
import eventex.core.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", eventex.core.views.home),
]
