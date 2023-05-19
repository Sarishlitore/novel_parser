from book_reader.book_reader import *
from ebooklib import epub


class EpubReader(BookReader):
    def read(self, book_name: str, dirname='/'):
        book = epub.read_epub('test.epub')
