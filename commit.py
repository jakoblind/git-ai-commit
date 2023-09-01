import requests
import sys
import subprocess
import json

OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
OPENAI_API_ENDPOINT = "https://api.openai.com/v1/chat/completions"

HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {OPENAI_API_KEY}'
}


def get_git_diff():
    """
    Get the diff of the files that were changed.
    """
    return subprocess.getoutput('git diff --cached')


def get_changed_files():
    """
    Get the list of files that were changed.
    """
    return subprocess.getoutput('git diff --name-only --cached').split('\n')


def generate_commit_message():
    diff = get_git_diff()
    changed_files = get_changed_files()

    if not changed_files:
        print("No files have been changed.")
        sys.exit(1)

    payload = {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant for generating git commit messages."
            },
            {
                "role": "user",
                "content": f"Given that the changed files are {', '.join(changed_files)} and the changes are:\n{diff}\nGenerate a commit message for these changes:"
            }
        ],
        "model": "gpt-4",
        "max_tokens": 20
    }

    response = requests.post(
        OPENAI_API_ENDPOINT, headers=HEADERS, data=json.dumps(payload))

    if response.status_code == 200:
        response_data = response.json()
        if 'choices' in response_data and len(response_data['choices']) > 0:
            generated_message = response_data['choices'][0]['message']['content'].strip(
                '"')
            print(generated_message.strip())
        else:
            print("Unexpected response format from API.")
            sys.exit(1)
    else:
        print("Error calling API:", response.text)
        sys.exit(1)


if __name__ == "__main__":
    generate_commit_message()
