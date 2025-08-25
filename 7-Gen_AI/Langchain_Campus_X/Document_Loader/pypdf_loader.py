from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('')

docs = loader.load()

print(len(docs))
print(docs)

print(docs[0])