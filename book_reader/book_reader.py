from abc import ABC, abstractmethod
from book.book import Book


class BookReader(ABC):
    @abstractmethod
    def read(self, book_name: str, dirname='/') -> Book:
        pass
