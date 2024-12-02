from visa_approval.pipline.training_pipeline import TrainPipeline

if __name__ == "__main__":
    pipeline = TrainPipeline()  # Create an instance
    pipeline.run_pipeline()      # Call the method on the instance
