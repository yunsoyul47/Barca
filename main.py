import streamlit as st
import streamlit.components.v1 as components

# 페이지 기본 설정
st.set_page_config(
    page_title="FC 바르셀로나 역대 시즌 & 유니폼 아카이브 (2001/02 - 현재)",
    page_icon="🔵🔴",
    layout="wide"
)

# 커스텀 CSS (Blaugrana 테마 스타일링)
st.markdown("""
<style>
    .main {
        background-color: #0B0E14;
        color: #E2E8F0;
    }
    h1, h2, h3 {
        color: #EDBB00 !important;
        font-family: 'Pretendard', sans-serif;
    }
    .stAppHeader {
        background-color: rgba(11, 14, 20, 0.9);
    }
    .season-card {
        background: linear-gradient(135deg, #151922, #1E2430);
        border: 1px solid rgba(237, 187, 0, 0.2);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 24px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }
    .trophy-badge {
        background-color: #A50044;
        color: white;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: bold;
        display: inline-block;
        margin: 2px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.3);
    }
    .kit-label {
        text-align: center;
        color: #EDBB00;
        font-weight: bold;
        font-size: 0.9rem;
        margin-bottom: 5px;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 고품질 일러스트 유니폼 SVG 생성 함수
# ---------------------------------------------------------
def render_kit_svg(pattern, kit_type="home", primary="#004D98", secondary="#A50044", accent="#EDBB00", collar_style="vneck"):
    stroke_color = "rgba(0,0,0,0.3)"
    
    # 패턴 정의
    patterns_svg = ""
    if pattern == "half":
        patterns_svg = f'<rect x="200" y="80" width="100" height="280" fill="{secondary}" clip-path="url(#body-clip)"/>'
    elif pattern == "horizontal":
        stripes = "".join([f'<rect x="100" y="{y}" width="200" height="24" fill="{secondary}"/>' for y in range(120, 360, 48)])
        patterns_svg = f'<g clip-path="url(#body-clip)">{stripes}</g>'
    elif pattern == "checker":
        checkers = ""
        for row in range(7):
            for col in range(4):
                if (row + col) % 2 == 1:
                    checkers += f'<rect x="{100 + col*25}" y="{80 + row*40}" width="25" height="40" fill="{secondary}"/>'
        patterns_svg = f'<g clip-path="url(#body-clip)">{checkers}</g>'
    elif pattern == "vertical_thin":
        stripes = "".join([f'<rect x="{x}" y="80" width="12" height="280" fill="{secondary}"/>' for x in range(112, 288, 24)])
        patterns_svg = f'<g clip-path="url(#body-clip)">{stripes}</g>'
    elif pattern == "vertical_wide":
        stripes = "".join([f'<rect x="{x}" y="80" width="33" height="280" fill="{secondary}"/>' for x in range(133, 267, 66)])
        patterns_svg = f'<g clip-path="url(#body-clip)">{stripes}</g>'
    elif pattern == "sash":
        patterns_svg = f'<polygon points="100,80 140,80 300,320 260,320" fill="{secondary}" clip-path="url(#body-
