from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50, unique=True)
    featured_image = models.ImageField(upload_to='featured-images/', null=True, blank=True)
    body = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):

        return '{} pubished on {}'.format(self.title, self.published.strftime('%d %B, %Y'))
