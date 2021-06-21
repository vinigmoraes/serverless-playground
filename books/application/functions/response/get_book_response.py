from dataclasses import dataclass

from dataclasses_json import dataclass_json

from books.core.domain.book import Book


@dataclass
@dataclass_json
class GetBookResponse:
    id: str
    title: str
    isbn: str
    hardcover: bool
    pages: int
    author: str
    cover_image_link: str

    def __init__(self, book: Book):
        self.id = str(book.id)
        self.title = book.title
        self.isbn = book.isbn
        self.hardcover = book.hardcover
        self.author = book.author
        self.pages = book.pages
        self.cover_image_link = book.cover_image_link
