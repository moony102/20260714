import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="MBTI 아이돌 추천기", page_icon="🌟")

st.title("🌟 MBTI별 맞춤 직업 & 아이돌 추천기")
st.write("당신의 MBTI를 선택하면, 성향에 맞는 직업과 같은 유형의 대표적인 아이돌을 추천해 드립니다!")
st.markdown("---")

# 16가지 MBTI별 데이터 (직업 및 이미지 URL)
# 실제 사진이 있는 경우 위키미디어 공용 링크를, 없는 경우 안정적인 더미 이미지 링크를 사용했습니다.
mbti_data = {
    "ISTJ": {
        "idol": "진니 (시크릿넘버)", 
        "career": "재무 관리자, 공무원, 회계사", 
        "img": "https://dummyimage.com/400x500/6a5acd/ffffff&text=Jinny+(ISTJ)"
    },
    "ISFJ": {
        "idol": "다현 (트와이스)", 
        "career": "보건의료 종사자, 교사, 사회복지사", 
        "img": "https://dummyimage.com/400x500/ff69b4/ffffff&text=Dahyun+(ISFJ)"
    },
    "INFJ": {
        "idol": "소진 (걸스데이)", 
        "career": "심리 상담가, 작가, 디자이너", 
        "img": "https://dummyimage.com/400x500/20b2aa/ffffff&text=Sojin+(INFJ)"
    },
    "INTJ": {
        "idol": "류진 (ITZY)", 
        "career": "데이터 과학자, 시스템 엔지니어, 건축가", 
        "img": "https://upload.wikimedia.org/wikipedia/commons/1/14/Ryujin_of_ITZY_in_2020.jpg"
    },
    "ISTP": {
        "idol": "윈터 (에스파)", 
        "career": "시스템 분석가, 소프트웨어 개발자, 엔지니어", 
        "img": "https://dummyimage.com/400x500/778899/ffffff&text=Winter+(ISTP)"
    },
    "ISFP": {
        "idol": "수빈 (투모로우바이투게더)", 
        "career": "패션 디자이너, 예술가, 수의사", 
        "img": "https://dummyimage.com/400x500/87cefa/ffffff&text=Soobin+(ISFP)"
    },
    "INFP": {
        "idol": "예리 (레드벨벳)", 
        "career": "순수 예술가, 카피라이터, 크리에이터", 
        "img": "https://dummyimage.com/400x500/dda0dd/ffffff&text=Yeri+(INFP)"
    },
    "INTP": {
        "idol": "진 (방탄소년단)", 
        "career": "컴퓨터 프로그래머, 대학교수, 연구원", 
        "img": "https://dummyimage.com/400x500/4682b4/ffffff&text=Jin+(INTP)"
    },
    "ESTP": {
        "idol": "연정 (우주소녀)", 
        "career": "기업가, 마케팅 디렉터, 스포츠 에이전트", 
        "img": "https://dummyimage.com/400x500/ff4500/ffffff&text=Yeonjung+(ESTP)"
    },
    "ESFP": {
        "idol": "엑시 (우주소녀)", 
        "career": "이벤트 기획자, 연예인, 승무원", 
        "img": "https://dummyimage.com/400x500/ff1493/ffffff&text=Exy+(ESFP)"
    },
    "ENFP": {
        "idol": "RM (방탄소년단)", 
        "career": "크리에이티브 디렉터, 홍보 전문가, 싱어송라이터", 
        "img": "https://upload.wikimedia.org/wikipedia/commons/c/cd/RM_at_the_White_House_press_briefing%2C_31_May_2022.jpg"
    },
    "ENTP": {
        "idol": "민경 (희나피아)", 
        "career": "발명가, 벤처 사업가, 정치인", 
        "img": "https://dummyimage.com/400x500/d2691e/ffffff&text=Minkyeung+(ENTP)"
    },
    "ESTJ": {
        "idol": "민지 (뉴진스)", 
        "career": "경영 컨설턴트, 프로젝트 매니저, 감독관", 
        "img": "https://upload.wikimedia.org/wikipedia/commons/e/e8/20230905_Minji_%28NewJeans%29.jpg"
    },
    "ESFJ": {
        "idol": "혜리 (걸스데이)", 
        "career": "교육자, 인사 담당자, 간호사", 
        "img": "https://upload.wikimedia.org/wikipedia/commons/8/87/Hyeri_2014_cropped.jpg"
    },
    "ENFJ": {
        "idol": "지민 (방탄소년단)", 
        "career": "교사, 사회운동가, PR 전문가", 
        "img": "https://dummyimage.com/400x500/32cd32/ffffff&text=Jimin+(ENFJ)"
    },
    "ENTJ": {
        "idol": "아이린 (레드벨벳)", 
        "career": "경영자, 기업 변호사, 전략 기획자", 
        "img": "https://upload.wikimedia.org/wikipedia/commons/c/c5/240511_Red_Velvet_Irene.jpg"
    }
}

# 사용자 입력 받기
mbti_options = ["선택하세요"] + list(mbti_data.keys())
selected_mbti = st.selectbox("📌 본인의 MBTI 유형을 골라주세요:", mbti_options)

# 결과 출력
if selected_mbti != "선택하세요":
    info = mbti_data[selected_mbti]
    
    st.subheader(f"당신과 같은 **{selected_mbti}** 유형의 아이돌은?")
    st.success(f"**{info['idol']}** 입니다! 🎉")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Streamlit은 URL을 바로 입력받아 이미지를 렌더링할 수 있습니다.
        st.image(info["img"], caption=f"{info['idol']} ({selected_mbti})", use_container_width=True)
        
    with col2:
        st.write("### 💼 추천 직업군")
        st.info(info["career"])
        
        st.write("### 💡 특징")
        st.write(f"{selected_mbti} 유형은 본인만의 뚜렷한 강점을 바탕으로 해당 직업군에서 뛰어난 성과를 낼 수 있는 잠재력을 가지고 있습니다.")

else:
    st.info("위의 드롭다운 메뉴에서 MBTI를 선택하면 결과가 나타납니다.")
