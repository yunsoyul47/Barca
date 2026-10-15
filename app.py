import streamlit as st
import streamlit.components.v1 as components

# 페이지 기본 설정
st.set_page_config(
    page_title="FC Barcelona 역대 시즌 & 유니폼 Archive",
    page_icon="🔵🔴",
    layout="wide"
)

# 커스텀 CSS (Blaugrana 테마)
st.markdown("""
<style>
    .main {
        background-color: #0b0e14;
        color: #e0e0e0;
    }
    .stAppHeader {
        background-color: rgba(11, 14, 20, 0.8);
    }
    h1, h2, h3 {
        color: #EDBB00 !important;
        font-family: 'Pretendard', sans-serif;
    }
    .season-card {
        background: linear-gradient(145deg, #151922, #1c2331);
        border: 1px solid rgba(237, 187, 0, 0.2);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
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
    }
    .metric-box {
        background-color: #0f141d;
        border-left: 3px solid #004D98;
        padding: 8px 12px;
        border-radius: 4px;
        margin-top: 6px;
    }
</style>
""", unsafe_allow_html=True)

# SVG 유니폼 생성 함수
def get_kit_svg(pattern_type, kit_type="home", primary_color="#004D98", secondary_color="#A50044"):
    if kit_type == "home":
        if pattern_type == "half": # 2008-09, 2024-25 반반
            body = f'<rect x="25" y="20" width="25" height="70" fill="{primary_color}"/><rect x="50" y="20" width="25" height="70" fill="{secondary_color}"/>'
            sleeves = f'<path d="M 5,25 L 25,20 L 25,45 L 12,48 Z" fill="{secondary_color}"/><path d="M 95,25 L 75,20 L 75,45 L 88,48 Z" fill="{primary_color}"/>'
        elif pattern_type == "horizontal": # 2015-16 가로 스트라이프
            body = f'<rect x="25" y="20" width="50" height="70" fill="{primary_color}"/>'
            body += f'<rect x="25" y="32" width="50" height="9" fill="{secondary_color}"/><rect x="25" y="50" width="50" height="9" fill="{secondary_color}"/><rect x="25" y="68" width="50" height="9" fill="{secondary_color}"/>'
            sleeves = f'<path d="M 5,25 L 25,20 L 25,45 L 12,48 Z" fill="{primary_color}"/><path d="M 95,25 L 75,20 L 75,45 L 88,48 Z" fill="{primary_color}"/>'
        elif pattern_type == "checker": # 2019-20 체커보드
            body = f'<rect x="25" y="20" width="50" height="70" fill="{primary_color}"/>'
            body += f'<rect x="25" y="20" width="25" height="23" fill="{secondary_color}"/><rect x="50" y="43" width="25" height="23" fill="{secondary_color}"/><rect x="25" y="66" width="25" height="24" fill="{secondary_color}"/>'
            sleeves = f'<path d="M 5,25 L 25,20 L 25,45 L 12,48 Z" fill="{primary_color}"/><path d="M 95,25 L 75,20 L 75,45 L 88,48 Z" fill="{primary_color}"/>'
        else: # 기본 세로 스트라이프
            body = f'<rect x="25" y="20" width="50" height="70" fill="{primary_color}"/>'
            body += f'<rect x="35" y="20" width="10" height="70" fill="{secondary_color}"/><rect x="55" y="20" width="10" height="70" fill="{secondary_color}"/>'
            sleeves = f'<path d="M 5,25 L 25,20 L 25,45 L 12,48 Z" fill="{primary_color}"/><path d="M 95,25 L 75,20 L 75,45 L 88,48 Z" fill="{primary_color}"/>'
    else: # 어웨이
        body = f'<rect x="25" y="20" width="50" height="70" fill="{primary_color}"/>'
        sleeves = f'<path d="M 5,25 L 25,20 L 25,45 L 12,48 Z" fill="{primary_color}"/><path d="M 95,25 L 75,20 L 75,45 L 88,48 Z" fill="{primary_color}"/>'
        if pattern_type == "sash": # 대각선 선
            body += f'<polygon points="25,20 35,20 75,80 65,80" fill="{secondary_color}"/>'

    return f'''
    <svg viewBox="0 0 100 100" width="100%" height="160" xmlns="http://www.w3.org/2000/svg">
        <filter id="shadow" x="-10%" y="-10%" width="120%" height="120%">
            <feDropShadow dx="0" dy="4" stdDeviation="3" flood-opacity="0.4"/>
        </filter>
        <g filter="url(#shadow)">
            {sleeves}
            {body}
            <!-- 깃/목 라인 -->
            <path d="M 40,20 Q 50,28 60,20 Z" fill="#EDBB00" />
        </g>
    </svg>
    '''

