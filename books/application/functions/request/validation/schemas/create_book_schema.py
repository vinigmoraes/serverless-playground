CREATE_BOOK_SCHEMA = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "minLength": 1},
        "isbn": {"type": "string", "minLength": 13, "maxLength": 13},
        "hardcover": {"type": "boolean"},
        "book_cover_image": {"type": "string"},
        "pages": {"type": "number"},
        "author": {"type": "string"}
    },
    "required": [
        "title",
        "isbn",
        "hardcover",
        "book_cover_image",
        "pages",
        "author"
    ],
}
