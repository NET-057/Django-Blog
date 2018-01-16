from django.contrib import admin
from .models import PostBlog

class ChangeBlogAdmin(admin.ModelAdmin):
	list_display = ['title', "update","timestamp"]
	list_display_links = ['update']
	list_filter = ['update','timestamp']
	search_fields = ['title']
	class Meta:
		model = PostBlog


admin.site.register(PostBlog,ChangeBlogAdmin)



