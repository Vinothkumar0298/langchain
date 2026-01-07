from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
import os
import pandas as pd

with open("inputs/Restaurant_Reviews.txt", "r", encoding='utf-8') as f:
    text = f.read()

text = text.replace("\n"," ")
value = len(text)
chunk_holder = []
current_size = 0
while (current_size < value):
    chunk_holder.append(text[current_size:current_size + 500])
    current_size += 400


emebed = OllamaEmbeddings(model="mxbai-embed-large")

add_documents = not os.path.exists("./chroma_lang_chain_db")
db_location = "./chroma_lang_chain_db"

if add_documents:
    documents = []
    ids = []

    for x,short_note in enumerate(chunk_holder):
        document = Document(
            page_content= short_note,
            metadata = {"paragraph":f"paragraph{x}"},
            id =str(x)
        )
        documents.append(document)
        ids.append(str(x))


vector_store = Chroma(
    collection_name="indico",
    persist_directory=db_location,
    embedding_function=emebed
)

if add_documents:

    vector_store.add_documents(documents=documents,ids=ids)

vector_retrivers = vector_store.as_retriever(
    search_kwargs={'k':5}
)