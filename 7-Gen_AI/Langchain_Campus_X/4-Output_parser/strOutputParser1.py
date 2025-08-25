from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='google/gemma-2-2b-it',
    task='text-generation'
)
model = ChatHuggingFace(llm=llm)
# 1st prompt
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)
# 2nd fromd
template2 = PromptTemplate(
    template='Write a 5 line summary of following text. \n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = template1| model | parser | template2 | model | parser

result = chain.invoke({'topic': 'black hole'})


print(result) 

