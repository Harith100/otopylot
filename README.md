# 🤖 Otopylot - Command Line Interface Assistant (Work in Progress)

> ⚠️ **Note**: This project is currently under active development. Features, functionality, and security measures may change as development progresses.

## 📝 Overview

Otopylot is a Python-based assistant that leverages Groq's LLM capabilities to interpret natural language requests and convert them into file system operations or system commands. This enables users to manage their files and directories through conversational language rather than remembering specific command syntax.

## ✨ Features

- 💬 **Natural Language Processing**: Convert casual requests into system commands
- 📁 **File Management**: Create, delete, rename, and list files or directories
- 🖥️ **Command Execution**: Execute system commands based on natural language input
- 🔄 **Contextual Memory**: Maintains chat history for more coherent interactions

## 🛠️ Tech Stack

- **Language**: Python
- **LLM Provider**: Groq
- **Model**: llama3-8b-8192
- **Libraries**: 
  - `groq` for API interaction
  - `os` and `subprocess` for system operations

## 🚀 Getting Started

### Prerequisites

- Python 3.6+
- Groq API key

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Harith100/otopylot.git
   cd otopylot
   ```

2. Install required dependencies:
   ```bash
   pip install groq
   ```

3. Set up your Groq API key:
   ```python
   # Replace with your actual API key or preferably use environment variables
   os.environ["GROQ_API_KEY"] = "your_api_key_here"
   ```

### Usage

Run the script:
```bash
python otopylot.py
```

Example interactions:
```
Enter your command: create a folder called Projects
Result: Directory 'Projects' created successfully.

Enter your command: list all files in the current directory
Result: [List of files in the current directory]
```

## ⚠️ Security Notice

This tool executes system commands based on LLM output. While efforts are made to sanitize inputs, please use with caution as it may pose security risks. Currently, the tool:

- Executes Python code using `exec()` 
- Runs shell commands using `subprocess.run()`
- Has limited command validation

## 🚧 Development Status

This project is in early development. Planned improvements include:

- Enhanced security measures and command validation
- Support for more complex file operations
- Better error handling and user feedback
- Moving API key to environment variables
- Adding configuration options
- Implementing command whitelisting
- Comprehensive documentation and examples

## 🔒 Security Roadmap

- [ ] Implement proper command sanitization
- [ ] Create allowlist for safe commands
- [ ] Add user confirmation for potentially dangerous operations
- [ ] Improve error handling and logging
- [ ] Add unit tests and security tests


## 🙏 Acknowledgements

- Groq for providing the LLM API
- LLaMA model creators for the underlying language model
