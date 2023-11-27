import os

from airflow.models.connection import Connection

KAGGLE_USERNAME = "KAGGLE_USERNAME"
KAGGLE_KEY = "KAGGLE_KEY"


class TemporaryCredentials:
    def __init__(self, connection: Connection):
        self.connection = connection
        self.extra = self.connection.extra_dejson
        if not self.extra.get("username"):
            raise ValueError("username is missing")
        if not self.extra.get("key"):
            raise ValueError("key is missing")
        self.user_before = os.getenv(KAGGLE_USERNAME)
        self.key_before = os.getenv(KAGGLE_KEY)

    def __enter__(self):
        os.environ[KAGGLE_USERNAME] = self.extra["username"]
        os.environ[KAGGLE_KEY] = self.extra["key"]

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.user_before:
            os.environ[KAGGLE_USERNAME] = self.user_before
        else:
            os.environ.pop(KAGGLE_USERNAME, None)
        if self.key_before:
            os.environ[KAGGLE_KEY] = self.key_before
        else:
            os.environ.pop(KAGGLE_KEY, None)
