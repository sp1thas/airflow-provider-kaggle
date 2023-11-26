__version__ = "1.0.0"


## This is needed to allow Airflow to pick up specific metadata fields it needs for certain features.
def get_provider_info():
    return {
        "package-name": "airflow-provider-kaggle",  # Required
        "name": "Kaggle",  # Required
        "description": "A airflow provider for Kaggle API",  # Required
        "connection-types": [
            {
                "connection-type": "kaggle",
                "hook-class-name": "kaggle_provider.hooks.kaggle.KaggleHook",
            }
        ],
        "extra-links": [],
        "versions": [__version__],  # Required
    }
