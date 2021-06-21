import base64
import os

from books.infrastructure.book_repository import BookRepository
from books.infrastructure.bucket_repository import BucketRepository


class AddCoverImageUseCase:
    def __init__(self, book_repository: BookRepository = None, bucket_repository: BucketRepository = None):
        self.book_repository = book_repository or BookRepository()
        self.bucket_repository = bucket_repository or BucketRepository(
            bucket_name=os.environ['APPLICATION_BUCKET'],
            folder=os.environ['BOOK_COVER_IMAGE_FOLDER']
        )

    def add(self, book_id, base64_cover_image):
        book = self.book_repository.find_by(book_id)

        book_cover_image = base64.b64decode(base64_cover_image)

        filename = open(f"{book.id}.png", "wb")
        filename.write(book_cover_image)
        filename.close()

        self.bucket_repository.upload(f"{book.id}.png", book_id)

        os.remove(f"{book.id}.png")

        book.add_cover_image_link()

        self.book_repository.save(book)
