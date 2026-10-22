import streamlit as st
import streamlit.components.v1 as components

# 페이지 기본 설정
st.set_page_config(
    page_title="FC 바르셀로나 역대 시즌 & 유니폼/스쿼드 아카이브",
    page_icon="🔵🔴",
    layout="wide"
)

# 커스텀 CSS (Blaugrana 테마)
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
# 1. 고품질 일러스트 유니폼 SVG 생성 함수
# ---------------------------------------------------------
def render_kit_svg(pattern, kit_type="home", primary="#004D98", secondary="#A50044", accent="#EDBB00", collar_style="vneck"):
    stroke_color = "rgba(0,0,0,0.3)"
    
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
        patterns_svg = f'<polygon points="100,80 140,80 300,320 260,320" fill="{secondary}" clip-path="url(#body-clip)"/>'
    elif pattern == "vertical":
        stripes = "".join([f'<rect x="{x}" y="80" width="20" height="280" fill="{secondary}"/>' for x in range(120, 280, 40)])
        patterns_svg = f'<g clip-path="url(#body-clip)">{stripes}</g>'

    if collar_style == "polo":
        collar_svg = f'''
        <path d="M 165,80 L 200,120 L 235,80 L 220,70 L 200,85 L 180,70 Z" fill="{accent}" />
        <polygon points="185,80 200,120 215,80" fill="#111" opacity="0.3"/>
        '''
    elif collar_style == "round":
        collar_svg = f'''
        <path d="M 170,80 Q 200,110 230,80" fill="none" stroke="{accent}" stroke-width="8"/>
        '''
    else:
        collar_svg = f'''
        <path d="M 170,80 L 200,115 L 230,80" fill="none" stroke="{accent}" stroke-width="7"/>
        '''

    svg_code = f"""
    <svg viewBox="0 0 400 420" width="100%" height="220" xmlns="http://www.w3.org/2000/svg" style="filter: drop-shadow(0px 8px 12px rgba(0,0,0,0.6));">
      <defs>
        <linearGradient id="fabricGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#ffffff" stop-opacity="0.15"/>
          <stop offset="50%" stop-color="#000000" stop-opacity="0.0"/>
          <stop offset="100%" stop-color="#000000" stop-opacity="0.35"/>
        </linearGradient>

        <clipPath id="body-clip">
          <path d="M 130,80 L 170,80 Q 200,105 230,80 L 270,80 Q 285,130 295,190 L 280,350 L 120,350 L 105,190 Q 115,130 130,80 Z"/>
        </clipPath>

        <clipPath id="left-sleeve">
          <path d="M 130,80 L 105,190 L 50,165 L 85,70 Z"/>
        </clipPath>
        <clipPath id="right-sleeve">
          <path d="M 270,80 L 295,190 L 350,165 L 315,70 Z"/>
        </clipPath>
      </defs>

      <path d="M 130,80 L 170,80 Q 200,105 230,80 L 270,80 Q 285,130 295,190 L 280,350 L 120,350 L 105,190
