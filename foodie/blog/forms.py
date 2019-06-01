from django import forms
from django.contrib.auth.models import User
from blog.models import  Post # Comment, UserProfile

class NewPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'body', 'category', 'featured_image',)
