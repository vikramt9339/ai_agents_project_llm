#!/usr/bin/env python3
"""
Test script to verify API key configuration
"""
from config import get_openai_client, create_chat_completion

def test_configuration():
    """Test the API configuration"""
    print("🧪 Testing API Configuration...")
    
    try:
        # Test 1: Get client
        client = get_openai_client()
        print("✅ Client created successfully")
        
        # Test 2: Simple API call
        response = create_chat_completion([
            {"role": "user", "content": "Say 'Hello from the test script!'"}
        ])
        
        print("✅ API call successful!")
        print(f"Response: {response.choices[0].message.content}")
        
        return True
        
    except Exception as e:
        print(f"❌ Configuration test failed: {e}")
        return False

if __name__ == "__main__":
    test_configuration() 