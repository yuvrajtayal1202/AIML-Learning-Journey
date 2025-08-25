from langchain_community.document_loaders import DirectoryLoader, PyMuPDFLoader

loader = DirectoryLoader(
    path='director-name'
    glob='*'  #  all files *
    loader_cls= PyMuPDFLoader
    )

docs = loader.load()

print(len(docs))
