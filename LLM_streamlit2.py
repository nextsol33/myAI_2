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

st.title('GPT와 대화 - made by KBN')

content = st.text_input("주제를 입력해주세요.")
# st.write(f"대화의 주제는 {content}입니다")


genre = st.radio(
    "What's your favorite topic?",
    ["Breave", "Wisdom", "Funny"],
    index=None,
)

# st.write("You selected:", genre)

if genre == 'Breave':
    st.write('You selected : Breave.')
elif genre == 'Wisdom':
    st.write('You selected : Wisdom.')
elif genre == 'Funny':
    st.write('You selected : Funny.')

if st.button('GPT에 요청하기'):
    with st.spinner("요청을 수행하는 중..."):
        if genre == 'Breave':
            result = chat_model.predict(content + "에 대해 명언을 알려줘")
        elif genre == 'Wisdom':
            result = chat_model.predict(content + "에 대해 3행시를 지어줘")
        elif genre == 'Funny':
            result = chat_model.predict(content + "에 대해 유머스런 이야기를 만들어해줘.")
        st.write(result)

