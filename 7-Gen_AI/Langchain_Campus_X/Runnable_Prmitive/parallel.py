from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='google/gemma-2-2b-it',
    task='text-generation'
)
model = ChatHuggingFace(llm=llm)


prompt1 = PromptTemplate(
    template='Generate a  tweet about a topic  {topic}',
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template='Generate a  Linkedin post about a topic  {topic}',
    input_variables=['topic']
)

prompt3 = PromptTemplate(
    template='Exaplain the following  \n {joke}',
    input_variables=['joke']
)

parser = StrOutputParser()

paraller_chain = RunnableParallel({
    'tweet' : RunnableSequence(prompt1, model, parser),
    'linkedin' : RunnableSequence(prompt2, model, parser)
})

result = paraller_chain.invoke({'topic' : 'AI'})

print('Tweet: ' ,  result['tweet'])
print('Linkedin: ' ,  result['linkedin'])