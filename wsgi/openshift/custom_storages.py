
from django.conf import settings
from storages.backends.s3boto import S3BotoStorage
import os


class StaticStorage(S3BotoStorage):
    location = settings.STATICFILES_LOCATION

class MediaStorage(S3BotoStorage):
    location = settings.MEDIAFILES_LOCATION

    def isdir(self, str_path):
        return os.path.isdir(str_path)
