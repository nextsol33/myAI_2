# 프론트앤드 연결하기
# streamlit.io
# pip install streamlit
# Docs-Install-Get Started에서 예제 샘플로 구현
# API reference에서 사용법 참고

# streamlit 설치 및 실행
# pip install streamlit
# python -m streamlit run 파일이름.py

# python-dotenv 사용
# github에 올릴때는 사용하지 않음. 등록하는 방법이 별도로 존재
# dotenv install
# from dotenv import load_dotenv
# load_dotenv()

# chat model - 대화형 기능
from langchain.chat_models import ChatOpenAI
chat_model = ChatOpenAI()

import streamlit as st

st.title('Talk to chtGPT - made by KBN')

content = st.text_input("Please enter the topic you would like to TALK")
# st.write(f"Topic is {content}.")


genre = st.radio(
    "What's your favorite topic?",
    ["Maxim", "3 line poem", "Funny"],
    index=None,
)

# st.write("You selected:", genre)

if genre == 'Maxim':
    st.write(f"You selected : {content} form {Maxim}.")
elif genre == '3 line poem':
    st.write(f"You selected : {content} form {3 line poem}.")
elif genre == 'Funny':
    st.write(f"You selected : {content} form {Fun Story}.")

if st.button('Request to chatGPT'):
    with st.spinner("Making a request to chatGPT"):
        if genre == 'Maxim':
            result = chat_model.predict("Tell me 5 maxims about " + content)
        elif genre == '3 line poem':
            result = chat_model.predict("Write a three-line poem about " + content)
        elif genre == 'Funny':
            result = chat_model.predict("Make a humorous story with " + content)
        st.write(result)

