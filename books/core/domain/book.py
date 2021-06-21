import os
import uuid
from dataclasses import dataclass

from books.application.functions.request.create_book_request import CreateBookRequest


@dataclass
class Book:
    id: uuid
    title: str
    isbn: str
    hardcover: bool
    pages: int
    author: str
    cover_image_link: str = None

    @staticmethod
    def create(request: CreateBookRequest):
        return Book(
            id=uuid.uuid4(),
            title=request.title,
            isbn=request.isbn,
            hardcover=request.hardcover,
            pages=request.pages,
            author=request.author
        )

    @staticmethod
    def from_json(json):
        return Book(
            id=json['id'],
            title=json['title'],
            isbn=json['isbn'],
            hardcover=json['hardcover'],
            pages=json['pages'],
            author=json['author']
        )

    def add_cover_image_link(self):
        bucket = os.environ['APPLICATION_BUCKET']
        folder = os.environ['BOOK_COVER_IMAGE_FOLDER']
        link = f"https://{bucket}.s3.amazonaws.com/{folder}/{self.id}.png"

        self.cover_image_link = link
