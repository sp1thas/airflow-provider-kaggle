import os
import unittest.mock

import pytest
from typing import Generator
from airflow.models.connection import Connection

from kaggle_provider.hooks.kaggle import KaggleHook


@pytest.fixture(scope="session")
def conn() -> Connection:
    return Connection(
        conn_id="kaggle_default", conn_type="kaggle", extra=os.getenv("KAGGLE_JSON")
    )


@pytest.fixture(scope="session")
def hook(conn) -> Generator[KaggleHook, None, None]:
    with unittest.mock.patch(
        "kaggle_provider.hooks.kaggle.KaggleHook.get_conn", return_value=conn
    ):
        yield KaggleHook()
