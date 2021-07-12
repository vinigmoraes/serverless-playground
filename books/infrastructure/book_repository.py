import logging
import os
from typing import Optional

import boto3

from books.core.domain.book import Book

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class BookRepository:
    def __init__(self, table_name=None):
        self._table_name = os.getenv("BOOK_TABLE_NAME", table_name)
        self._table = boto3.resource(
            "dynamodb"
        ).Table(self._table_name)

    def save(self, book: Book):
        book_json = {
            "id": str(book.id),
            "title": book.title,
            "isbn": book.isbn,
            "hardcover": book.hardcover,
            "pages": book.pages,
            "author": book.author,
            "cover_image_link": book.cover_image_link
        }

        self._table.put_item(Item=book_json)

    def find_by(self, book_id) -> Optional[Book]:
        logger.info(f"Searching on database for book: {book_id}")

        try:
            response = self._table.get_item(Key={"id": book_id})

            logger.info(f"Book: {response['Item']} found on database")
        except KeyError:
            logger.info("Item not found in database")
            return None

        return Book.from_json(json=response["Item"])
