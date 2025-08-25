from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)


class Feedback(BaseModel):
    sentiment: Literal['Positive', 'Negative'] = Field(description='Give the setiment of the feedback')
    
parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the  followign feed text into postive or negative \n {feedback} \n {format}',
    input_variables=['feedback'],
    partial_variables={'format':parser2.get_format_instructions()}
)


parser = StrOutputParser()

classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template='Write an appropiate response for this positive feedback \n {feedback}',
    input_variables=['feedback']
)
prompt3 = PromptTemplate(
    template='Write an appropiate response for this negative feedback \n {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x['sentiment'] == 'Positive', prompt2 | model | parser),
    (lambda x:x['sentiment'] == 'Negative', prompt3 | model | parser),
     RunnableLambda(lambda x: 'Could not find sentimrnt')
)

chain = classifier_chain | branch_chain

print(chain.invoke({'feedback' : 'THis is a Terrible phone'}))

chain.get_graph().print_ascii()