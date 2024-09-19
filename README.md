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