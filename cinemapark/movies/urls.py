from django.urls import path
from . import views
from .views import index

urlpatterns = [
    path('movies/<int:mov_id>/', views.movies),
]
