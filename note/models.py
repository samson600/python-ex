from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Audio_note(models.Model):
    title = models.CharField(max_length=50)
    audio = models.FileField(upload_to='audio/', null=True)
    audio_id = models.CharField(max_length=150)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

