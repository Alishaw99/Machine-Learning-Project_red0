from visa_approval.pipline.training_pipeline import TrainPipleline

if __name__ == "__main__":
    pipeline = TrainPipleline()  # Create an instance
    pipeline.run_pipeline()      # Call the method on the instance
