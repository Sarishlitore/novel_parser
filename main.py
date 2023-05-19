from book_reader.fb2_reader import Fb2Reader
from book_translator.book_translator import BookTranslator
from book_writer.fb2_writer import FB2Writer
from source.source_by_nxt_btn import Fanfiction, Novelnext, Scribblehub

if __name__ == '__main__':
    scribble = Scribblehub.form_source('https://www.scribblehub.com/series/525262/vice-captain-of-straw-hat-pirates/',
                                       'https://www.scribblehub.com/read/525262-vice-captain-of-straw-hat-pirates/chapter/525263/',
                                       'https://www.scribblehub.com/read/525262-vice-captain-of-straw-hat-pirates/chapter/713796/')
    book = scribble.scrape()
    book_translator = BookTranslator('en', 'ru')
    translated_book = book_translator.translate_book(book)
    book_writer = FB2Writer()
    book_writer.write(translated_book, 'book_test')
