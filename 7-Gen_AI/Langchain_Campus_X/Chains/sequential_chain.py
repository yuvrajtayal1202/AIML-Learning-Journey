from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


prompt1 = PromptTemplate(
    template='Generate a detailed report on  {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 porinter summary from the following text: \n  {text}',
    input_variables=['text']
)



llm = HuggingFaceEndpoint(
repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",

    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic':'vedant'})

print(result)

chain.get_graph().print_ascii()