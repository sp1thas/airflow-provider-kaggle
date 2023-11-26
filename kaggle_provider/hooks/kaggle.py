from __future__ import annotations

import os.path
import traceback
from typing import Any, Tuple, Optional, Union

import sh
from airflow.hooks.base import BaseHook
from airflow.models.connection import Connection

from kaggle_provider.utils.credentials import CredentialsTemporaryFile


class KaggleHook(BaseHook):
    """
    Kaggle Hook that interacts with Kaggle API.

    :param kaggle_conn_id: connection that has the kaggle authentication credentials.
    :type kaggle_conn_id: str
    :param kaggle_bin_path: Kaggle binary path.
    :type kaggle_bin_path: str
    """

    conn_name_attr = "kaggle_conn_id"
    default_conn_name = "kaggle_default"
    conn_type = "kaggle"
    hook_name = "Kaggle"

    @classmethod
    def get_ui_field_behaviour(cls) -> dict[str, Any]:
        """Returns custom field behaviour"""

        return {
            "hidden_fields": ["host", "schema", "port", "login", "password"],
        }

    def __init__(
        self,
        kaggle_conn_id: str = default_conn_name,
        kaggle_bin_path: str | None = None,
    ) -> None:
        super().__init__()
        self.kaggle_conn_id = kaggle_conn_id
        self.kaggle_bin_path = kaggle_bin_path or self._get_kaggle_bin()

        if self.kaggle_bin_path and not os.path.exists(self.kaggle_bin_path):
            raise RuntimeError(f"{self.kaggle_bin_path} does not exist")

        self.command = sh.Command(self.kaggle_bin_path)

    @staticmethod
    def _get_kaggle_bin() -> Optional[str]:
        potential_paths = (
            os.path.join(os.getenv("HOME", ""), ".local", "bin", "kaggle"),
        )
        for p_path in potential_paths:
            if os.path.exists(p_path):
                return p_path
        raise RuntimeError("kaggle binary can not be found")

    def get_conn(self) -> Connection:
        """
        Returns kaggle connection.
        """
        return self.get_connection(self.kaggle_conn_id)

    def run(
        self,
        command: Optional[str] = None,
        subcommand: Optional[str] = None,
        **optional_arguments: Union[str, bool],
    ) -> str:
        """
        Performs the kaggle command

        :param command: kaggle command
        :type command: str
        :param subcommand: kaggle subcommand
        :type subcommand: str
        :param optional_arguments: additional kaggle command optional arguments
        :type optional_arguments: dict
        """
        command_base = []
        if command:
            command_base.append(command)
            if subcommand:
                command_base.append(subcommand)

        command = self.command.bake(*command_base, **optional_arguments)  # type: ignore

        with CredentialsTemporaryFile(connection=self.get_conn()):
            stdout = command()  # type: ignore

        self.log.info(f"\n{stdout}\n")  # type: ignore
        return stdout

    def test_connection(self) -> Tuple[bool, str]:
        """Test a connection"""
        try:
            self.run(command="config", subcommand="view")
            return True, "Connection successfully tested"
        except Exception as e:
            return False, "\n".join(traceback.format_exception(e))
