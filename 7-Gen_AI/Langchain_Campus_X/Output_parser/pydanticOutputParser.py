from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import PydanticToolsParser, ResponseSchema
from pydantic import BaseModel, EmailStr, Field
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='google/gemma-2-2b-it',
    task='text-generation'
)
model = ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name:str = Field(description= 'Name of the person')
    age: int = Field(gt=19, description='Age of the persom')
    city:str = Field(description='Name of the city ')
    
parser = PydanticToolsParser(pydantic_object=Person)

template = PromptTemplate(
    template='Generate the the name, age andf city of a fictioal {place} person {format_instructions}'
    input_variables=['place']
    partial_variables={'format_instruction' : parser.get_format_instruction()}   
)

prompt = template.invoke({'place' : 'indian'})

result = model.invoke(prompt)

fianl_result = parser.parse(result.content)

print(fianl_result)