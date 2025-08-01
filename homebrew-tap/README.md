# Homebrew Tap for AI Bot Agent

This repository contains the Homebrew formula for installing AI Bot Agent via Homebrew.

## Installation

```bash
# Add the tap
brew tap thiennp/ai-bot-agent

# Install AI Bot Agent
brew install ai-bot-agent
```

## Usage

After installation, you can use the AI Bot Agent with the short command `ai`:

```bash
# Set up your OpenAI API key
ai setup

# Start interactive chat
ai chat

# Ask a question
ai ask "What is machine learning?"

# Generate code
ai code "Create a web scraper"

# Analyze a file
ai analyze main.py

# Search the web
ai search "latest Python features"
```

## Commands

- `ai setup` - Configure OpenAI API key
- `ai chat` - Interactive chat mode
- `ai ask` - Ask single questions
- `ai code` - Generate code
- `ai analyze` - Analyze files
- `ai search` - Search the web
- `ai help` - Show help

## Alternative Installation

You can also install from PyPI:

```bash
pip install ai-bot-agent
ai-bot setup
ai-bot chat
```

## Links

- **GitHub Repository**: https://github.com/thiennp/cli-smart
- **PyPI Package**: https://pypi.org/project/ai-bot-agent/
- **Documentation**: https://github.com/thiennp/cli-smart#readme 