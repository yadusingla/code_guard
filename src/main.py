import os
from dotenv import load_dotenv
from services.github_service import *
from services.quality_service import *
from services.security_service import *
from services.comment_service import *
from services.ai_review_service import *

# Load environment variables from .env file
load_dotenv()

def main():
    repo_name = "Procol-Tech/procol-backend"
    pr_number = 5863

    # Retrieve GitHub token from environment variable
    print("Retrieving GitHub token from environment variable...")
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise ValueError("GITHUB_TOKEN environment variable not set.")
    print("GitHub token retrieved successfully.")

    # Get PR data
    print(f"Fetching pull request #{pr_number} from repository {repo_name}...")
    pr = get_pull_request(repo_name, pr_number, token)
    print(f"Pull request title: {pr.title}")
    print(f"Author: {pr.user.login}")
    print(f"Pull request #{pr_number} fetched successfully.")

    # Get changed files
    print("Getting changed files...")
    file_changes = get_changed_files(pr)
    print("Changed files fetched successfully.")

    # Run AI review
    print("Running AI review...")
    ai_suggestions = review_code_with_ai(file_changes)
    print("AI review completed.")

    # Run code quality analysis
    # print("Running code quality analysis...")
    # quality_result = analyze_code_quality()
    # print("Code quality analysis completed.")
    # formatted_quality_comment = format_comment(quality_result, "Pylint")
    # print("Posting code quality analysis comment to pull request...")
    # post_comment(pr, formatted_quality_comment)
    # print("Code quality analysis comment posted successfully.")

    # # Run security checks
    # print("Running security checks...")
    # security_result = check_security()
    # print("Security checks completed.")
    # formatted_security_comment = format_comment(security_result, "Bandit")
    # print("Posting security analysis comment to pull request...")
    # post_comment(pr, formatted_security_comment)
    # print("Security analysis comment posted successfully.")

if __name__ == "__main__":
    main()
