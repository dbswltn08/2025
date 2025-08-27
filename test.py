import streamlit as st
import random

# -----------------------------
# 1. 문제 데이터 (정답 영어/한글 허용 + MV 링크)
# -----------------------------
quiz_data = [
    {
        "question": "한쪽 팔을 위로 들고 다른 손은 허리에 두며, 말 타는 듯 위아래로 뛰는 춤.",
        "answer": "강남스타일",
        "answer_alias": ["gangnam style"],
        "artist": "싸이",
        "youtube_url": "https://www.youtube.com/watch?v=9bZkp7q19f0"
    },
    {
        "question": "후렴에서 점프하며 양손을 위로 힘차게 뻗는 파워풀한 동작.",
        "answer": "불타오르네",
        "answer_alias": ["fire"],
        "artist": "BTS",
        "youtube_url": "https://www.youtube.com/watch?v=ALj5MKjy2BU"
    },
    {
        "question": "후렴에서 손가락으로 총 모양을 만들고 쏘는 듯한 포즈.",
        "answer": "뚜두뚜두",
        "answer_alias": ["ddudu ddudu", "ddu-du ddu-du"],
        "artist": "BLACKPINK",
        "youtube_url": "https://www.youtube.com/watch?v=IHNzOHi8sJs"
    },
    {
        "question": "무대 시작에 의자를 이용하다가 후렴에서 두 팔을 크게 벌리고 위로 뻗는 동작.",
        "answer": "에너제틱",
        "answer_alias": ["energetic", "워너원"],
        "artist": "Wanna One",
        "youtube_url": "https://www.youtube.com/watch?v=H5nsSgpc_Xk"  # KCON 2017 LA 공연
    }
    # 필요 시 나머지 문제들도 동일한 형식으로 추가
]

# -----------------------------
# 2. Streamlit 앱 구조
# -----------------------------
st.title("💃🕺 K-POP 댄스 퀴즈 🎶")
st.write("춤 설명을 보고 어떤 K-POP 곡인지 맞혀보세요!")

# 세션 상태 초기화
if "current_quiz" not in st.session_state:
    st.session_state.current_quiz = random.choice(quiz_data)
if "show_hint" not in st.session_state:
    st.session_state.show_hint = False

# 현재 문제 표시
st.subheader("문제 ❓")
st.write(st.session_state.current_quiz["question"])

# 힌트 버튼
if st.button("힌트 보기 🔎"):
    st.session_state.show_hint = True

# 힌트 표시 (가수 이름)
if st.session_state.show_hint:
    st.info(f"👉 힌트: 이 곡의 아티스트는 **{st.session_state.current_quiz['artist']}** 입니다.")

# 사용자 입력
user_answer = st.text_input("정답을 입력하세요:", "")

# 제출 버튼
if st.button("제출") and user_answer.strip():
    # 소문자 변환 및 공백 제거
    user_answer_clean = user_answer.strip().lower()
    correct_answers = [st.session_state.current_quiz["answer"].lower()] + \
                      [alias.lower() for alias in st.session_state.current_quiz.get("answer_alias", [])]

    if user_answer_clean in correct_answers:
        st.success("🎉 정답입니다!")
    else:
        st.error(f"❌ 오답! 정답은 **{st.session_state.current_quiz['answer']}** 입니다.")

    # 뮤직비디오 보여주기
    st.video(st.session_state.current_quiz["youtube_url"])

# 다음 문제 버튼
next_clicked = st.button("다음 문제 ▶️")
if next_clicked:
    st.session_state.current_quiz = random.choice(quiz_data)
    st.session_state.show_hint = False
    st.experimental_rerun()  # 버튼 클릭 시 즉시 새 문제 표시
