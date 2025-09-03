import streamlit as st
import os

# Streamlit 페이지 설정
st.set_page_config(
    page_title="BCI 연구 계획서",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# HTML 파일 경로 설정 (폴더 구조에 맞게 수정)
# app.py와 같은 위치에 있는 'htmls' 폴더 안의 'index.html' 파일을 찾습니다.
html_file_path = os.path.join("htmls", "index.html")

# HTML 파일을 불러와서 페이지에 표시합니다.
try:
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Streamlit에 HTML 코드 렌더링
    st.components.v1.html(html_content, height=2000, scrolling=True)

except FileNotFoundError:
    st.error(f"오류: HTML 파일을 찾을 수 없습니다. '{html_file_path}' 경로를 확인해 주세요.")
    st.info("""
    GitHub와 streamlit.io에 배포할 때는 폴더 구조가 정확해야 합니다.
    
    `app.py` 파일과 같은 위치에 `htmls` 폴더가 있고,
    그 안에 `index.html` 파일이 있는지 확인해 주세요.
    """)

except Exception as e:
    st.error(f"HTML 파일을 불러오는 중 오류가 발생했습니다: {e}")
