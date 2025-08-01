#!/bin/bash

echo "🚀 Creating GitHub Release for AI Bot Agent..."

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "❌ Not in a git repository"
    exit 1
fi

# Get current version from pyproject.toml
VERSION=$(grep 'version = ' pyproject.toml | cut -d'"' -f2)
echo "📦 Version: $VERSION"

# Check if tag already exists
if git tag -l | grep -q "v$VERSION"; then
    echo "⚠️  Tag v$VERSION already exists"
    read -p "Do you want to delete and recreate it? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        git tag -d "v$VERSION"
        git push origin ":refs/tags/v$VERSION" 2>/dev/null || true
    else
        echo "❌ Release cancelled"
        exit 1
    fi
fi

# Create and push tag
echo "🏷️  Creating tag v$VERSION..."
git tag "v$VERSION"
git push origin "v$VERSION"

# Create release notes
RELEASE_NOTES="## What's New in v$VERSION

### 🎉 New Features
- **Automated OpenAI API Key Setup**: Run \`ai-bot setup\` to automatically configure your API key
- **Browser Integration**: Opens OpenAI API key page automatically
- **Key Validation**: Tests API keys before saving
- **Secure Storage**: Saves keys securely in .env files

### 🚀 Easy Installation
\`\`\`bash
# Install from PyPI
pip install ai-bot-agent

# Install from Homebrew (coming soon)
brew install ai-bot-agent
\`\`\`

### 📝 Usage
\`\`\`bash
# Set up your API key
ai-bot setup

# Start chatting
ai-bot chat

# Or use the short command (with Homebrew)
ai chat
\`\`\`

### 🔧 Commands
- \`ai-bot setup\` - Configure OpenAI API key
- \`ai-bot chat\` - Interactive chat mode
- \`ai-bot ask\` - Ask single questions
- \`ai-bot code\` - Generate code
- \`ai-bot analyze\` - Analyze files
- \`ai-bot search\` - Search the web

### 📦 Installation Options
1. **PyPI**: \`pip install ai-bot-agent\`
2. **Homebrew**: \`brew install ai-bot-agent\` (coming soon)
3. **Source**: \`git clone https://github.com/thiennp/cli-smart.git\`

### 🔗 Links
- **PyPI**: https://pypi.org/project/ai-bot-agent/
- **GitHub**: https://github.com/thiennp/cli-smart
- **Documentation**: https://github.com/thiennp/cli-smart#readme"

echo "$RELEASE_NOTES" > "release_notes_v$VERSION.md"

echo "📝 Release notes created: release_notes_v$VERSION.md"
echo ""
echo "Next steps:"
echo "1. Go to https://github.com/thiennp/cli-smart/releases"
echo "2. Click 'Create a new release'"
echo "3. Select tag 'v$VERSION'"
echo "4. Copy content from release_notes_v$VERSION.md"
echo "5. Publish the release"
echo ""
echo "After creating the release, you can update the Homebrew formula with:"
echo "1. Download the source tarball from the release"
echo "2. Calculate SHA256: shasum -a 256 ai-bot-agent-$VERSION.tar.gz"
echo "3. Update Formula/ai-bot-agent.rb with the SHA256" 