from __future__ import annotations

import json
import traceback
from typing import Any, Tuple

from airflow.hooks.base import BaseHook
from airflow.models.connection import Connection

from kaggle_provider._utils.credentials import TemporaryCredentials
from kaggle_provider._utils.encoder import DefaultEncoder


class KaggleHook(BaseHook):
    """
    Kaggle Hook that interacts with Kaggle API.

    :param kaggle_conn_id: connection that has the kaggle authentication credentials.
    :type kaggle_conn_id: str
    """

    conn_name_attr = "kaggle_conn_id"
    default_conn_name = "kaggle_default"
    conn_type = "kaggle"
    hook_name = "Kaggle"

    @classmethod
    def get_ui_field_behaviour(cls) -> dict[str, Any]:
        """Returns custom field behaviour"""

        return {
            "hidden_fields": ["port", "password", "login", "schema", "host"],
            "relabeling": {},
            "placeholders": {},
        }

    def __init__(
        self,
        kaggle_conn_id: str = default_conn_name,
    ) -> None:
        super().__init__()
        self.kaggle_conn_id = kaggle_conn_id

    def get_conn(self) -> Connection:
        """
        Returns kaggle connection.
        """
        return self.get_connection(self.kaggle_conn_id)

    def run(
        self,
        command: str,
        *args: Any,
        **kwargs: Any,
    ) -> Any:
        """
        Performs the kaggle command

        :param command: kaggle command
        :type command: str
        :param args: required positional kaggle command arguments
        :type kwargs: optional keyword kaggle command arguments
        """
        with TemporaryCredentials(connection=self.get_conn()):
            import kaggle

            try:
                clb = getattr(kaggle.api, command)
            except AttributeError as e:
                raise ValueError(f"Unknown command: {command}") from e

            response = clb(*args or (), **kwargs or {})

            return json.loads(json.dumps(response, cls=DefaultEncoder))

    def test_connection(self) -> Tuple[bool, str]:
        """Test a connection"""
        try:
            with TemporaryCredentials(connection=self.get_conn()):
                import kaggle

                return True, "Connection successfully tested"
        except Exception as e:
            return False, "\n".join(traceback.format_exception(e))  # type: ignore
