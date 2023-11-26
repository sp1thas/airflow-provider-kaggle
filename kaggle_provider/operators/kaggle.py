from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Union

from airflow.exceptions import AirflowException
from airflow.models import BaseOperator

from kaggle_provider.hooks.kaggle import KaggleHook

if TYPE_CHECKING:
    from airflow.utils.context import Context


class KaggleOperator(BaseOperator):
    """
    Calls Kaggle CLI.

    :param kaggle_conn_id: connection to run the operator with
    :type kaggle_conn_id: str
    :param command: The Kaggle command. (templated)
    :type command: str
    :param subcommand: The Kaggle subcommand. (templated)
    :type subcommand: str
    :param optional_arguments: The Kaggle optional arguments. (templated)
    :type optional_arguments: a dictionary of key/value pairs
    """

    # Specify the arguments that are allowed to parse with jinja templating
    template_fields = [
        "command",
        "subcommand",
        "optional_arguments",
    ]
    template_fields_renderers = {"optional_arguments": "py"}
    template_ext = ()
    ui_color = "#f4a460"

    def __init__(
        self,
        *,
        command: str | None = None,
        subcommand: str | None = None,
        optional_arguments: Dict[str, Union[str, bool]] | None = None,
        kaggle_conn_id: str = KaggleHook.default_conn_name,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.kaggle_conn_id = kaggle_conn_id
        self.command = command
        self.subcommand = subcommand
        self.optional_arguments = optional_arguments or {}
        if kwargs.get("xcom_push") is not None:
            raise AirflowException(
                "'xcom_push' was deprecated, use 'BaseOperator.do_xcom_push' instead"
            )

    def execute(self, context: Context) -> Any:
        hook = KaggleHook(kaggle_conn_id=self.kaggle_conn_id)

        self.log.info("Call Kaggle CLI")
        output = hook.run(
            command=self.command, subcommand=self.subcommand, **self.optional_arguments
        )

        return output
