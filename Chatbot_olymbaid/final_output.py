from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from exception import customexception
import sys
def final_result(combined_information,query,chat_model):
    try:
        prompt_text_chat = """
            You are a medical chatbot and an expert in anatomy.
            Answer the question based only on the following context, which can include text, images and tables:
            {context}
            Question: {question}
            Don't answer if you are not sure and decline to answer and say "Sorry, I don't have much information about it."
            Just return the helpful answer in as much as detailed possible.
            Answer:
            """

        prompt_chat = ChatPromptTemplate.from_template(prompt_text_chat)
        summarize_chain_chat = {"combined_information": lambda x: x} | prompt_chat | chat_model | StrOutputParser()
        response=summarize_chain_chat.invoke(query)
        return response
    except Exception as e:
        raise customexception(e,sys)
