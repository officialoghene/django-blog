from django.shortcuts import render
from blog.models import Post, Category
from blog.forms import NewPostForm
#Login
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required



# Create your views here.

def index(request):
	posts = Post.objects.all().order_by('-published')
	big = Post.objects.all().order_by('-published')[0]
	welcome = Post.objects.all().order_by('-published')[:6]
	trend =	Post.objects.all().order_by('-published')[:5]

	return render(request, 'index.html', {'posts': posts, 'big': big, 'welcome': welcome, "trend": trend})


@login_required
def create_post(request):

	post_created = False

	if request.method == 'POST':
		post_form = NewPostForm(data=request.POST)

		if post_form.is_valid():
			new_post = post_form.save(commit=False)
			new_post.author = request.user

			if 'featured_image' in request.FILES:
				new_post.featured_image = request.FILES['featured_image']

			new_post.save()

			post_created = True

		else:
			print(post_form.errors)
	else:
		post_form = NewPostForm
	return render(request, 'createpost.html', {'post_form': post_form, 'post_created': post_created,})
