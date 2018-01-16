from django.shortcuts import render,get_object_or_404,Http404
from django.core.paginator import Paginator
from .models import PostBlog
from django.db.models import Q
from django.http import HttpResponse,HttpResponseRedirect
from .form import Post_Blog



def show_all_blog(request):
	queryset_list = PostBlog.objects.all()
	query = request.GET.get('q')
	if query:
		queryset_list = PostBlog.objects.filter(
			Q(title__icontains=query)|
			Q(content__icontains=query)).distinct()

	paginator = Paginator(queryset_list,3)
	page = request.GET.get('page')
	context = {'object_list':paginator.get_page(page)}
	return render(request, 'all_blog.html', context)



def blog_detail(request,id=None):
	obj = get_object_or_404(PostBlog,pk=id)
	context = {'blog':obj}
	return render(request, 'blog_detail.html', context)


def add_blog(request):
	# if not request.user.is_staff or not request.user.is_superuser:
	# 	raise Http404

	form = Post_Blog(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		# instance.user = request.user
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {'form':form}
	return render(request,'add_blog.html',context)

def update_blog(request,id=None):
	instance = get_object_or_404(PostBlog,pk=id)
	form = Post_Blog(request.POST or None,request.FILES or None,instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {'form':form}
	return render(request,'add_blog.html',context)

def delete_blog(request,id=None):
	instance = get_object_or_404(PostBlog,pk=id)
	instance.delete()
	return HttpResponseRedirect(instance.get_absolute_url()) 

