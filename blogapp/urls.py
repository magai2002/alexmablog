from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('post/<int:pk>', views.post, name='post'),
    path('posts/', views.posts, name='posts'),
	path('categories/<int:pk>', views.categories_posts, name='categories'),
]