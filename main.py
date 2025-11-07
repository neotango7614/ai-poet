from langchain_openai import OpenAI
from langchain_community.chat_models import ChatOpenAI
import streamlit as st

# llm = OpenAI()
# result = llm.predict("hi!")
# print(result)

# load_dotenv()

chat_model = ChatOpenAI()

content = "코딩"

result = chat_model.invoke(content + "에 대한 시를 써줘").content
print(result)

st.title('인공지능 시인')
title = st.text_input('시의 주제를 제시해 주세요')
if st.button("시 작성 요청"):
    with st.spinner('Wait for it'):
        result = chat_model.predict(title + "에 대한 시를 써줘")
        st.write(result)


