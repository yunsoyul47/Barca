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
    """
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
        "desc": "클럽의 고전적인 세로 스트라이프와 함께 1970년대 요한 크루이프 시대를 오마주한 화이트 어웨이 유니폼을 선보였습니다."
    },
    {
        "season": "2022/23", "era": "현대 에라", "manager": "차비 에르난데스", "top_scorer": "로베르트 레반도프스키 (33골)",
        "trophies": ["라리가", "수페르코파 데 에스파냐"], "h_pat": "vertical_thin", "h_p": "#041E42", "h_s": "#A50044", "h_a": "#004D98", "h_c": "round",
        "a_pat": "solid", "a_p": "#E5C158", "a_s": "#E5C158", "a_a": "#004D98", "a_c": "round",
        "desc": "1992 올림픽 개최 30주년을 기념하는 다크 블루 3색 스트라이프와 올림픽 금메달을 형상화한 골드 어웨이를 착용했습니다."
    },
    {
        "season": "2021/22", "era": "현대 에라", "manager": "로날드 쿠만 / 차비 에르난데스", "top_scorer": "멤피스 데파이 (13골)",
        "trophies": ["무관"], "h_pat": "vertical", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "round",
        "a_pat": "solid", "a_p": "#A2C3D2", "a_s": "#A2C3D2", "a_a": "#A50044", "a_c": "round",
        "desc": "리오넬 메시가 이적한 첫 시즌. 클럽 엠블럼의 십자가와 스트라이프 패턴을 유니폼 상의에 직접 반영한 파격적인 디자인이었습니다."
    },
    {
        "season": "2020/21", "era": "현대 에라", "manager": "로날드 쿠만", "top_scorer": "리오넬 메시 (38골)",
        "trophies": ["코파 델 레이"], "h_pat": "vertical", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "round",
        "a_pat": "solid", "a_p": "#111111", "a_s": "#111111", "a_a": "#EDBB00", "a_c": "vneck",
        "desc": "1910년대 황금기를 오마주하여 스트라이프 사이에 노란색 골드 라인을 추가한 정갈한 디자인을 보여주었습니다."
    },
    {
        "season": "2019/20", "era": "현대 에라", "manager": "에르네스토 발베르데 / 키케 세티엔", "top_scorer": "리오넬 메시 (31골)",
        "trophies": ["무관"], "h_pat": "checker", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "vneck",
        "a_pat": "sash", "a_p": "#EDBB00", "a_s": "#004D98", "a_a": "#A50044", "a_c": "vneck",
        "desc": "구단 역사상 최초로 크로아티아 스타일의 체커보드(바둑판) 디자인을 도입하여 호불호와 화제를 동시에 모았습니다."
    },
    {
        "season": "2018/19", "era": "MSN & post-MSN", "manager": "에르네스토 발베르데", "top_scorer": "리오넬 메시 (51골)",
        "trophies": ["라리가", "수페르코파 데 에스파냐"], "h_pat": "vertical_thin", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "vneck",
        "a_pat": "solid", "a_p": "#E2F512", "a_s": "#E2F512", "a_a": "#004D98", "a_c": "round",
        "desc": "바르셀로나의 10개 구(District)를 상징하는 10개의 얇은 세로 줄무늬를 배치한 유니폼입니다."
    },
    {
        "season": "2017/18", "era": "MSN & post-MSN", "manager": "에르네스토 발베르데", "top_scorer": "리오넬 메시 (45골)",
        "trophies": ["라리가", "코파 델 레이"], "h_pat": "vertical", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "round",
        "a_pat": "solid", "a_p": "#4B9CD3", "a_s": "#4B9CD3", "a_a": "#A50044", "a_c": "round",
        "desc": "중앙 스트라이프는 굵고 외곽으로 갈수록 얇아지는 현대적인 페이드 스트라이프 디자인을 구현했습니다."
    },
    {
        "season": "2016/17", "era": "MSN 에라", "manager": "루이스 엔리케", "top_scorer": "리오넬 메시 (54골)",
        "trophies": ["코파 델 레이", "수페르코파 데 에스파냐"], "h_pat": "vertical", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "vneck",
        "a_pat": "solid", "a_p": "#4B2E83", "a_s": "#4B2E83", "a_a": "#E2F512", "a_c": "vneck",
        "desc": "1992년 웸블리 챔피언스리그 우승 25주년을 기념하여 고전적인 세로 줄무늬로 회귀한 유니폼입니다."
    },
    {
        "season": "2015/16", "era": "MSN 에라", "manager": "루이스 엔리케", "top_scorer": "루이스 수아레스 (59골)",
        "trophies": ["라리가", "코파 델 레이", "UEFA 슈퍼컵", "FIFA 클럽 월드컵"], "h_pat": "horizontal", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "vneck",
        "a_pat": "solid", "a_p": "#EDBB00", "a_s": "#EDBB00", "a_a": "#004D98", "a_c": "round",
        "desc": "구단 116년 역사상 최초로 홈 유니폼에 가로 스트라이프(Horizontal Stripes)를 채택한 파격적인 유니폼입니다."
    },
    {
        "season": "2014/15", "era": "MSN 에라", "manager": "루이스 엔리케", "top_scorer": "리오넬 메시 (58골)",
        "trophies": ["UEFA 챔피언스 리그 (트레블)", "라리가", "코파 델 레이"], "h_pat": "vertical_wide", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "vneck",
        "a_pat": "solid", "a_p": "#E75480", "a_s": "#E75480", "a_a": "#004D98", "a_c": "round",
        "desc": "메시-수아레스-네이마르(MSN) 라인의 첫 시즌이자 구단 역사상 두 번째 트레블(3관왕)을 달성한 전설적인 유니폼입니다."
    },
    {
        "season": "2013/14", "era": "황금기 후반", "manager": "헤라르도 타타 마르티노", "top_scorer": "리오넬 메시 (41골)",
        "trophies": ["수페르코파 데 에스파냐"], "h_pat": "vertical", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "vneck",
        "a_pat": "vertical", "a_p": "#EDBB00", "a_s": "#A50044", "a_a": "#004D98", "a_c": "round",
        "desc": "어웨이 유니폼에 카탈루냐 깃발(Senyera)의 노랑-빨강 세로 줄무늬 디자인을 최초로 도입했습니다."
    },
    {
        "season": "2012/13", "era": "황금기 후반", "manager": "티토 비라노바", "top_scorer": "리오넬 메시 (60골)",
        "trophies": ["라리가 (승점 100점)"], "h_pat": "sash", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "round",
        "a_pat": "solid", "a_p": "#EDBB00", "a_s": "#E75480", "a_a": "#004D98", "a_c": "round",
        "desc": "경계선이 번지는 파격적인 그래디언트 번짐 효과를 홈과 어웨이(오렌지-옐로우) 모두에 적용했습니다."
    },
    {
        "season": "2011/12", "era": "펩 에라", "manager": "펩 과르디올라", "top_scorer": "리오넬 메시 (73골)",
        "trophies": ["코파 델 레이", "수페르코파", "UEFA 슈퍼컵", "FIFA 클럽 월드컵"], "h_pat": "vertical_thin", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "round",
        "a_pat": "solid", "a_p": "#111111", "a_s": "#111111", "a_a": "#FFFFFF", "a_c": "round",
        "desc": "메시가 한 시즌 73골이라는 불멸의 기록을 세운 시즌으로, 촘촘하게 배열된 얇은 세로 스트라이프가 특징입니다."
    },
    {
        "season": "2010/11", "era": "펩 에라", "manager": "펩 과르디올라", "top_scorer": "리오넬 메시 (53골)",
        "trophies": ["UEFA 챔피언스 리그", "라리가", "수페르코파 데 에스파냐"], "h_pat": "vertical", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "round",
        "a_pat": "solid", "a_p": "#00A8B5", "a_s": "#00A8B5", "a_a": "#004D98", "a_c": "round",
        "desc": "웸블리에서 맨유를 꺾고 UCL을 제패한 전성기. 목 넥라인에 노란색 림 포인트를 더했습니다."
    },
    {
        "season": "2009/10", "era": "펩 에라", "manager": "펩 과르디올라", "top_scorer": "리오넬 메시 (47골)",
        "trophies": ["라리가", "수페르코파", "UEFA 슈퍼컵", "FIFA 클럽 월드컵"], "h_pat": "vertical", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "vneck",
        "a_pat": "solid", "a_p": "#E75480", "a_s": "#E75480", "a_a": "#111111", "a_c": "round",
        "desc": "전무후무한 6관왕(6-Sextuple) 신화를 완성한 시즌. 밝은 블루와 레드의 클래식한 세로 비율을 유지했습니다."
    },
    {
        "season": "2008/09", "era": "펩 에라", "manager": "펩 과르디올라", "top_scorer": "리오넬 메시 (38골)",
        "trophies": ["UEFA 챔피언스 리그 (트레블)", "라리가", "코파 델 레이"], "h_pat": "half", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "vneck",
        "a_pat": "solid", "a_p": "#FEF200", "a_s": "#FEF200", "a_a": "#004D98", "a_c": "round",
        "desc": "펩 과르디올라 부임 첫해 스페인 클럽 최초 '트레블'을 달성한 역사적 50:50 반반 유니폼입니다."
    },
    {
        "season": "2007/08", "era": "레이카르트 에라", "manager": "프랑크 레이카르트", "top_scorer": "티에리 앙리 (19골)",
        "trophies": ["무관"], "h_pat": "vertical_wide", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "round",
        "a_pat": "solid", "a_p": "#87CEEB", "a_s": "#87CEEB", "a_a": "#004D98", "a_c": "round",
        "desc": "캄 노우(Camp Nou) 개장 50주년을 기념하여 엠블럼 주위에 월계수 자수 테두리를 둘렀습니다."
    },
    {
        "season": "2006/07", "era": "레이카르트 에라", "manager": "프랑크 레이카르트", "top_scorer": "호나우지뉴 (24골)",
        "trophies": ["수페르코파 데 에스파냐"], "h_pat": "vertical_wide", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "vneck",
        "a_pat": "solid", "a_p": "#E2F512", "a_s": "#E2F512", "a_a": "#004D98", "a_c": "round",
        "desc": "구단 역사상 처음으로 유니폼 가슴 중앙에 상업 스폰서 대신 UNICEF 로고를 유상 기부 형태로 부착했습니다."
    },
    {
        "season": "2005/06", "era": "레이카르트 에라", "manager": "프랑크 레이카르트", "top_scorer": "사뮈엘 에토 (34골)",
        "trophies": ["UEFA 챔피언스 리그", "라리가", "수페르코파 데 에스파냐"], "h_pat": "vertical", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "vneck",
        "a_pat": "solid", "a_p": "#FEF200", "a_s": "#FEF200", "a_a": "#004D98", "a_c": "vneck",
        "desc": "호나우지뉴의 베르나베우 기립박수와 함께 파리에서 파리 생제르맹을 꺾고 14년 만에 UCL 우승을 차지했습니다."
    },
    {
        "season": "2004/05", "era": "레이카르트 에라", "manager": "프랑크 레이카르트", "top_scorer": "사뮈엘 에토 (29골)",
        "trophies": ["라리가"], "h_pat": "vertical_wide", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "vneck",
        "a_pat": "solid", "a_p": "#00A8B5", "a_s": "#00A8B5", "a_a": "#004D98", "a_c": "vneck",
        "desc": "6년 간의 무관을 깨고 라리가 우승을 차지한 암흑기 탈출의 해. 리오넬 메시의 1군 데뷔골이 터진 시즌입니다."
    },
    {
        "season": "2003/04", "era": "암흑기 & 재건", "manager": "프랑크 레이카르트", "top_scorer": "호나우지뉴 (22골)",
        "trophies": ["무관"], "h_pat": "vertical", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "polo",
        "a_pat": "solid", "a_p": "#C0C0C0", "a_s": "#C0C0C0", "a_a": "#004D98", "a_c": "round",
        "desc": "후안 라포르타 회장 부임과 호나우지뉴 영입으로 명가 재건의 위대한 첫걸음을 내딛은 시즌입니다."
    },
    {
        "season": "2002/03", "era": "암흑기 & 재건", "manager": "루이 판 할 / 안토니 리프스", "top_scorer": "파트릭 클라위버르트 (21골)",
        "trophies": ["무관"], "h_pat": "vertical_wide", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "polo",
        "a_pat": "solid", "a_p": "#004D98", "a_s": "#004D98", "a_a": "#EDBB00", "a_c": "round",
        "desc": "리그 6위라는 극심한 침체기를 겪었으나 챔피언스리그에서는 11연승 기록을 세우기도 했습니다."
    },
    {
        "season": "2001/02", "era": "암흑기 & 재건", "manager": "카를레스 렉사치", "top_scorer": "히바우두 / 파트릭 클라위버르트 (18골)",
        "trophies": ["무관"], "h_pat": "vertical_wide", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "polo",
        "a_pat": "solid", "a_p": "#E75480", "a_s": "#E75480", "a_a": "#004D98", "a_c": "round",
        "desc": "2000년대 초반 유니폼의 특징인 짙은 인디고 블루 색상과 정통 폴로 카라 목선이 돋보이는 키트입니다."
    }
]

# ---------------------------------------------------------
# UI 레이아웃 구현
# ---------------------------------------------------------
st.title("🔵🔴 FC Barcelona Kit & Season Archive")
st.caption("2001/02 시즌부터 현재까지의 역사적 프로필과 정교한 유니폼 일러스트 아카이브")

# 사이드바 필터
st.sidebar.header("🔍 시즌 검색 및 필터")
era_options = ["전체", "현대 에라", "MSN & post-MSN", "MSN 에라", "황금기 후반", "펩 에라", "레이카르트 에라", "암흑기 & 재건"]
selected_era = st.sidebar.selectbox("시대별 보기", era_options)
search_query = st.sidebar.text_input("시즌 / 감독 / 선수 검색", "")

# 데이터 필터링
filtered_seasons = SEASONS_DATA

if selected_era != "전체":
    filtered_seasons = [s for s in filtered_seasons if s["era"] == selected_era]

if search_query:
    q = search_query.lower()
    filtered_seasons = [
        s for s in filtered_seasons
        if q in s["season"].lower() or q in s["manager"].lower() or q in s["top_scorer"].lower() or q in s["desc"].lower()
    ]

st.write(f"총 **{len(filtered_seasons)}개**의 시즌이 조회되었습니다.")

# 시즌별 카드로 출력
for season in filtered_seasons:
    with st.container():
        st.markdown(f"### 📅 {season['season']} 시즌 <span style='font-size:0.9rem; color:#888;'>({season['era']})</span>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1.5, 1.5, 3])
        
        # 홈 유니폼 일러스트
        with col1:
            st.markdown("<div class='kit-label'>HOME KIT</div>", unsafe_allow_html=True)
            home_svg = render_kit_svg(season["h_pat"], "home", season["h_p"], season["h_s"], season["h_a"], season["h_c"])
            components.html(home_svg, height=230)
            
        # 어웨이 유니폼 일러스트
        with col2:
            st.markdown("<div class='kit-label'>AWAY KIT</div>", unsafe_allow_html=True)
            away_svg = render_kit_svg(season["a_pat"], "away", season["a_p"], season["a_s"], season["a_a"], season["a_c"])
            components.html(away_svg, height=230)
            
        # 시즌 정보
        with col3:
            st.markdown(f"**👔 감독:** {season['manager']}")
            st.markdown(f"**⚽ 시즌 최다 득점자:** {season['top_scorer']}")
            
            # 트로피 배지
            trophy_html = "<div><b>🏆 획득 타이틀:</b><br>"
            for t in season["trophies"]:
                trophy_html += f'<span class="trophy-badge">{t}</span>'
            trophy_html += "</div>"
            st.markdown(trophy_html, unsafe_allow_html=True)
            
            st.info(season["desc"])
            
        st.divider()
