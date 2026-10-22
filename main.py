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
        patterns_svg = f'<polygon points="100,80 140,80 300,320 260,320" fill="{secondary}" clip-path="url(#body-clip)"/>'
    elif pattern == "vertical":
        stripes = "".join([f'<rect x="{x}" y="80" width="20" height="280" fill="{secondary}"/>' for x in range(120, 280, 40)])
        patterns_svg = f'<g clip-path="url(#body-clip)">{stripes}</g>'

    # 카라(넥라인) 스타일
    if collar_style == "polo":
        collar_svg = f'''
        <path d="M 165,80 L 200,120 L 235,80 L 220,70 L 200,85 L 180,70 Z" fill="{accent}" />
        <polygon points="185,80 200,120 215,80" fill="#111" opacity="0.3"/>
        '''
    elif collar_style == "round":
        collar_svg = f'''
        <path d="M 170,80 Q 200,110 230,80" fill="none" stroke="{accent}" stroke-width="8"/>
        '''
    else:  # vneck
        collar_svg = f'''
        <path d="M 170,80 L 200,115 L 230,80" fill="none" stroke="{accent}" stroke-width="7"/>
        '''

    svg_code = f'''
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

      <!-- 몸통 기본 -->
      <path d="M 130,80 L 170,80 Q 200,105 230,80 L 270,80 Q 285,130 295,190 L 280,350 L 120,350 L 105,190 Q 115,130 130,80 Z" fill="{primary}"/>
      {patterns_svg}

      <!-- 왼쪽 소매 -->
      <path d="M 130,80 L 105,190 L 50,165 L 85,70 Z" fill="{primary}"/>
      <rect x="30" y="50" width="120" height="150" fill="{secondary}" clip-path="url(#left-sleeve)" opacity="0.4"/>
      <path d="M 50,165 L 105,190" stroke="{accent}" stroke-width="6"/>

      <!-- 오른쪽 소매 -->
      <path d="M 270,80 L 295,190 L 350,165 L 315,70 Z" fill="{primary}"/>
      <rect x="250" y="50" width="120" height="150" fill="{secondary}" clip-path="url(#right-sleeve)" opacity="0.4"/>
      <path d="M 350,165 L 295,190" stroke="{accent}" stroke-width="6"/>

      <!-- 명암 질감 덮개 -->
      <path d="M 130,80 L 170,80 Q 200,105 230,80 L 270,80 Q 285,130 295,190 L 280,350 L 120,350 L 105,190 Q 115,130 130,80 Z" fill="url(#fabricGrad)"/>

      <!-- 디테일 외곽선 및 재봉선 -->
      <path d="M 130,80 L 170,80 Q 200,105 230,80 L 270,80 Q 285,130 295,190 L 280,350 L 120,350 L 105,190 Q 115,130 130,80 Z" fill="none" stroke="{stroke_color}" stroke-width="2"/>
      <path d="M 130,80 L 105,190" fill="none" stroke="{stroke_color}" stroke-width="2"/>
      <path d="M 270,80 L 295,190" fill="none" stroke="{stroke_color}" stroke-width="2"/>

      <!-- 엠블럼 상징 (좌측 가슴) -->
      <g transform="translate(150, 130)">
        <path d="M -12,-15 L 12,-15 L 12,0 C 12,12 0,18 0,18 C 0,18 -12,12 -12,0 Z" fill="#EDBB00" stroke="#000" stroke-width="1.5"/>
        <path d="M -9,-12 L 9,-12 L 9,-2 C 9,8 0,14 0,14 C 0,14 -9,8 -9,-2 Z" fill="#A50044"/>
        <rect x="-4" y="-10" width="8" height="2" fill="#004D98"/>
        <circle cx="0" cy="4" r="3" fill="#EDBB00"/>
      </g>

      <!-- 나이키 스우시 상징 (우측 가슴) -->
      <path d="M 235,125 Q 242,128 250,120 Q 244,131 233,128 Z" fill="{accent}"/>

      <!-- 카라/넥라인 -->
      {collar_svg}
    </svg>
    '''
    return svg_code

# ---------------------------------------------------------
# 2001/02 ~ 2024/25 전 시즌 데이터베이스
# ---------------------------------------------------------
SEASONS_DATA = [
    {
        "season": "2024/25", "era": "현대 에라", "manager": "한지 플릭", "top_scorer": "로베르트 레반도프스키",
        "trophies": ["진행 중"], "h_pat": "half", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "vneck",
        "a_pat": "solid", "a_p": "#111111", "a_s": "#111111", "a_a": "#EDBB00", "a_c": "vneck",
        "desc": "구단 창립 125주년을 기념하여 2008-09 트레블 시즌을 오마주한 50:50 반반 유니폼으로 복귀했습니다."
    },
    {
        "season": "2023/24", "era": "현대 에라", "manager": "차비 에르난데스", "top_scorer": "로베르트 레반도프스키 (26골)",
        "trophies": ["무관"], "h_pat": "vertical_wide", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "round",
        "a_pat": "solid", "a_p": "#FFFFFF", "a_s": "#FFFFFF", "a_a": "#004D98", "a_c": "round",
