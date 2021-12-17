from django.db import models

# Create your models here.
# Posts models

class User(models.Model):#User model
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)

    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    bio=models.TextField(blank=True)
    is_admin=models.BooleanField(default=False)
    birthdate=models.DateField(blank=True,null=True)

    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)
    country = models.CharField(max_length=3,blank=True)
    city = models.CharField(max_length=200,blank=True)
    def __str__(self):
        return self.email