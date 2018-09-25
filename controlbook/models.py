from django.db import models


# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def pages_count(self):
        return self.pages.count()


class Page(models.Model):
    book = models.ForeignKey(Book, related_name='pages', on_delete=models.CASCADE)
    number = models.IntegerField()
    content = models.TextField(default='', blank=True, null=True)

    def __str__(self):
        return f'{self.book.name} - {self.number}'

    #class Meta:
    #    unique_together = ("book", "number")
