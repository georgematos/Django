from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Category, Post

def home(request):

	name = "George"

	languages = ['Python', 'PHP', 'Java', 'Ruby']

	# for language in languages:
	# 	Category.objects.create(name=language)
	
	categories = Category.objects.all()

	category_python = Category.objects.get(name='Python')

	# post = Post()
	# post.name = "My first very post"
	# post.content = "Content of my first post"
	# post.status = "Published"
	# post.category = category_python
	# post.save()
	
	post = Post.objects.get(pk=1)

	context = {
		'name': name,
		'languages': languages,
		'categories': categories,
		'post': post,
	}

	# Category.objects.create(name="Python")

	return render(request, 'blog/home.html', context)

