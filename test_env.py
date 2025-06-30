#!/usr/bin/env python3
"""
Test script to verify .env file configuration
"""
import os
from dotenv import load_dotenv

def test_env_configuration():
    """Test the environment configuration"""
    print("🔧 Testing Environment Configuration...")
    print("=" * 50)
    
    # Load .env file
    load_dotenv()
    
    # Check API key
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key:
        print(f"✅ API Key found: {api_key[:20]}...{api_key[-10:]}")
        
        # Check if API key is complete (should be around 50+ characters)
        if len(api_key) < 50:
            print("⚠️  Warning: API key seems too short. It might be truncated.")
        else:
            print("✅ API key length looks correct")
    else:
        print("❌ No API key found!")
        return False
    
    # Test OpenAI client creation
    try:
        from config import get_openai_client
        client = get_openai_client()
        print("✅ OpenAI client created successfully")
        
        # Test a simple API call
        print("🧪 Testing API connection...")
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "Say 'Hello from the test script!'"}],
            max_tokens=10
        )
        print("✅ API connection successful!")
        print(f"Response: {response.choices[0].message.content}")
        return True
        
    except Exception as e:
        print(f"❌ API test failed: {e}")
        return False

if __name__ == "__main__":
    test_env_configuration() 