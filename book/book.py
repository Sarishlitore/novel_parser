from dataclasses import dataclass


@dataclass
class Book:
    @dataclass
    class Chapter:
        _title: str
        _content: list[str]

        @property
        def title(self) -> str:
            return self._title

        @property
        def content(self) -> list[str]:
            return self._content

    _title: str = 'unknown'
    _author: str = 'unknown'
    _chapters_list = None

    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    @property
    def chapters_list(self) -> list[Chapter]:
        return self._chapters_list

    def add_chapter(self, chapter_title: str, chapter_content: list[str]):
        if self._chapters_list is None:
            self._chapters_list = []
        self._chapters_list.append(Book.Chapter(chapter_title, chapter_content))
