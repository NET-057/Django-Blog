from django import forms
from .models import PostBlog


class Post_Blog(forms.ModelForm):
	class Meta:
		model = PostBlog
		fields = ['title','content','image']

	