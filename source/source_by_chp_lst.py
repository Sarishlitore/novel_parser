from source.source import *


class SourceByChapterList(Source, ABC):
    def __init__(self, book_url: str, book_title_xpath: str, book_author_xpath: str, chapter_list_url: str,
                 chapter_title_xpath: str, chapter_content_xpath: str):
        super().__init__(book_url, book_title_xpath, book_author_xpath)
        self._chapter_list_url = chapter_list_url
        self._chapter_title_xpath = chapter_title_xpath
        self._chapter_content_xpath = chapter_content_xpath

    def scape_chapter_url_list(self):
        pass

