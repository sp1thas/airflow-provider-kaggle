"""
Unittest module to test Hooks.

Requires the unittest, pytest, and requests-mock Python libraries.

Run test:

    python3 -m unittest tests.hooks.test_kaggle.TestKaggleHook

"""

import logging
from unittest import mock

import requests_mock

# Import Hook
from kaggle_provider.hooks.kaggle import KaggleHook

log = logging.getLogger(__name__)


# Mock the `conn_kaggle` Airflow connection
@mock.patch.dict(
    "os.environ", AIRFLOW_CONN_CONN_KAGGLE="http://https%3A%2F%2Fwww.httpbin.org%2F"
)
class TestKaggleHook:
    """
    Test Kaggle Hook.
    """

    @requests_mock.mock()
    def test_post(self, m):
        # Mock endpoint
        m.post("https://www.httpbin.org/", json={"data": "mocked response"})

        # Instantiate hook
        hook = KaggleHook(kaggle_conn_id="conn_kaggle", method="post")

        # Kaggle Hook's run method executes an API call
        response = hook.run()

        # Retrieve response payload
        payload = response.json()

        # Assert success status code
        assert response.status_code == 200

        # Assert the API call returns expected mocked payload
        assert payload["data"] == "mocked response"

    @requests_mock.mock()
    def test_get(self, m):
        # Mock endpoint
        m.get("https://www.httpbin.org/", json={"data": "mocked response"})

        # Instantiate hook
        hook = KaggleHook(
            kaggle_conn_id="conn_kaggle",
        )

        # Kaggle Hook's run method executes an API call
        response = hook.run()

        # Retrieve response payload
        payload = response.json()

        # Assert success status code
        assert response.status_code == 200

        # Assert the API call returns expected mocked payload
        assert payload["data"] == "mocked response"
