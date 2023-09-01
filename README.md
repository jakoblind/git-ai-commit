# git-ai-commit

Never write a git commit message again (unless you want to) with this tool. Set up a git commit hook calling this script that reads the diffs from git and sends them to ChatGTP API to generate a git commit message.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contribute](#contribute)
- [License](#license)

## Features

- **Automatic Commit Messages**: Automatically generates commit messages using ChatGPT.
- **Git Diff Context**: Utilizes the names of changed files and the diffs as context to produce more relevant commit messages.

## Installation

1. Ensure you have a working Python environment.
2. Install the required Python package:

   ```bash
   pip install requests
   ```

3. Clone this repository or download the scripts to a known location on your machine.
4. Update the Python script with your OpenAI API key.
5. Navigate to your target Git repository and set up the hook:

   - Navigate to .git/hooks within the repository.
   - If it doesn't already exist, create a file named prepare-commit-msg.
   - Add the hook script content as provided earlier.
   - Important: In the prepare-commit-msg hook, update the line GENERATED_MSG=$(python3 /path/to/chatgpt_commit.py) to point to the correct path of the `chatgpt_commit.py` script on your machine.
   - Make the `prepare-commit-msg` file executable:

   ```bash
   chmod +x .git/hooks/prepare-commit-msg
   ```

## Usage

When you run the git commit command without specifying the -m option, Git will automatically call the ChatGPT API to generate a commit message based on the changes you've made.

## Contribute

Feel free to dive in! Open an issue or submit pull requests. Contributions are always welcome.

## Disclaimer

Using this tool with extensive diffs or frequent commits may result in large amounts of data being sent to the ChatGPT API, potentially leading to significant API costs. Always monitor your usage and adjust as necessary. I am not responsible for any unexpected charges or excessive costs associated with the use of this tool.

## License

MIT © Jakob Lind
