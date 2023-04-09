#!/bin/bash

# Go one directory up
cd ..

# Get the username and password from environment variables
quayIoUsername="$dev_bot_user"
quayIoPassword="$dev_bot_pass"

# Define the Docker image name and tag
dockerImageName="devbot
dockerImageTag="latest"

# Build the Docker image
docker build -t "$dockerImageName:$dockerImageTag" .

# Log in to the quay.io container registry
docker login quay.io -u "$quayIoUsername" -p "$quayIoPassword"

# Tag the Docker image with the quay.io repository
quayIoRepository="quay.io/codefresh_sa/DevBot"
docker tag "$dockerImageName:$dockerImageTag" "$quayIoRepository:$dockerImageTag"

# Push the Docker image to the quay.io container registry
docker push "$quayIoRepository:$dockerImageTag"

# Clean up: remove the local Docker image
docker rmi "$dockerImageName:$dockerImageTag"
