from django.urls import path
from apps.settings.views import *

urlpatterns = [
    path('', index,name='index'),
    path('blog.html', blog, name='index1'),

    
]