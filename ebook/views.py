from django.shortcuts import render
from .models import Category, Ebook
def home(request):
	pass

def categories(request):
	categories = Category.objects.all()
	
	return render(request, 'ebook/categories.html', {
		'categories': categories,
		})

def ebooks(request):
	ebooks = Ebook.objects.all()
	return render(request, 'ebook/ebooks.html', {
		'ebooks': ebooks,
		})
