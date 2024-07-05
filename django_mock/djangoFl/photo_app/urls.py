from django.urls import path
from . import views



urlpatterns = [
    path('upload/', views.upload_photo, name='upload_photo'),
    path('', views.photo_list, name='photo_list'),
    path('delete/<int:photo_id>/', views.delete_photo, name='delete_photo')
]