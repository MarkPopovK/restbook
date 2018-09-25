from django.core.management.base import BaseCommand
from controlbook.models import Book, Page
import os
from django.db import transaction

class Command(BaseCommand):
    bookfile = 'controlbook/book1.txt'

    @transaction.atomic
    def handle(self, *args, **options):
        with open(self.bookfile, 'r') as booktxt:
            text = booktxt.read()
            pages = split_on_pages(text)
            # print(pages)
            book = Book(name='A Nice Book!')
            book.save()
            for i, page in enumerate(pages, 1):
                new_page = Page(book=book,
                                content=page,
                                number=i)
                new_page.save()
                print(new_page)

def split_on_pages(text, words_per_page=30):
    text = text.split(' ')
    pages = []
    while text:
        pages.append(' '.join(text[:words_per_page]))
        text = text[words_per_page:]
    return pages
