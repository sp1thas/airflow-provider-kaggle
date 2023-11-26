import os

from airflow.models.connection import Connection


class CredentialsTemporaryFile:
    def __init__(self, connection: Connection):
        self.connection = connection
        self.folder_path = os.path.join(os.environ.get("HOME", ""), ".kaggle")
        os.makedirs(self.folder_path, exist_ok=True)
        self.file_path = os.path.join(self.folder_path, "kaggle.json")
        self.extra = self.connection.extra_dejson
        if not self.extra.get("username"):
            raise ValueError("username is missing")
        if not self.extra.get("key"):
            raise ValueError("key is missing")

    def __enter__(self):
        self.f = open(self.file_path, "w")
        self.f.write(self.connection.extra)
        self.f.close()
        os.chmod(self.file_path, 0o600)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.remove(self.file_path)
