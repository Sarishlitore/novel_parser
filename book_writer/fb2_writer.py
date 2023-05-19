from book_writer.book_writer import *
from FB2 import FictionBook2, Author
from slugify import slugify


class FB2Writer(BookWriter):
    def write(self, book: Book, dirname: str):
        fb2book = FictionBook2()
        fb2book.titleInfo.title = book.title
        fb2book.titleInfo.authors = [Author(firstName=book.author)]
        for chapter in book.chapters_list:
            fb2book.chapters.append((chapter.title, chapter.content))
            print(f'{chapter.title} written')
        fb2book.write(f'{dirname}/{slugify(book.title)}.fb2')
        print(f'{book.title} written')
