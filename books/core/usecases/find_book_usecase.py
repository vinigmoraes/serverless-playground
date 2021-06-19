import logging

from books.core.domain.exceptions.book_not_found_exception import BookNotFoundException
from books.infrastructure.book_repository import BookRepository

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class FindBookUseCase:
    def __init__(self, book_repository: BookRepository = None):
        self.book_repository = book_repository or BookRepository()

    def find(self, book_id):
        book = self.book_repository.find_by(book_id)

        if book is None:
            logger.info(f"Book {book_id} not found")
            raise BookNotFoundException(book_id)

        return book
