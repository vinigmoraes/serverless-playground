class BookNotFoundException(Exception):

    def __init__(self, book_id):
        self.message = f"Book: {book_id} not found"
        self.status_code = 404
