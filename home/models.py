from django.db import models

operator_choice = [
    ('bl','Banglalink'),
    ('rb','Robi'),
    ('gp','Grameenphone'),
    ('tt','Taletalk')
]

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    operator = models.CharField(max_length=15, choices=operator_choice)
    date = models.DateField()

    def __init__(self):
        return self.name
        


