import os
import sys
import gradio
import openai
from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma

import constants

os.environ["OPENAI_API_KEY"] = constants.APIKEY
def chatbot(pergunta):

  # Enable to save to disk & reuse the model (for repeated queries on the same data)
  PERSIST = False

  

  if PERSIST and os.path.exists("persist"):
    print("Reusing index...\n")
    vectorstore = Chroma(persist_directory="persist", embedding_function=OpenAIEmbeddings())
    index = VectorStoreIndexWrapper(vectorstore=vectorstore)
  else:
    #loader = TextLoader("data/data.txt") # Use this line if you only need data.txt
    loader = DirectoryLoader("data/")
    if PERSIST:
      index = VectorstoreIndexCreator(vectorstore_kwargs={"persist_directory":"persist"}).from_loaders([loader])
    else:
      index = VectorstoreIndexCreator().from_loaders([loader])

  chain = ConversationalRetrievalChain.from_llm(
    llm=ChatOpenAI(model="gpt-3.5-turbo"),
    retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
  )
  context = """
  você irá operar como assistente de suporte da Samsung. Você NÃO DEVE, em hipótese nenhuma, falar de outra empresa a não ser a Samsung.
  Garanta que você possa oferecer suporte ao cliente em relação aos produtos e à empresa de maneira profissional, educada e informativa. 
  Você deve ser estritamente profissional e educado em todas as interações com o cliente. 
  Você não deve falar de outras empresas ou de produtos que não sejam da Samsung. 
  Você não deve falar de outros assuntos triviais não relacionados à empresa. 
  Você não deve inventar fatos, e será honesto caso não tenha acesso à informação pedida.
  É PROIBIDO FALAR DE PRODUTOS DE OUTRAS EMPRESAS.
  É PROIBIDO FALAR DE OUTRAS EMPRESAS.
  SÓ É PERMITIDO FALAR DA SAMSUNG.
  """
  chat_history = []
  
  content = pergunta + "\n" + context
  result = chain({"question": context + "" + pergunta, "chat_history": chat_history})

  chat_history.append((pergunta, result['answer']))
  resultado = result['answer']
  return resultado

demo = gradio.Interface(fn = chatbot, inputs = "text", outputs = "text", title = "Samsung Chatbot")

demo.launch(share=True)
