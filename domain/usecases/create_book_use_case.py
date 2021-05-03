from domain.book import Book
from repository.book_repository import BookRepository
from web.book.request.create_book_request import CreateBookRequest


class CreateBookUseCase:
    def __init__(self, book_repository: BookRepository=None):
        self.book_repository = book_repository or BookRepository()

    def create(self, request: CreateBookRequest):
        book = Book(title=request.title)

        self.book_repository.save(book)

        return book
