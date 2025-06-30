#!/usr/bin/env python3
"""
Setup script to configure environment variables for API keys
"""
import os
import sys

def create_env_file():
    """Create a .env file with user input"""
    
    print("🔧 Setting up environment variables for your AI project")
    print("=" * 50)
    
    # Get API key from user
    api_key = input("Enter your OpenAI API key: ").strip()
    
    if not api_key:
        print("❌ API key is required!")
        return False
    
    # Create .env file content
    env_content = f"""# OpenAI API Configuration
OPENAI_API_KEY={api_key}
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
"""
    
    # Write to .env file
    try:
        with open('.env', 'w') as f:
            f.write(env_content)
        print("✅ .env file created successfully!")
        return True
    except Exception as e:
        print(f"❌ Error creating .env file: {e}")
        return False

def check_dependencies():
    """Check if required packages are installed"""
    required_packages = [
        ('python-dotenv', 'dotenv'),
        ('openai', 'openai')
    ]
    missing_packages = []
    
    for package_name, import_name in required_packages:
        try:
            __import__(import_name)
        except ImportError:
            missing_packages.append(package_name)
    
    if missing_packages:
        print(f"⚠️  Missing packages: {', '.join(missing_packages)}")
        print("Install them with: pip install " + " ".join(missing_packages))
        return False
    
    print("✅ All required packages are installed")
    return True

def main():
    print("🚀 AI Agents Project Environment Setup")
    print("=" * 40)
    
    # Check dependencies
    if not check_dependencies():
        print("\nPlease install missing packages and run this script again.")
        sys.exit(1)
    
    # Create .env file
    if create_env_file():
        print("\n🎉 Setup complete! You can now use the config.py module in your notebooks.")
        print("\nExample usage:")
        print("from config import get_openai_client")
        print("client = get_openai_client()")
    else:
        print("\n❌ Setup failed. Please try again.")
        sys.exit(1)

if __name__ == "__main__":
    main() 