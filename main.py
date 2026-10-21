
import streamlit as st

st.set_page_config(
    page_title="FC Barcelona Season Archive",
    page_icon="⚽",
    layout="wide"
)

SEASONS = [
    {
        "season": "2001/02",
        "era": "초기 2000년대",
        "coach": "Carles Rexach",
        "players": "Rivaldo, Xavi, Puyol",
        "achievement": "라리가 4위",
        "description": "리발도가 활약하고 사비와 푸욜이 성장하던 시기.",
        "colors": ["#004D98", "#A50044"]
    },
    {
        "season": "2002/03",
        "era": "초기 2000년대",
        "coach": "Louis van Gaal / Radomir Antić",
        "players": "Xavi, Puyol, Kluivert",
        "achievement": "라리가 6위",
        "description": "시즌 중 감독 교체를 겪으며 팀 재정비가 이루어졌다.",
        "colors": ["#A50044", "#004D98"]
    },
    {
        "season": "2003/04",
        "era": "초기 2000년대",
        "coach": "Frank Rijkaard",
        "players": "Ronaldinho, Xavi, Puyol",
        "achievement": "라리가 2위",
        "description": "호나우지뉴의 합류와 함께 팀이 다시 상승세를 보였다.",
        "colors": ["#004D98", "#A50044"]
    },
    {
        "season": "2004/05",
        "era": "호나우지뉴 시대",
        "coach": "Frank Rijkaard",
        "players": "Ronaldinho, Eto'o, Deco",
        "achievement": "라리가 우승",
        "description": "호나우지뉴를 중심으로 라리가 우승을 차지했다.",
        "colors": ["#004D98", "#A50044"]
    },
    {
        "season": "2005/06",
        "era": "호나우지뉴 시대",
        "coach": "Frank Rijkaard",
        "players": "Ronaldinho, Eto'o, Messi",
        "achievement": "라리가·챔피언스리그 우승",
        "description": "유럽 정상에 오르며 황금기를 이어 갔다.",
        "colors": ["#A50044", "#004D98"]
    },
    {
        "season": "2008/09",
        "era": "과르디올라 시대",
        "coach": "Pep Guardiola",
        "players": "Messi, Xavi, Iniesta",
        "achievement": "트레블 달성",
        "description": "라리가, 코파 델 레이, 챔피언스리그를 모두 우승했다.",
        "colors": ["#004D98", "#A50044"]
    },
    {
        "season": "2009/10",
        "era": "과르디올라 시대",
        "coach": "Pep Guardiola",
        "players": "Messi, Xavi, Iniesta",
        "achievement": "라리가 우승",
        "description": "패스 중심의 축구를 바탕으로 리그 정상에 올랐다.",
        "colors": ["#A50044", "#004D98"]
    },
    {
        "season": "2010/11",
        "era": "과르디올라 시대",
        "coach": "Pep Guardiola",
        "players": "Messi, Xavi, Iniesta",
        "achievement": "라리가·챔피언스리그 우승",
        "description": "맨체스터 유나이티드를 꺾고 챔피언스리그 우승을 차지했다.",
        "colors": ["#004D98", "#A50044"]
    },
    {
        "season": "2014/15",
        "era": "MSN 시대",
        "coach": "Luis Enrique",
        "players": "Messi, Suárez, Neymar",
        "achievement": "트레블 달성",
        "description": "MSN 공격진을 앞세워 세 개의 주요 대회를 우승했다.",
        "colors": ["#A50044", "#004D98"]
    },
    {
        "season": "2015/16",
        "era": "MSN 시대",
        "coach": "Luis Enrique",
        "players": "Messi, Suárez, Neymar",
        "achievement": "라리가·코파 델 레이 우승",
        "description": "강력한 공격력을 바탕으로 국내 대회 2관왕을 기록했다.",
        "colors": ["#004D98", "#A50044"]
    },
    {
        "season": "2018/19",
        "era": "메시 후기 시대",
        "coach": "Ernesto Valverde",
        "players": "Messi, Suárez, Piqué",
        "achievement": "라리가 우승",
        "description": "메시의 활약을 바탕으로 리그 우승을 차지했다.",
        "colors": ["#A50044", "#004D98"]
    },
    {
        "season": "2022/23",
        "era": "새로운 세대",
        "coach": "Xavi Hernández",
        "players": "Lewandowski, Pedri, Gavi",
        "achievement": "라리가 우승",
        "description": "수비력을 바탕으로 리그 우승을 되찾았다.",
        "colors": ["#004D98", "#A50044"]
    },
    {
        "season": "2023/24",
        "era": "새로운 세대",
        "coach": "Xavi Hernández",
        "players": "Lewandowski, Lamine Yamal, Pedri",
        "achievement": "라리가 2위",
        "description": "젊은 선수들이 성장하며 다음 세대를 준비했다.",
        "colors": ["#A50044", "#004D98"]
    },
    {
        "season": "2024/25",
        "era": "새로운 세대",
        "coach": "Hansi Flick",
        "players": "Lamine Yamal, Raphinha, Lewandowski",
        "achievement": "라리가·코파 델 레이·수페르코파 우승",
        "description": "공격적인 축구로 국내 주요 대회에서 성과를 거뒀다.",
        "colors": ["#004D98", "#A50044"]
    }
]

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #081426, #15102c);
    color: #f8fafc;
}
section[data-testid="stSidebar"] {
    background: #101a2e;
}
h1, h2, h3 { color: #ffffff; }
div[data-testid="stMetric"] {
    background: #111d33;
    padding: 16px;
    border-radius: 12px;
    border: 1px solid #334155;
}
</style>
""", unsafe_allow_html=True)

st.title("⚽ FC Barcelona")
st.subheader("Season Profiles · Kit History · Club Archive")
st.caption("2001/02–2024/25 시즌별 기록")

col1, col2, col3 = st.columns(3)
col1.metric("수록 시즌", len(SEASONS))
col2.metric("클럽 설립", "1899")
col3.metric("상징적인 컬러", "Blaugrana")

st.divider()

eras = ["전체"] + sorted(set(item["era"] for item in SEASONS))
selected_era = st.selectbox("시대별 필터", eras)
keyword = st.text_input(
    "시즌 검색",
    placeholder="시즌, 감독, 선수, 우승 기록 검색..."
)

filtered = []
for item in SEASONS:
    if selected_era != "전체" and item["era"] != selected_era:
        continue

    searchable = " ".join([
        item["season"],
        item["era"],
        item["coach"],
        item["players"],
        item["achievement"],
        item["description"]
    ]).casefold()

    if keyword.casefold() not in searchable:
        continue

    filtered.append(item)

st.write(f"검색 결과: **{len(filtered)}개 시즌**")

if not filtered:
    st.warning("검색 결과가 없습니다. 다른 검색어를 입력해 주세요.")
    st.stop()

season_names = [item["season"] for item in filtered]
selected_season = st.selectbox("시즌 선택", season_names)

data = next(
    item for item in filtered
    if item["season"] == selected_season
)

left, right = st.columns([1, 1.3], gap="large")

with left:
    st.markdown("### 👕 홈 유니폼 미리보기")

    color1, color2 = data["colors"]

    svg = f"""
    <svg xmlns="http://www.w3.org/2000/svg"
         viewBox="0 0 300 320" width="100%">
      <defs>
        <linearGradient id="shirtShade" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stop-color="#ffffff" stop-opacity=".20"/>
          <stop offset="100%" stop-color="#000000" stop-opacity=".20"/>
        </linearGradient>
        <clipPath id="shirtClip">
          <path d="M105 55 L75 70 L35 120 L65 145
                   L88 120 L88 270 L212 270 L212 120
                   L235 145 L265 120 L225 70 L195 55
                   Q150 90 105 55 Z"/>
        </clipPath>
      </defs>
      <ellipse cx="150" cy="286" rx="85" ry="13"
               fill="#000000" opacity=".25"/>
      <g clip-path="url(#shirtClip)">
        <rect x="30" y="50" width="240" height="225"
              fill="{color1}"/>
        <rect x="70" y="50" width="30" height="225"
              fill="{color2}"/>
        <rect x="130" y="50" width="30" height="225"
              fill="{color2}"/>
        <rect x="190" y="50" width="30" height="225"
              fill="{color2}"/>
        <rect x="30" y="50" width="240" height="225"
              fill="url(#shirtShade)"/>
      </g>
      <path d="M105 55 L75 70 L35 120 L65 145
               L88 120 L88 270 L212 270 L212 120
               L235 145 L265 120 L225 70 L195 55
               Q150 90 105 55 Z"
            fill="none" stroke="#dbeafe" stroke-opacity=".6"
            stroke-width="3"/>
      <path d="M105 55 Q150 95 195 55"
            fill="none" stroke="#e2e8f0" stroke-width="5"/>
      <text x="150" y="168" font-size="20" font-weight="900"
            text-anchor="middle" fill="#ffffff">BARÇA</text>
      <text x="150" y="192" font-size="11" font-weight="700"
            text-anchor="middle" fill="#ffffff">{data["season"]}</text>
    </svg>
    """

    st.markdown(
        f'<div style="background:#101a2d;border-radius:16px;'
        f'padding:12px;text-align:center">{svg}</div>',
        unsafe_allow_html=True
    )
    st.caption(
        "시대와 색상을 바탕으로 만든 참고용 유니폼 일러스트입니다. "
        "실제 공식 유니폼 사진은 아닙니다."
    )

with right:
    st.markdown(f"## {data['season']} 시즌")
    st.caption(data["era"])

    st.markdown("### 시즌 요약")
    st.write(data["description"])

    st.markdown("### 주요 기록")
    st.info(data["achievement"])

    st.markdown("### 감독")
    st.write(data["coach"])

    st.markdown("### 주요 선수")
    st.write(data["players"])

    st.markdown("### 유니폼 컬러")
    st.markdown(
        f'<span style="display:inline-block;width:24px;height:24px;'
        f'background:{color1};border-radius:5px;vertical-align:middle;'
        f'margin-right:8px;border:1px solid #ffffff55"></span>'
        f'<code>{color1}</code> &nbsp; '
        f'<span style="display:inline-block;width:24px;height:24px;'
        f'background:{color2};border-radius:5px;vertical-align:middle;'
        f'margin-right:8px;border:1px solid #ffffff55"></span>'
        f'<code>{color2}</code>',
        unsafe_allow_html=True
    )

st.divider()
st.markdown("### 📚 시즌 아카이브")

for item in filtered:
    with st.expander(f"{item['season']} · {item['achievement']}"):
        st.write(f"**시대:** {item['era']}")
        st.write(f"**감독:** {item['coach']}")
        st.write(f"**주요 선수:** {item['players']}")
        st.write(item["description"])

st.caption(
    "FC Barcelona 시즌 아카이브 · 기록은 주요 시즌 중심으로 구성한 예시입니다."
)
