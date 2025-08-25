from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)


prompt1 = PromptTemplate(
    template='Generate Samll and simple notes from the followignt text  \n {text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='Generate a 5 short questiona nswers from the following text: \n  {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='merge the provided nodes and quiz in a simple document: \n  notes --> {notes} and quiz --> {quiz}',
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()


parallel_chain = RunnableParallel({
    'notes' : prompt1 | model | parser,
    'quiz' : prompt2 | model | parser
})

merge_chain = prompt3 | model | parser

chain = parallel_chain | merge_chain


text = '''
Hello
'''

result = chain.invoke({'text': text})

print(result)

chain.get_graph().print_ascii()