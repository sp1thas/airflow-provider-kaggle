from airflow.decorators import dag
from pendulum import datetime

from kaggle_provider.operators.kaggle import KaggleOperator


@dag(
    start_date=datetime(2023, 1, 1),
    schedule=None,
    tags=["kaggle"],
)
def kaggle_workflow():
    competitions_list_op = KaggleOperator(
        task_id="competitions_list",
        command="competitions_list",
        op_kwargs={"sort_by": "prize"},
    )

    datasets_list_op = KaggleOperator(
        task_id="datasets_list",
        command="datasets_list",
        op_kwargs={"sort_by": "votes", "user": "sp1thas"},
    )

    competitions_list_op >> datasets_list_op


kaggle_workflow()
