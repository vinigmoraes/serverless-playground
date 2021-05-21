from unittest.mock import MagicMock

import pytest
from _pytest.fixtures import fixture

from books.domain.book import Book
from books.domain.exceptions.book_not_found_exception import BookNotFoundException
from books.domain.usecases.find_book_usecase import FindBookUseCase
from books.infrastructure.book_repository import BookRepository


class TestFindBookUseCase:
    _book_id = "BOOK-123"

    @fixture()
    def repository(self):
        return MagicMock(spec=BookRepository("books"))

    @fixture
    def use_case(self, repository):
        return FindBookUseCase(repository)

    def test_should_return_book_successfully(self, use_case, repository):
        expected_response = Book(book_id=self._book_id, title="Clean Code")

        repository.find_by = MagicMock(return_value=expected_response)

        book = use_case.find(self._book_id)

        assert expected_response.title == book.title

    def test_should_raise_exception_when_book_is_not_found(self, use_case, repository):
        repository.find_by = MagicMock(return_value=None)

        with pytest.raises(BookNotFoundException):
            use_case.find(self._book_id)
