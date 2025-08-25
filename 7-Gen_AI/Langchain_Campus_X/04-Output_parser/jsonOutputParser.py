from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser 

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='google/gemma-2-2b-it',
    task='text-generation'
)
model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me the name, age and city of a fictional person {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction' : parser.get_format_instructions()}
)


chain = template | model | parser
 
result = chain.invoke({})

print(result)