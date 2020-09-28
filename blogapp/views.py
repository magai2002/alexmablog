from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.core.mail import send_mail

def index(request):
	featured = Post.objects.order_by('-published_date')[0:4]
	context = {
		'featured': featured
	}
	return render(request, 'index.html', context)

def about(request):
	return render(request, 'about.html', {})

def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		#send email
		send_mail(
			'Message from ' + message_name, #subject
			message, #message
			message_email, #from email
			['magaialexey@gmail.com'], #to email
			)

		return render(request, 'success.html', {})

	else:
		return render(request, 'contact.html', {})


def posts(request):
	post_list = Post.objects.all().order_by('-published_date')
	paginator = Paginator(post_list, 8)
	page = request.GET.get('page')
	
	try:
		paginated_queryset = paginator.page(page)
	except PageNotAnInteger:
		paginated_queryset = paginator.page(1)
	except EmptyPage:
		paginated_queryset = paginator.page(paginator.num_pages)


	context = {
		'post_list': paginated_queryset,
	}


	return render(request, 'posts.html', context)


def post(request, pk):
	post = get_object_or_404(Post, pk=pk)
	categories = Category.objects.all()
	context = {
		'post': post,
		'cats': categories
	}
	return render(request, 'post.html', context)

def categories_posts(request, pk):
	category = Category.objects.filter(id=pk)
	category_posts = Post.objects.filter(categories=pk)

	paginator = Paginator(category_posts, 4)
	page = request.GET.get('page')
	
	try:
		paginated_queryset = paginator.page(page)
	except PageNotAnInteger:
		paginated_queryset = paginator.page(1)
	except EmptyPage:
		paginated_queryset = paginator.page(paginator.num_pages)


	context = {
		'category_posts': paginated_queryset,
		'category': category
	}


	return render(request, 'cat_posts.html', context)