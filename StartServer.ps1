# Function to write colored output
function Write-ColoredText {
    param (
        [string]$text,
        [string]$color
    )
    Write-Host $text -ForegroundColor $color
}

# Set the DEV environment variable
Write-ColoredText "Setting DEV environment variable" "Magenta"
[System.Environment]::SetEnvironmentVariable("DEV", $true, [System.EnvironmentVariableTarget]::Process)


# Run 'pelican content' to create the appropriate output
Write-ColoredText "Running 'pelican content'..." "Magenta"
$pelicanContentResult = pelican content

# Check the exit code of 'pelican content'
if ($LASTEXITCODE -ne 0) {
    Write-ColoredText "Error: 'pelican content' failed." "Red"
    Write-Host $pelicanContentResult
} else {
    # Get command line arguments
    $arguments = $args
    Write-Host $pelicanContentResult
    # Check if the --reload flag is present
    if ($arguments -contains "-R" -or $arguments -contains "--reload"  ) {
        Write-ColoredText "Reload flag detected. Running 'pelican --autoreload --listen'." "Green"
        pelican --autoreload --listen
    } else {
        Write-ColoredText "No reload flag detected. Running 'pelican --listen'." "Green"
        pelican --listen
    }
}


