# AI Agents Project LLM

A comprehensive project for learning and experimenting with Large Language Models (LLMs) and AI agents.

## 🚀 Quick Start

### 1. Environment Setup

First, install the required dependencies:

```bash
pip install python-dotenv openai requests beautifulsoup4 ipython
```

### 2. API Key Configuration

**Option A: Using the setup script (Recommended)**
```bash
python setup_env.py
```

**Option B: Manual setup**
1. Create a `.env` file in the project root
2. Add your API key:
```
OPENAI_API_KEY=your_actual_api_key_here
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
```

### 3. Using the Configuration

In your Jupyter notebooks, replace hardcoded API keys with:

```python
from config import get_openai_client, create_chat_completion

# Method 1: Get client and use directly
client = get_openai_client()
response = client.chat.completions.create(
    model="openai/gpt-4o-mini",
    messages=[{"role": "user", "content": "Hello!"}]
)

# Method 2: Use helper function
response = create_chat_completion([
    {"role": "user", "content": "Hello!"}
])
```

## 📁 Project Structure

```
ai_agents_project_llm/
├── week1/                 # Weekly learning materials
│   ├── day1.ipynb        # Introduction to LLMs
│   ├── day2.ipynb        # AI Agents basics
│   ├── day3.ipynb        # Advanced concepts
│   └── day5.ipynb        # Practical applications
├── config.py             # API configuration and utilities
├── setup_env.py          # Environment setup script
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## 🔐 Security Notes

- Never commit your `.env` file to version control
- The `.gitignore` file is configured to exclude sensitive files
- API keys are loaded from environment variables for security

## 📚 Learning Path

1. **Week 1**: Start with `day1.ipynb` to understand LLM basics
2. **Week 2**: Progress through the notebooks in order
3. **Week 3**: Experiment with your own AI agent projects

## 🤝 Contributing

Feel free to contribute by:
- Adding new examples
- Improving documentation
- Creating additional learning materials

## 📄 License

This project is for educational purposes.
