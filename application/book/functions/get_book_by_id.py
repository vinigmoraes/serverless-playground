from application.book.response.get_book_response import GetBookResponse
from core.domain.book import Book


def get(event, context):
    book = Book("Lord of The rings")

    json_response = GetBookResponse.create(book)

    return {
        "statusCode": 200,
        "body": json_response
    }
