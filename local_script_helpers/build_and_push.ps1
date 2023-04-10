# Go one directory up
Set-Location ..

# Get the username and password from environment variables
$quayIoUsername = $env:dev_bot_user
$quayIoPassword = $env:dev_bot_pass

# Define the Docker image name and tag
$dockerImageName = "devbot"

# Get the latest release tag from GitHub
$latestRelease = (Invoke-RestMethod -Uri "https://api.github.com/repos/aperture-sci/DevBot/releases/latest").tag_name

# Build the Docker image with the latest release tag
docker build -t "$dockerImageName:$latestRelease" .

# Log in to the quay.io container registry
docker login quay.io -u $quayIoUsername -p $quayIoPassword

# Tag the Docker image with the quay.io repository and latest release tag
$quayIoRepository = "quay.io/codefresh_sa/DevBot"
docker tag "$dockerImageName:$latestRelease" "$quayIoRepository:$latestRelease"

# Push the Docker image to the quay.io container registry
docker push "$quayIoRepository:$latestRelease"

# Clean up: remove the local Docker image
docker rmi "$dockerImageName:$latestRelease"
