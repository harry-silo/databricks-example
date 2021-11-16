from fashionMnistDataset.common import Job
import mlflow

class SampleJob(Job):

    def launch(self):
        self.logger.info("Launching sample job")

        listing = self.dbutils.fs.ls("dbfs:/")

        for l in listing:
            self.logger.info(f"DBFS directory: {l}")

        df = self.spark.range(0, 1000)

        df.write.format(self.conf["output_format"]).mode("overwrite").save(
            self.conf["output_path"]
        )
        
        self.logger.info("Sample job finished!")
        mlflow.set_experiment('first push')

if __name__ == "__main__":
    job = SampleJob()
    job.launch()
