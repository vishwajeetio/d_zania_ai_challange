from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
import openai
import chromadb
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def extract_text_from_pdf(pdf_path):
    documents = []
    loader = PyPDFLoader(pdf_path)
    documents.extend(loader.load())
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=10)
    chunked_documents = text_splitter.split_documents(documents)
    return chunked_documents

def store_embeddings_in_chromadb(text_chunks, pdf_path):
    client = chromadb.Client()
    persist_directory = f"collections/{pdf_path.split('.')[0]}"
    if client.list_collections():
        consent_collection = client.create_collection("consent_collection")
    else:
        print("Collection already exists")
    vectordb = Chroma.from_documents(
        documents=text_chunks,
        embedding=OpenAIEmbeddings(),
        persist_directory=persist_directory,
    )
    return vectordb
    

def process_pdf(pdf_path):
    text_chunks = extract_text_from_pdf(pdf_path)
    print(f"Extracted {len(text_chunks)} text chunks from the PDF")
    # embeddings = [generate_embeddings(chunk) for chunk in text_chunks]
    vectordb = store_embeddings_in_chromadb(text_chunks, pdf_path)
    
    return vectordb