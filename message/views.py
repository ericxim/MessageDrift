from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.list import ListView
from .models import Post
from .forms import PostForm
import random

def index(request):
	posts = Post.objects.all()
	random_post_id = random.choice(posts.values_list('id', flat=True))
	random_post = Post.objects.get(id=random_post_id)

	context = {
		'random_post' : random_post,
	}

	return render(request, 'message/index.html', context)

def about(request):
	return render(request, 'message/about.html')

def create_post(request):
	form = PostForm()

	if request.method == 'POST':
		print(request.POST)
		form = PostForm(request.POST)
		if form.is_valid():
			new_post = form.save()
		return redirect(f'/post/?search={new_post.id}')

	context = {
		'form' : form,
	}

	return render(request, 'message/create.html', context)

def view_post(request):
    posts = Post.objects.all()
    random_post = random.choice(posts.values_list('id', flat=True))
    if request.method == 'GET':
        search = request.GET.get('search', random_post)
        try:
          post = Post.objects.get(pk=search)
          post.views += 1
          post.save()
          context = {
				'post':post
			}
          return render(request, 'message/post.html', context)
        except Post.DoesNotExist:
          return render(request, 'message/post.html')
      
    else:
        post = Post.objects.get(id=random_post)
        post.views = post.view + 1
        post.save()

        context = {
			'post' : post,
		}
        return render(request, 'message/post.html', context)

def error_404_view(request, exception):
	return render(request, './404.html')

