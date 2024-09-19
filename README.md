# Code Wise: Code Review and Discord Notifier

This Python script reviews code snippets using OpenAI's GPT model and sends improvement suggestions to a Discord channel.

## Features

- **Code Review:** Uses OpenAI's GPT model to suggest improvements for the given code snippet.
- **Discord Integration:** Sends the code review suggestions to a specified Discord channel.

## Prerequisites

- Python 3.x
- Docker (optional, for containerized environments)
- `python-dotenv` library (for loading environment variables)
- OpenAI API key
- Discord Webhook URL

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
   cd YOUR_REPOSITORY
    ```
2. **Create a .env file:**

Create a .env file in the root of the project and add your OpenAI API key and Discord Webhook URL

```bash
OPENAI_API_KEY=your_openai_api_key
OPENAI_ENGINE=gpt-4
DISCORD_WEBHOOK_URL=your_discord_webhook_url
```

# Usage

Run the script from the command line, passing the path to the code file and the programming language as arguments:

```bash
python application.py path/to/your/code_file.py python
```

## Usage on Gitlab Actions

```bash
jobs:
  review:
    runs-on: ubuntu-latest
    needs: build 
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Get committed code
        id: get_code
        run: |
          # Get the latest commit hash
          COMMIT_HASH=$(git rev-parse HEAD)
          
          # Extract the code changes
          git diff-tree --no-commit-id --name-only -r $COMMIT_HASH > files.txt
          
          # Check if files.txt is empty
          if [ ! -s files.txt ]; then
            echo "No files changed."
            exit 0
          fi
          
          # Concatenate the content of all changed files into one file
          for file in $(cat files.txt); do
            echo "Processing $file"
            # Ensure the file exists before trying to read it
            if [ -f "$file" ]; then
              echo "=== File: $file ===" >> combined_code.txt
              cat "$file" >> combined_code.txt
              echo "" >> combined_code.txt
            else
              echo "File $file does not exist."
            fi
          done
          
          # Check if combined_code.txt was created successfully
          if [ -f combined_code.txt ]; then
            echo "combined_code.txt created successfully."
          else
            echo "Failed to create combined_code.txt."
            exit 1
          fi
          
          # Output the combined code file as an artifact
          echo "::set-output name=code_file::combined_code.txt"
      
      
      - name: Log in to GitHub Packages
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: echo $GITHUB_TOKEN | docker login ghcr.io -u ${{ github.actor }} --password-stdin
  
      - name: Pull Docker image
        run: docker pull ghcr.io/leds-org/leds-tools-codewise:latest  

      - name: Run Docker container
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ENGINE: ${{ secrets.OPENAI_ENGINE }}
          DISCORD_WEBHOOK_URL: ${{ secrets.DISCORD_WEBHOOK_URL }}
        run: |          
          docker run \
            --env OPENAI_API_KEY=$OPENAI_API_KEY \
            --env OPENAI_ENGINE=$OPENAI_ENGINE \
            --env DISCORD_WEBHOOK_URL=$DISCORD_WEBHOOK_URL \
            -v $(pwd)/combined_code.txt:/app/combined_code.txt:ro \
            ghcr.io/leds-org/leds-tools-codewise:latest python /app/application.py /app/combined_code.txt python

```

## Parameters

* path/to/your/code_file.py: Path to the file containing the code you want to review.
* python: Programming language of the code (e.g., python, javascript, java).

The script will read the code from the specified file, generate improvement suggestions, and send them as a message to your Discord channel.

# Docker Usage

If you want to run this script in a Docker container, follow these steps:

1. **Build the Docker image**:

```bash

docker build -t code-review-discord .

```

2. **Run the Docker container**:

```bash

docker run --env-file .env -v $(pwd)/path/to/code:/app/code-review-discord code-review-discord python /app/code-review-discord/application.py /app/code-review-discord/code_file.py python
```

* Replace path/to/code with the directory containing your code file.
* Replace code_file.py with the name of your code file.

