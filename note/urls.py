from django.urls import path
from .views import *
from rest_framework import routers
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# router.register(r'users', UserViewset)

urlpatterns = [
       path('notes/', NotesAPI.as_view()),
       path('notes/<int:pk>/', NotesAPI.as_view()),
       path('note/delete/<int:pk>', NoteDeleteAPI.as_view())
] + router.urls