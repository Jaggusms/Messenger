import streamlit as st
from PIL import Image
import base64,os
PAGE_TITLE = "Jagadeesh Messenger"
st.set_page_config(page_title=PAGE_TITLE,layout="wide")
st.get_option("theme.primaryColor")
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(f"""<style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-attachment: fixed;
        background-size: cover
    }}</style>""",unsafe_allow_html=True)
add_bg_from_local('source/charcoal.png') 

with open("css/style.css") as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
from datetime import datetime


st.write("Please wait loading!")

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://Jaggusmk:4321@cluster0.bzwyzf9.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
data=list(client.newdatabase.messges.find())[::-1]
d=dict()
out=0
message="Hi Welcome"
with st.form("form 1",clear_on_submit=True):
    message=st.text_area(label="Enter New Message", placeholder="Message")
    out=st.form_submit_button("Submit")
    if out:  
        d['Time'],d['message']=datetime.now(),message
        client['newdatabase']['messges'].insert_one(d)
        st.success("Submit Successfully, Please refresh the page")
for i in  data:
     if i.get("message","")!="":
         st.write(str(i.get("message","")))

 
