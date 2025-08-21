import streamlit as st

# MBTI별 추천 직업 데이터 예시 (간단 버전)
job_recommendations = {
    "INTJ": ["🧠 전략 기획자", "📊 데이터 분석가", "🔬 연구원", "⚙️ 엔지니어"],
    "ENTP": ["🚀 기업가", "📣 마케팅 전문가", "📝 기획자", "⚖️ 변호사"],
    "INFJ": ["💬 상담가", "✍️ 작가", "📚 교사", "🧘 심리학자"],
    "ESFP": ["🎭 배우", "📺 방송인", "🎉 이벤트 플래너", "🤝 영업직"],
}

# 🌟 메인 타이틀
st.markdown("<h1 style='text-align: center;'>🌍✨ MBTI 기반 진로 추천 🎯🚀</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>당신의 성격 유형에 딱 맞는 직업을 찾아보세요! 💡💼</h3>", unsafe_allow_html=True)

st.write("---")

# 🎨 MBTI 선택 박스
mbti = st.selectbox("💎 당신의 MBTI를 선택해주세요! 🌈", list(job_recommendations.keys()))

# 추천 결과 출력
if mbti:
    st.markdown(f"## 🔮 {mbti} 유형에게 어울리는 직업 리스트 🏆🌟")
    st.write("✨ 당신의 성향을 반짝이는 커리어로 연결해보세요! ✨")
    
    for job in job_recommendations[mbti]:
        st.markdown(f"- {job}")

    st.balloons()  # 🎈 추천 나오면 풍선 터뜨리기
    st.success("🌟 당신의 미래가 눈부시게 빛날 거예요! 🌟")
