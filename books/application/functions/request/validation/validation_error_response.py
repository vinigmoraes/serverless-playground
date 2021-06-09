from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json

from books.application.functions.request.validation.error_response import ValidationError


@dataclass_json
@dataclass
class ValidationErrorResponse:
    errors: List[ValidationError]
