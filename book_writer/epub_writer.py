from book_writer.book_writer import *
from ebooklib import epub

book = epub.read_epub('test.epub')

class EpubWriter(BookWriter):
    def write(self, book: Book, dirname: str):
        pass
