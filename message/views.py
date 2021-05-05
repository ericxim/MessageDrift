from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import *
from .forms import PostForm
import random

def index(request):
  communities = Communities.objects.all() 
  posts = Post.objects.all()
  random_post_id = random.choice(posts.values_list('id', flat=True))
  random_post = Post.objects.get(id=random_post_id)

  context = {
		'random_post' : random_post,
		'communitites': communities,
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

class ViewPost(DetailView):
  template_name = 'message/post.html'
  def get_queryset(self):
    self.post = get_object_or_404(Post, pk=self.kwargs['pk'])
    self.post.views += 1
    self.post.save()
    return Post.objects.filter(pk=self.post.id)
  
        
class ViewCommunity(ListView):
  template_name = 'message/community.html'
  context_object_name = 'post_list'
  
  def get_queryset(self):
    self.community = get_object_or_404(Communities, name=self.kwargs['name'])
    return Post.objects.filter(community_id=self.community.id)

  
  def get_context_data(self, **kwargs):
    community = Communities.objects.get(name=self.kwargs['name'])
    context = super(ViewCommunity, self).get_context_data(**kwargs)
    context['community'] = self.community
    return context
  
def error_404_view(request, exception):
	return render(request, './404.html')

