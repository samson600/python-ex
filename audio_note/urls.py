
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.authentication import TokenAuthentication


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user-login/', obtain_auth_token),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/audio-note/', include('note.urls')),
    path('api/user/', include('user_api.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
