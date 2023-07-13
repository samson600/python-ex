from django.shortcuts import render,HttpResponse
from rest_framework import viewsets, permissions
from .models import *
from .serializer import *
import pyttsx3, uuid
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from rest_framework import status
from django.contrib.auth.models import User
from .serializer import RegisterUserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import Http404
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.request import Request



#views 
    
class RegisterUserAPI(APIView):
    def post(self, request, formet=None):
        # serializer = RegisterUserSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        first_name = request.data['first_name']
        last_name = request.data['last_name']
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']
        password2 = request.data['password2']
        if not username or not email or not password or not password2:
            return Response({"type":"error", "message":"Required fields are empty!"})
        elif password != password2:
            return Response({"status":"error", "message":"Password not matched!"})
        elif User.objects.filter(username=username).exists():
            return Response({"status":"error", "message":"User already exists!"})
        elif User.objects.filter(email=email).exists():
            return Response({"type":"error", "message":"Email aready exist!"})
        else:
            user = User.objects.create(
                first_name=first_name, 
                last_name=last_name, 
                username=username, 
                email=email, 
                password=password
                )
            user.save()
            return Response({"type":"success", "success":"Account created successfully!"})
        
class LoginAPIView(APIView):
    permission_classes = (AllowAny,)

    serializer_class = LoginSerializer

    def post(self, request: Request) -> Response:
        """Return user after login."""
        #user = request.data.get('user', {})

        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_200_OK)        

class NotesAPI(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        note = Audio_note.objects.all()
        serializer = NoteSerializer(note, many=True)
        return Response(serializer.data)
    permission_classes = [IsAuthenticated]
    def post(self, request, method=None):
        title = request.data['title']
        text = request.data['text']
        voice = request.data['voice']
        user = Users.objects.get(id=1)
        audio_id = uuid.uuid4()
        filename = uuid.uuid4().hex+'.mp3'

        engine = pyttsx3.init()
        # convert this text to speech
        voices = engine.getProperty("voices")
        if voice == 'female':
            engine.setProperty('voice', voices[0].id)
        elif voice == 'male':
            engine.setProperty('voice', voices[1].id)
        engine.save_to_file(text, "media/audio/"+filename)
        engine.say(text)
   
        audio_note = Audio_note.objects.create(
            title= title,
            audio = 'audio/'+filename,
            audio_id = audio_id,
            user = user
        )
        audio_note.save()
        return Response({"type":"success", "message":"Note successfully saved!"})
    

class SingleNoteAPI(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Audio_note.objects.get(pk=pk)
        except Audio_note.DoesNotExist:
            raise Http404 
    permission_classes = [IsAuthenticated]
    def get(self, request, pk, format=None):
        note = self.get_object(pk)
        serializer = NoteSerializer(note)
        return Response(serializer.data)
     # def get(self, request, method=None):
        #audio = Audio_note.objects.all()

        # user = self.request.query_params.get('user')
        # if user is not None:
        #     queryset = audio.filter(user_id=user)
        #     serializer = NoteSerializer(queryset, many=True)
        #     return Response(serializer.data)
        # return Response({})
    permission_classes = [IsAuthenticated]
    def delete(self, request, pk, format=None):
        note = self.get_object(pk)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
   
# ViewSets define the view behavior.
#permission_classes = [IsAuthenticated]
class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]

class UserObtainAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        checkUser = User.objects.filter(username=username)
        if not checkUser:
            return Response({'type':'error','message':'User does not exist!'})
        checkPasswoed = User.objects.filter(password=password)
        if not checkPasswoed:
            return Response({'type':'error','message':'Incorrect password!'})
        user = authenticate(username=username, password=password)
        response = super(UserObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)
        userSerializer = UserSerializer(user)
        return Response({'token': token.key, 'user': userSerializer.data})
        return Response({})
    


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Audio_note.objects.filter(audio_id="e6d8ad61-68ca-4527-b19e-417c9844cb32")
    serializer_class = NoteSerializer
    #permission_classes = [permissions.IsAuthenticated]




    