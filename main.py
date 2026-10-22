import streamlit as st
import streamlit.components.v1 as components

# 페이지 기본 설정
st.set_page_config(
    page_title="FC 바르셀로나 역대 시즌 & 유니폼/스쿼드 아카이브",
    page_icon="🔵🔴",
    layout="wide"
)

# 커스텀 CSS
st.markdown("""
<style>
    .main { background-color: #0B0E14; color: #E2E8F0; }
    h1, h2, h3 { color: #EDBB00 !important; font-family: 'Pretendard', sans-serif; }
    .trophy-badge {
        background-color: #A50044; color: white; padding: 4px 10px;
        border-radius: 20px; font-size: 0.85rem; font-weight: bold;
        display: inline-block; margin: 2px;
    }
    .kit-label { text-align: center; color: #EDBB00; font-weight: bold; font-size: 0.9rem; margin-bottom: 5px; }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 1. 고품질 일러스트 유니폼 SVG 생성 함수
# ---------------------------------------------------------
def render_kit_svg(pattern, kit_type="home", primary="#004D98", secondary="#A50044", accent="#EDBB00", collar_style="vneck"):
    stroke_color = "rgba(0,0,0,0.3)"
    
    if pattern == "half":
        patterns_svg = f'<rect x="200" y="80" width="100" height="280" fill="{secondary}" clip-path="url(#body-clip)"/>'
    elif pattern == "horizontal":
        stripes = "".join([f'<rect x="100" y="{y}" width="200" height="24" fill="{secondary}"/>' for y in range(120, 360, 48)])
        patterns_svg = f'<g clip-path="url(#body-clip)">{stripes}</g>'
    elif pattern == "checker":
        checkers = "".join([f'<rect x="{100 + c*25}" y="{80 + r*40}" width="25" height="40" fill="{secondary}"/>' for r in range(7) for c in range(4) if (r + c) % 2 == 1])
        patterns_svg = f'<g clip-path="url(#body-clip)">{checkers}</g>'
    elif pattern == "vertical_thin":
        stripes = "".join([f'<rect x="{x}" y="80" width="12" height="280" fill="{secondary}"/>' for x in range(112, 288, 24)])
        patterns_svg = f'<g clip-path="url(#body-clip)">{stripes}</g>'
    elif pattern == "vertical_wide":
        stripes = "".join([f'<rect x="{x}" y="80" width="33" height="280" fill="{secondary}"/>' for x in range(133, 267, 66)])
        patterns_svg = f'<g clip-path="url(#body-clip)">{stripes}</g>'
    elif pattern == "sash":
        patterns_svg = f'<polygon points="100,80 140,80 300,320 260,320" fill="{
