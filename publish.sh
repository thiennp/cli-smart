#!/bin/bash

echo "🚀 Publishing AI Bot Agent to PyPI..."

# Check if we're in a virtual environment
if [[ "$VIRTUAL_ENV" == "" ]]; then
    echo "⚠️  Warning: Not in a virtual environment. Activating venv..."
    source venv/bin/activate
fi

# Install build tools
echo "📦 Installing build tools..."
pip install --upgrade build twine

# Clean previous builds
echo "🧹 Cleaning previous builds..."
rm -rf dist/ build/ *.egg-info/

# Build the package
echo "🔨 Building package..."
python -m build

# Check the build
echo "✅ Checking build..."
python -m twine check dist/*

echo ""
echo "📦 Package built successfully!"
echo ""
echo "To publish to PyPI:"
echo "1. Create a PyPI account at https://pypi.org/account/register/"
echo "2. Create an API token at https://pypi.org/manage/account/token/"
echo "3. Run: python -m twine upload dist/*"
echo ""
echo "To test on TestPyPI first:"
echo "python -m twine upload --repository testpypi dist/*"
echo ""
echo "Package files created:"
ls -la dist/ 