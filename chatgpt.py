#!/usr/bin/env python3
import os
import sys
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import TextLoader, DirectoryLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.vectorstores import Chroma
import constants

os.environ["OPENAI_API_KEY"] = constants.API_KEY

CACHE = False
query = sys.argv[1]
loader = TextLoader("data.txt")
# loader = DirectoryLoader(".", glob="*.txt")

if CACHE and os.path.exists("persist"):
    print("Reusing index...\n")
    vectorstore = Chroma(persist_directory="persist", embedding_function=OpenAIEmbeddings())
    index = VectorstoreIndexCreator(vectorstore=vectorstore).from_loaders([loader])
else:
    index = VectorstoreIndexCreator().from_loaders([loader])

chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model="gpt-3.5-turbo"),
    retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
)
print(chain.run(query))
