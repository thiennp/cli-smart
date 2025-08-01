#!/bin/bash

echo "🍺 Setting up Homebrew Tap for AI Bot Agent..."

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "❌ Not in a git repository"
    exit 1
fi

# Get current version from pyproject.toml
VERSION=$(grep 'version = ' pyproject.toml | cut -d'"' -f2)
echo "📦 Version: $VERSION"

echo ""
echo "📋 Steps to set up Homebrew installation:"
echo ""
echo "1. Create a GitHub release:"
echo "   - Go to https://github.com/thiennp/cli-smart/releases"
echo "   - Click 'Create a new release'"
echo "   - Tag: v$VERSION"
echo "   - Title: AI Bot Agent v$VERSION"
echo "   - Copy content from release_notes_v$VERSION.md"
echo ""
echo "2. Create a Homebrew tap repository:"
echo "   - Go to https://github.com/new"
echo "   - Repository name: homebrew-ai-bot-agent"
echo "   - Make it public"
echo "   - Don't initialize with README"
echo ""
echo "3. Add the formula to your tap:"
echo "   - Clone your tap repository"
echo "   - Copy Formula/ai-bot-agent.rb to your tap"
echo "   - Update the SHA256 in the formula"
echo ""
echo "4. Calculate SHA256 for the formula:"
echo "   - Download the source tarball from the release"
echo "   - Run: shasum -a 256 cli-smart-$VERSION.tar.gz"
echo "   - Update the sha256 line in the formula"
echo ""
echo "5. Test the formula locally:"
echo "   brew install --build-from-source Formula/ai-bot-agent.rb"
echo ""
echo "6. Push to your tap repository:"
echo "   git add ."
echo "   git commit -m 'Add ai-bot-agent formula'"
echo "   git push origin main"
echo ""
echo "7. Users can then install with:"
echo "   brew tap thiennp/ai-bot-agent"
echo "   brew install ai-bot-agent"
echo "   ai setup"
echo "   ai chat"
echo ""
echo "📝 Formula template is ready in Formula/ai-bot-agent.rb"
echo "📝 Tap documentation is ready in homebrew-tap/README.md" 