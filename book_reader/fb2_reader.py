from book_reader.book_reader import *
from xml.etree import ElementTree
from book_reader import xpath


class Fb2Reader(BookReader):
    def read(self, file_name: str, dirname='') -> Book:
        file = f'{dirname}/{file_name}'
        tree = ElementTree.parse(file)
        raw = tree.getroot()
        title = raw.find(xpath.BOOK_TITLE).text
        author = raw.find(xpath.AUTHOR).text
        book = Book(_title=title, _author=author)
        for chapter in raw.findall(xpath.SECTION):
            chapter_title = chapter.find(xpath.CHAPTER_TITLE).find(xpath.PARAGRAPH).text
            chapter_content = [par.text for par in chapter.findall(xpath.PARAGRAPH)]
            book.add_chapter(chapter_title=chapter_title, chapter_content=chapter_content)
        return book
