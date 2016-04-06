from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(blank=True)
	photo = models.URLField(blank=True)
	# blank 非必填字段,表单验证时使用	
	location = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
	    return self.title
	
