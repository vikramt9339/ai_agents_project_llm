import json
import time
import sys
import os
from IPython.display import display, Markdown, HTML, clear_output
import html

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import get_openai_client

# Get the OpenAI client
openai = get_openai_client()

# Define the model to use
MODEL = "gpt-4o-mini"

def stream_brochure(company_name, url):
    """
    Stream a beautiful brochure with enhanced formatting and styling
    """
    # Create a beautiful header
    header_html = f"""
    <div style="
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        text-align: center;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    ">
        <h1 style="margin: 0; font-size: 2.5em; font-weight: 300; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
            🏢 {company_name}
        </h1>
        <p style="margin: 10px 0 0 0; font-size: 1.1em; opacity: 0.9;">
            📄 AI-Generated Company Brochure
        </p>
        <div style="margin-top: 15px; padding: 10px; background: rgba(255,255,255,0.1); border-radius: 8px;">
            <small>🔗 Source: {url}</small>
        </div>
    </div>
    """
    
    # Display the header
    display(HTML(header_html))
    
    # Create a progress indicator
    progress_html = """
    <div style="
        background: #f8f9fa;
        border: 2px solid #e9ecef;
        border-radius: 10px;
        padding: 15px;
        margin: 20px 0;
        text-align: center;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    ">
        <div style="display: flex; align-items: center; justify-content: center; gap: 10px;">
            <div class="spinner" style="
                width: 20px;
                height: 20px;
                border: 3px solid #f3f3f3;
                border-top: 3px solid #667eea;
                border-radius: 50%;
                animation: spin 1s linear infinite;
            "></div>
            <span style="color: #6c757d; font-weight: 500;">🤖 AI is crafting your brochure...</span>
        </div>
    </div>
    
    <style>
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    </style>
    """
    
    display(HTML(progress_html))
    
    # Start the stream
    stream = openai.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": get_brochure_user_prompt(company_name, url)}
        ],
        stream=True
    )
    
    response = ""
    display_handle = display(HTML(""), display_id=True)
    
    # Process the stream with enhanced formatting
    for chunk in stream:
        if chunk.choices[0].delta.content:
            response += chunk.choices[0].delta.content
            
            # Clean and format the response
            formatted_response = format_brochure_content(response)
            
            # Create beautiful content wrapper
            content_html = f"""
            <div style="
                background: white;
                border-radius: 15px;
                padding: 30px;
                margin: 20px 0;
                box-shadow: 0 4px 20px rgba(0,0,0,0.08);
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                line-height: 1.6;
                color: #333;
            ">
                {formatted_response}
            </div>
            """
            
            # Update the display
            if display_handle:
                display_handle.update(HTML(content_html))
    
    # Add a beautiful footer
    footer_html = """
    <div style="
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 20px;
        border-radius: 15px;
        margin-top: 20px;
        text-align: center;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    ">
        <div style="display: flex; align-items: center; justify-content: center; gap: 15px;">
            <span style="font-size: 1.2em;">✨</span>
            <span style="font-weight: 500;">Brochure generated successfully!</span>
            <span style="font-size: 1.2em;">✨</span>
        </div>
        <p style="margin: 10px 0 0 0; opacity: 0.9; font-size: 0.9em;">
            Powered by AI • Generated with ❤️
        </p>
    </div>
    """
    
    display(HTML(footer_html))
    
    return response

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

# Enhanced system prompt for better brochure generation
system_prompt = """
You are an expert marketing copywriter and graphic designer. Create beautiful, professional company brochures that are:

1. **Visually appealing** - Use clear headings, bullet points, and structured content
2. **Professional** - Maintain a business-appropriate tone
3. **Comprehensive** - Cover key company information including:
   - Company overview and mission
   - Products/services offered
   - Key benefits and features
   - Contact information
4. **Engaging** - Use compelling language that captures attention
5. **Well-structured** - Organize content with clear sections and headings

Format your response using markdown with:
- ## for main sections
- ### for subsections
- **Bold** for emphasis
- Bullet points for lists
- Clear paragraphs for descriptions

Make the brochure informative, attractive, and professional.
"""

def get_brochure_user_prompt(company_name, url):
    """
    Generate a user prompt for brochure creation
    """
    return f"""
    Create a beautiful, professional brochure for {company_name} based on information from their website at {url}.
    
    The brochure should include:
    - An engaging company overview
    - Mission and vision statements
    - Key products or services
    - Unique value propositions
    - Contact information
    
    Make it visually appealing and professional, suitable for business use.
    """ 