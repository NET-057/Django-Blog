from django.conf.urls import include,url
from . import views


app_name = "blog"
urlpatterns = [

    url(r'^$',views.show_all_blog,name='all_blog'),
    url(r'^(?P<id>[0-9]+)$',views.blog_detail,name='blog_detail'),
    url(r'^add/$',views.add_blog,name='add_blog'),
    url(r'^(?P<id>[0-9]+)/edit$',views.update_blog,name='update'),
    url(r'^delete/(?P<id>[0-9]+)$',views.delete_blog,name='delete')

]

