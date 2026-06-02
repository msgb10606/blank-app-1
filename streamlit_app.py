
import streamlit as st

# 앱 제목 설정
st.title("🍿 영화관 세트 메뉴 골라보기")
st.subheader("원하는 조합을 선택하시면 세트 메뉴를 추천해 드려요!")

# 1. 기존 데이터 정의
popcorn_options = ["기본", "카라멜", "어니언"]
drink_options = ["생수", "탄산음료"]

# 레이아웃을 위해 2개의 컬럼 생성
col1, col2 = st.columns(2)

with col1:
    # 팝콘 선택 셀렉트박스
    selected_popcorn = st.selectbox("🍿 팝콘 맛을 선택하세요", popcorn_options)

with col2:
    # 음료 선택 셀렉트박스
    selected_drink = st.selectbox("🥤 음료를 선택하세요", drink_options)

# 구분선
st.divider()

# 2. 사용자가 선택한 결과 출력
st.markdown(f"### 🎯 추천 세트 메뉴")
st.success(f"**세트 메뉴: {selected_popcorn} 팝콘, {selected_drink}**")


# --- (참고) 만약 기존 코드처럼 모든 조합을 한 번에 화면에 다 보여주고 싶다면? ---
with st.expander("👀 모든 가능한 세트 메뉴 조합 보기"):
    for popcorn in popcorn_options:
        for drink in drink_options:
            st.write(f"• 세트 메뉴: {popcorn} 팝콘, {drink}")