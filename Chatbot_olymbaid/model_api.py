from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
import getpass
import os
import export
import anthropic
from exception import customexception
import sys
import os
from getpass import getpass
from dotenv import load_dotenv
load_dotenv()
#GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
#ANTHROPIC_API_KEY=os.environ.get["ANTHROPIC_API_KEY"]
ANTHROPIC_API_KEY=os.getenv("ANTHROPIC_API_KEY")
#export ANTHROPIC_API_KEY = "dajbjbajsbsa"
os.environ["ANTHROPIC_API_KEY"] = ANTHROPIC_API_KEY

def load_embedding_model():
    embedding_model = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004",google_api_key=GOOGLE_API_KEY)
    return embedding_model
def load_chat_model():
    chat_model=ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",google_apikey=GOOGLE_API_KEY,temperature=0,max_tokens=2000,
    timeout=2000)
    return chat_model
def load_anthropic_model():
    try:
        a="ANTHROPIC_API_KEY"
        return a
    except Exception as e:
        raise customexception(e,sys)
