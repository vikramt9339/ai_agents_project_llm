# Add this to your day5.ipynb notebook

# 1. Update the import statement in Cell 0 to include HTML:
"""
import os
import requests
import json
from openai import OpenAI
from dotenv import load_dotenv
from typing import List
from bs4 import BeautifulSoup
from IPython.display import Markdown, display, update_display, HTML
"""

# 2. Add this function as a new cell after the stream_brochure function:

def format_brochure_content(content):
    """
    Format the brochure content with beautiful styling
    """
    # Convert markdown to HTML with custom styling
    formatted = content
    
    # Add custom styling for different elements
    formatted = formatted.replace("## ", '<h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px; margin-top: 30px;">')
    formatted = formatted.replace("### ", '<h3 style="color: #764ba2; margin-top: 25px;">')
    formatted = formatted.replace("**", '<strong style="color: #667eea;">')
    formatted = formatted.replace("**", '</strong>')
    
    # Style bullet points
    formatted = formatted.replace("- ", '<li style="margin: 8px 0; padding-left: 10px;">• ')
    formatted = formatted.replace("\n- ", '</li><li style="margin: 8px 0; padding-left: 10px;">• ')
    
    # Add icons for common sections
    formatted = formatted.replace("About", "🏢 About")
    formatted = formatted.replace("Services", "🛠️ Services")
    formatted = formatted.replace("Products", "📦 Products")
    formatted = formatted.replace("Contact", "📞 Contact")
    formatted = formatted.replace("Mission", "🎯 Mission")
    formatted = formatted.replace("Vision", "👁️ Vision")
    
    # Style paragraphs
    paragraphs = formatted.split('\n\n')
    styled_paragraphs = []
    for p in paragraphs:
        if p.strip() and not p.startswith('<'):
            styled_paragraphs.append(f'<p style="margin: 15px 0; text-align: justify;">{p}</p>')
        else:
            styled_paragraphs.append(p)
    
    formatted = '\n\n'.join(styled_paragraphs)
    
    return formatted

# 3. Add this helper function as another new cell:

def create_brochure_section(title, content, icon="📄"):
    """
    Create a beautiful brochure section
    """
    return f"""
    <div style="
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-left: 4px solid #667eea;
        padding: 20px;
        margin: 20px 0;
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    ">
        <h3 style="
            color: #667eea;
            margin: 0 0 15px 0;
            display: flex;
            align-items: center;
            gap: 10px;
        ">
            {icon} {title}
        </h3>
        <div style="color: #495057; line-height: 1.6;">
            {content}
        </div>
    </div>
    """

# 4. Test the beautiful brochure (add this as a new cell):

print("🎨 Beautiful brochure functions added!")
print("Now you can use:")
print("- stream_brochure('Company Name', 'https://company-website.com')")
print("- create_brochure_section('Title', 'Content', '🎯')") 