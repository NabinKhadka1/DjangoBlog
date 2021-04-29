from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path('list/',views.blog_list,name="list_detail"),
    path('detail/<int:id>/',views.blog_detail,name="blog_detail"),
    path('create/',views.blog_create,name="blog_create"),
]