from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from Chatbot_olymbaid.model_api import load_embedding_model
from Chatbot_olymbaid.db_connect import connect_pineconedb
from exception import customexception
import sys
def result_pinecone(query,embedding_model,index):
  try:
    embedding=embedding_model.embed_query(query)
    #embedding=embedding.tolist()

    result=index.query(
      vector=embedding,
      top_k=4,
    )
    return result
  except Exception as e:
        raise customexception(e,sys)



