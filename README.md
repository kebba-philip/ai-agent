# AI Code Agent
This is  a command-line AI coding agent build with Python. The agent uses LLM to understand coding tasks and interact with a project.

# Built With
- Python
- OpenAI Python SDK
- OpenRouter
- `argparse`
- `python-dotenv`
- `uv`


##  WARNING
`Do not give this program to others for them to use! It doesn't have all the security and safety features that a production AI agent would have. This is for learning purposes only.`

## Features

- AI-powered coding assistant
- List files and directories
- Read file contents
- Create and modify files
- Execute Python files
- Restrict file operations to a permitted working directory
- LLM tool/function calling
- Multi-step agent loop
- Optional token usage information
- Maximum iteration limit to prevent infinite loops


# Project Structure
```text
ai-agent/
├── README.md
├── __pycache__/
├── calculator
│   ├── README.md
│   ├── main.py
│   ├── pkg
│   │   ├── __pycache__/
│   │   ├── calculator.py
│   │   └── render.py
│   └── tests.py
├── call_function.py
├── config.py
├── functions
│   ├── __pycache__/
│   ├── get_file_content.py
│   ├── get_files_info.py
│   ├── run_python_file.py
│   └── write_file.py
├── main.py
├── prompts.py
├── pyproject.toml
├── test_get_file_content.py
├── test_get_files_info.py
├── test_run_python_file.py
├── test_write_file.py
└── uv.lock
```

# Built With
- Python
- OpenAI Python SDK
- OpenRouter
- `argparse`
- `python-dotenv`
- `uv`

## How It Works

The agent follows an iterative tool-calling workflow:

```text
User
  ↓
AI Model
  ↓
Tool Call
  ↓
Python Function
  ↓
Tool Result
  ↓
AI Model
  ↓
Final Response
```

The agent can make multiple tool calls before producing its final response.

For example, when asked:

```text
How does the calculator render results?
```

the agent can inspect the relevant files, read their contents, analyze the code, and return an explanation.

## Available Tools

### `get_files_info`

Lists files and directories within the permitted working directory.

```text
get_files_info({"directory": "pkg"})
```

### `get_file_content`

Reads the contents of a file.

```text
get_file_content({"file_path": "pkg/calculator.py"})
```

### `run_python_file`

Executes a Python file with optional command-line arguments.

```text
run_python_file({
    "file_path": "tests.py"
})
```

### `write_file`

Creates or modifies a file.

```text
write_file({
    "file_path": "example.py",
    "content": "print('Hello')"
})
```

## Security

The agent restricts file operations to a predefined working directory:

```text
./calculator
```

The LLM does not control the working directory.

Paths are validated using functions such as:

```python
os.path.abspath()
os.path.normpath()
os.path.commonpath()
```

This prevents the agent from accessing files outside the permitted directory.

For example, paths such as:

```text
../secret.txt
```

are rejected.

## Setup

```bash
git clone https://github.com/kebba-philip/ai-agent.git


Install the project dependencies:

```bash
uv sync
```

Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_api_key_here
```

## Usage

Run the agent with a prompt:

```bash
uv run main.py "what files are in the calculator directory?"
```

Run with verbose output:

```bash
uv run main.py "what files are in the calculator directory?" --verbose
```

Verbose mode displays information such as:

```text
User prompt: what files are in the calculator directory?

Prompt tokens: 123
Response tokens: 45

 - Calling function: get_files_info({'directory': '.'})
-> ...
```

## Example Tasks

Inspect files:

```bash
uv run main.py "what files are in the calculator directory?"
```

Read source code:

```bash
uv run main.py "explain how calculator.py works"
```

Run tests:

```bash
uv run main.py "run the calculator tests"
```

Create a file:

```bash
uv run main.py "create a file called hello.py that prints Hello World"
```

## Agent Loop

The agent is limited to a maximum number of iterations to prevent it from running indefinitely:

```python
for _ in range(20):
    ...
```

Each iteration can either request one or more tools or return a final response.

Once the model produces a response without tool calls, the agent stops.

**This project demonstrates:**

- LLM API integration
- Prompt engineering
- Function/tool calling
- JSON schemas
- `subprocess`
- File-system operations
- Path validation
- Command-line interfaces
- Environment variables
- Agent loops
- Multi-step tool use
- Secure tool execution

## Testing

Run the file-listing tests with:

```bash
uv run test_get_files_info.py
```

You can also test the agent manually:

```bash
uv run main.py "how does the calculator render results to the console?"
```

## About

[Kebba Njie](https://github.com/kebba-philip/ai-agent.git).

Built as part of my backend development journey with [Boot.dev](https://www.boot.dev/).

Learn more about Boot.dev:
[![Boot.dev](https://img.shields.io/badge/Learn%20Backend%20Development-Boot.dev-black?style=for-the-badge)](https://www.boot.dev/)
