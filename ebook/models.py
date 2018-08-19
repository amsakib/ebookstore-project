from django.db import models
from django.contrib.auth.models import User

# category model
class Category(models.Model):

    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

# ebook model
class Ebook(models.Model):
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13)
    pages = models.IntegerField()
    price = models.FloatField()
    image = models.ImageField(upload_to='images/')
    # this will be the download link of the ebook
    ebook = models.FileField(upload_to='ebooks/')

    # has one to many relationship with Category
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    body = models.TextField()
    pub_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ebook = models.ForeignKey(Ebook, on_delete=models.CASCADE)


    def pub_date_pretty(self):
        return self.pub_time.strftime('%b %e %Y')