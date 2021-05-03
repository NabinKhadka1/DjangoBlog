from django.shortcuts import render

from blog.models import Post
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import PostForm

# posts = [
#     {
#         'title': 'Blog Post 1',
#         'author': 'NK',
#         'body': 'This is the body part of the blog',
#         'publish': '2021 Jan 15',
#         'created': '2021 Jan 15',
#         'updated': '2021 Jan 15'
#     },
#     {
#         'title':'Blog Post 2',
#         'author': 'SK',
#         'body': 'This is the body part of the blog',
#         'publish': '2021 Jan 19',
#         'updated': '2021 Jan 19',
#         'created': '2021 Jan 19',
#     }

# ]
    

# Create your views here.
def blog_list(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
        }
    return render(request,'blog/list.html',context)
    
def blog_detail(request, id):
    post = Post.objects.get(pk=id)
    return render(request,'blog/details.html',context={'post':post})

def blog_create(request):
    if request.method == 'POST':
        author = request.POST.get('author')
        title = request.POST.get('title')
        body = request.POST.get('body')
        Post.objects.create(author_id=1,title=title,body=body)
        return redirect(reverse('blog:list_detail'))
    context = {'users':User.objects.all()}
    return render(request,'blog/create.html',context)

def create_django_forms(request):
    forms = PostForm()
    if request.method == 'POST':
        forms = PostForm(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect(reverse('blog:list_detail'))
    context = {'form':forms}
    return render(request,'blog/create_django_form.html',context)