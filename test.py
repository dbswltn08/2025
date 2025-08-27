import streamlit as st
import random

# -----------------------------
# 1. 문제 데이터 (안무 존재 + 대표 춤 설명)
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
        "answer_alias": ["ddu-du ddu-du", "ddudu ddudu"],
        "artist": "BLACKPINK",
        "youtube_url": "https://www.youtube.com/watch?v=IHNzOHi8sJs"
    },
    {
        "question": "무대 시작에 의자를 이용하다가 후렴에서 두 팔을 크게 벌리고 위로 뻗는 동작.",
        "answer": "에너제틱",
        "answer_alias": ["energetic"],
        "artist": "Wanna One",
        "youtube_url": "https://www.youtube.com/watch?v=H5nsSgpc_Xk"
    },
    {
        "question": "양손을 볼 옆에 대고 상체를 들썩이며 깜찍하게 추는 춤.",
        "answer": "Gee",
        "answer_alias": ["지"],
        "artist": "소녀시대",
        "youtube_url": "https://www.youtube.com/watch?v=U7mPqycQ0tQ"
    },
    {
        "question": "허리에 손을 얹고 총 모양을 만들며 골반 웨이브를 하는 섹시한 춤.",
        "answer": "Love Shot",
        "answer_alias": ["러브샷"],
        "artist": "EXO",
        "youtube_url": "https://www.youtube.com/watch?v=pSudEWBAYRE"
    },
    {
        "question": "후렴에서 양손을 귀 옆에 대며 '샤샤샤'라고 하는 귀여운 안무.",
        "answer": "Cheer Up",
        "answer_alias": ["치어업"],
        "artist": "TWICE",
        "youtube_url": "https://www.youtube.com/watch?v=c7rCyll5AeY"
    },
    {
        "question": "손을 이마에 대고 외계인 신호를 보내는 듯한 동작.",
        "answer": "Signal",
        "answer_alias": ["시그널"],
        "artist": "TWICE",
        "youtube_url": "https://www.youtube.com/watch?v=VQtonf1fv_s"
    },
    {
        "question": "무릎을 굽혔다 일어나며 두 팔을 크게 위로 흔드는 파워풀한 춤.",
        "answer": "IDOL",
        "answer_alias": ["아이돌"],
        "artist": "BTS",
        "youtube_url": "https://www.youtube.com/watch?v=pBuZEGYXA6E"
    },
    {
        "question": "양손으로 손가락 하트를 만들어 위아래로 흔드는 안무.",
        "answer": "Heart Shaker",
        "answer_alias": ["하트 셰이커"],
        "artist": "TWICE",
        "youtube_url": "https://www.youtube.com/watch?v=rRzxEiBLQCA"
    },
    {
        "question": "후렴에서 손으로 과일을 따는 듯 양손을 위아래로 움직이는 안무.",
        "answer": "빨간맛",
        "answer_alias": ["red flavor"],
        "artist": "레드벨벳",
        "youtube_url": "https://www.youtube.com/watch?v=WyiIGEHQP8o"
    }
]

# -----------------------------
# 2. Streamlit 앱 UI
# -----------------------------
st.title("💃🕺 K-POP 댄스 퀴즈 🎶")
st.write("춤 설명을 보고 어떤 K-POP 곡인지 맞혀보세요!")

# 세션 상태 초기화
if "remaining_quiz" not in st.session_state:
    st.session_state.remaining_quiz = quiz_data.copy()
    random.shuffle(st.session_state.remaining_quiz)

if "current_quiz" not in st.session_state and st.session_state.remaining_quiz:
    st.session_state.current_quiz = st.session_state.remaining_quiz.pop()

if "show_hint" not in st.session_state:
    st.session_state.show_hint = False

if "user_answer" not in st.session_state:
    st.session_state.user_answer = ""

# 문제가 남아있을 경우
if "current_quiz" in st.session_state and st.session_state.current_quiz:
    st.subheader("문제 ❓")
    st.write(st.session_state.current_quiz["question"])

    # 힌트 버튼
    if st.button("힌트 보기 🔎"):
        st.session_state.show_hint = True

    # 힌트 표시 (가수 이름)
    if st.session_state.show_hint:
        st.info(f"👉 힌트: 이 곡의 아티스트는 **{st.session_state.current_quiz['artist']}** 입니다.")

    # 사용자 입력 (세션 값 연동)
    st.session_state.user_answer = st.text_input(
        "정답을 입력하세요:",
        value=st.session_state.user_answer
    )

    # 제출 버튼
    if st.button("제출") and st.session_state.user_answer.strip():
        user_answer_clean = st.session_state.user_answer.strip().lower()
        correct_answers = [st.session_state.current_quiz["answer"].lower()] + \
                          [alias.lower() for alias in st.session_state.current_quiz.get("answer_alias", [])]

        if user_answer_clean in correct_answers:
            st.success("🎉 정답입니다!")
        else:
            st.error(f"❌ 오답! 정답은 **{st.session_state.current_quiz['answer']}** 입니다.")

        # 뮤직비디오 표시
        st.video(st.session_state.current_quiz["youtube_url"])

    # 다음 문제 버튼
    if st.button("다음 문제 ▶️"):
        if st.session_state.remaining_quiz:
            st.session_state.current_quiz = st.session_state.remaining_quiz.pop()
            st.session_state.show_hint = False
            st.session_state.user_answer = ""  # 입력값 초기화
            st.rerun()
        else:
            st.session_state.current_quiz = None
            st.rerun()

# 문제가 다 끝난 경우
else:
    st.success("👏 모든 문제를 풀었습니다! 퀴즈가 끝났습니다.")
