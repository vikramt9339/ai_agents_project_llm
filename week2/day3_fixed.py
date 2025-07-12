# Complete working chat function with all dependencies
import os
from openai import OpenAI
import gradio as gr

# Define the client and model
openai = OpenAI(
    api_key='YOUR_API_KEY_HERE',  # Replace with your actual API key
    base_url='https://api.openai.com/v1'
)
MODEL = 'gpt-4o-mini'

# Define the system message
system_message = "You are a helpful assistant in a clothes store. You should try to gently encourage \
the customer to try items that are on sale. Hats are 60% off, and most other items are 50% off. \
For example, if the customer says 'I'm looking to buy a hat', \
you could reply something like, 'Wonderful - we have lots of hats - including several that are part of our sales event.'\
Encourage the customer to buy hats if they are unsure what to get."

system_message += "\nIf the customer asks for shoes, you should respond that shoes are not on sale today, \
but remind the customer to look at hats!"

def chat(message, history):
    relevant_system_message = system_message
    if 'belt' in message:
        relevant_system_message += " The store does not sell belts; if you are asked for belts, be sure to point out other items on sale."
    
    messages = [{"role": "system", "content": relevant_system_message}] + history + [{"role": "user", "content": message}]

    stream = openai.chat.completions.create(model=MODEL, messages=messages, stream=True)

    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ''
        yield response

# Launch the interface
if __name__ == "__main__":
    gr.ChatInterface(fn=chat, type="messages").launch() 