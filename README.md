# 🤖 AI Bot Agent

A powerful AI assistant that runs from the command line with various capabilities including chat, code generation, file analysis, and web search.

## Features

- **Interactive Chat Mode**: Have conversations with the AI
- **Code Generation**: Generate code from natural language descriptions
- **File Analysis**: Analyze and get insights about your files
- **Web Search**: Search for information on the web
- **Rich CLI Interface**: Beautiful terminal interface with colors and formatting
- **Conversation History**: Maintains context across interactions
- **Multiple AI Models**: Support for different OpenAI models
- **Easy Setup**: Automated OpenAI API key configuration

## Installation

### Prerequisites

- Python 3.8 or higher
- OpenAI API key

### Quick Start

#### Option 1: Homebrew (Recommended for macOS)

```bash
# Install via Homebrew
brew install ai-bot-agent

# Set up your API key
ai setup

# Start using the bot
ai chat
```

#### Option 2: PyPI

```bash
# Install the package
pip install ai-bot-agent

# Set up your API key
ai-bot setup
```

This will:
- Open the OpenAI API key page in your browser
- Guide you through creating an API key
- Test and save your key automatically

#### Option 3: Source Installation

```bash
git clone https://github.com/thiennp/cli-smart.git
cd cli-smart
pip install -r requirements.txt
python main.py setup
```

## Usage

### Easy Setup

Set up your OpenAI API key with automated assistance:

```bash
# With Homebrew installation
ai setup

# With PyPI installation
ai-bot setup
```

This command will:
- Open https://platform.openai.com/api-keys in your browser
- Guide you through creating an API key
- Test the key to ensure it works
- Save it securely to your `.env` file

### Interactive Chat Mode

Start an interactive conversation with the AI:

```bash
# With Homebrew installation
ai chat

# With PyPI installation
ai-bot chat
```

### Ask a Single Question

Ask a specific question:

```bash
# With Homebrew installation
ai ask "What is machine learning?"

# With PyPI installation
ai-bot ask "What is machine learning?"
```

### Generate Code

Generate code from a description:

```bash
# With Homebrew installation
ai code "Create a simple web scraper"

# With PyPI installation
ai-bot code "Create a simple web scraper"
```

Generate code in a specific language:

```bash
# With Homebrew installation
ai code "Create a REST API" --lang javascript

# With PyPI installation
ai-bot code "Create a REST API" --lang javascript
```

### Analyze Files

Analyze a file and get insights:

```bash
# With Homebrew installation
ai analyze main.py

# With PyPI installation
ai-bot analyze main.py
```

### Search the Web

Search for information:

```bash
# With Homebrew installation
ai search "latest Python features"

# With PyPI installation
ai-bot search "latest Python features"
```

### Clear History

Clear conversation history:

```bash
# With Homebrew installation
ai clear

# With PyPI installation
ai-bot clear
```

### Get Help

Show help information:

```bash
# With Homebrew installation
ai help

# With PyPI installation
ai-bot help
```

## Configuration

The setup command automatically creates a `.env` file with your configuration:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

You can also manually edit the `.env` file to customize:

```env
# OpenAI API Configuration
OPENAI_API_KEY=your_openai_api_key_here

# Optional: Customize the AI model
OPENAI_MODEL=gpt-3.5-turbo

# Optional: Set default temperature for responses
OPENAI_TEMPERATURE=0.7

# Optional: Set maximum tokens for responses
OPENAI_MAX_TOKENS=1000
```

## Examples

### Chat Mode Examples

```
You: What is Python?
AI Bot: Python is a high-level, interpreted programming language...

You: Write a function to calculate fibonacci numbers
AI Bot: Here's a Python function to calculate Fibonacci numbers...

You: Explain machine learning in simple terms
AI Bot: Machine learning is like teaching a computer to learn...
```

### Code Generation Examples

```bash
# Generate a Python web scraper
ai code "Create a web scraper that extracts titles from a news website"

# Generate a JavaScript function
ai code "Create a function to validate email addresses" --lang javascript

# Generate a data analysis script
ai code "Create a script to analyze CSV data and create visualizations"
```

## Features in Detail

### Easy Setup
- Automated browser opening to OpenAI API key page
- Step-by-step guidance for API key creation
- Automatic validation and testing of API keys
- Secure storage in `.env` file

### Interactive Chat Mode
- Maintains conversation context
- Rich formatting with colors
- Easy-to-use interface
- Built-in commands (exit, clear, help)

### Code Generation
- Supports multiple programming languages
- Generates complete, working code
- Includes explanations and usage examples
- Optimized for different use cases

### File Analysis
- Analyzes code structure and purpose
- Identifies potential issues
- Provides improvement suggestions
- Works with various file types

### Web Search
- Search for current information
- Get real-time data
- Research capabilities
- Information gathering

## Installation Options

### 1. Homebrew (macOS)
```bash
brew install ai-bot-agent
ai setup
ai chat
```

### 2. PyPI (All Platforms)
```bash
pip install ai-bot-agent
ai-bot setup
ai-bot chat
```

### 3. Source (Development)
```bash
git clone https://github.com/thiennp/cli-smart.git
cd cli-smart
pip install -r requirements.txt
python main.py setup
python main.py chat
```

## Troubleshooting

### Common Issues

1. **API Key Error**
   ```
   Error: OpenAI client not initialized. Please check your API key.
   ```
   Solution: Run `ai setup` or `ai-bot setup` to configure your API key

2. **Module Not Found**
   ```
   ModuleNotFoundError: No module named 'openai'
   ```
   Solution: Install dependencies with `pip install ai-bot-agent`

3. **Permission Denied**
   ```
   PermissionError: [Errno 13] Permission denied
   ```
   Solution: Make sure the script is executable: `chmod +x main.py`

### Getting Help

- Use `ai help` or `ai-bot help` for command help
- Use `ai --help` or `ai-bot --help` for general help
- Check the logs for detailed error messages

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Typer](https://typer.tiangolo.com/) for CLI
- Styled with [Rich](https://rich.readthedocs.io/) for beautiful terminal output
- Powered by [OpenAI](https://openai.com/) API

## Version History

- **v1.0.0**: Initial release with basic chat, code generation, and file analysis features
- **v1.1.0**: Added automated setup command for easy API key configuration 