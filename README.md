# **Simple Quiz Game with Docker**
This project demonstrates how to create a Python console application (a simple quiz game) and containerize it using Docker.

## **Table of Contents**
- [Setup Instructions](#setup-instructions)
- [Usage Examples](#usage-examples)
- [Versioning and Tags](#versioning-and-tags)
- [Explanation of Docker Concepts Used](#explanation-of-docker-concepts-used)
- [Screenshots](#screenshots)
- [Folder Structure](#folder-structure)

## **Setup Instructions**

### **Prerequisites**
- Docker installed on your machine. [Install Docker](https://docs.docker.com/get-docker/)
- Git (optional, for cloning the repository)

### **Steps to Run the Application**

#### **Clone the Repository (if not already cloned):**
```sh
git clone https://github.com/JoPuskar/quiz-game-docker.git
cd quiz-game-docker
```

#### **Build the Docker Image:**
```sh
docker build -t quiz-game:1.0 .
```

#### **Run the Docker Container:**
```sh
docker run -it -v $(pwd)/results:/app/results quiz-game:1.0
```

#### **Check Results:**
The quiz results will be saved in the `results/quiz_results.txt` file on your local machine.

## **Usage Examples**

### **Running the Quiz Game**
When you run the container, the quiz game will start.

### **Viewing Results**
After completing the quiz, check the `results/quiz_results.txt` file:
```sh
cat results/quiz_results.txt
```

## **Versioning and Tags**
To ensure proper versioning, we use **Docker tags** to manage different releases of the project.

### **Tagging the Docker Image Properly**
Each build should have a version tag:
```sh
docker build -t quiz-game:1.0 .
```
We also create additional tags:
```sh
# Tag the image with "latest"
docker tag quiz-game:1.0 quiz-game:latest

# Tag the image for "staging"
docker tag quiz-game:1.0 quiz-game:staging
```

### **Pushing Tagged Versions to Docker Hub**
1. **Login to Docker Hub**  
   ```sh
   docker login
   ```
2. **Tag the image with your Docker Hub username**  
   ```sh
   docker tag quiz-game:1.0 your-dockerhub-username/quiz-game:1.0
   ```
   
3. **Push the tagged image**  
   ```sh
   docker push your-dockerhub-username/quiz-game:1.0
   docker push your-dockerhub-username/quiz-game:latest
   ```

### **Using Tags in `docker-compose.yml`**
If using **Docker Compose**, specify the version tag inside `docker-compose.yml`:
```yaml
version: '3'
services:
  quiz-game:
    image: your-dockerhub-username/quiz-game:1.0
    ports:
      - "5000:5000"
```

### **Pulling Specific Versions**
When running a container, specify the correct tag:
```sh
# Run version 1.0
docker run -it quiz-game:1.0

# Run the latest version
docker run -it quiz-game:latest
```

## **Explanation of Docker Concepts Used**

### **1. Dockerfile**
The `Dockerfile` defines the environment and steps to build the Docker image.

**Key components:**
- **Base Image:** `python:3.9-slim` is used as the base image to ensure Python is available.
- **WORKDIR:** Sets the working directory inside the container to `/app`.
- **COPY:** Copies the `quiz_game.py` script into the container.
- **ENTRYPOINT:** Specifies the command to run when the container starts (`python quiz_game.py`).
- **VOLUME:** Mounts a volume to persist quiz results outside the container.

### **2. Volume Mounting**
The `-v $(pwd)/results:/app/results` flag in the `docker run` command mounts a local directory (`results`) to the container's `/app/results` directory.

This ensures that quiz results are saved on your local machine and persist even after the container is stopped.

### **3. Interactive Mode**
The `-it` flag in the `docker run` command enables interactive mode and allocates a pseudo-TTY, allowing the quiz game to accept user input.

## **Screenshots**
1. Running the Quiz Game
   
   ![Screenshot (6)](https://github.com/user-attachments/assets/a463981f-3aa8-404c-944b-6469e1618c86)
   ![Screenshot7](https://github.com/user-attachments/assets/6bd6acb4-97a4-46bc-90b8-a915b10b4af2)

2. Quiz Results File
   
   ![Screenshot (8)](https://github.com/user-attachments/assets/42155bc5-a9f8-46d3-bbdd-fced4c5aa9aa)

3. Versioning and Tags
   
   ![Screenshot (9)](https://github.com/user-attachments/assets/45686682-4580-408b-83fb-6a2a2f605e7f)

## **Folder Structure**
```
quiz-game-docker/
├── quiz_game.py          # Python quiz game script
├── Dockerfile            # Dockerfile for containerization
├── README.md             # Documentation
└── results/              # Directory for quiz results (created after running the container)
```

Enjoy the quiz game! 🚀

