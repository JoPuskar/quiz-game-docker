# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY quiz_game.py .

# Install any necessary dependencies (None so far)

# Set the entry point to run the Python Script
ENTRYPOINT ["python", "quiz_game.py"]

# Use a volume to persist quiz results
VOLUME /app/results
