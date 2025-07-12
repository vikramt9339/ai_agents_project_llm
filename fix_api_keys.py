#!/usr/bin/env python3
"""
Script to replace API keys with placeholder text in Jupyter notebooks
"""

import re
import json
import os

def fix_notebook_file(file_path):
    """Replace API keys with placeholder text in a Jupyter notebook"""
    print(f"Processing: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace actual API keys with placeholders
    # Pattern for OpenAI API keys (sk- followed by alphanumeric characters)
    content = re.sub(r'sk-[a-zA-Z0-9]{48}', 'your-openai-api-key-here', content)
    
    # Pattern for OpenRouter API keys (if they follow a different pattern)
    content = re.sub(r'your-openrouter-api-key-here[a-zA-Z0-9]+', 'your-openrouter-api-key-here', content)
    
    # Pattern for any remaining API keys that might be in the format shown in the error
    content = re.sub(r'your-openai-api-key-here[a-zA-Z0-9_-]+', 'your-openai-api-key-here', content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Fixed: {file_path}")

def main():
    """Main function to fix all affected files"""
    files_to_fix = [
        'week1/week1 EXERCISE.ipynb',
        'week2/day1.ipynb', 
        'week2/day2.ipynb',
        '.virtual_documents/week5/Untitled.ipynb'
    ]
    
    for file_path in files_to_fix:
        if os.path.exists(file_path):
            fix_notebook_file(file_path)
        else:
            print(f"File not found: {file_path}")
    
    print("\nAll files processed. Please commit and push again.")

if __name__ == "__main__":
    main() 