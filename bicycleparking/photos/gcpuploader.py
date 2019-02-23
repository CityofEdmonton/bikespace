from google.cloud import storage
import uuid
import os.path
import os
from django.conf import settings
from .photoupload import PhotoUploader


class GCPUploader(PhotoUploader):
    """This class is used for uploading pictures to Google Cloud Platform's blob store."""

    def __init__(self):
        self.client = storage.Client()
        self.bucket = self.client.get_bucket(settings.GCP_BUCKET)

    def write(self, filename, file):
        key = str(uuid.uuid1()) + os.path.splitext(filename)[1]
        blob = self.bucket.blob(key)
        blob.upload_from_file(file)
        return key

    def read(self, key):
        pass
