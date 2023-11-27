__version__ = "1.0.0"


def get_provider_info():
    return {
        "package-name": "airflow-provider-kaggle",
        "name": "Kaggle",
        "description": "A airflow provider for Kaggle API",
        "connection-types": [
            {
                "connection-type": "kaggle",
                "hook-class-name": "kaggle_provider.hooks.kaggle.KaggleHook",
            }
        ],
        "extra-links": [],
        "versions": [__version__],
    }
