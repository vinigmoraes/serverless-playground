from books.domain.book import Book
from books.infrastructure.book_repository import BookRepository
from books.application.functions.request.create_book_request import CreateBookRequest


class CreateBookUseCase:
    def __init__(self, book_repository: BookRepository = None):
        self.book_repository = book_repository or BookRepository()

    def create(self, request: CreateBookRequest):
        book = Book.create(request)

        self.book_repository.save(book)

        return book
