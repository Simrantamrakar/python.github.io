from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField
# Create your models here.


class NewsCategori(models.Model):
    categori_name = models.CharField(max_length=150)

    class Meta:
        ordering = ['id',]

    def __str__(self):
        return self.categori_name
    
class NewsDetails(models.Model):
    categori = models.ForeignKey(NewsCategori, on_delete=models.CASCADE, related_name ="newcategori")
    image =models.ImageField(upload_to ='newimage/')
    title = models.CharField(max_length=150)
    discriptions = RichTextField()
    news_slug = AutoSlugField(populate_from='title', unique = True, default =None)
    class Meta:
        ordering = ['-id',]

    def __str__(self):
        return self.title
    
class NewsAbout(models.Model):
    categori_name = models.CharField(max_length=150)

    class Meta:
        ordering = ['id',]

    def __str__(self):
        return self.categori_name
    
class Details(models.Model):
    # ctg = models.TextField()
    image =models.ImageField(upload_to ='newimage/')
    title = models.CharField(max_length=150)
    discriptions = models.TextField()

    class Meta:
        ordering = ['-id',]

    def __str__(self):
        return self.title

    
class GeeksModel(models.Model):
    geeks_field = RichTextField()
    
class Contact(models.Model):
    name= models.CharField(max_length=150)
    email= models.EmailField()
    message= models.TextField()
    subject= models.CharField(max_length=150)

    class Meta:
        ordering = ['-id',]

    def __str__(self):
        return self.name
    
class Info(models.Model):
    location= models.CharField(max_length=200)
    contact= models.PositiveIntegerField()
    email= models.EmailField()

    class Meta:
        ordering = ['-id',]

