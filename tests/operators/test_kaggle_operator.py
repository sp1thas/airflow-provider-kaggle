import pytest

from kaggle_provider.operators.kaggle import KaggleOperator


@pytest.mark.skip(reason="not implemented yet")
def test_operator():
    operator = KaggleOperator(
        command=None,
        subcommand=None,
        optional_arguments={"v": True},
        task_id="run_operator",
        kaggle_conn_id="conn_kaggle",
    )
    stdout = operator.execute(context={})
    assert stdout == ""
