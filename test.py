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
        "question": "후렴에서 양팔을 벌리고 몸을 좌우로 흔드는 국민 댄스.",
        "answer": "사랑을 했다",
        "answer_alias": ["love scenario", "i kon"],
        "artist": "iKON",
        "youtube_url": "https://www.youtube.com/watch?v=vecSVX1QYbQ"
    },
    {
        "question": "양손으로 얼굴 옆에 눈물 모양을 만들며 우는 듯한 포즈.",
        "answer": "TT",
        "answer_alias": ["티티", "twice"],
        "artist": "TWICE",
        "youtube_url": "https://www.youtube.com/watch?v=ePpPVE-GGJw"
    },
    {
        "question": "허리에 손을 두고 권총을 쏘는 듯한 관능적인 포즈.",
        "answer": "러브샷",
        "answer_alias": ["love shot", "exo"],
        "artist": "EXO",
        "youtube_url": "https://www.youtube.com/watch?v=pSudEWBAYRE"
    },
    {
        "question": "무대 시작에 의자를 이용하다가 후렴에서 두 팔을 크게 벌리고 위로 뻗는 동작.",
        "answer": "에너제틱",
        "answer_alias": ["energetic", "워너원"],
        "artist": "Wanna One",
        "youtube_url": "https://www.youtube.com/watch?v=H5nsSgpc_Xk"  # KCON 2017 LA 공연
    },
    {
        "question": "후렴에서 한쪽 손으로 얼굴을 가리고 눈만 살짝 드러내는 매혹적인 춤.",
        "answer": "피 땀 눈물",
        "answer_alias": ["blood sweat tears", "bts"],
        "artist": "BTS",
        "youtube_url": "https://www.youtube.com/watch?v=hmE9f-TEutc"
    },
    {
        "question": "후렴에서 손가락을 권총 모양으로 만들어 'Bang!' 하는 듯한 포즈.",
        "answer": "킬디스러브",
        "answer_alias": ["kill this love", "blackpink"],
        "artist": "BLACKPINK",
        "youtube_url": "https://www.youtube.com/watch?v=2S24-y0Ij3Y"
    },
    {
        "question": "양손을 머리 위로 올려 고양이 귀 모양을 만들고 흔드는 귀여운 춤.",
        "answer": "살짝 설렜어",
        "answer_alias": ["oh my girl", "slightly touched"],
        "artist": "오마이걸",
        "youtube_url": "https://www.youtube.com/watch?v=1WJhnjxkLNk"
    },
    {
        "question": "후렴에서 양팔을 크게 돌리며 중독적인 리듬에 맞춰 추는 헬리콥터 춤.",
        "answer": "링딩동",
        "answer_alias": ["ring ding dong", "shinee"],
        "artist": "샤이니",
        "youtube_url": "https://www.youtube.com/watch?v=roughtzsCDI"
    },
    {
        "question": "후렴에서 양손을 얼굴 옆으로 올리고 위아래로 흔드는 귀여운 춤.",
        "answer": "너무너무너무",
        "answer_alias": ["very very very", "ioi"],
        "artist": "아이오아이",
        "youtube_url": "https://www.youtube.com/watch?v=Q3J3qH2K_Gw"
    },
    {
        "question": "후렴 시작 부분에서 손가락을 입술에 대고 '쉿' 포즈를 하는 안무.",
        "answer": "러시안룰렛",
        "answer_alias": ["russian roulette", "red velvet"],
        "artist": "레드벨벳",
        "youtube_url": "https://www.youtube.com/watch?v=uR8Mrt1IpXg"
    },
    {
        "question": "후렴에서 양팔을 강하게 휘두르며 강렬한 에너지를 뿜어내는 춤.",
        "answer": "체리밤",
        "answer_alias": ["cherry bomb", "nct 127"],
        "artist": "NCT 127",
        "youtube_url": "https://www.youtube.com/watch?v=WkuHLzMMTZM"
    },
    {
        "question": "후렴에서 손가락으로 총 모양을 만들고 발랄하게 쏘는 듯한 포즈.",
        "answer": "피카부",
        "answer_alias": ["peek a boo", "red velvet"],
        "artist": "레드벨벳",
        "youtube_url": "https://www.youtube.com/watch?v=J_CFBjAyPWE"
    }
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

# 다음 문제 버튼 (즉시 갱신)
if st.button("다음 문제 ▶️"):
    st.session_state.current_quiz = random.choice(quiz_data)
    st.session_state.show_hint = False
    st.experimental_rerun()  # 즉시 화면 갱신
