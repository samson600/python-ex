from .models import *
from rest_framework import serializers



# Serializers define the API representation.
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio_note
        fields = '__all__'