from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('./pdf.pdf')

docs = loader.load()

print(len(docs))
print(docs)

print(docs[0])