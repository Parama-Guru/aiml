import streamlit as st
from Chatbot_olymbaid.from_pinecone import result_pinecone
from Chatbot_olymbaid.from_mongo import result_mongo
from Chatbot_olymbaid.final_output import final_result
from Chatbot_olymbaid.final_output import refined_query
from Chatbot_olymbaid.elements import elements
from Chatbot_olymbaid.input_img import img_output
from Chatbot_olymbaid.input_img import delete_previous_images
from PIL import Image
import base64
from io import BytesIO
import os
import shutil
import atexit

def sample(embedding_model,index,collection,chat_model):
    st.markdown(
        """
            <style>
                .appview-container .main .block-container {{
                    padding-top: {padding_top}rem;
                    padding-bottom: {padding_bottom}rem;
                    }}

            </style>""".format(
            padding_top=1, padding_bottom=1
        ),
        unsafe_allow_html=True,
    )
    st.markdown("""
    <h3 style='text-align: left; color: black; padding-top: 35px; border-bottom: 3px solid red;'>
        Medical Anatomy Chatbot 🧘‍♂️🔬
    </h3>""", unsafe_allow_html=True)
    side_bar_message = """
    Hi! 👋 I'm here to help you with your medical anatomy.
    Feel free to ask me anything about medical anatomy!
    """
    with st.sidebar:
        st.title('🦜🔗 Welcome to the Medical ChatBot')
        st.markdown(side_bar_message)

    save_dir = 'uploaded_images'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    def cleanup():
        if os.path.exists(save_dir):
            shutil.rmtree(save_dir)
    atexit.register(cleanup)

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        delete_previous_images(save_dir)
        img = Image.open(uploaded_file)
        save_path = os.path.join(save_dir, uploaded_file.name)
        img.save(save_path)
    with st.form('my_form'):
        user_question= st.text_area('Enter text:','')
        submitted = st.form_submit_button('Submit')
    if submitted :
        with st.spinner("Processing..."):
            if not os.listdir(save_dir):
                query=refined_query(user_question,chat_model)
                result_p = result_pinecone(query,embedding_model,index)
            else:
            #     query=refined_query(user_question,img_summary,chat_model)
                query=img_output()
                result_p = result_pinecone(query,embedding_model,index)
            result_m , images=result_mongo(result_p,collection)
            response=final_result(result_m,query,chat_model)
            st.write(response)
            #st.write(query)
            for image in images:
                image_data = base64.b64decode(image)
                imagee = Image.open(BytesIO(image_data))
                st.image(imagee, caption='Image', use_column_width=True)

if __name__=="__main__":
    embedding_model,index,collection,chat_model=elements()
    sample(embedding_model,index,collection,chat_model)