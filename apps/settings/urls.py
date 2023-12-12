from django.urls import path
from apps.settings.views import *

urlpatterns = [
    path('', index,name='index'),
    path('blog.html', index1, name='index1'),
    path('blog-post.html', index2, name='index2'  ),
    
]