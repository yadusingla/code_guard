# src/services/comment_service.py

def format_comment(analysis_result, tool_name):
    print(f"Formatting comment with tool: {tool_name}")
    print(f"Analysis result: {analysis_result}")
    formatted_comment = f"[{tool_name} Analysis]\n{analysis_result}"
    print(f"Formatted comment: {formatted_comment}")
    return formatted_comment
