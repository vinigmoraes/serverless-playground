import logging

import boto3

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class BucketRepository:
    _s3_client = boto3.client('s3')

    def __init__(self, bucket_name, folder):
        self.bucket_name = bucket_name
        self.folder = folder

    def upload(self, file, book_id):
        logger.info(f"Uploading file: {file} to bucket: {self.bucket_name}/{self.folder}")

        self._s3_client.upload_file(file, f"{self.bucket_name}", f"{self.folder}/{book_id}.png")
