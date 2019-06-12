
from  django.urls import  path, re_path

from  . import  views

urlpatterns = [
    path('test', views.index, name='index'),  #

    re_path(r'^checkProduct/(?P<slug>[\w-]+)/$', views.searchProduct),
    path('', views.index, name='index'),  #
]