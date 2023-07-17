from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import LoginSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.authtoken.models import Token

class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        checkUser = User.objects.filter(username=username)
        if not checkUser:
            return Response({'type':'error','message':'User does not exist!'})
        checkPasswoed = User.objects.filter(password=password)
        if not checkPasswoed:
            return Response({'type':'error','message':'Incorrect password!'})
        
        user = User.objects.get(username=username)
        token = Token.objects.get_or_create(user=user)
        userSerializer = UserSerializer(user)
        return Response({'token': str(token[0]),'user': userSerializer.data})
    
class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
       






    