#!/bin/bash

# Go one directory up
cd ..

# Get the username and password from environment variables
username=lrochette
password=$dev_bot_pass
repository=docker.io
# Define the Docker image name and tag
imageName="$username/devbot"

# Get the latest release tag from GitHub
#latestRelease=$(curl -s https://api.github.com/repos/aperture-sci/DevBot-loan/releases/latest | jq -r .tag_name)
latestRelease=0.0.7

# Build the Docker image with the latest release tag
docker build --platform linux/amd64 -t "$imageName:$latestRelease" .

# Log in to the $repository container registry
docker login $repository -u "$username" -p "$password"

# Tag the Docker image with the $repository repository and latest release tag
#docker tag "$imageName:$latestRelease" "quay.io/$imageName:$latestRelease"

# Push the Docker image to the $repository container registry
docker push "$repository/$imageName:$latestRelease"

# Clean up: remove the local Docker image
#docker rmi "$imageName:$latestRelease"
