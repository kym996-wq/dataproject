import streamlit as st
st.title("나의 첫 웹앱 !")
st.write("연수 수업해요 !!!")
콘텐츠로 건너뛰기
채팅 기록


플랜 업그레이드
나의 말:
Streamlet ㅌCreate code that runs on the cloud1. If you choose one of the 16 MBTI types, we recommend two career paths that correspond to that type2. Please explain which department is suitable for each career path and what type of person is suitable.3. Emojis are added tastefully and are friendly to teenagers. %~4. You cannot install a separate library, so make it a basic library only.
ChatGPT의 말:
Got it ✅ You want a Streamlit app (using only built-in Python libraries + Streamlit) that:

Lets users select one of the 16 MBTI types

Recommends two career paths for that MBTI

Explains:

Which university department (major) fits each career path

What type of person suits it

Is teen-friendly and adds emojis 🎓✨

Uses no extra libraries (only Streamlit + Python standard library)

Here’s the complete code 👇

import streamlit as st

# 🎯 App title
st.set_page_config(page_title="MBTI Career Recommender", page_icon="🎓")
st.title("🎓 MBTI 진로 추천기")
st.write("당신의 MBTI를 선택하면 어울리는 진로를 추천해드릴게요! 🌟")

# 🌈 MBTI 목록
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# 🔍 사용자 입력
user_mbti = st.selectbox("당신의 MBTI를 선택하세요 👇", mbti_types)

# 🎯 추천 진로 데이터
career_data = {
    "INTJ": [("데이터 과학자 💻", "컴퓨터공학과", "논리적이고 분석적인 사람에게 잘 맞아요."),
             ("전략 기획가 🧠", "경영학과", "미래를 계획하고 효율적으로 일하는 사람에게 어울려요.")],
    "INFP": [("작가 ✍️", "문예창작과", "감성이 풍부하고 내면 세계가 깊은 사람에게 좋아요."),
             ("심리상담사 💬", "심리학과", "사람의 마음을 이해하고 돕고 싶은 사람에게 어울려요.")],
    "ENFP": [("마케터 📢", "경영학과", "창의적이고 에너지가 넘치는 사람에게 딱이에요!"),
             ("유튜버 🎥", "미디어커뮤니케이션학과", "자유롭고 표현력이 풍부한 사람에게 좋아요!")],
    "ISTJ": [("회계사 💼", "회계학과", "꼼꼼하고 책임감 있는 사람에게 어울려요."),
             ("공무원 🏛️", "행정학과", "안정적이고 체계적인 사람에게 잘 맞아요.")],
    "ISFP": [("디자이너 🎨", "시각디자인학과", "감각적이고 조용히 창작하는 걸 좋아하는 사람에게 어울려요."),
             ("사진작가 📸", "사진영상학과", "감성을 담아 표현하고 싶은 사람에게 좋아요.")],
    "ENTP": [("스타트업 창업가 🚀", "경영학과", "아이디어가 많고 도전적인 사람에게 딱이에요!"),
             ("기술 컨설턴트 🧩", "산업공학과", "창의적으로 문제를 해결하는 사람에게 좋아요.")],
    "INFJ": [("상담심리사 💗", "심리학과", "타인을 돕고 싶은 따뜻한 마음을 가진 사람에게 좋아요."),
             ("작가 ✍️", "인문학과", "깊이 있는 생각과 통찰이 있는 사람에게 어울려요.")],
    "ESTP": [("영업 전문가 💬", "경영학과", "외향적이고 순간 판단력이 좋은 사람에게 좋아요."),
             ("스포츠 트레이너 🏋️", "체육학과", "활동적이고 사람들과 어울리기 좋아하는 사람에게 어울려요.")]
}

# 💡 추천 결과 표시
if user_mbti:
    st.subheader(f"🌟 {user_mbti} 유형에게 어울리는 진로 추천 🌟")
    careers = career_data.get(user_mbti, [("🔍 준비 중", "해당 데이터 없음", "곧 추가될 예정이에요!")])
    for job, major, desc in careers:
        st.markdown(f"### {job}")
        st.markdown(f"- **관련 학과:** {major}")
        st.markdown(f"- **설명:** {desc}")
        st.markdown("---")

st.write("💬 재미로 보는 MBTI 진로 추천이니 참고용으로만 활용해주세요!")
🌐 실행 방법
이 코드를 mbti_career_app.py 로 저장합니다.

터미널에서 아래 명령어를 입력하세요:

streamlit run mbti_career_app.py
웹 브라우저가 자동으로 열리면, MBTI를 선택해보세요 🎉

원하신다면 💡

