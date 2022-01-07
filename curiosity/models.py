from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField

# Create your models here.

# This was written by Sushant Abrin

# Category models
class Category(models.Model):
    title = models.CharField(max_length=100)
    cat_id = models.AutoField(primary_key=True)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')
    date_added = models.DateTimeField(auto_now_add=True,null=True)

    def image_tag(self):
        return format_html('<img src ="/media/{}" style = "width:40px;height:40px;border-radius:50%" />'.format(self.image))

    def __str__(self):
        return self.title


# Post models

class Post(models.Model):
    post_id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=200)
    content = HTMLField()
    url=models.CharField(max_length=100)
    cat = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')
    date_added = models.DateTimeField(auto_now_add=True,null=True)

    # def image_tag(self):
    #     return format_html('<img src ="/media/{}" style = "width:40px;height:40px;border-radius:50%" />'.format(self.image))

    def __str__(self):
        return self.title # this will return actual title of category instead of class object
