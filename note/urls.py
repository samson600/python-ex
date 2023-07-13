from django.urls import path
from .views import *
from rest_framework import routers
from note.views import UserViewSet, NoteViewSet
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
#router.register(r'', NoteViewSet)

urlpatterns = [
       path('auth/', LoginAPIView.as_view()),
       path('user-registation/', RegisterUserAPI.as_view()),
       path('notes/', NotesAPI.as_view()),
       path('notes/<int:pk>/', SingleNoteAPI.as_view()),
] + router.urls