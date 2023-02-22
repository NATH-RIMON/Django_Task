from django.db import models

# Create your models here.
class Product(models.Model):
   image= models.ImageField( upload_to='Product')
   title=models.CharField(max_length=50)
   description= models.TextField()
   def __str__(self):
    return self # TODO