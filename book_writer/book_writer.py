from abc import ABC, abstractmethod

from FB2 import FictionBook2
from slugify import slugify
from book.book import Book


class BookWriter(ABC):
    @abstractmethod
    def write(self, book: Book, dirname: str):
        pass


class FB2Writer(BookWriter):
    def write(self, book: Book, dirname: str):
        fb2book = FictionBook2()
        fb2book.titleInfo.title = book.name
        fb2book.titleInfo.author = book.author
        for chapter in book.chapters_list:
            fb2book.chapters.append((chapter.name, chapter.content))
            print(f'{chapter.name} written')
        fb2book.write(f'{dirname}/{slugify(book.name)}.fb2')
        print(f'{book.name} written')
