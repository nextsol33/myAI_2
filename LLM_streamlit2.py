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

st.title('Talk to chatGPT with chatting - made by KBN')

content = st.text_input("Please enter the topic you would like to TALK")
# st.write(f"Topic is {content}.")


genre = st.radio(
    "What's your favorite topic?",
    ["Maxim", "Bible_verse", "Funny"],
    index=None,
)

# st.write("You selected:", genre)

if genre == 'Maxim':
    st.write(f"You selected : Maxim of {content}.")
elif genre == 'Bible_verse':
    st.write(f"You selected : Bible verse of {content}.")
elif genre == 'Funny':
    st.write(f"You selected : Funny stroy of {content}.")

if st.button('Request to chatGPT'):
    with st.spinner("Making a request to chatGPT"):
        if genre == 'Maxim':
            result = chat_model.predict("Tell me 5 maxims about " + content + " with source in korean")
        elif genre == 'Bible_verse':
            result = chat_model.predict("Let me know a Bible verse about " + content + " in korean")
        elif genre == 'Funny':
            result = chat_model.predict("Make me about humorous in 500 characters about " + content + " in korean")
        st.write(result)
