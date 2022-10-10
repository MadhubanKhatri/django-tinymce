from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def home(request):
    if request.method=='POST':
        title = request.POST['post_title']
        content = request.POST['post_description']
        create_post = Post.objects.create(title=title, desc=content)
        create_post.save()
    all_posts = Post.objects.all()[::-1]
    data = {'posts':all_posts}
    return render(request,'index.html',data)