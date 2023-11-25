from pendulum import datetime

from airflow.decorators import dag

from kaggle_provider.operators.kaggle import KaggleOperator
from kaggle_provider.sensors.kaggle import KaggleSensor


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

    Showcases the kaggle provider package's operator and sensor.

    To run this example, create a kaggle connection with:
    - id: kaggle_default
    - type: kaggle
    """
    pass


kaggle_workflow()
