from django.db import models

# Create your models here.
class Employee(models.Model):
    name= models.CharField(max_length=150)
    email= models.EmailField()
    address= models.CharField(max_length=200)
    phone= models.PositiveIntegerField()

    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return self.name
    
