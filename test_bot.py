#!/usr/bin/env python3
"""
Test script for AI Bot Agent
Tests basic functionality without requiring API keys.
"""

import sys
import os
from pathlib import Path

def test_imports():
    """Test if all required modules can be imported."""
    print("Testing imports...")
    
    try:
        import typer
        print("✓ typer imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import typer: {e}")
        return False
    
    try:
        from rich.console import Console
        print("✓ rich.console imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import rich.console: {e}")
        return False
    
    try:
        from rich.prompt import Prompt
        print("✓ rich.prompt imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import rich.prompt: {e}")
        return False
    
    try:
        from dotenv import load_dotenv
        print("✓ python-dotenv imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import python-dotenv: {e}")
        return False
    
    try:
        import openai
        print("✓ openai imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import openai: {e}")
        return False
    
    return True

def test_file_structure():
    """Test if all required files exist."""
    print("\nTesting file structure...")
    
    required_files = [
        "main.py",
        "requirements.txt",
        "README.md",
        "env.example"
    ]
    
    all_exist = True
    for file in required_files:
        if Path(file).exists():
            print(f"✓ {file} exists")
        else:
            print(f"❌ {file} missing")
            all_exist = False
    
    return all_exist

def test_main_script():
    """Test if main.py can be executed."""
    print("\nTesting main script...")
    
    try:
        # Test if the script can be imported
        import main
        print("✓ main.py can be imported")
        
        # Test if the app object exists
        if hasattr(main, 'app'):
            print("✓ app object exists")
        else:
            print("❌ app object not found")
            return False
            
        return True
    except Exception as e:
        print(f"❌ Failed to import main.py: {e}")
        return False

def test_help_command():
    """Test if the help command works."""
    print("\nTesting help command...")
    
    try:
        import subprocess
        result = subprocess.run([sys.executable, "main.py", "--help"], 
                              capture_output=True, text=True, timeout=10)
        
        if result.returncode == 0:
            print("✓ Help command works")
            return True
        else:
            print(f"❌ Help command failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Help command test failed: {e}")
        return False

def main():
    """Run all tests."""
    print("🧪 Testing AI Bot Agent...\n")
    
    tests = [
        ("Import Test", test_imports),
        ("File Structure Test", test_file_structure),
        ("Main Script Test", test_main_script),
        ("Help Command Test", test_help_command)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n{'='*50}")
        print(f"Running: {test_name}")
        print('='*50)
        
        if test_func():
            passed += 1
            print(f"✅ {test_name} PASSED")
        else:
            print(f"❌ {test_name} FAILED")
    
    print(f"\n{'='*50}")
    print(f"Test Results: {passed}/{total} tests passed")
    print('='*50)
    
    if passed == total:
        print("🎉 All tests passed! The AI Bot Agent is ready to use.")
        print("\nNext steps:")
        print("1. Copy env.example to .env")
        print("2. Add your OpenAI API key to .env")
        print("3. Run: python main.py chat")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 