from django.db import models
from django.urls import reverse
from django.conf import settings
import os
from io import BytesIO 
from PIL import Image 
from django.core.files import File 
from django.utils.text import slugify

# Create your models here.

#project model for landing page
class Project(models.Model):
    title = models.CharField(max_length=500)
    small_description = models.CharField(max_length=500)
    technology_used = models.CharField(max_length=500)
    main_image = models.ImageField(upload_to='project_images', default='static/images/test.png')
    large_description = models.TextField()
    carousel_image_1 = models.ImageField(upload_to='project_images', default='static/images/test.png')
    carousel_image_2 = models.ImageField(upload_to='project_images', default='static/images/test.png')
    carousel_image_3 = models.ImageField(upload_to='project_images', default='static/images/test.png')
    date_modified = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)

    #title of the project is returned for admin
    def __str__(self):
        return self.title

#web log model for log page
class webLog(models.Model):
    date = models.CharField(max_length=100)
    description = models.CharField(max_length=500)