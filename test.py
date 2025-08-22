import streamlit as st

st.set_page_config(page_title="K-POP 댄스 퀴즈🎶", page_icon="💃")

st.title("💃🕺 K-POP 댄스 퀴즈 앱 🎶")
st.write("춤 설명만 보고 어떤 K-POP 안무인지 맞혀보세요!")

# 문제 데이터 (정답을 리스트로 저장: 원래 제목 + 발음)
questions = [
    {
        "desc": "양손을 얼굴 옆에 두고 고양이처럼 귀여운 포즈를 취하는 포인트 안무.",
        "answers": ["cheer up", "치어럽"],
        "artist": "TWICE"
    },
    {
        "desc": "손가락으로 총을 만드는 동작이 유명한 안무.",
        "answers": ["ddu-du ddu-du", "뚜두뚜두"],
        "artist": "BLACKPINK"
    },
    {
        "desc": "말춤이라고 불리는 세계적으로 유명한 댄스.",
