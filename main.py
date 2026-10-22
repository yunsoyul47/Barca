import streamlit as st
import streamlit.components.v1 as components
from barca_data import render_kit_svg, render_squad_pitch, SQUAD_DATA, SEASONS_DATA

# 페이지 기본 설정
st.set_page_config(
    page_title="FC 바르셀로나 역대 시즌 & 유니폼/스쿼드 아카이브",
    page_icon="🔵🔴",
    layout="wide"
)

# 커스텀 CSS (Blaugrana 테마)
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

st.title("🔵🔴 FC Barcelona Kit & Squad Archive")
st.caption("2001/02 시즌부터 현재까지의 역대 유니폼/프로필 및 주요 시대별 전술 스쿼드 보드")

# 메인 탭 분리
tab1, tab2 = st.tabs(["👕 시즌별 프로필 & 유니폼", "⚽ 시대별 대표 스쿼드 (피치 뷰)"])

# -------------------- TAB 1: 유니폼/프로필 --------------------
with tab1:
    st.sidebar.header("🔍 시즌 검색 및 필터")
    era_options = ["전체", "현대 에라", "MSN & post-MSN", "MSN 에라", "황금기 후반", "펩 에라", "레이카르트 에라", "암흑기 & 재건"]
    selected_era = st.sidebar.selectbox("시대별 보기", era_options)
    search_query = st.sidebar.text_input("시즌 / 감독 / 선수 검색", "")

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

    for season in filtered_seasons:
        with st.container():
            st.markdown(f"### 📅 {season['season']} 시즌 <span style='font-size:0.9rem; color:#888;'>({season['era']})</span>", unsafe_allow_html=True)
            col1, col2, col3 = st.columns([1.5, 1.5, 3])
            
            with col1:
                st.markdown("<div class='kit-label'>HOME KIT</div>", unsafe_allow_html=True)
                home_svg = render_kit_svg(season["h_pat"], "home", season["h_p"], season["h_s"], season["h_a"], season["h_c"])
                components.html(home_svg, height=230)
                
            with col2:
                st.markdown("<div class='kit-label'>AWAY KIT</div>", unsafe_allow_html=True)
                away_svg = render_kit_svg(season["a_pat"], "away", season["a_p"], season["a_s"], season["a_a"], season["a_c"])
                components.html(away_svg, height=230)
                
            with col3:
                st.markdown(f"**👔 감독:** {season['manager']}")
                st.markdown(f"**⚽ 시즌 최다 득점자:** {season['top_scorer']}")
                
                trophy_html = "<div><b>🏆 획득 타이틀:</b><br>"
                for t in season["trophies"]:
                    trophy_html += f'<span class="trophy-badge">{t}</span>'
                trophy_html += "</div>"
                st.markdown(trophy_html, unsafe_allow_html=True)
                st.info(season["desc"])
                
            st.divider()

# -------------------- TAB 2: 시대별 대표 스쿼드 --------------------
with tab2:
    st.subheader("📋 FC 바르셀로나 주요 시대별 베스트 11 라인업")
    
    squad_key = st.selectbox("확인할 에라(Era)를 선택하세요:", list(SQUAD_DATA.keys()))
    selected_squad = SQUAD_DATA[squad_key]
    
    col_pitch, col_info = st.columns([3, 2])
    
    with col_pitch:
        st.markdown(f"#### 🏟️ 포메이션: {selected_squad['formation']}")
        pitch_svg = render_squad_pitch(selected_squad["players"])
        components.html(pitch_svg, height=540)
        
    with col_info:
        st.markdown("#### 💡 에라 주요 특징 및 전술")
        st.success(selected_squad["desc"])
        
        st.markdown("#### 🏃‍♂️ 선발 명단 (Starting XI)")
        for p in selected_squad["players"]:
            st.markdown(f"- **`{p['pos']}`** : {p['name']}")
