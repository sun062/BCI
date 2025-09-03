import streamlit as st
import os

# Streamlit 페이지 설정
st.set_page_config(
    page_title="BCI 연구 계획서",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 파일 경로 정의
html_file_path = "./htmls/index.html"

# HTML 파일을 불러와서 페이지에 표시
try:
    if not os.path.exists(html_file_path):
        raise FileNotFoundError(f"File not found: {html_file_path}")

    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Streamlit에 HTML 코드 렌더링
    st.components.v1.html(html_content, height=2000, scrolling=True)

except FileNotFoundError as e:
    st.error(f"오류: {e}")
    st.info("""
    **'htmls/index.html' 파일을 찾을 수 없습니다.**

    `app.py` 파일과 같은 위치에 `htmls`라는 이름의 폴더를 만들고, 그 안에 `index.html` 파일을 저장해 주세요.

    **폴더 구조 예시:**
    ```
    - your_project_folder/
      ├── app.py
      └── htmls/
          └── index.html
    ```
    """)
