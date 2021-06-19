from logging import Logger

import boto3

logger = Logger(__name__)


class BucketRepository:
    _s3_client = boto3.client('s3')

    def __init__(self, bucket_name, folder):
        self.bucket_name = bucket_name
        self.folder = folder

    def upload(self, file):
        logger.info(f"Uploading file: {file} to bucket: {self.bucket_name}")

        self._s3_client.put_object(Body=file, Bucket=f"{self.bucket_name}/{self.folder}")
