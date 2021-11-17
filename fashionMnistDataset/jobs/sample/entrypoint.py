from fashionMnistDataset.common import Job
import mlflow

class SampleJob(Job):

    def launch(self):
        
        mlflow.set_experiment('first push')

if __name__ == "__main__":
    job = SampleJob()
    job.launch()
