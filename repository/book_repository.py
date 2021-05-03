import os

import boto3

from domain.book import Book


class BookRepository:
    __table = boto3.resource("dynamodb").Table(os.environ["BOOK_TABLE_NAME"])

    def save(self, book: Book):
        self.__table.put_item(Book=book.to_json())
