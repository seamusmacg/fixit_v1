from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

#Create your models here.

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name


    def get_absolute_url(self):
          return reverse('blog')



class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
   
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('blog-detail', args=(str(self.id)))
