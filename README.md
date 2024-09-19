# Code Review API with OpenAI and Discord Integration

This project provides a Code Review API built with Python and FastAPI. It integrates with OpenAI's GPT-4 model to analyze code snippets and suggest improvements, and sends these suggestions to a Discord channel via a webhook.

The application can handle different programming languages such as Python, C#, and Java, offering suggestions for code improvement in each language. It runs in a Docker container and is set up to be built and published via GitHub Actions.

# Features

* Code Review Suggestions: Uses OpenAI’s GPT-4 to analyze code snippets and provide feedback.
* Discord Integration: Automatically sends code improvement suggestions to a Discord channel via a webhook.
* Supports Multiple Languages: Python, C#, and Java.
* Dockerized: The application is containerized using Docker.
* GitHub Actions: Automates building and publishing the Docker image to GitHub Packages.

# Prerequisites

* Docker
* Python 3.10 or higher
* OpenAI API key
* Discord Webhook URL
