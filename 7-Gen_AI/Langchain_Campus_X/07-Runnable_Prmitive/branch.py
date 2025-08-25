
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence,RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='google/gemma-2-2b-it',
    task='text-generation'
)
model = ChatHuggingFace(llm=llm)

prompt = PromptTemplate(
    template='Write a detailed report on \n {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='summarize the following text \n {text} ',
    input_variables=['text']
)

parser = StrOutputParser()


report_gen_chain = RunnableSequence(prompt, model, parser)

branch_chain = RunnableBranch(
        (lambda x: len(x.split()) > 500 , RunnableSequence(prompt2, model, parser)),
        RunnablePassthrough()
        
)

final_chain = RunnableSequence (report_gen_chain ,branch_chain)

result = final_chain.invoke({'topic' : 'cricket'})

print(result)