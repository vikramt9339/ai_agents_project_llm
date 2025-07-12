#!/usr/bin/env python3
"""
Script to replace hardcoded API keys with placeholder text
"""

import re
import os

def replace_api_keys_in_file(file_path):
    """Replace API keys with placeholder text in a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace various API key patterns
        original_content = content
        
        # Replace sk-proj- keys (OpenAI project keys)
        content = re.sub(
            r'sk-proj-[a-zA-Z0-9_-]{48}',
            'your-openai-api-key-here',
            content
        )
        
        # Replace sk-or-v1- keys (OpenRouter keys)
        content = re.sub(
            r'sk-or-v1-[a-zA-Z0-9_-]{48}',
            'your-openrouter-api-key-here',
            content
        )
        
        # Replace simple 'keyyy' or 'key' placeholders
        content = re.sub(
            r"'keyyy'",
            "'your-api-key-here'",
            content
        )
        content = re.sub(
            r"'key'",
            "'your-api-key-here'",
            content
        )
        
        # If content changed, write it back
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Fixed API keys in {file_path}")
            return True
        else:
            print(f"ℹ️  No API keys found in {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return False

def main():
    """Main function to fix API keys in all problematic files"""
    
    # Files mentioned in the GitHub error
    files_to_fix = [
        '.virtual_documents/week5/Untitled.ipynb',
        'week1/week1 EXERCISE.ipynb',
        'week2/day1.ipynb',
        'week2/day2.ipynb'
    ]
    
    print("🔍 Fixing API keys in files...")
    
    fixed_count = 0
    for file_path in files_to_fix:
        if os.path.exists(file_path):
            if replace_api_keys_in_file(file_path):
                fixed_count += 1
        else:
            print(f"⚠️  File not found: {file_path}")
    
    print(f"\n🎉 Fixed API keys in {fixed_count} files!")
    print("\n📝 Next steps:")
    print("1. Add these files to .gitignore if they contain sensitive data")
    print("2. Use environment variables for API keys instead of hardcoding")
    print("3. Try pushing to GitHub again")

if __name__ == "__main__":
    main() 