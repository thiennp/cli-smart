# 🚀 Quick Start Guide

Get your AI Bot Agent running in minutes!

## Prerequisites

- Python 3.8 or higher
- OpenAI API key (get one at https://platform.openai.com/)

## Installation

### Option 1: Automatic Installation (Recommended)

```bash
# Run the installation script
./install.sh
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
cp env.example .env
# Edit .env and add your OpenAI API key
```

## Configuration

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
python main.py chat
```

### Quick Commands

```bash
# Ask a single question
python main.py ask "What is machine learning?"

# Generate code
python main.py code "Create a web scraper"

# Analyze a file
python main.py analyze main.py

# Search the web
python main.py search "latest Python features"
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
python main.py code "Create a web scraper that extracts titles from a news website"

# Generate a JavaScript function
python main.py code "Create a function to validate email addresses" --lang javascript
```

### File Analysis
```bash
# Analyze your code
python main.py analyze main.py

# Get insights about any file
python main.py analyze requirements.txt
```

## Troubleshooting

### Common Issues

1. **"No module named 'typer'"**
   ```bash
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **"OpenAI API key not found"**
   - Make sure you've added your API key to the `.env` file
   - Check that the `.env` file is in the project root

3. **Permission denied**
   ```bash
   chmod +x main.py
   chmod +x install.sh
   ```

### Getting Help

```bash
# Show all available commands
python main.py --help

# Show help for specific command
python main.py chat --help
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