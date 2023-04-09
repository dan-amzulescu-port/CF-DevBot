# Update requirements.txt & run lint

# Go one directory up
Set-Location ..

# Get the current working directory
$currentDirectory = Get-Location

# Set the path to the venv subfolder
$venvPath = Join-Path -Path $currentDirectory -ChildPath "venv"

# Change to the venv subfolder
Set-Location -Path $venvPath

# Run pip freeze to generate requirements.txt
pip freeze > ..\src\requirements.txt

# Change back to the original directory
Set-Location -Path $currentDirectory

# Run Flake8 for linting

# Check if flake8 is installed
if (-not (Get-Command flake8 -ErrorAction SilentlyContinue)) {
    Write-Host "flake8 is not installed. Installing..."
    # Install flake8 using pip
    pip install flake8
    Write-Host "flake8 installed successfully."
} else {
    Write-Host "flake8 is already installed."
}

# Set the path to the directory you want to start the recursive search from
$directoryPath = Join-Path -Path $currentDirectory -ChildPath "src"

# Loop through all Python files in the directory and its subdirectories
Get-ChildItem -Path $directoryPath -File -Recurse -Filter *.py | ForEach-Object {
    # Run Flake8 on the current Python file
    $output = flake8 --ignore=E501 $_.FullName 2>&1

    # Check if there are any error messages
    if ($output -match ":(\d+):\d+:") {
        # Add the error messages to the array
        $errors += $output
    }
}

# Check if there are any errors
if ($errors.Count -eq 0) {
    Write-Host "Hooray! No errors."
} else {
    # Output the flake8 error messages
    $errors
}