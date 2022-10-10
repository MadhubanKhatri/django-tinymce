Hello Friends, 
Welcome back to my blog. In this blog, I will show you how to add **TinyMce Editor**  in Django just in few minutes. 

## What is TinyMce ?
TinyMCE is an online rich-text editor released as open-source software under the MIT License. It has the ability to convert HTML text area fields or other HTML elements to editor instances. [Wikipedia](https://en.wikipedia.org/wiki/TinyMCE)

Let's Start :)
1.) Create a project named-'tiny_mce'
```python
your_directory/.../django-admin startproject tiny_mce
```
2.) Open 'tiny_mce' folder in your favourite code editor and run the following command in terminal
```python
pip install django-tinymce
#command will install tinymce in your system
```

3.) Create an 'main' app in 'tiny_mce' folder using following command
```python
python manage.py startapp main
```

4.) Open setting.py file and add 'main' app & 'tiny_mce'
```python
INSTALLED_APPS = [
      #some other apps installed
      ..
      ..
      'main',
      'tinymce'
]
```

5.) open project 'urls.py' file and add the code below
```python
from django.contrib import admin  #already added
from django.urls import path, include #import include

urlpatterns = [
    path('admin/', admin.site.urls),   #already added
    path('', include('main.urls'))   #add this line
]
```

6.) create 'urls.py' file in 'main' app and add the following code
```python
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home')
]
```

7.) open 'views.py' file and add code
```python
from django.shortcuts import render
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
```

8.) Create a 'templates' folder in 'tiny_mce' folder and add this directory in 'settings.py'
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR,'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

9.) open models.py and create a Post model.
```python
from django.db import models
from tinymce.models import HTMLField   #import HTMLField 

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    desc = HTMLField()     #add here as Description section

    def __str__(self):
        return self.title
```
10.) Register 'Post' model in admin.py file
```python
from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)

```

11.) create a 'index.html' in 'templates' folder
```html
<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <script src="https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js" referrerpolicy="origin"></script>

    <script>
        tinymce.init({
            selector: '#exampleFormControlTextarea1'
        });
    </script>
    <style>
        #posts{
            position:absolute;
            top:15px;
            right:0px;
        }
    </style>
    <title>Index page</title>
</head>

<body>
    <div class="container mx-5 my-3 w-50" style="border-right: 1px solid;">
        <h3>Create a Post</h3>
        <form method="post" action="{% url 'home' %}">
        {% csrf_token %}
        <div class="mb-3">
            <label for="exampleFormControlInput1" class="form-label">Post Title</label>
            <input type="text" class="form-control" name="post_title" id="exampleFormControlInput1" placeholder="Title">
        </div>
        <div class="mb-3">
            <label for="exampleFormControlTextarea1" class="form-label">Content</label>
            <textarea class="form-control" name="post_description" id="exampleFormControlTextarea1" rows="3"></textarea>
        </div>
        <div class="mb-3">
            <input type="submit" class="btn btn-primary"/>
        </div>
        </form>
    </div>

    <div class="container w-50" id="posts">
        {% for post in posts %}
            <div class="container mx-5">
                <h3 style="border-bottom:1px solid; display:inline">{{post.title}}</h3>
                <p>{{post.desc|safe}}</p>
                <hr>
            </div>
        {% endfor %}
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous">
        </script>

</body>

</html>
```

### Thank you for visit my blogs.
  
