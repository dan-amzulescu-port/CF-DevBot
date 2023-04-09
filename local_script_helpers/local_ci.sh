#!/bin/bash

# Update requirements.txt

# Go one directory up
cd ..

# Get the current working directory
currentDirectory=$(pwd)

# Set the path to the venv subfolder
venvPath="$currentDirectory/venv"

# Change to the venv subfolder
cd "$venvPath"

# Run pip freeze to generate requirements.txt
pip freeze > ../src/requirements.txt

# Change back to the original directory
cd "$currentDirectory"

# Run Flake8 for linting

# Check if flake8 is installed
if ! command -v flake8 >/dev/null 2>&1; then
    echo "flake8 is not installed. Installing..."
    # Install flake8 using pip
    pip install flake8
    echo "flake8 installed successfully."
else
    echo "flake8 is already installed."
fi

# Set the path to the directory you want to start the recursive search from
directoryPath="$currentDirectory/src"

# Create an array to store the flake8 error messages
errors=()

# Loop through all Python files in the directory and its subdirectories
find "$directoryPath" -name "*.py" -type f | while read -r file; do
    # Run Flake8 on the current Python file and capture the output
    output=$(flake8 --ignore=E501 "$file" 2>&1)

    # Check if there are any error messages
    if [[ $output =~ :[0-9]+:[0-9]+ ]]; then
        # Add the error messages to the array
        errors+=("$output")
    fi
done

# Check if there are any errors
if [ ${#errors[@]} -eq 0 ]; then
    echo "Hooray! No errors."
else
    # Output the flake8 error messages
    printf "%s\n" "${errors[@]}"
fi
