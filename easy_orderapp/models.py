from django.db import models


class easy_orderapp(models.Model):
    title = models.CharField(max_length = 150)
    text = models.TextField(max_length = 150)
    content = models.CharField(max_length = 150)
    blogcontent= models.TextField("")
    date = models.DateField()
    author = models.CharField(max_length= 150)
    
    
class shopproduct(models.Model):
    title = models.CharField(max_length = 150, default = "Product Title")
    description = models.TextField(default ="product description")
    price = models.CharField(max_length = 150,default = "00.00")
    img =models.ImageField(upload_to='images/')  
    
class UserUpdateForms(models.Model):
    FirstName =models.CharField(max_length = 150)
    LastName =models.CharField(max_length = 150)
    email= models.CharField(max_length = 150)
    Password1 =models.CharField(max_length = 120)
    password2 = models.CharField(max_length = 120) 
    
    
# Create your models here.