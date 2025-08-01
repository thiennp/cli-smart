#!/bin/bash

echo "🤖 Installing AI Bot Agent with 'ai' command..."

# Check if Python 3.8+ is installed
python_version=$(python3 --version 2>&1 | grep -oE '[0-9]+\.[0-9]+' | head -1)
required_version="3.8"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" = "$required_version" ]; then
    echo "✓ Python $python_version is compatible"
else
    echo "❌ Python 3.8 or higher is required. Current version: $python_version"
    exit 1
fi

# Install the package
echo "📦 Installing AI Bot Agent..."
pip3 install ai-bot-agent

# Create the 'ai' command
echo "🔧 Creating 'ai' command..."
AI_SCRIPT="/usr/local/bin/ai"

# Create the script
cat > "$AI_SCRIPT" << 'EOF'
#!/bin/bash
exec ai-bot "$@"
EOF

# Make it executable
chmod +x "$AI_SCRIPT"

echo "✅ Installation complete!"
echo ""
echo "You can now use:"
echo "• ai setup    - Configure your OpenAI API key"
echo "• ai chat     - Start interactive chat"
echo "• ai ask      - Ask questions"
echo "• ai code     - Generate code"
echo "• ai analyze  - Analyze files"
echo "• ai search   - Search the web"
echo "• ai help     - Show help"
echo ""
echo "Start by running: ai setup" 