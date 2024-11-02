# src/services/github_service.py

from github import Github
from github import PullRequest
def get_pull_request(repo_name, pr_number, token):
    print(f"Fetching pull request #{pr_number} from repository {repo_name}")
    g = Github(token)
    repo = g.get_repo(repo_name)
    return repo.get_pull(pr_number)

def post_comment(pr, message):
    print(f"Posting comment to pull request #{pr.number}")
    pr.create_issue_comment(message)

def get_changed_files(pr):
    changed_files = pr.get_files()
    file_changes = {}

    for file in changed_files:
        filename = file.filename
        patch = file.patch  # Diff of changes in unified format

        # Print the filename and patch for debugging
        print(f"File: {filename}")
        print("Changes:")
        print(patch)
        print("-" * 50)  # Separator for readability

        # Store changes for further processing
        file_changes[filename] = patch

    return file_changes

def post_line_comment(pr: PullRequest, filename: str, line: int, message: str):
    # Get the latest commit SHA on the PR
    commit_id = pr.head.sha
    
    # Post the comment on the specified file and line
    pr.create_review_comment(
        body=message,
        commit_id=commit_id,
        path=filename,
        position=line  # Position of the line in the diff (not the absolute line number)
    )