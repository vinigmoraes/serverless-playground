CREATE_BOOK_SCHEMA = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "minLength": 1},
        "isbn": {"type": "string", "minLength": 13, "maxLength": 13},
        "hardcover": {"type": "boolean"},
        "pages": {"type": "number"},
        "author": {"type": "string"}
    },
    "required": [
        "title",
        "isbn",
        "hardcover",
        "pages",
        "author"
    ],
}
