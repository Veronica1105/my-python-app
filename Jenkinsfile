pipeline {
    // 'agent any' means Jenkins can use any available agent to run this pipeline
    agent any

    environment {
        // Define some variables for reuse. Docker image names must be lowercase.
        DOCKER_IMAGE_NAME     = "my-python-app"
        DOCKER_CONTAINER_NAME = "my-python-app-instance"
    }

    // The 'stages' block contains the main work of our pipeline
    stages {
        // Stage 1: Build the Docker image from our Dockerfile
        stage('1. Build Docker Image') {
            steps {
                // 'script' allows us to run shell commands
                script {
                    echo "Building Docker image..."
                    // The 'sh' step executes a shell command.
                    // ${BUILD_NUMBER} is a built-in Jenkins variable (e.g., 1, 2, 3...)
                    sh "docker build -t ${DOCKER_IMAGE_NAME}:${BUILD_NUMBER} ."
                }
            }
        }

        // Stage 2: Deploy the newly built image as a container
        stage('2. Deploy Application') {
            steps {
                script {
                    echo "Deploying container..."
                    // This is a small script to ensure no old container is running
                    sh """
                    if [ \$(docker ps -q -f name=${DOCKER_CONTAINER_NAME}) ]; then
                        echo "Stopping and removing old container..."
                        docker stop ${DOCKER_CONTAINER_NAME}
                        docker rm ${DOCKER_CONTAINER_NAME}
                    fi
                    """
                    // Run the new container using the image we just built
                    // We map port 5001 on the host to port 5000 in the container
                    sh "docker run -d --name ${DOCKER_CONTAINER_NAME} -p 5001:5000 ${DOCKER_IMAGE_NAME}:${BUILD_NUMBER}"
                }
            }
        }
    }

    // 'post' runs after all stages are complete
    post {
        // 'always' means this will run whether the pipeline succeeded or failed
        always {
            echo "Pipeline has finished."
        }
    }
}
```
