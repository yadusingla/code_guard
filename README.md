# Code Review Automation Tool

This tool automates the process of reviewing code changes in a GitHub pull request. It integrates with various services to provide AI-based code review, code quality analysis, and security checks.

## Features

- **AI Code Review**: Uses AI to review code changes and provide suggestions for improvements.
- **Code Quality Analysis**: Analyzes the code quality using tools like Pylint.
- **Security Checks**: Performs security checks on the codebase.

## Setup

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a `.env` file in the root directory and add the following environment variables:
    ```env
    GITHUB_TOKEN=<your-github-token>
    REPO_NAME=<repository-name>
    PR_NUMBER=<pull-request-number>
    ANTHROPIC_API_KEY=<your-anthropic-api-key>
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

Run the main script to start the code review process:
