# barca_data.py (유니폼 SVG 및 전 데이터 세트)

def render_kit_svg(pattern, kit_type="home", primary="#004D98", secondary="#A50044", accent="#EDBB00", collar_style="vneck"):
    stroke = "rgba(0,0,0,0.3)"
    
    if pattern == "half":
        pat_svg = f'<rect x="200" y="80" width="100" height="280" fill="{secondary}" clip-path="url(#body-clip)"/>'
    elif pattern == "horizontal":
        stripes = "".join([f'<rect x="100" y="{y}" width="200" height="24" fill="{secondary}"/>' for y in range(120, 360, 48)])
        pat_svg = f'<g clip-path="url(#body-clip)">{stripes}</g>'
    elif pattern == "checker":
        checkers = "".join([f'<rect x="{100 + c*25}" y="{80 + r*40}" width="25" height="40" fill="{secondary}"/>' for r in range(7) for c in range(4) if (r + c) % 2 == 1])
        pat_svg = f'<g clip-path="url(#body-clip)">{checkers}</g>'
    elif pattern == "vertical_thin":
        stripes = "".join([f'<rect x="{x}" y="80" width="12" height="280" fill="{secondary}"/>' for x in range(112, 288, 24)])
        pat_svg = f'<g clip-path="url(#body-clip)">{stripes}</g>'
    elif pattern == "vertical_wide":
        stripes = "".join([f'<rect x="{x}" y="80" width="33" height="280" fill="{secondary}"/>' for x in range(133, 267, 66)])
        pat_svg = f'<g clip-path="url(#body-clip)">{stripes}</g>'
    elif pattern == "sash":
        pat_svg = f'<polygon points="100,80 140,80 300,320 260,320" fill="{secondary}" clip-path="url(#body-clip)"/>'
    else:
        stripes = "".join([f'<rect x="{x}" y="80" width="20" height="280" fill="{secondary}"/>' for x in range(120, 280, 40)])
        pat_svg = f'<g clip-path="url(#body-clip)">{stripes}</g>'

    if collar_style == "polo":
        collar_svg = f'<path d="M 165,80 L 200,120 L 235,80 L 220,70 L 200,85 L 180,70 Z" fill="{accent}" /><polygon points="185,80 200,120 215,80" fill="#111" opacity="0.3"/>'
    elif collar_style == "round":
        collar_svg = f'<path d="M 170,80 Q 200,110 230,80" fill="none" stroke="{accent}" stroke-width="8"/>'
    else:
        collar_svg = f'<path d="M 170,80 L 200,115 L 230,80" fill="none" stroke="{accent}" stroke-width="7"/>'

    return (
        f'<svg viewBox="0 0 400 420" width="100%" height="220" xmlns="http://www.w3.org/2000/svg" style="filter: drop-shadow(0px 8px 12px rgba(0,0,0,0.6));">'
        f'<defs>'
        f'<linearGradient id="fabricGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#ffffff" stop-opacity="0.15"/><stop offset="50%" stop-color="#000000" stop-opacity="0.0"/><stop offset="100%" stop-color="#000000" stop-opacity="0.35"/></linearGradient>'
        f'<clipPath id="body-clip"><path d="M 130,80 L 170,80 Q 200,105 230,80 L 270,80 Q 285,130 295,190 L 280,350 L 120,350 L 105,190 Q 115,130 130,80 Z"/></clipPath>'
        f'<clipPath id="left-sleeve"><path d="M 130,80 L 105,190 L 50,165 L 85,70 Z"/></clipPath>'
        f'<clipPath id="right-sleeve"><path d="M 270,80 L 295,190 L 350,165 L 315,70 Z"/></clipPath>'
        f'</defs>'
        f'<path d="M 130,80 L 170,80 Q 200,105 230,80 L 270,80 Q 285,130 295,190 L 280,350 L 120,350 L 105,190 Q 115,130 130,80 Z" fill="{primary}"/>'
        f'{pat_svg}'
        f'<path d="M 130,80 L 105,190 L 50,165 L 85,70 Z" fill="{primary}"/>'
        f'<rect x="30" y="50" width="120" height="150" fill="{secondary}" clip-path="url(#left-sleeve)" opacity="0.4"/>'
        f'<path d="M 50,165 L 105,190" stroke="{accent}" stroke-width="6"/>'
        f'<path d="M 270,80 L 295,190 L 350,165 L 315,70 Z" fill="{primary}"/>'
        f'<rect x="250" y="50" width="120" height="150" fill="{secondary}" clip-path="url(#right-sleeve)" opacity="0.4"/>'
        f'<path d="M 350,165 L 295,190" stroke="{accent}" stroke-width="6"/>'
        f'<path d="M 130,80 L 170,80 Q 200,105 230,80 L 270,80 Q 285,130 295,190 L 280,350 L 120,350 L 105,190 Q 115,130 130,80 Z" fill="url(#fabricGrad)"/>'
        f'<path d="M 130,80 L 170,80 Q 200,105 230,80 L 270,80 Q 285,130 295,190 L 280,350 L 120,350 L 105,190 Q 115,130 130,80 Z" fill="none" stroke="{stroke}" stroke-width="2"/>'
        f'<path d="M 130,80 L 105,190" fill="none" stroke="{stroke}" stroke-width="2"/>'
        f'<path d="M 270,80 L 295,190" fill="none" stroke="{stroke}" stroke-width="2"/>'
        f'<g transform="translate(150, 130)"><path d="M -12,-15 L 12,-15 L 12,0 C 12,12 0,18 0,18 C 0,18 -12,12 -12,0 Z" fill="#EDBB00" stroke="#000" stroke-width="1.5"/><path d="M -9,-12 L 9,-12 L 9,-2 C 9,8 0,14 0,14 C 0,14 -9,8 -9,-2 Z" fill="#A50044"/><rect x="-4" y="-10" width="8" height="2" fill="#004D98"/><circle cx="0" cy="4" r="3" fill="#EDBB00"/></g>'
        f'<path d="M 235,125 Q 242,128 250,120 Q 244,131 233,128 Z" fill="{accent}"/>'
        f'{collar_svg}'
        f'</svg>'
    )

def render_squad_pitch(players):
    pitch_bg = (
        '<rect x="0" y="0" width="500" height="600" fill="#1b4d2e" rx="10"/>'
        '<rect x="15" y="15" width="470" height="570" fill="none" stroke="rgba(255,255,255,0.4)" stroke-width="2"/>'
        '<line x1="15" y1="300" x2="485" y2="300" stroke="rgba(255,255,255,0.4)" stroke-width="2"/>'
        '<circle cx="250" cy="300" r="60" fill="none" stroke="rgba(255,255,255,0.4)" stroke-width="2"/>'
        '<rect x="150" y="15" width="200" height="90" fill="none" stroke="rgba(255,255,255,0.4)" stroke-width="2"/>'
        '<rect x="150" y="495" width="200" height="90" fill="none" stroke="rgba(255,255,255,0.4)" stroke-width="2"/>'
    )
    
    player_nodes = ""
    for p in players:
        pos_bg = "#A50044" if p["pos"] in ["ST", "LW", "RW", "CF"] else "#004D98"
        if p["pos"] in ["CDM", "CM", "CAM"]:
            pos_bg = "#006699"
        elif p["pos"] == "GK":
            pos_bg = "#EDBB00"
            
        text_color = "#111" if p["pos"] == "GK" else "#FFF"

        player_nodes += (
            f'<g transform="translate({p["x"]}, {p["y"]})">'
            f'<circle cx="0" cy="0" r="18" fill="{pos_bg}" stroke="#EDBB00" stroke-width="2.5" />'
            f'<text x="0" y="-3" font-size="10" font-weight="bold" fill="{text_color}" text-anchor="middle">{p["pos"]}</text>'
            f'<rect x="-45" y="12" width="90" height="18" fill="rgba(15,20,30,0.85)" rx="4"/>'
            f'<text x="0" y="25" font-size="11" font-weight="bold" fill="#EDBB00" text-anchor="middle">{p["name"]}</text>'
            f'</g>'
        )

    return f'<svg viewBox="0 0 500 600" width="100%" height="520" xmlns="http://www.w3.org/2000/svg" style="filter: drop-shadow(0px 8px 12px rgba(0,0,0,0.7));">{pitch_bg}{player_nodes}</svg>'

SQUAD_DATA = {
    "2014-2017 MSN 에라 (루이스 엔리케)": {
        "formation": "4-3-3",
        "desc": "세계 축구 역사상 가장 파괴적인 공격 삼각편대 MSN(메시-수아레스-네이마르)과 부스케츠의 완벽한 CDM 스위핑이 빛난 트레블 스쿼드.",
        "players": [
            {"name": "M. 슈테겐", "pos": "GK", "x": 250, "y": 540},
            {"name": "D. 알베스", "pos": "RB", "x": 420, "y": 450},
            {"name": "G. 피케", "pos": "CB", "x": 320, "y": 460},
            {"name": "J. 마스체라노", "pos": "CB", "x": 180, "y": 460},
            {"name": "J. 알바", "pos": "LB", "x": 80, "y": 450},
            {"name": "S. 부스케츠", "pos": "CDM", "x": 250, "y": 370},
            {"name": "I. 라키티치", "pos": "CM", "x": 360, "y": 280},
            {"name": "A. 이니에스타", "pos": "CM", "x": 140, "y": 280},
            {"name": "L. 메시", "pos": "RW", "x": 400, "y": 120},
            {"name": "L. 수아레스", "pos": "ST", "x": 250, "y": 90},
            {"name": "네이마르 Jr", "pos": "LW", "x": 100, "y": 120}
        ]
    },
    "2008-2012 펩 에라 (티키타카 전성기)": {
        "formation": "4-3-3 (False 9)",
        "desc": "사비-이니에스타-부스케츠 최고 미드필더진과 펄스나인 메시를 앞세워 6관왕 및 2회 UCL 우승을 차지한 전설적인 팀.",
        "players": [
            {"name": "V. 발데스", "pos": "GK", "x": 250, "y": 540},
            {"name": "D. 알베스", "pos": "RB", "x": 420, "y": 440},
            {"name": "G. 피케", "pos": "CB", "x": 320, "y": 460},
            {"name": "C. 푸욜", "pos": "CB", "x": 180, "y": 460},
            {"name": "E. 아비달", "pos": "LB", "x": 80, "y": 440},
            {"name": "S. 부스케츠", "pos": "CDM", "x": 250, "y": 370},
            {"name": "사비 E.", "pos": "CM", "x": 350, "y": 270},
            {"name": "A. 이니에스타", "pos": "CM", "x": 150, "y": 270},
            {"name": "D. 비야", "pos": "LW", "x": 100, "y": 120},
            {"name": "L. 메시", "pos": "CF", "x": 250, "y": 120},
            {"name": "페드로 R.", "pos": "RW", "x": 400, "y": 120}
        ]
    },
    "2004-2006 레이카르트 에라 (외계인 호나우지뉴)": {
        "formation": "4-3-3",
        "desc": "호나우지뉴의 화려한 삼바 축구와 사뮈엘 에토의 결정력으로 14년 만에 유럽 정상(UCL)에 등수한 에라.",
        "players": [
            {"name": "V. 발데스", "pos": "GK", "x": 250, "y": 540},
            {"name": "J. 벨레티", "pos": "RB", "x": 410, "y": 450},
            {"name": "C. 푸욜", "pos": "CB", "x": 320, "y": 460},
            {"name": "R. 마르케스", "pos": "CB", "x": 180, "y": 460},
            {"name": "G. 브롱크호스트", "pos": "LB", "x": 90, "y": 450},
            {"name": "에드미우손", "pos": "CDM", "x": 250, "y": 370},
            {"name": "데쿠", "pos": "CM", "x": 350, "y": 280},
            {"name": "사비 E.", "pos": "CM", "x": 150, "y": 280},
            {"name": "L. 메시", "pos": "RW", "x": 400, "y": 120},
            {"name": "S. 에토", "pos": "ST", "x": 250, "y": 90},
            {"name": "호나우지뉴", "pos": "LW", "x": 100, "y": 120}
        ]
    },
    "2024-2025 현재 (한지 플릭 에라)": {
        "formation": "4-2-3-1",
        "desc": "라마시아의 초신성 라민 야말, 쿠바르시와 레반도프스키의 결정력이 유기적으로 결합된 차세대 압박 축구 라인업.",
        "players": [
            {"name": "M. 슈테겐", "pos": "GK", "x": 250, "y": 540},
            {"name": "J. 쿤데", "pos": "RB", "x": 420, "y": 450},
            {"name": "R. 아라우호", "pos": "CB", "x": 320, "y": 460},
            {"name": "P. 쿠바르시", "pos": "CB", "x": 180, "y": 460},
            {"name": "A. 발데", "pos": "LB", "x": 80, "y": 450},
            {"name": "M. 카사도", "pos": "CDM", "x": 320, "y": 360},
            {"name": "페드리", "pos": "CDM", "x": 180, "y": 360},
            {"name": "D. 올모", "pos": "CAM", "x": 250, "y": 240},
            {"name": "R. 야말", "pos": "RW", "x": 400, "y": 130},
            {"name": "R. 레반도프스키", "pos": "ST", "x": 250, "y": 90},
            {"name": "하피냐", "pos": "LW", "x": 100, "y": 130}
        ]
    }
}

SEASONS_DATA = [
    {"season": "2024/25", "era": "현대 에라", "manager": "한지 플릭", "top_scorer": "레반도프스키", "trophies": ["진행 중"], "h_pat": "half", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "vneck", "a_pat": "solid", "a_p": "#111111", "a_s": "#111111", "a_a": "#EDBB00", "a_c": "vneck", "desc": "창립 125주년 기념 2008-09 오마주 50:50 반반 유니폼."},
    {"season": "2023/24", "era": "현대 에라", "manager": "차비", "top_scorer": "레반도프스키 (26골)", "trophies": ["무관"], "h_pat": "vertical_wide", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "round", "a_pat": "solid", "a_p": "#FFFFFF", "a_s": "#FFFFFF", "a_a": "#004D98", "a_c": "round", "desc": "크루이프 시대 오마주 클래식 화이트 어웨이."},
    {"season": "2022/23", "era": "현대 에라", "manager": "차비", "top_scorer": "레반도프스키 (33골)", "trophies": ["라리가", "수페르코파"], "h_pat": "vertical_thin", "h_p": "#041E42", "h_s": "#A50044", "h_a": "#004D98", "h_c": "round", "a_pat": "solid", "a_p": "#E5C158", "a_s": "#E5C158", "a_a": "#004D98", "a_c": "round", "desc": "1992 올림픽 30주년 다크블루 3색 스트라이프."},
    {"season": "2021/22", "era": "현대 에라", "manager": "쿠만/차비", "top_scorer": "데파이 (13골)", "trophies": ["무관"], "h_pat": "vertical", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "round", "a_pat": "solid", "a_p": "#A2C3D2", "a_s": "#A2C3D2", "a_a": "#A50044", "a_c": "round", "desc": "메시 이적 후 첫 시즌 엠블럼 십자가 패턴 변형 유니폼."},
    {"season": "2020/21", "era": "현대 에라", "manager": "쿠만", "top_scorer": "메시 (38골)", "trophies": ["코파 델 레이"], "h_pat": "vertical", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "round", "a_pat": "solid", "a_p": "#111111", "a_s": "#111111", "a_a": "#EDBB00", "a_c": "vneck", "desc": "골드 라인을 추가한 오마주 세로 스트라이프 유니폼."},
    {"season": "2019/20", "era": "현대 에라", "manager": "발베르데/세티엔", "top_scorer": "메시 (31골)", "trophies": ["무관"], "h_pat": "checker", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "vneck", "a_pat": "sash", "a_p": "#EDBB00", "a_s": "#004D98", "a_a": "#A50044", "a_c": "vneck", "desc": "최초 체커보드(바둑판) 디자인 홈 키트."},
    {"season": "2018/19", "era": "MSN & post-MSN", "manager": "발베르데", "top_scorer": "메시 (51골)", "trophies": ["라리가", "수페르코파"], "h_pat": "vertical_thin", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "vneck", "a_pat": "solid", "a_p": "#E2F512", "a_s": "#E2F512", "a_a": "#004D98", "a_c": "round", "desc": "바르셀로나 10개 구 상징 10개 세로줄 유니폼."},
    {"season": "2017/18", "era": "MSN & post-MSN", "manager": "발베르데", "top_scorer": "메시 (45골)", "trophies": ["라리가", "코파 델 레이"], "h_pat": "vertical", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "round", "a_pat": "solid", "a_p": "#4B9CD3", "a_s": "#4B9CD3", "a_a": "#A50044", "a_c": "round", "desc": "페이드 스트라이프 디자인 유니폼."},
    {"season": "2016/17", "era": "MSN 에라", "manager": "엔리케", "top_scorer": "메시 (54골)", "trophies": ["코파 델 레이", "수페르코파"], "h_pat": "vertical", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "vneck", "a_pat": "solid", "a_p": "#4B2E83", "a_s": "#4B2E83", "a_a": "#E2F512", "a_c": "vneck", "desc": "1992 웸블리 UCL 우승 25주년 복귀 유니폼."},
    {"season": "2015/16", "era": "MSN 에라", "manager": "엔리케", "top_scorer": "수아레스 (59골)", "trophies": ["라리가", "코파 델 레이", "클럽월드컵"], "h_pat": "horizontal", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "vneck", "a_pat": "solid", "a_p": "#EDBB00", "a_s": "#EDBB00", "a_a": "#004D98", "a_c": "round", "desc": "최초 가로 스트라이프 홈 키트."},
    {"season": "2014/15", "era": "MSN 에라", "manager": "엔리케", "top_scorer": "메시 (58골)", "trophies": ["UCL (트레블)", "라리가", "코파 델 레이"], "h_pat": "vertical_wide", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "vneck", "a_pat": "solid", "a_p": "#E75480", "a_s": "#E75480", "a_a": "#004D98", "a_c": "round", "desc": "MSN 첫해 역사적인 두 번째 트레블 달성."},
    {"season": "2013/14", "era": "황금기 후반", "manager": "마르티노", "top_scorer": "메시 (41골)", "trophies": ["수페르코파"], "h_pat": "vertical", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "vneck", "a_pat": "vertical", "a_p": "#EDBB00", "a_s": "#A50044", "a_a": "#004D98", "a_c": "round", "desc": "카탈루냐 깃발(Senyera) 줄무늬 어웨이 도입."},
    {"season": "2012/13", "era": "황금기 후반", "manager": "비라노바", "top_scorer": "메시 (60골)", "trophies": ["라리가 (승점 100점)"], "h_pat": "sash", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "round", "a_pat": "solid", "a_p": "#EDBB00", "a_s": "#E75480", "a_a": "#004D98", "a_c": "round", "desc": "그래디언트 번짐 효과의 유니폼."},
    {"season": "2011/12", "era": "펩 에라", "manager": "과르디올라", "top_scorer": "메시 (73골)", "trophies": ["코파 델 레이", "클럽월드컵"], "h_pat": "vertical_thin", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "round", "a_pat": "solid", "a_p": "#111111", "a_s": "#111111", "a_a": "#FFFFFF", "a_c": "round", "desc": "메시 한 시즌 73골 불멸의 기록 달성 시즌."},
    {"season": "2010/11", "era": "펩 에라", "manager": "과르디올라", "top_scorer": "메시 (53골)", "trophies": ["UCL", "라리가", "수페르코파"], "h_pat": "vertical", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "round", "a_pat": "solid", "a_p": "#00A8B5", "a_s": "#00A8B5", "a_a": "#004D98", "a_c": "round", "desc": "웸블리 UCL 제패 전성기 정점 키트."},
    {"season": "2009/10", "era": "펩 에라", "manager": "과르디올라", "top_scorer": "메시 (47골)", "trophies": ["라리가", "클럽월드컵"], "h_pat": "vertical", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "vneck", "a_pat": "solid", "a_p": "#E75480", "a_s": "#E75480", "a_a": "#111111", "a_c": "round", "desc": "전무후무 6관왕 신화 완성 시즌."},
    {"season": "2008/09", "era": "펩 에라", "manager": "과르디올라", "top_scorer": "메시 (38골)", "trophies": ["UCL (트레블)", "라리가", "코파 델 레이"], "h_pat": "half", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "vneck", "a_pat": "solid", "a_p": "#FEF200", "a_s": "#FEF200", "a_a": "#004D98", "a_c": "round", "desc": "스페인 클럽 최초 트레블 달성 반반 유니폼."},
    {"season": "2007/08", "era": "레이카르트 에라", "manager": "레이카르트", "top_scorer": "앙리 (19골)", "trophies": ["무관"], "h_pat": "vertical_wide", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "round", "a_pat": "solid", "a_p": "#87CEEB", "a_s": "#87CEEB", "a_a": "#004D98", "a_c": "round", "desc": "캄 노우 개장 50주년 월계수 자수 키트."},
    {"season": "2006/07", "era": "레이카르트 에라", "manager": "레이카르트", "top_scorer": "호나우지뉴 (24골)", "trophies": ["수페르코파"], "h_pat": "vertical_wide", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "vneck", "a_pat": "solid", "a_p": "#E2F512", "a_s": "#E2F512", "a_a": "#004D98", "a_c": "round", "desc": "UNICEF 로고 최초 부착 시즌."},
    {"season": "2005/06", "era": "레이카르트 에라", "manager": "레이카르트", "top_scorer": "에토 (34골)", "trophies": ["UCL", "라리가", "수페르코파"], "h_pat": "vertical", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "vneck", "a_pat": "solid", "a_p": "#FEF200", "a_s": "#FEF200", "a_a": "#004D98", "a_c": "vneck", "desc": "14년 만의 UCL 우승 제패 시즌."},
    {"season": "2004/05", "era": "레이카르트 에라", "manager": "레이카르트", "top_scorer": "에토 (29골)", "trophies": ["라리가"], "h_pat": "vertical_wide", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "vneck", "a_pat": "solid", "a_p": "#00A8B5", "a_s": "#00A8B5", "a_a": "#004D98", "a_c": "vneck", "desc": "6년 무관 탈출 라리가 우승, 메시 데뷔골 시즌."},
    {"season": "2003/04", "era": "암흑기 & 재건", "manager": "레이카르트", "top_scorer": "호나우지뉴 (22골)", "trophies": ["무관"], "h_pat": "vertical", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "polo", "a_pat": "solid", "a_p": "#C0C0C0", "a_s": "#C0C0C0", "a_a": "#004D98", "a_c": "round", "desc": "라포르타 부임 및 호나우지뉴 영입 명가 재건 첫걸음."},
    {"season": "2002/03", "era": "암흑기 & 재건", "manager": "판 할 / 리프스", "top_scorer": "클라위버르트 (21골)", "trophies": ["무관"], "h_pat": "vertical_wide", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "polo", "a_pat": "solid", "a_p": "#004D98", "a_s": "#004D98", "a_a": "#EDBB00", "a_c": "round", "desc": "리그 침체기 속 UCL 11연승 기록."},
    {"season": "2001/02", "era": "암흑기 & 재건", "manager": "렉사치", "top_scorer": "히바우두 / 클라위버르트 (18골)", "trophies": ["무관"], "h_pat": "vertical_wide", "h_p": "#004D98", "h_s": "#A50044", "h_a": "#EDBB00", "h_c": "polo", "a_pat": "solid", "a_p": "#E75480", "a_s": "#E75480", "a_a": "#004D98", "a_c": "round", "desc": "짙은 인디고 블루와 정통 폴로 카라 유니폼."}
]
