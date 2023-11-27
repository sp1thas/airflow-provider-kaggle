def test_hook_creds(conn):
    assert conn.conn_id == "kaggle_default"
    assert conn.conn_type == "kaggle"


def test_hook_datasets_list(hook):
    resp = hook.run("datasets_list", user="sp1thas", sort_by="votes")

    assert resp[0]["creatorUrl"] == "sp1thas"


def test_hook_competitions_list(hook):
    resp = hook.run(
        "competitions_list",
        sort_by="numberOfTeams",
        search="Titanic - Machine Learning from Disaster",
    )
    assert len(resp) == 1
    assert resp[0]["titleNullable"] == "Titanic - Machine Learning from Disaster"
