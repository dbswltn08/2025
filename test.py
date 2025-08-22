import streamlit as st

st.set_page_config(page_title="K-POP 댄스 퀴즈🎶", page_icon="💃")

st.title("💃🕺 K-POP 댄스 퀴즈 앱 🎶")
st.write("춤 설명만 보고 어떤 K-POP 안무인지 맞혀보세요!")

# 문제 데이터 (정답을 리스트로 저장: 영어 제목 + 한국어 발음)
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
    },
    {
        "desc": "손으로 하트를 그리며 '사랑해'를 표현하는 안무.",
        "answers": ["boy with luv", "작은 것들을 위한 시", "보이윗럽"],
        "artist": "BTS"
    },
    {
        "desc": "양손을 번쩍 들고 허리를 흔드는 '꿀벌춤'이 포인트인 곡.",
        "answers": ["gee", "지"],
        "artist": "Girls' Generation"
    },
    {
        "desc": "어깨를 과장되게 으쓱하며 추는 '어깨춤'이 유명한 곡.",
        "answers": ["savage love", "새비지러브"],
        "artist": "Jawsh 685, Jason Derulo, BTS"
    },
    {
        "desc": "손바닥을 마주치며 '꽝'하는 듯한 동작이 포인트.",
        "answers": ["bang bang bang", "뱅뱅뱅"],
        "artist": "BIGBANG"
    },
    {
        "desc": "손으로 얼굴을 가리면서 고개를 숙이는 '포인트 포즈'가 인상적인 곡.",
        "answers": ["love shot", "러브샷"],
        "artist": "EXO"
    },
    {
        "desc": "양손을 펴서 흔드는 동작으로 '돈을 세는' 듯한 제스처가 유명.",
        "answers": ["money", "머니"],
        "artist": "LISA"
    },
    {
        "desc": "고개를 크게 까닥이며 추는 '머리 까딱 춤'이 포인트.",
        "answers": ["idol", "아이돌"],
        "artist": "BTS"
    },
    {
        "desc": "한쪽 발을 앞으로 차며 허리를 숙이는 '칼군무'가 압도적인 곡.",
        "answers": ["sherlock", "셜록"],
        "artist": "SHINee"
    },
    {
        "desc": "손가락으로 작은 하트를 만들며 따라하는 사람들이 많았던 곡.",
        "answers": ["tt", "티티"],
        "artist": "TWICE"
    },
    {
        "desc": "양손을 올려 왕관 모양을 만드는 안무가 포인트.",
        "answers": ["lion", "라이언"],
        "artist": "(G)I-DLE"
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
        st.rerun()  # 최신 Streamlit에서는 st.rerun() 사용
    else:
        st.balloons()
        st.write(f"🎊 퀴즈 완료! 최종 점수: {st.session_state.score}/{len(questions)}")
