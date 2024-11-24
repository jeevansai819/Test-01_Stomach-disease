# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dataset and Python script to the container
COPY stomach_diseases_dataset.csv .
COPY display_dataset.py .

# Run the Python script
CMD ["python", "display_dataset.py"]
