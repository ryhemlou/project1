from django.db import models

# Create your models here.

class Feature(models.Model):
    #id : int we dont need id caus each model have an id
    name= models.CharField(max_length=100)
    details= models.CharField(max_length=500)
    
    #this model is linked to database in admin




class SocialAccount(models.Model):
    email = models.EmailField(unique=True)  # Ensure that each email is unique in the database

    def __str__(self):
        return self.email




