from django.db import models


class Category(models.Model):

    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name


class Ebook(models.Model):
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13)
    pages = models.IntegerField()
    price = models.FloatField()
    image = models.ImageField(upload_to='images/')
    ebook = models.FileField(upload_to='ebooks/')

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title