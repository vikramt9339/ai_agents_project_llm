#!/usr/bin/env python3
"""
Test script to demonstrate the beautiful streaming brochure generator
"""
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from streaming_brochure import stream_brochure, create_brochure_section
from IPython.display import display, HTML

def test_brochure_generator():
    """Test the beautiful brochure generator"""
    print("🎨 Testing Beautiful Brochure Generator...")
    
    try:
        # Test 1: Create a brochure section
        print("📄 Creating a sample brochure section...")
        section_html = create_brochure_section(
            title="Our Services",
            content="We provide cutting-edge technology solutions including AI, cloud computing, and digital transformation services that help businesses thrive in the digital age.",
            icon="🛠️"
        )
        
        # Display the section
        display(HTML(section_html))
        
        # Test 2: Generate a full brochure (commented out to avoid API costs)
        print("✅ Brochure section created successfully!")
        print("\n🚀 To generate a full streaming brochure, run:")
        print("brochure_content = stream_brochure('Your Company', 'https://your-website.com')")
        
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

if __name__ == "__main__":
    test_brochure_generator() 