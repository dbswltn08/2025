import streamlit as st

st.set_page_config(page_title="K-POP 댄스 퀴즈🎶", page_icon="💃")

st.title("💃🕺 K-POP 댄스 퀴즈 앱 🎶")
st.write("텍스트 설명만 보고 어떤 K-POP 안무인지 맞혀보세요!")

# 문제 데이터
questions = [
    {
        "desc": "양손을 얼굴 옆에 두고 고양이처럼 귀여운 포즈를 취하는 포인트 안무. 트와이스의 대표곡!",
        "answer": "Cheer Up",
        "artist": "TWICE"
    },
    {
        "desc": "손가락으로 총을 만드는 동작이 유명한 안무. 블랙핑크의 히트곡!",
        "answer": "DDU-DU DDU-DU",
        "artist": "BLACKPINK"
    },
    {
        "desc": "말춤이라고 불리는 세계적으로 유명한 댄스. 싸이의 곡!",
        "answer": "Gangnam Style",
        "artist": "PSY"
    }
]

# 세션 상태 초기화
if "q_idx" not in st.session_state:
    st.session_state.q_idx = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "show_hint" not in st.session_state:
    st.session_state.show_hint = False

q = questions[st.session_state.q_idx]

st.subheader(f"문제 {st.session_state.q_idx + 1}")
st.write(q["desc"])

# 힌트 버튼
if st.button("힌트 보기 🕵️"):
    st.session_state.show_hint = True

if st.session_state.show_hint:
    st.info(f"👉 가수 힌트: **{q['artist']}**")

user_answer = st.text_input("정답을 입력하세요:", key=f"answer_{st.session_state.q_idx}")

if st.button("제출"):
    if user_answer.strip().lower() == q["answer"].lower():
        st.success("정답입니다! 🎉")
        st.session_state.score += 1
    else:
        st.error(f"땡! 정답은 **{q['answer']}** 입니다.")

    # 다음 문제 준비
    if st.session_state.q_idx < len(questions) - 1:
        st.session_state.q_idx += 1
        st.session_state.show_hint = False  # 다음 문제에서는 힌트 초기화
    else:
        st.balloons()
        st.write(f"🎊 퀴즈 완료! 최종 점수: {st.session_state.score}/{len(questions)}")

