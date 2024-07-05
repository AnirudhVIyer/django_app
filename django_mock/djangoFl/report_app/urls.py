from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_page, name='report_page'),
    path('generate/', views.generate_pdf, name='generate_pdf'),
]
