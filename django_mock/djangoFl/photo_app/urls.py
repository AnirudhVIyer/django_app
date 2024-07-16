from django.urls import path
from . import views



urlpatterns = [
    path('upload/', views.api_upload_photo, name='upload_photo'),
    path('', views.api_photo_list, name='photo_list'),
    path('delete/<int:photo_id>/', views.api_delete_photo, name='delete_photo')
]