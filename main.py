#!/usr/bin/env python3
"""
AI Bot Agent - Command Line Interface
A powerful AI assistant that runs from the command line with various capabilities.
"""

import os
import sys
import json
import asyncio
import subprocess
import webbrowser
from typing import Optional, List, Dict, Any
from pathlib import Path
import typer
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.live import Live
from rich.layout import Layout
import openai
from dotenv import load_dotenv
import requests
import time
import datetime

# Load environment variables
load_dotenv()

# Initialize Rich console
console = Console()

# Initialize Typer app
app = typer.Typer(
    name="ai-bot",
    help="AI Bot Agent - Your intelligent command line assistant",
    add_completion=False
)

class AIBotAgent:
    def __init__(self):
        self.client = None
        self.conversation_history = []
        self.system_prompt = """You are an intelligent AI assistant running from the command line. 
        You can help with:
        - Answering questions and providing information
        - Writing and analyzing code
        - File operations and system tasks
        - Web searches and research
        - Creative writing and brainstorming
        - Problem solving and analysis
        
        Be helpful, accurate, and concise in your responses."""
        
        self.initialize_openai()
    
    def initialize_openai(self):
        """Initialize OpenAI client with API key."""
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            console.print("[red]Warning: OPENAI_API_KEY not found in environment variables.[/red]")
            console.print("Please set your OpenAI API key in a .env file or environment variable.")
            return
        
        try:
            self.client = openai.OpenAI(api_key=api_key)
            console.print("[green]✓ OpenAI client initialized successfully[/green]")
        except Exception as e:
            console.print(f"[red]Error initializing OpenAI client: {e}[/red]")
    
    def chat(self, message: str, model: str = "gpt-3.5-turbo") -> str:
        """Send a message to the AI and get a response."""
        if not self.client:
            return "Error: OpenAI client not initialized. Please check your API key."
        
        try:
            # Add user message to conversation history
            self.conversation_history.append({"role": "user", "content": message})
            
            # Prepare messages for API call
            messages = [{"role": "system", "content": self.system_prompt}] + self.conversation_history
            
            with console.status("[bold green]Thinking...", spinner="dots"):
                response = self.client.chat.completions.create(
                    model=model,
                    messages=messages,
                    max_tokens=1000,
                    temperature=0.7
                )
            
            ai_response = response.choices[0].message.content
            
            # Add AI response to conversation history
            self.conversation_history.append({"role": "assistant", "content": ai_response})
            
            return ai_response
            
        except Exception as e:
            return f"Error: {str(e)}"
    
    def search_web(self, query: str) -> str:
        """Perform a web search (placeholder - would need actual search API)."""
        return f"Web search for '{query}' would be implemented here. Consider using DuckDuckGo API or similar."
    
    def analyze_file(self, file_path: str) -> str:
        """Analyze a file and provide insights."""
        try:
            path = Path(file_path)
            if not path.exists():
                return f"Error: File '{file_path}' not found."
            
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Analyze file content
            analysis_prompt = f"""Analyze this file and provide insights:
            
            File: {file_path}
            Size: {len(content)} characters
            Content:
            {content[:2000]}...
            
            Please provide:
            1. File type and purpose
            2. Key components or functions
            3. Potential issues or improvements
            4. Summary
            """
            
            return self.chat(analysis_prompt)
            
        except Exception as e:
            return f"Error analyzing file: {str(e)}"
    
    def generate_code(self, description: str, language: str = "python") -> str:
        """Generate code based on description."""
        code_prompt = f"""Generate {language} code for the following description:
        
        {description}
        
        Please provide:
        1. Complete, working code
        2. Brief explanation of the code
        3. Usage examples if applicable
        """
        
        return self.chat(code_prompt)
    
    def clear_history(self):
        """Clear conversation history."""
        self.conversation_history = []
        console.print("[green]Conversation history cleared.[/green]")

def display_banner():
    """Display the AI Bot banner."""
    banner = """
    🤖 AI Bot Agent v1.0
    Your intelligent command line assistant
    """
    console.print(Panel(banner, style="bold blue"))

def display_help():
    """Display help information."""
    help_text = """
    [bold]Available Commands:[/bold]
    
    [green]setup[/green] - Set up OpenAI API key
    [green]chat[/green] - Start interactive chat mode
    [green]ask[/green] - Ask a single question
    [green]code[/green] - Generate code from description
    [green]analyze[/green] - Analyze a file
    [green]search[/green] - Search the web
    [green]clear[/green] - Clear conversation history
    [green]help[/green] - Show this help message
    [green]exit[/green] - Exit the bot
    
    [bold]Examples:[/bold]
    ai-bot setup
    ai-bot chat
    ai-bot ask "What is Python?"
    ai-bot code "Create a simple web scraper"
    ai-bot analyze main.py
    """
    console.print(Panel(help_text, title="Help", style="green"))

