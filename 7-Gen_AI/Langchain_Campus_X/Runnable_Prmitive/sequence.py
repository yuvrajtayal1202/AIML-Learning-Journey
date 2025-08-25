from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='google/gemma-2-2b-it',
    task='text-generation'
)
model = ChatHuggingFace(llm=llm)


prompt = PromptTemplate(
    template='Write a Joke about \n {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Exaplain the following  \n {joke}',
    input_variables=['joke']
)

parser = StrOutputParser()

chain = RunnableSequence(prompt, model, parser, prompt2, model, parser)

print(chain.invoke({'topic' : 'indian politics'}))