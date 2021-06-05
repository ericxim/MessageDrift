from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import *
from .forms import PostForm

class ViewIndex(ListView):
  template_name = 'message/index.html'
  context_object_name = 'post_list'
  model = Post
  
  def get_context_data(self, **kwargs):
    context = super(ViewIndex, self).get_context_data(**kwargs)
    context['communities'] = Communities.objects.all()
    return context


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
    self.community = get_object_or_404(Communities, name=self.kwargs['slug'])
    return Post.objects.filter(community_id=self.community.id)

  
  def get_context_data(self, **kwargs):
    community = Communities.objects.get(name=self.kwargs['slug'])
    context = super(ViewCommunity, self).get_context_data(**kwargs)
    context['community'] = self.community
    return context
  
def error_404_view(request, exception):
	return render(request, './404.html')

