from __future__ import annotations

import pprint
from typing import TYPE_CHECKING, Any, Collection, Mapping

from airflow.models import BaseOperator

from kaggle_provider.hooks.kaggle import KaggleHook

if TYPE_CHECKING:
    from airflow.utils.context import Context


class KaggleOperator(BaseOperator):
    """
    :param command: kaggle command.
    :param op_args: Required positional arguments. (templated)
    :param op_kwargs: Optional keyword arguments. (templated)
    :param kaggle_conn_id: connection to run the operator with
    :type kaggle_conn_id: str
    """

    # Specify the arguments that are allowed to parse with jinja templating
    template_fields = ["command", "op_args", "op_kwargs"]
    template_fields_renderers = {"op_args": "py", "op_kwargs": "py"}
    template_ext = ()
    ui_color = "#20beff"

    def __init__(
        self,
        command: str,
        op_args: Collection[Any] | None = None,
        op_kwargs: Mapping[str, Any] | None = None,
        kaggle_conn_id: str = KaggleHook.default_conn_name,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.command = command
        self.op_args = op_args
        self.op_kwargs = op_kwargs
        self.kaggle_conn_id = kaggle_conn_id

    def execute(self, context: Context) -> Any:
        hook = KaggleHook(kaggle_conn_id=self.kaggle_conn_id)

        response = hook.run(self.command, *self.op_args or (), **self.op_kwargs or {})
        self.log.info(pprint.pformat(response))
        return response
