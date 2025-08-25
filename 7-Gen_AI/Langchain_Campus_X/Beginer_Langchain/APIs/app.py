from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes 
from langchain_community.llms import ollama
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

# os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

app = FastAPI(
    title="LangChain Server",
    version= '1.0',
    description='A simple API Server'
)


add_routes(
    app , ChatOpenAI(), path='/openai'
)

model = ChatOpenAI()

llm = ollama(model='llama2')

prompt1=ChatPromptTemplate.from_template('Write me an essay  {topic} around with 100 words')
prompt2=ChatPromptTemplate.from_template('Write me an poem  {topic} around with 100 words')


add_routes(
    app,
    prompt1|model,
    path='/essay'
)
add_routes(
    app,
    prompt2|model,
    path='/poem'
)


if __name__ == "__main__":
    uvicorn.run(app, host = 'localhost', port=8000)