import os
import uuid

from books.application.functions.request.create_book_request import CreateBookRequest


class Book:
    id: str
    title: str
    cover_image_link: str = None

    def __init__(self, book_id, title):
        self.id = book_id
        self.title = title

    @staticmethod
    def create(request: CreateBookRequest):
        return Book(
            book_id=uuid.uuid4(),
            title=request.title
        )

    @staticmethod
    def from_json(json):
        return Book(
            book_id=json['id'],
            title=json['title'],
        )

    def add_cover_image_link(self):
        bucket = os.environ['APPLICATION_BUCKET']
        folder = os.environ['BOOK_COVER_IMAGE_FOLDER']
        link = f"https://{bucket}.s3.amazonaws.com/{folder}/{self.id}.png"

        self.cover_image_link = link
