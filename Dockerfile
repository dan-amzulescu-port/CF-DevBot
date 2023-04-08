# Use Python 3.11 base image
FROM python:3.11

# Set working directory
WORKDIR /app

# Install git
RUN apt-get update && apt-get install -y git

# Clone the repository
RUN git clone https://github.com/aperture-sci/devbot.git

# Change to the cloned repository's directory
WORKDIR /app/devbot

# Install requirements
RUN pip install -r src/requirements.txt

# Set back to the working directory
WORKDIR /app

# Add any additional commands or configurations here, if needed

# Start your application or perform other actions as desired

