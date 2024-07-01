from django.db import models

# Create your models here.

class testimonial(models.Model):
    name= models.CharField(max_length=150)
    position= models.CharField(max_length=150)
    phone_number= models.PositiveIntegerField()
    descriptions= models.TextField()
    date= models.DateField(auto_now=True)