!pip install gradio
import os
import google.generativeai as genai
import gradio as gr

os.environ["GEN_AI_API_KEY"] = "AIzaSyAQLrfHZtIYyqOKUpJcBCRVXID_bt1SaJg"


# Load API key securely
api_key = os.getenv("GEN_AI_API_KEY")  # Ensure you set this in your environment variables
if not api_key:
    raise ValueError("API key not found. Please set GEMINI_API_KEY as an environment variable.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="gemini-pro")

# Store conversation history for better context retention
chat_history = []

def chat_with_bot(user_input):
    global chat_history
    chat_history.append(f"You: {user_input}")

    try:
        response = model.generate_content("\n".join(chat_history))
        bot_reply = response.text
    except Exception as e:
        bot_reply = f"Error: {str(e)}"

    chat_history.append(f"Bot: {bot_reply}")
    return bot_reply

# Create Gradio Web Interface
gr.Interface(fn=chat_with_bot, inputs="text", outputs="text", title="AI Chatbot", description="Chat with AI!").launch()

!pip install langchain
!pip install langchain openai faiss-cpu tiktoken
!pip install google-generativeai

import google.generativeai as genai
genai.configure(api_key="GOOGLE_API_KEY")

!pip install google-generativeai langchain-google-genai
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import os
os.environ["GOOGLE_API_KEY"] = "AIzaSyAr9ULR9aWE6iZ3haCHRHUC9FPN6LRBUdI"  # Replace with your key
model=ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.environ["GOOGLE_API_KEY"])

messages=[
    SystemMessage(content="You are an oncologist expert."),
    HumanMessage(content="What are the developments and advancements take place in drug repurposing for anaplastic thyroid cancer in last five years?")
]
result=model.invoke(messages)
print(f"Answer from Google: {result.content}")

messages=[
    SystemMessage(content="You are an oncologist expert."),
    HumanMessage(content="What are the developments and advancements take place in drug repurposing for anaplastic thyroid cancer in last five years?"),
    AIMessage(content="I want to know about what drugs are known for repurposing anaplastic cancer treatment.")
]
result=model.invoke(messages)
print(f"Answer from Google: {result.content}")

model=ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.environ["GOOGLE_API_KEY"])

from langchain.schema import SystemMessage, HumanMessage, AIMessage

chat_history=[
    SystemMessage(content="You are an oncologist expert.")
]


while True:
    query = input("You:")
    if query.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=query))

    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))

    print(f"AI:,{response}")
chat_history.append(system_message)

while True:
    query = input("You:")
    if query.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=query))

    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))

    print(f"AI:,{response}")






