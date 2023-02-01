from book_translator.book_translator import BookTranslator
from book_writer.book_writer import FB2Writer
from source.source_by_nxt_btn import Fanfiction, Novelnext

if __name__ == '__main__':
    novelnext = Novelnext.form_source('',
                                      '',
                                      '')
    book = novelnext.scrape(1)
    book_writer = FB2Writer()
    book_writer.write(book, 'book_test')
    book_translator = BookTranslator(src='en', dest='ru')
    translated_book = book_translator.translate_book(book)
    book_writer.write(translated_book, 'book_test')
