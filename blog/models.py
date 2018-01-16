from django.db import models
from django.urls import reverse
from django.conf import settings

class PostBlog(models.Model):
	# user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	image = models.ImageField(null=True,blank=True,height_field="height_field",width_field='width_field')
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	content = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
	update = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return "/blog"

	class Meta:
		ordering = ['-timestamp','-update']



