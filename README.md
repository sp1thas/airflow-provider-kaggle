<p align="center">
  <a href="https://www.airflow.apache.org">
    <img alt="Airflow" src="https://cwiki.apache.org/confluence/download/attachments/145723561/airflow_transparent.png?api=v2" width="60" />
  </a>
  <a href="https://www.kaggle.com">
    <img alt="Kaggle" src="https://www.svgrepo.com/show/349422/kaggle.svg" width="60" />
  </a>
</p>
<h1 align="center">
  Airflow Kaggle Provider
</h1>
<h3 align="center">
  Airflow operators and hooks for interacting with the Kaggle API
</h3>
<p align="center">
    <img alt="Mypy checked" src="https://img.shields.io/badge/mypy-checked-blue">
    <img alt="Code style: Black" src="https://img.shields.io/badge/code%20style-black-black">
    <img alt="pre-commit enabled" src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white">
    <img alt="Apache Airflow version" src="https://img.shields.io/badge/Apache_Airflow-%3E=2.0-orange">
</p>

## Overview

This airflow provider allows you to interact with the Kaggle API using the corresponding CLI tool. This provider is
implemented in an abstract way in order to provide the maximum backward and forward compatibility, as a result,
using this provider you can run any command supported by the [kaggle-api](https://github.com/Kaggle/kaggle-api).

## Installation

Pre-requisites: An environment running `apache-airflow` >= 2.0

```shell
pip install airflow-provider-kaggle
```

## Configuration

In order to use this airflow-provider, you have to create a `kaggle` connection:

- `Conn ID`: `kaggle_default`
- `Conn Type`: `Kaggle`
- `Extra`: `<kaggle.json>`

**NOTE**: More details on how to get your Kaggle credentials are available [here](https://github.com/Kaggle/kaggle-api#api-credentials)

## Usage

### Operators

#### `kaggle_provider.operators.kaggle.KaggleOperator`

This is the main operator that can be used to execute any kaggle cli command:

```python
from kaggle_provider.operators.kaggle import KaggleOperator

list_competitions_op = KaggleOperator(
    task_id='foo',
    command='competitions_list',
    op_kwargs={'sort_by': 'prize'}
)
```

### Hooks

#### `kaggle_provider.hooks.kaggle.KaggleHook`

This is the kaggle hook which is used by the operator and can also be used directly
in your custom operator too.

```python
from kaggle_provider.hooks.kaggle import KaggleHook

hook = KaggleHook()
hook.run('datasets_list', sort_by="votes", user="sp1thas")
```


### Available commands

 - `competitions_list`
 - `competition_submit`
 - `competition_submissions`
 - `competition_list_files`
 - `competition_download_file`
 - `competition_download_files`
 - `competition_leaderboard_download`
 - `competition_leaderboard_view`
 - `dataset_list`
 - `dataset_metadata_prep`
 - `dataset_metadata_update`
 - `dataset_metadata`
 - `dataset_list_files`
 - `dataset_status`
 - `dataset_download_file`
 - `dataset_download_files`
 - `dataset_create_version`
 - `dataset_initialize`
 - `dataset_create_new`
 - `download_file`
 - `kernels_list`
 - `kernels_initialize`
 - `kernels_push`
 - `kernels_pull`
 - `kernels_output`
 - `kernels_status`
 - `model_get`
 - `model_list`
 - `model_initialize`
 - `model_create_new`
 - `model_delete`
 - `model_update`
 - `model_instance_get`
 - `model_instance_initialize`
 - `model_instance_create`
 - `model_instance_delete`
 - `model_instance_update`
 - `model_instance_version_create`
 - `model_instance_version_download`
 - `model_instance_version_delete`
 - `download_needed`

Details regarding the command arguments can be found in the corresponding method docstring of this
[module](https://github.com/Kaggle/kaggle-api/blob/main/kaggle/api/kaggle_api_extended.py)