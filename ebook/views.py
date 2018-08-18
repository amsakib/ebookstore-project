from django.shortcuts import render, get_object_or_404
from .models import Category, Ebook
from django.core.paginator import Paginator

def home(request):
    ebooks = Ebook.objects.order_by('-id')[:8]
    return render(request, 'ebook/home.html', {
        'ebooks' : ebooks 
    })

def categories(request):
    categories = Category.objects.order_by('name')
    return render(request, 'ebook/categories.html', {
		'categories': categories,
		})

def category(request, category_id):
    category = get_object_or_404(Category, pk = category_id)
    ebooks = category.ebook_set.all()

    paginator = Paginator(ebooks, 12)
    try:
        page = request.GET['page']
    except:
        page = 1
    ebooks = paginator.get_page(page)

    return render(request, 'ebook/category.html', {
		'category' : category,
		'ebooks' : ebooks
		})

def ebooks(request):
    ebooks = Ebook.objects.all()
    paginator = Paginator(ebooks, 12)
    try:
        page = request.GET['page']
    except:
        page = 1
    ebooks = paginator.get_page(page)
    return render(request, 'ebook/ebooks.html', {
		'ebooks': ebooks,
		})

def ebook(request, ebook_id):
    ebook = get_object_or_404(Ebook, pk = ebook_id)
    return render(request, 'ebook/ebook.html', {
		'ebook' : ebook
		})
