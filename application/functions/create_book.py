import json

from domain.usecases.create_book_usecase import CreateBookUseCase
from application.application_call import ApplicationCall
from application.functions.book.request.create_book_request import CreateBookRequest
from application.functions.book.response.create_book_response import CreateBookResponse


def execute(event, context, use_case: CreateBookUseCase = None):
    use_case = use_case or CreateBookUseCase()

    json_body = json.loads(event["body"])

    request = CreateBookRequest.from_json(json_body)

    book = use_case.create(request)

    return ApplicationCall.respond(status_code=201, response=CreateBookResponse(book.id, book.title))
