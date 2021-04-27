import json

from application.book.application_call import ApplicationCall
from application.book.request.create_book_request import CreateBookRequest
from application.book.response.create_book_response import CreateBookResponse
from core.domain.book import Book
from core.domain.create_book_use_case import CreateBookUseCase


def execute(event, context, use_case=None):
    use_case = CreateBookUseCase()

    json_body = json.loads(event["body"])

    request = CreateBookRequest.from_json(json_body)

    book = Book(title=request.title)

    return ApplicationCall.respond(status_code=201, response=CreateBookResponse(book.id, book.title))
