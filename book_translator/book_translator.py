import time
from googletrans import Translator
from book.book import Book


class BookTranslator:
    __one_translation_size = 10000

    def __init__(self, src: str, dest: str, **kwargs):
        self._src = src
        self._dest = dest
        self._translator = Translator(**kwargs)

    def _translate(self, text_: str):
        try:
            return self._translator.translate(text=text_, src=self._src, dest=self._dest)
        except Exception as ex:
            print(f'{ex} {text_}')
            return []

    def translate_book(self, book: Book, sleep_time=5) -> Book:
        translated_book_name = self._translate(book.name).text
        translated_book_author = self._translate(book.author).text
        translated_book = Book(translated_book_name, translated_book_author)
        for chapter in book.chapters_list:
            chapter_name = self._translate(chapter.name).text
            chapter_content = [par.text for par in self._translate(chapter.content)]
            time.sleep(sleep_time)
            translated_book.add_chapter(chapter_name, chapter_content)
            print(f'{chapter_name} translated')
        print(f'{book.name} translated')
        return translated_book
