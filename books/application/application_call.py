class ApplicationCall:
    status_code: int
    body: str

    @staticmethod
    def respond(status_code: int, response=None):
        return {
            "statusCode": status_code,
            "body": response.to_json()
        }
