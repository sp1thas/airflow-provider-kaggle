from pendulum import datetime

from airflow.decorators import dag

from kaggle_provider.operators.kaggle import KaggleOperator


@dag(
    start_date=datetime(2023, 1, 1),
    schedule=None,
    # ``default_args`` will get passed on to each task. You can override them on a per-task basis during
    # operator initialization.
    default_args={"retries": 2, "kaggle_conn_id": "kaggle_default"},
    tags=["example"],
)
def kaggle_workflow():
    """
    ### Kaggle DAG

    Showcases the kaggle provider package's operator.

    To run this example, create a kaggle connection with:
    - id: kaggle_default
    - type: kaggle
    """

    # $ kaggle c list --sort-by prize -v
    competitions_list_op = KaggleOperator(
        command="c",
        subcommand="list",
        optional_arguments={"sort-by": "prize", "v": True},
    )

    # $ kaggle d list --sort-by votes -m
    datasets_list_op = KaggleOperator(
        command="d",
        subcommand="list",
        optional_arguments={"sort-by": "votes", "m": True},
    )

    competitions_list_op >> datasets_list_op


kaggle_workflow()
