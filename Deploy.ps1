# Function to write colored output
function Write-ColoredText {
    param (
        [string]$text,
        [string]$color
    )
    Write-Host $text -ForegroundColor $color
}

# Set the DEV environment variable
Write-ColoredText "Turning off DEV environment variable" "Magenta"
[System.Environment]::SetEnvironmentVariable("DEV", $null, [System.EnvironmentVariableTarget]::Process)

Write-ColoredText "Genereating production output" "Magenta"
$pelicanContentResult = pelican content


if ($LASTEXITCODE -ne 0) {
    Write-ColoredText "Error: 'pelican content' failed." "Red"
    Write-Host $pelicanContentResult
    exit
}

Write-ColoredText "Running ghp-import output to prepare output file" "Magenta"
$ghpImportResult = ghp-import output

if ($LASTEXITCODE -ne 0) {
    Write-ColoredText "Error: 'ghp-import output' failed." "Red"
    Write-Host $ghpImportResult
    exit
}

Write-ColoredText "Pushing new version to Github Pages" "Magenta"
$gitPushResult = git push origin gh-pages

if ($LASTEXITCODE -ne 0) {
    Write-ColoredText "Error: 'git push origin gh-pages' failed." "Red"
    Write-Host $gitPushResult
    exit
}
else{
    Write-ColoredText "Deploy succeded" "Green"
    exit
}

