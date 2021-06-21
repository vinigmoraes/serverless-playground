import json

from books.application.functions.request.add_book_cover_image import AddCoverImageRequest
from books.core.usecases.add_cover_image_usecase import AddCoverImageUseCase


def execute(event, context, use_case: AddCoverImageUseCase = None):
    use_case = use_case or AddCoverImageUseCase()

    book_id = event["pathParameters"]["id"]

    request = AddCoverImageRequest.from_json(json.loads(event["body"]))

    use_case.add(book_id, request.cover_image_base64)

    return {
        "statusCode": 200
    }
