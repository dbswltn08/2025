import streamlit as st

st.set_page_config(page_title="K-POP 댄스 퀴즈🎶", page_icon="💃")

st.title("💃🕺 K-POP 댄스 퀴즈 앱 🎶")
st.write("춤 설명만 보고 어떤 K-POP 안무인지 맞혀보세요!")

# 문제 데이터 (정답을 리스트로 저장: 원래 제목 + 한국어 발음)
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
        "answers": ["gangnam style", "강남스타일"],
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

def normalize(text: str) -> str:
    """소문자 + 공백 제거"""
    return text.strip().lower().replace(" ", "")

# 현재 문제 불러오기
q = questions[st.session_state.q_idx]

st.subheader(f"문제 {st.session_state.q_idx + 1}")
st.write(q["desc"])

# 힌트 버튼
if st.button("힌트 보기 🕵️"):
    st.session_state.show_hint = True

if st.session_state.show_hint:
    st.info(f"👉 가수 힌트: **{q['artist']}**")

# 사용자 입력
user_answer = st.text_input("정답을 입력하세요:", key=f"answer_{st.session_state.q_idx}")

# 제출 버튼
if st.button("제출"):
    user_norm = normalize(user_answer)
    correct = any(user_norm == normalize(ans) for ans in q["answers"])

    if correct:
        st.success("정답입니다! 🎉")
        st.session_state.score += 1
    else:
        st.error(f"땡! 정답은 {', '.join(q['answers'])} 입니다.")

    # 다음 문제로 즉시 이동
    if st.session_state.q_idx < len(questions) - 1:
        st.session_state.q_idx += 1
        st.session_state.show_hint = False
        st.experimental_rerun()
    else:
        st.balloons()
        st.write(f"🎊 퀴즈 완료! 최종 점수: {st.session_state.score}/{len(questions)}")
