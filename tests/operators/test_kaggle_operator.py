from kaggle_provider.operators.kaggle import KaggleOperator


def test__operator_competitions_list(hook):
    operator = KaggleOperator(
        task_id="foo",
        command="competitions_list",
        op_kwargs={"sort_by": "numberOfTeams"},
    )
    response = operator.execute(context={})
    assert response[0]["titleNullable"] == "Titanic - Machine Learning from Disaster"