# 데이터 정의
SEASONS_DATA = [
    {
        "season": "2024-25",
        "era": "현대 에라",
        "manager": "한지 플릭",
        "top_scorer": "로베르트 레반도프스키",
        "trophies": ["진행 중"],
        "home_pattern": "half",
        "home_p": "#004D98", "home_s": "#A50044",
        "away_pattern": "solid",
        "away_p": "#111111", "away_s": "#EDBB00",
        "desc": "클럽 창립 125주년 기념 시즌. 2008-09 시즌을 오마주한 50:50 반반 유니폼으로 돌아왔습니다."
    },
    {
        "season": "2019-20",
        "era": "현대 에라",
        "manager": "에르네스토 발베르데 / 키케 세티엔",
        "top_scorer": "리오넬 메시 (31골)",
        "trophies": ["무관"],
        "home_pattern": "checker",
        "home_p": "#004D98", "home_s": "#A50044",
        "away_pattern": "sash",
        "away_p": "#EDBB00", "away_s": "#004D98",
        "desc": "구단 역사상 최초로 크로아티아 국가대표팀 스타일의 체커보드(바둑판) 디자인을 도입한 혁신적인 유니폼입니다."
    },
    {
        "season": "2015-16",
        "era": "MSN 에라",
        "manager": "루이스 엔리케",
        "top_scorer": "루이스 수아레스 (59골)",
        "trophies": ["라리가", "코파 델 레이", "UEFA 슈퍼컵", "클럽 월드컵"],
        "home_pattern": "horizontal",
        "home_p": "#004D98", "home_s": "#A50044",
        "away_pattern": "solid",
        "away_p": "#EDBB00", "away_s": "#004D98",
        "desc": "축구단 역사상 처음으로 홈 유니폼에 가로 스트라이프(Horizontal Stripes)를 적용하여 큰 화제를 모았습니다."
    },
    {
        "season": "2014-15",
        "era": "MSN 에라",
        "manager": "루이스 엔리케",
        "top_scorer": "리오넬 메시 (58골)",
        "trophies": ["UEFA 챔피언스 리그 (트레블)", "라리가", "코파 델 레이"],
        "home_pattern": "vertical",
        "home_p": "#004D98", "home_s": "#A50044",
        "away_pattern": "solid",
        "away_p": "#E75480", "away_s": "#004D98",
        "desc": "메시, 수아레스, 네이마르(MSN) 라인의 첫 시즌이자 구단 역사상 두 번째 '트레블(3관왕)'을 달성한 전설적인 시즌."
    },
    {
        "season": "2008-09",
        "era": "펩 에라",
        "manager": "펩 과르디올라",
        "top_scorer": "리오넬 메시 (38골)",
        "trophies": ["UEFA 챔피언스 리그 (트레블)", "라리가", "코파 델 레이"],
        "home_pattern": "half",
        "home_p": "#004D98", "home_s": "#A50044",
        "away_pattern": "solid",
        "away_p": "#FEF200", "away_s": "#004D98",
        "desc": "펩 과르디올라 감독 부임 첫해 스페인 클럽 최초의 '트레블' 및 6관왕을 달성한 역사상 가장 위대한 시즌 중 하나."
    }
]

# Title Header
st.title("🔵🔴 FC Barcelona Season & Kit Archive")
st.caption("나무위키 FC 바르셀로나/유니폼 데이터를 기반으로 제작된 시즌별 프로필 및 유니폼 아카이브")

# 사이드바 필터링
st.sidebar.header("🔍 필터 및 검색")
selected_era = st.sidebar.selectbox("시대(Era) 선택", ["전체", "현대 에라", "MSN 에라", "펩 에라"])
search_query = st.sidebar.text_input("시즌 또는 선수/감독 검색", "")

# 데이터 필터링
filtered_seasons = SEASONS_DATA
if selected_era != "전체":
    filtered_seasons = [s for s in filtered_seasons if s["era"] == selected_era]

if search_query:
    filtered_seasons = [
        s for s in filtered_seasons 
        if search_query.lower() in s["season"].lower() 
        or search_query.lower() in s["manager"].lower() 
        or search_query.lower() in s["top_scorer"].lower()
    ]

st.write(f"총 **{len(filtered_seasons)}개**의 시즌 정보가 표시됩니다.")

# 시즌 메인 리스트 출력
for season in filtered_seasons:
    with st.container():
        st.markdown(f"### 📅 {season['season']} Season ({season['era']})")
        
        col1, col2, col3 = st.columns([1.5, 1.5, 3])
        
        with col1:
            st.markdown("<p style='text-align: center; color: #EDBB00; font-weight: bold;'>Home Kit</p>", unsafe_allow_html=True)
            svg_code = get_kit_svg(season["home_pattern"], "home", season["home_p"], season["home_s"])
            components.html(svg_code, height=170)
            
        with col2:
            st.markdown("<p style='text-align: center; color: #EDBB00; font-weight: bold;'>Away Kit</p>", unsafe_allow_html=True)
            svg_code_away = get_kit_svg(season["away_pattern"], "away", season["away_p"], season["away_s"])
            components.html(svg_code_away, height=170)
            
        with col3:
            st.markdown(f"**👔 감독:** {season['manager']}")
            st.markdown(f"**⚽ 최다 득점자:** {season['top_scorer']}")
            
            # 트로피 태그 렌더링
            trophy_html = "<div><b>🏆 획득 타이틀:</b><br>"
            for t in season["trophies"]:
                trophy_html += f'<span class="trophy-badge">{t}</span>'
            trophy_html += "</div>"
            st.markdown(trophy_html, unsafe_allow_html=True)
            
            st.info(season["desc"])
            
        st.divider()
