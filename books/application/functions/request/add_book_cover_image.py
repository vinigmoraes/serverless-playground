class AddCoverImageRequest:
    cover_image_base64: str

    @classmethod
    def from_json(cls, json_body):
        cls.cover_image_base64 = json_body['cover_image_base64']

        return cls
