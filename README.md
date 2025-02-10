# quiz-game-docker
Simple Quiz Game with Docker
This project demonstrates how to create a Python console application (a simple quiz game) and containerize it using Docker.

Table of Contents
Setup Instructions

Usage Examples

Explanation of Docker Concepts Used

Screenshots

Setup Instructions
Prerequisites
Docker installed on your machine. Install Docker

Git (optional, for cloning the repository).

Steps to Run the Application
Clone the Repository (if not already cloned):

bash
Copy
git clone https://github.com/JoPuskar/quiz-game-docker.git

cd quiz-game-docker

Build the Docker Image:
docker build -t quiz-game:1.0 .

Run the Docker Container:
docker run -it -v $(pwd)/results:/app/results quiz-game:1.0

Check Results:

The quiz results will be saved in the results/quiz_results.txt file on your local machine.

Usage Examples
Running the Quiz Game
When you run the container, the quiz game will start

Viewing Results
After completing the quiz, check the results/quiz_results.txt file:

cat results/quiz_results.txt

Output:

Explanation of Docker Concepts Used
1. Dockerfile
The Dockerfile defines the environment and steps to build the Docker image.

Key components:

Base Image: python:3.9-slim is used as the base image to ensure Python is available.

WORKDIR: Sets the working directory inside the container to /app.

COPY: Copies the quiz_game.py script into the container.

ENTRYPOINT: Specifies the command to run when the container starts (python quiz_game.py).

VOLUME: Mounts a volume to persist quiz results outside the container.

2. Volume Mounting
The -v $(pwd)/results:/app/results flag in the docker run command mounts a local directory (results) to the container's /app/results directory.

This ensures that quiz results are saved on your local machine and persist even after the container is stopped.

3. Interactive Mode
The -it flag in the docker run command enables interactive mode and allocates a pseudo-TTY, allowing the quiz game to accept user input.

Screenshots:
1. Running the Quiz Game

2. Quiz Results File

Folder Structure
quiz-game-docker/
├── quiz_game.py          # Python quiz game script
├── Dockerfile            # Dockerfile for containerization
├── README.md             # Documentation
├── results/              # Directory for quiz results (created after running the container)
└── screenshots/          # Screenshots of the application running