def setup_openai_key():
    """Set up OpenAI API key with automated assistance."""
    display_banner()
    
    console.print("[bold green]🔧 OpenAI API Key Setup[/bold green]")
    console.print("This will help you get and configure your OpenAI API key.\n")
    
    # Check if .env file exists
    env_file = Path(".env")
    if not env_file.exists():
        console.print("[yellow]Creating .env file...[/yellow]")
        env_file.write_text("OPENAI_API_KEY=your_openai_api_key_here\n")
    
    # Open OpenAI API key page
    console.print("[bold blue]Step 1: Getting your OpenAI API key[/bold blue]")
    console.print("Opening OpenAI API key page in your browser...")
    
    try:
        webbrowser.open("https://platform.openai.com/api-keys")
        console.print("[green]✓ Browser opened successfully[/green]")
    except Exception as e:
        console.print(f"[red]Could not open browser automatically: {e}[/red]")
        console.print("Please manually visit: https://platform.openai.com/api-keys")
    
    console.print("\n[bold yellow]Instructions:[/bold yellow]")
    console.print("1. Sign in to your OpenAI account")
    console.print("2. Click 'Create new secret key'")
    console.print("3. Give it a name (e.g., 'AI Bot Agent')")
    console.print("4. Copy the API key (it starts with 'sk-')")
    console.print("5. Keep it secure - you won't see it again!")
    
    # Wait for user to get the key
    console.print("\n[bold blue]Step 2: Enter your API key[/bold blue]")
    api_key = Prompt.ask(
        "Enter your OpenAI API key",
        password=True,
        default=""
    )
    
    if not api_key or api_key == "your_openai_api_key_here":
        console.print("[red]No valid API key provided. Setup cancelled.[/red]")
        return False
    
    # Validate the API key format
    if not api_key.startswith("sk-"):
        console.print("[red]Invalid API key format. OpenAI API keys start with 'sk-'[/red]")
        return False
    
    # Test the API key
    console.print("\n[bold blue]Step 3: Testing your API key[/bold blue]")
    try:
        test_client = openai.OpenAI(api_key=api_key)
        # Try a simple API call to test the key
        response = test_client.models.list()
        console.print("[green]✓ API key is valid![/green]")
    except Exception as e:
        console.print(f"[red]❌ API key test failed: {e}[/red]")
        console.print("Please check your API key and try again.")
        return False
    
    # Save the API key to .env file
    console.print("\n[bold blue]Step 4: Saving your API key[/bold blue]")
    try:
        env_content = f"OPENAI_API_KEY={api_key}\n"
        env_file.write_text(env_content)
        console.print("[green]✓ API key saved to .env file[/green]")
    except Exception as e:
        console.print(f"[red]❌ Failed to save API key: {e}[/red]")
        console.print("Please manually add your API key to the .env file:")
        console.print(f"OPENAI_API_KEY={api_key}")
        return False
    
    console.print("\n[bold green]🎉 Setup Complete![/bold green]")
    console.print("Your OpenAI API key has been configured successfully.")
    console.print("\nYou can now use the AI Bot Agent:")
    console.print("• ai-bot chat - Start interactive chat")
    console.print("• ai-bot ask 'Your question' - Ask a single question")
    console.print("• ai-bot code 'Description' - Generate code")
    
    return True

@app.command()
def setup():
    """Set up OpenAI API key with automated assistance."""
    setup_openai_key()

@app.command()
def chat():
    """Start interactive chat mode."""
    bot = AIBotAgent()
    display_banner()
    
    console.print("\n[bold green]Interactive Chat Mode[/bold green]")
    console.print("Type 'exit' to quit, 'clear' to clear history, 'help' for help\n")
    
    while True:
        try:
            user_input = Prompt.ask("\n[bold blue]You[/bold blue]")
            
            if user_input.lower() in ['exit', 'quit', 'q']:
                console.print("[yellow]Goodbye! 👋[/yellow]")
                break
            elif user_input.lower() == 'clear':
                bot.clear_history()
                continue
            elif user_input.lower() == 'help':
                display_help()
                continue
            elif not user_input.strip():
                continue
            
            # Get AI response
            response = bot.chat(user_input)
            
            # Display response
            console.print(f"\n[bold green]AI Bot[/bold green]: {response}")
            
        except KeyboardInterrupt:
            console.print("\n[yellow]Goodbye! 👋[/yellow]")
            break
        except Exception as e:
            console.print(f"[red]Error: {e}[/red]")

@app.command()
def ask(
    question: str = typer.Argument(..., help="The question to ask the AI")
):
    """Ask a single question to the AI."""
    bot = AIBotAgent()
    display_banner()
    
    console.print(f"\n[bold blue]Question:[/bold blue] {question}")
    
    response = bot.chat(question)
    console.print(f"\n[bold green]Answer:[/bold green] {response}")

@app.command()
def code(
    description: str = typer.Argument(..., help="Description of the code to generate"),
    language: str = typer.Option("python", "--lang", "-l", help="Programming language")
):
    """Generate code from a description."""
    bot = AIBotAgent()
    display_banner()
    
    console.print(f"\n[bold blue]Generating {language} code for:[/bold blue] {description}")
    
    response = bot.generate_code(description, language)
    console.print(f"\n[bold green]Generated Code:[/bold green]\n{response}")

@app.command()
def analyze(
    file_path: str = typer.Argument(..., help="Path to the file to analyze")
):
    """Analyze a file and provide insights."""
    bot = AIBotAgent()
    display_banner()
    
    console.print(f"\n[bold blue]Analyzing file:[/bold blue] {file_path}")
    
    response = bot.analyze_file(file_path)
    console.print(f"\n[bold green]Analysis:[/bold green]\n{response}")

@app.command()
def search(
    query: str = typer.Argument(..., help="Search query")
):
    """Search the web for information."""
    bot = AIBotAgent()
    display_banner()
    
    console.print(f"\n[bold blue]Searching for:[/bold blue] {query}")
    
    response = bot.search_web(query)
    console.print(f"\n[bold green]Search Results:[/bold green]\n{response}")

@app.command()
def clear():
    """Clear conversation history."""
    bot = AIBotAgent()
    bot.clear_history()

@app.command()
def help():
    """Show help information."""
    display_help()

if __name__ == "__main__":
    app() 