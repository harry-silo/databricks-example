import mlflow 
mlflow.set_experiment('/Shared/pipeline')
with mlflow.start_run() as run:
    mlflow.log_param("train", 0.01)