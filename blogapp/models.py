from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_models


class Category(models.Model):
	title = models.CharField(max_length=255)

	def __str__(self):
		return self.title

class Post(models.Model):
	title = models.CharField(max_length=255)
	title_tag = models.CharField(max_length=255)
	overview = models.TextField()
	content = tinymce_models.HTMLField(default='content')
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	published_date = models.DateTimeField(auto_now_add=True)
	categories = models.ManyToManyField(Category)

	def __str__(self):
		return self.title