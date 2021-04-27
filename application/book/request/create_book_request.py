class CreateBookRequest:
    title: str

    @classmethod
    def from_json(cls, json_body):
        cls.title = json_body["title"]

        return cls
