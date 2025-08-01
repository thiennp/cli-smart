# 🚀 Quick Start Guide

Get your AI Bot Agent running in minutes!

## Prerequisites

- Python 3.8 or higher
- OpenAI API key (get one at https://platform.openai.com/)

## Installation

### Option 1: Install from PyPI (Recommended)

```bash
# Install the package
pip install ai-bot-agent

# Set up your API key
ai-bot setup
```

### Option 2: Manual Installation

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up environment
ai-bot setup
```

## Configuration

The `ai-bot setup` command will:

1. **Open your browser** to the OpenAI API key page
2. **Guide you through** creating an API key
3. **Test the key** to ensure it works
4. **Save it securely** to your `.env` file

### Manual Configuration

If you prefer to set up manually:

1. **Get your OpenAI API key**:
   - Go to https://platform.openai.com/
   - Create an account or sign in
   - Navigate to API Keys
   - Create a new API key

2. **Configure the bot**:
   ```bash
   # Edit the .env file
   nano .env
   ```
   
   Add your API key:
   ```env
   OPENAI_API_KEY=your_actual_api_key_here
   ```

## Usage

### Start Interactive Chat

```bash
# Activate virtual environment (if not already activated)
source venv/bin/activate

# Start chat mode
ai-bot chat
```

### Quick Commands

```bash
# Ask a single question
ai-bot ask "What is machine learning?"

# Generate code
ai-bot code "Create a web scraper"

# Analyze a file
ai-bot analyze main.py

# Search the web
ai-bot search "latest Python features"
```

### Demo Mode

See the bot in action without API key:

```bash
python demo.py
```

## Examples

### Chat Mode
```
You: What is Python?
AI: Python is a high-level, interpreted programming language...

You: Write a function to calculate fibonacci numbers
AI: Here's a Python function to calculate Fibonacci numbers...
```

### Code Generation
```bash
# Generate a web scraper
ai-bot code "Create a web scraper that extracts titles from a news website"

# Generate a JavaScript function
ai-bot code "Create a function to validate email addresses" --lang javascript
```

### File Analysis
```bash
# Analyze your code
ai-bot analyze main.py

# Get insights about any file
ai-bot analyze requirements.txt
```

## Troubleshooting

### Common Issues

1. **"No module named 'typer'"**
   ```bash
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **"OpenAI API key not found"**
   - Run `ai-bot setup` to configure your API key
   - Or manually add your API key to the `.env` file

3. **Permission denied**
   ```bash
   chmod +x main.py
   chmod +x install.sh
   ```

### Getting Help

```bash
# Show all available commands
ai-bot --help

# Show help for specific command
ai-bot chat --help
```

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Check out the [demo.py](demo.py) to see capabilities
- Run tests with [test_bot.py](test_bot.py)

## Support

If you encounter issues:
1. Check the troubleshooting section above
2. Run the test suite: `python test_bot.py`
3. Check the logs for detailed error messages

Happy coding! 🤖✨ 