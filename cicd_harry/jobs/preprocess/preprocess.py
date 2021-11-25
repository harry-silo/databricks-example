import mlflow 
mlflow.set_experiment('pipeline')
with mlflow.start_run() as run:
    mlflow.log_param("preprocess", 0.01)