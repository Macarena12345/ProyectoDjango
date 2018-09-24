from django.shortcuts import render
from .froms import PostForm
def  post_new(request):
    form = PostForm()
    return render (request, 'blog/post_edit.html', {'form': form})
# Create your views here.
