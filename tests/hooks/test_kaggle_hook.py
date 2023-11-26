import pytest

from kaggle_provider.hooks.kaggle import KaggleHook


@pytest.mark.skip(reason="not implemented yet")
def test_hook_creds():
    # Instantiate hook
    hook = KaggleHook(kaggle_conn_id="conn_kaggle")
    assert hook.creds == {"KAGGLE_USER": "foo", "KAGGLE_KEY": "bar"}
    stdout = hook.run(command=None, subcommand=None, v=True)
    assert stdout == ""
