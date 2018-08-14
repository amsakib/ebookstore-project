from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('categories/', views.categories),
    path('category/<int:category_id>', views.category),
    path('ebooks/', views.ebooks),
    path('ebook/<int:ebook_id>', views.ebook)
]
