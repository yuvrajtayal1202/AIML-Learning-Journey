
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence,RunnableParallel, RunnablePassthrough, RunnableLambda

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='google/gemma-2-2b-it',
    task='text-generation'
)
model = ChatHuggingFace(llm=llm)

def word_counter(text):
    return len(text.split())

prompt = PromptTemplate(
    template='Write a Joke about \n {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Exaplain the following  \n {joke}',
    input_variables=['joke']
)

parser = StrOutputParser()


joke_gen_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'word_count' : RunnableLambda(word_counter)
})

chain = RunnableSequence(joke_gen_chain, parallel_chain)

chain.invoke({'topic' : 'cricket'})

print('Joke' , chain['joke'])
print('explanation' , chain['explanation'])