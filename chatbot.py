from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import DirectoryLoader
from langchain.chat_models import ChatOpenAI
import magic
import os
import nltk
import constants


#cadastro da chave api presente no arquivo constants.py
os.environ["OPENAI_API_KEY"] = constants.APIKEY
openai_api_key = os.environ["OPENAI_API_KEY"]

def Samsung_Chatbot(pergunta):

    # nltk.download('averaged_perceptron_tagger')

    # pip install unstructured
    # Other dependencies to install https://python.langchain.com/en/latest/modules/indexes/document_loaders/examples/unstructured_file.html
    # pip install python-magic-bin
    # pip install chromadb
    # carregando diretório 
    loader = DirectoryLoader("data/")
    # carregando textos na variavel documents
    documents = loader.load()
    # preparando função para dividir os textos em partes de 1000 caracteres cada
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    # utilizando a função para dividir os textos
    texts = text_splitter.split_documents(documents)
    # transformando partes do texto em embeddings 
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    # preparando a procura dos documentos por embeddings através da biblioteca faiss do langchain
    docsearch = FAISS.from_documents(texts, embeddings)
    #Carregando LLM
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    # Criando retriever de informações
    #qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=docsearch.as_retriever())
    # Run a query

    qa = RetrievalQA.from_chain_type(llm=llm,
                                    chain_type="stuff",
                                    retriever=docsearch.as_retriever(),
                                    return_source_documents=True)
    result = qa({"query": pergunta})
    resp = result['result']
    #retornando resposta do chatgpt
    return resp

    