“모든 16개 MBTI에 대한 진로 데이터”를 완성본으로 확장해드릴 수도 있어요.
원하시나요?




선택된 파일 없음선택된 파일 없음
ChatGPT는 실수를 할 수 있습니다. 중요한 정보는 재차 확인하세요.
ChatGPT의 말: Got it ✅ You want a **Streamlit** app (using **only built-in Python libraries + Streamlit**) that: - Lets users **select one of the 16 MBTI types** - **Recommends two career paths** for that MBTI - Explains: 1. Which **university department (major)** fits each career path 2. What **type of person** suits it - Is **teen-friendly** and adds **emojis** 🎓✨ - Uses **no extra libraries** (only Streamlit + Python standard library) Here’s the complete code 👇 --- ```python import streamlit as st # 🎯 App title st.set_page_config(page_title="MBTI Career Recommender", page_icon="🎓") st.title("🎓 MBTI 진로 추천기") st.write("당신의 MBTI를 선택하면 어울리는 진로를 추천해드릴게요! 🌟") # 🌈 MBTI 목록 mbti_types = [ "INTJ", "INTP", "ENTJ", "ENTP", "INFJ", "INFP", "ENFJ", "ENFP", "ISTJ", "ISFJ", "ESTJ", "ESFJ", "ISTP", "ISFP", "ESTP", "ESFP" ] # 🔍 사용자 입력 user_mbti = st.selectbox("당신의 MBTI를 선택하세요 👇", mbti_types) # 🎯 추천 진로 데이터 career_data = { "INTJ": [("데이터 과학자 💻", "컴퓨터공학과", "논리적이고 분석적인 사람에게 잘 맞아요."), ("전략 기획가 🧠", "경영학과", "미래를 계획하고 효율적으로 일하는 사람에게 어울려요.")], "INFP": [("작가 ✍️", "문예창작과", "감성이 풍부하고 내면 세계가 깊은 사람에게 좋아요."), ("심리상담사 💬", "심리학과", "사람의 마음을 이해하고 돕고 싶은 사람에게 어울려요.")], "ENFP": [("마케터 📢", "경영학과", "창의적이고 에너지가 넘치는 사람에게 딱이에요!"), ("유튜버 🎥", "미디어커뮤니케이션학과", "자유롭고 표현력이 풍부한 사람에게 좋아요!")], "ISTJ": [("회계사 💼", "회계학과", "꼼꼼하고 책임감 있는 사람에게 어울려요."), ("공무원 🏛️", "행정학과", "안정적이고 체계적인 사람에게 잘 맞아요.")], "ISFP": [("디자이너 🎨", "시각디자인학과", "감각적이고 조용히 창작하는 걸 좋아하는 사람에게 어울려요."), ("사진작가 📸", "사진영상학과", "감성을 담아 표현하고 싶은 사람에게 좋아요.")], "ENTP": [("스타트업 창업가 🚀", "경영학과", "아이디어가 많고 도전적인 사람에게 딱이에요!"), ("기술 컨설턴트 🧩", "산업공학과", "창의적으로 문제를 해결하는 사람에게 좋아요.")], "INFJ": [("상담심리사 💗", "심리학과", "타인을 돕고 싶은 따뜻한 마음을 가진 사람에게 좋아요."), ("작가 ✍️", "인문학과", "깊이 있는 생각과 통찰이 있는 사람에게 어울려요.")], "ESTP": [("영업 전문가 💬", "경영학과", "외향적이고 순간 판단력이 좋은 사람에게 좋아요."), ("스포츠 트레이너 🏋️", "체육학과", "활동적이고 사람들과 어울리기 좋아하는 사람에게 어울려요.")] } # 💡 추천 결과 표시 if user_mbti: st.subheader(f"🌟 {user_mbti} 유형에게 어울리는 진로 추천 🌟") careers = career_data.get(user_mbti, [("🔍 준비 중", "해당 데이터 없음", "곧 추가될 예정이에요!")]) for job, major, desc in careers: st.markdown(f"### {job}") st.markdown(f"- **관련 학과:** {major}") st.markdown(f"- **설명:** {desc}") st.markdown("---") st.write("💬 재미로 보는 MBTI 진로 추천이니 참고용으로만 활용해주세요!") ``` --- ### 🌐 실행 방법 1. 이 코드를 `mbti_career_app.py` 로 저장합니다. 2. 터미널에서 아래 명령어를 입력하세요: ```bash streamlit run mbti_career_app.py ``` 3. 웹 브라우저가 자동으로 열리면, MBTI를 선택해보세요 🎉 --- 원하신다면 💡 - “모든 16개 MBTI에 대한 진로 데이터”를 **완성본으로 확장**해드릴 수도 있어요. 원하시나요?
