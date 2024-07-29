from django.db import models

# Create your models here.

class Card(models.Model):
    image=models.ImageField(upload_to='image/')
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    #ordering=modes.BooleanField()
    def __str__(self):
       
        return self.title

    
class Contact(models.Model):
    first_name=models.CharField(max_length=50)   
    last_name=models.CharField(max_length=50)
    phone=models.IntegerField()
    message=models.TextField(max_length=250)
    def __str__(self):
        return f'{self.first_name},{self.last_name}'
     
      

class About(models.Model):
    image=models.ImageField(upload_to='About_image/')
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=250)
   
    class Meta:
        
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

    def __str__(self):
       
        return self.title
    

