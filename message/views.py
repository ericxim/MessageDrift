from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
import random


def index(request):

	total_posts = Post.objects.all()
	random_post_id = random.choice(total_posts.values_list('id', flat=True))
	random_post = Post.objects.get(id=random_post_id)

	context = {

		'random_post' : random_post,
		'random_post_id': random_post_id,

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
		return redirect('view_post', pk=new_post.pk)

	context = {

		'form' : form,

	}

	return render(request, 'message/create.html', context)

def view_post(request, pk):

	total_posts = Post.objects.all()
	random_post = random.choice(total_posts.values_list('id', flat=True))

	post = Post.objects.get(id=pk)

	context = {

		'post' : post,
		'random_post' : random_post,

	}

	return render(request, 'message/post.html', context)

def error_404_view(request, exception):

	return render(request, '404.html')

