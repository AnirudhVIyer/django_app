from django.contrib import admin
from django.urls import path, include
from . import views
from .views import CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.api_register, name='register'),
    path('login/', views.api_login, name='login'),
    path('logout/', views.api_logout, name='logout'),
    path('home/', views.api_user_home,name='user_home'),
    path('welcome/', views.api_welcome,name='welcome'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]