import streamlit as st
from Chatbot_olymbaid.from_pinecone import result_pinecone
from Chatbot_olymbaid.from_mongo import result_mongo
from Chatbot_olymbaid.final_output import final_result
import streamlit as st
from Chatbot_olymbaid.model_api import load_embedding_model
from Chatbot_olymbaid.db_connect import connect_pineconedb
from Chatbot_olymbaid.db_connect import connect_mongodb
from Chatbot_olymbaid.model_api import load_chat_model


embedding_model=load_embedding_model()
index=connect_pineconedb()
collection = connect_mongodb()
chat_model=load_chat_model()
def main():
    st.set_page_config("QA with Documents")
    st.title('🦜🔗 Welcome to the Medical ChatBot')
    with st.form('my_form'):
        user_question= st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
        submitted = st.form_submit_button('Submit')
    if submitted :
        with st.spinner("Processing..."):
            result_p = result_pinecone(user_question,embedding_model,index)
            result_m , images=result_mongo(result_p,collection)
            response=final_result(user_question,result_m)
            st.write(response.response)
            st.display(images)
    
if __name__=="__main__":
    main()