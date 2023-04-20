from django.urls import path
from demoapp import views

urlpatterns = [
    path('', views.demoapp),
    path('service/', views.service)
]