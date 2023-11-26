from __future__ import annotations

from typing import Any, Tuple, Dict, Optional, Union

from airflow.hooks.base import BaseHook


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

    @staticmethod
    def get_connection_form_widgets() -> dict[str, Any]:
        """Returns connection widgets to add to connection form"""
        from flask_appbuilder.fieldwidgets import (
            BS3PasswordFieldWidget,
            BS3TextFieldWidget,
        )
        from flask_babel import lazy_gettext
        from wtforms import PasswordField, StringField

        return {
            "user": StringField(lazy_gettext("User"), widget=BS3TextFieldWidget()),
            "key": PasswordField(lazy_gettext("Key"), widget=BS3PasswordFieldWidget()),
        }

    @staticmethod
    def get_ui_field_behaviour() -> dict:
        """Returns custom field behaviour"""
        import json

        return {
            "hidden_fields": [],
            "relabeling": {},
            "placeholders": {
                "extra": json.dumps(
                    {
                        "example_parameter": "parameter",
                    },
                    indent=4,
                ),
                "user": "HeirFlough",
                "key": "mY53cr3tk3y!",
            },
        }

    def __init__(
        self,
        kaggle_conn_id: str = default_conn_name,
    ) -> None:
        super().__init__()
        self.kaggle_conn_id = kaggle_conn_id
        self.creds = None

    def get_conn(self) -> Dict[str, str]:
        """
        Returns kaggle credentials.
        """
        conn = self.get_connection(self.kaggle_conn_id)

        return {"KAGGLE_USER": conn.user, "KAGGLE_KEY": conn.key}

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
        from sh import kaggle

        self.creds = self.get_conn()

        command_base = []
        if command:
            command_base.append(command)
            if subcommand:
                command_base.append(subcommand)

        command = kaggle.bake(*command_base, **optional_arguments, _env=self.creds)

        self.log.info(f"Running: f{str(command)}")

        return command()

    def test_connection(self) -> Tuple[bool, str]:
        """Test a connection"""
        try:
            self.run(command=None, subcommand=None, v=True)
            return True, "Connection successfully tested"
        except Exception as e:
            return False, str(e)
