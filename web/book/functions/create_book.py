import json

from domain.usecases.create_book_use_case import CreateBookUseCase
from web.book.application_call import ApplicationCall
from web.book.request.create_book_request import CreateBookRequest
from web.book.response.create_book_response import CreateBookResponse


def execute(event, context):
    use_case = CreateBookUseCase()

    json_body = json.loads(event["body"])

    request = CreateBookRequest.from_json(json_body)

    book = use_case.create(request)

    return ApplicationCall.respond(status_code=201, response=CreateBookResponse(book.id, book.title))
