from django.urls import path
from .views import UserViewset, LoginAPIView
from rest_framework import routers
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewset)

urlpatterns = [
        path('login/', LoginAPIView.as_view()),
] + router.urls