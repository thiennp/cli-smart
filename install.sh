#!/bin/bash

echo "🤖 Installing AI Bot Agent..."

# Check if Python 3.8+ is installed
python_version=$(python3 --version 2>&1 | grep -oE '[0-9]+\.[0-9]+' | head -1)
required_version="3.8"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" = "$required_version" ]; then
    echo "✓ Python $python_version is compatible"
else
    echo "❌ Python 3.8 or higher is required. Current version: $python_version"
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi

# Activate virtual environment and install dependencies
echo "📦 Installing dependencies..."
source venv/bin/activate
pip install -r requirements.txt

# Make main.py executable
chmod +x main.py

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file..."
    cp env.example .env
    echo "⚠️  Please edit .env file and add your OpenAI API key"
else
    echo "✓ .env file already exists"
fi

# Run tests to verify installation
echo "🧪 Running tests..."
python test_bot.py

echo ""
echo "🎉 Installation complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env file and add your OpenAI API key"
echo "2. Activate virtual environment: source venv/bin/activate"
echo "3. Run: python main.py --help"
echo "4. Start chatting: python main.py chat"
echo ""
echo "For help, run: python main.py help"
echo ""
echo "💡 Tip: You can also run the demo with: python demo.py" 