<p align="center">
  <a href="https://www.airflow.apache.org">
    <img alt="Airflow" src="https://cwiki.apache.org/confluence/download/attachments/145723561/airflow_transparent.png?api=v2" width="60" />
  </a>
  <a href="https://www.kaggle.com">
    <img alt="Kaggle" src="https://storage.googleapis.com/kaggle-organizations/4/thumbnail.png" width="60" />
  </a>
</p>
<h1 align="center">
  Airflow Kaggle Provider
</h1>
  <h3 align="center">
  Airflow operators and hooks for interacting with the Kaggle API
</h3>

<br/>

## Installation

Pre-requisites: An environment running `apache-airflow` >= 2.0

```
pip install airflow-provider-kaggle
```

## Configuration

In the Airflow Connections UI, create a new connection for Hightouch.

- `Conn ID`: `kaggle_default`
- `Conn Type`: `Kaggle`
- `User`: `<username>`
- `Password`: `<password>`
