import json
import logging

from books.application.functions.response.get_book_response import GetBookResponse
from books.core.domain.exceptions.book_not_found_exception import BookNotFoundException
from books.core.usecases.find_book_usecase import FindBookUseCase

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def get(event, context, use_case: FindBookUseCase = None):
    use_case = use_case or FindBookUseCase()

    logger.info(f"Received request to find book: {event['pathParameters']['id']}")

    book_id = event["pathParameters"]["id"]

    try:
        book = use_case.find(book_id)
    except BookNotFoundException as e:
        logger.info("BookNotFoundException caught")

        return {
            "statusCode": e.status_code,
            "body": json.dumps({'message': e.message})
        }

    response = GetBookResponse.create(book)

    logger.info(f"Response of find book: {response}")

    return {
        "statusCode": 200,
        "body": response
    }
