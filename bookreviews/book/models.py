from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True,null=True)
    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=250)
    isbn = models.CharField(max_length=13)
    author = models.CharField(max_length=250)
    description = models.TextField(blank=True,null=True) 
    release_date = models.DateField()
    page_count = models.IntegerField()
    image = models.ImageField(upload_to='book/images/')
    price = models.DecimalField(max_digits=8,decimal_places=1, default=0)
    publisher = models.CharField(max_length=250,default='')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.title
