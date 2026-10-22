<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FC Barcelona Season Profiles & Kits History (2001/02 - Present)</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800;900&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        blaugrana: {
                            blue: '#004D98',
                            red: '#A50044',
                            yellow: '#EDBB00',
                            darkBlue: '#002855',
                            dark: '#0B0F19'
                        }
                    },
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                    }
                }
            }
        }
    </script>
    <style>
        /* Custom Scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #0b0f19;
        }
        ::-webkit-scrollbar-thumb {
            background: #1e293b;
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #A50044;
        }
        
        .gold-glow {
            text-shadow: 0 0 12px rgba(237, 187, 0, 0.4);
        }
        .card-gradient {
            background: linear-gradient(135deg, rgba(0, 77, 152, 0.15) 0%, rgba(165, 0, 68, 0.15) 100%);
            backdrop-filter: blur(10px);
        }
    </style>
</head>
<body class="bg-[#0B0F19] text-gray-100 font-sans min-h-screen flex flex-col">

    <!-- Header Navigation -->
    <header class="sticky top-0 z-50 bg-[#0B0F19]/90 backdrop-blur-md border-b border-gray-800">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
            <!-- Logo / Brand Title -->
            <div class="flex items-center space-x-3 cursor-pointer" onclick="resetFilters()">
                <div class="w-11 h-11 rounded-full bg-gradient-to-tr from-blaugrana-blue via-blaugrana-red to-blaugrana-yellow flex items-center justify-center p-0.5 shadow-lg border border-blaugrana-yellow/50">
                    <div class="w-full h-full bg-[#0B0F19] rounded-full flex items-center justify-center text-blaugrana-yellow font-black text-lg">
                        FCB
                    </div>
                </div>
                <div>
                    <h1 class="text-xl font-black tracking-tight text-white flex items-center gap-2">
                        BARÇA <span class="text-blaugrana-yellow font-light text-sm hidden sm:inline">COMPLETE KIT & SEASON ARCHIVE</span>
                    </h1>
                    <p class="text-xs text-gray-400">FC 바르셀로나 2001/02 ~ 현재 전 시즌 프로필 & 고해상도 유니폼 일러스트</p>
                </div>
            </div>

            <!-- Search Bar -->
            <div class="relative w-48 sm:w-72">
                <input type="text" id="searchInput" oninput="handleSearch()" placeholder="시즌, 감독, 주요 선수 검색..." 
                    class="w-full bg-gray-900/90 border border-gray-700 rounded-full py-2 pl-9 pr-4 text-xs sm:text-sm text-gray-200 focus:outline-none focus:border-blaugrana-yellow transition-all shadow-inner">
                <i class="fa-solid fa-magnifying-glass absolute left-3 top-2.5 text-gray-400 text-xs sm:text-sm"></i>
            </div>
        </div>
    </header>

    <!-- Main Content Area -->
    <main class="flex-grow max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8 flex flex-col gap-8">

        <!-- Era Filter Tabs -->
        <section class="flex flex-col gap-3">
            <div class="text-xs uppercase font-semibold text-gray-400 tracking-wider flex items-center gap-2">
                <i class="fa-solid fa-filter text-blaugrana-yellow"></i> Era Filter (시대별 필터)
            </div>
            <div class="flex flex-wrap gap-2" id="eraButtons">
                <!-- JavaScript handles buttons -->
            </div>
        </section>

        <!-- Timeline Navigation Bar -->
        <section class="bg-gray-900/60 border border-gray-800 rounded-2xl p-4 sm:p-6 backdrop-blur-sm">
            <div class="flex justify-between items-center mb-4">
                <h2 class="text-sm font-bold text-gray-300 uppercase tracking-wider flex items-center gap-2">
                    <i class="fa-solid fa-clock-rotate-left text-blaugrana-yellow"></i> Season Timeline (2001/02 - 2024/25)
                </h2>
                <span id="seasonCount" class="text-xs font-medium text-blaugrana-yellow bg-blaugrana-yellow/10 px-3 py-1 rounded-full border border-blaugrana-yellow/30 shadow-sm">
                    -- Seasons Available
                </span>
            </div>
            
            <!-- Horizontal Scrollable Timeline Bar -->
            <div class="flex items-center gap-2.5 overflow-x-auto pb-3 pt-1 scrollbar-thin" id="timelineContainer">
                <!-- Timeline items generated by JS -->
            </div>
        </section>

        <!-- Selected Season Detail View -->
        <section id="seasonDetailContainer" class="w-full">
            <!-- Dynamic Content loaded here -->
        </section>

    </main>

    <!-- Footer -->
    <footer class="bg-gray-950 border-t border-gray-800 py-8 mt-auto">
        <div class="max-w-7xl mx-auto px-4 text-center text-xs text-gray-500 space-y-2">
            <p class="font-semibold text-gray-400">Visca el Barça i Visca Catalunya! 🔵🔴</p>
            <p>FC Barcelona Complete Season Archive & Detailed Kit Vector Visuals.</p>
            <p class="text-gray-600">All kit illustrations are rendered via SVG with dynamic realistic gradient textures and structural details.</p>
        </div>
    </footer>

    <!-- JavaScript Application Logic -->
    <script>
        // FC Barcelona Complete Seasons Database (2001/02 to 2024/25)
        const seasonsData = [
            {
                id: '2001-02',
                season: '2001-02',
                era: 'Early 2000s',
                manager: '카를레스 렉사치 (Carles Rexach)',
                topScorer: '히바우두 / 하비에르 사비올라 (각 18골)',
                trophies: ['무관 (라리가 4위, UCL 4강)'],
                keyPlayers: ['히바우두', '하비에르 사비올라', '파트릭 클라위버르트', '루이스 엔리케', '사비 에르난데스'],
                summary: '암흑기 속에서도 사비올라의 화려한 데뷔와 히바우두, 클라위버르트 공격진의 고군분투가 이어진 시즌. 챔피언스리그 4강 진출로 위안을 삼았습니다.',
                kitInfo: {
                    type: 'classic-vertical',
                    homeColors: { base: '#004D98', stripe: '#A50044', accent: '#EDBB00', collar: '#004D98' },
                    awayColors: { base: '#00A896', stripe: '#004D98', accent: '#A50044', collar: '#00A896' },
                    description: '골드 디테일이 가미된 딥 블루/가넷 세로 스트라이프 홈 킷과 상큼한 민트 블루 어웨이 킷.'
                }
            },
            {
                id: '2002-03',
                season: '2002-03',
                era: 'Early 2000s',
                manager: '루이스 판할 / 라도미르 안티치',
                topScorer: '파트릭 클라위버르트 (21골)',
                trophies: ['무관 (라리가 6위)'],
                keyPlayers: ['파트릭 클라위버르트', '하비에르 사비올라', '후안 로만 리켈메', '루이스 엔리케', '푸욜'],
                summary: '판할 감독의 재집권 실패와 극심한 부진을 겪었으나, 안티치 감독의 구원 투수 등판으로 리그 6위로 시즌을 마치며 유에파컵 티켓을 획득한 격동의 해.',
                kitInfo: {
                    type: 'classic-wide-stripes',
                    homeColors: { base: '#004D98', stripe: '#A50044', accent: '#EDBB00', collar: '#A50044' },
                    awayColors: { base: '#1A1A1A', stripe: '#004D98', accent: '#A50044', collar: '#1A1A1A' },
                    description: '선명하고 넓어진 블라우그라나 세로 스트라이프와 세련된 다크 그레이/골드 어웨이.'
                }
            },
            {
                id: '2003-04',
                season: '2003-04',
                era: 'Rijkaard Era',
                manager: '프랑크 레이카르트 (Frank Rijkaard)',
                topScorer: '호나우지뉴 (22골)',
                trophies: ['라리가 준우승'],
                keyPlayers: ['호나우지뉴', '에드가 다비즈', '하비에르 사비올라', '사비 에르난데스', '카를레스 푸욜'],
                summary: '후안 라포르타 회장 취임과 호나우지뉴의 영입으로 바르샤 부활의 신호탄을 쏜 시즌. 겨울 이적시장에 합류한 다비즈의 활약으로 리그 폭풍 후반기 연승을 기록했습니다.',
                kitInfo: {
                    type: 'classic-vertical',
                    homeColors: { base: '#004D98', stripe: '#A50044', accent: '#EDBB00', collar: '#004D98' },
                    awayColors: { base: '#C2D5A8', stripe: '#004D98', accent: '#A50044', collar: '#004D98' },
                    description: '전통적인 가넷과 블루 세로 줄무늬 & 밝은 골드-세이지 그린톤의 오리지널 어웨이.'
                }
            },
            {
                id: '2004-05',
                season: '2004-05',
                era: 'Rijkaard Era',
                manager: '프랑크 레이카르트 (Frank Rijkaard)',
                topScorer: '사뮈엘 에토 (29골)',
                trophies: ['라리가 우승 (6년 만의 우승)'],
                keyPlayers: ['호나우지뉴', '사뮈엘 에토', '데쿠', '줄리', '사비', '카를레스 푸욜'],
                summary: '사뮈엘 에토, 데쿠 등의 합류와 호나우지뉴의 압도적 삼바 축구로 6년 동안의 무관 사슬을 끊고 라리가 정상에 우뚝 선 위대한 재건 시즌.',
                kitInfo: {
                    type: 'classic-vertical',
                    homeColors: { base: '#004D98', stripe: '#A50044', accent: '#EDBB00', collar: '#A50044' },
                    awayColors: { base: '#D2E32C', stripe: '#004D98', accent: '#A50044', collar: '#004D98' },
                    description: '클래식 블라우그라나 패턴과 바르샤 역사상 첫 혁신적인 네온 형광 노랑 어웨이.'
                }
            },
            {
                id: '2005-06',
                season: '2005-06',
                era: 'Rijkaard Era',
                manager: '프랑크 레이카르트 (Frank Rijkaard)',
                topScorer: '사뮈엘 에토 (34골)',
                trophies: ['UEFA 챔피언스 리그 우승', '라리가 우승', '수페르코파 데 에스파냐'],
                keyPlayers: ['호나우지뉴', '사뮈엘 에토', '데쿠', '리오넬 메시', '빅토르 발데스'],
                summary: '파리 산티아고 베르나베우에서의 호나우지뉴 기립박수 신화와 아스날을 제치고 14년 만에 유럽 정상(더블)에 오른 레이카르트 바르샤의 최전성기.',
                kitInfo: {
                    type: 'classic-vertical',
                    homeColors: { base: '#004D98', stripe: '#A50044', accent: '#EDBB00', collar: '#004D98' },
                    awayColors: { base: '#EBF76A', stripe: '#004D98', accent: '#A50044', collar: '#004D98' },
                    description: '스페인과 유럽을 동시에 제패한 영광의 딥 블루/레드 홈 킷과 인기를 끈 형광 어웨이.'
                }
            },
            {
                id: '2006-07',
                season: '2006-07',
                era: 'Rijkaard Era',
                manager: '프랑크 레이카르트 (Frank Rijkaard)',
                topScorer: '호나우지뉴 (24골)',
                trophies: ['수페르코파 데 에스파냐', 'UEFA 슈퍼컵 준우승'],
                keyPlayers: ['호나우지뉴', '리오넬 메시', '사뮈엘 에토', '데쿠', '이안니스 구드요한센'],
                summary: '유니세프(UNICEF) 로고가 사상 처음 유니폼 전면에 새겨진 뜻깊은 시즌. 메시의 엘 클라시코 해트트릭 등 명장면을 남겼으나 아쉽게 리그 타이틀을 놓쳤습니다.',
                kitInfo: {
                    type: 'asymmetric-vertical',
                    homeColors: { base: '#004D98', stripe: '#A50044', accent: '#EDBB00', collar: '#004D98' },
                    awayColors: { base: '#E25C1D', stripe: '#004D98', accent: '#A50044', collar: '#E25C1D' },
                    description: '최초의 유니세프 스폰서 탑재 및 선명한 비비드 오렌지 어웨이 킷.'
                }
            },
            {
                id: '2007-08',
                season: '2007-08',
                era: 'Rijkaard Era',
                manager: '프랑크 레이카르트 (Frank Rijkaard)',
                topScorer: '티에리 앙리 (19골)',
                trophies: ['무관 (라리가 3위, UCL 4강)'],
                keyPlayers: ['리오넬 메시', '티에리 앙리', '호나우지뉴', '사뮈엘 에토', '사비', '이니에스타'],
                summary: '판타스틱 4(메시, 앙리, 에토, 호나우지뉴)의 결성으로 큰 기대를 모았으나 팀 조직력 흔들림으로 무관에 그치며 펩 과르디올라 시대의 개막을 준비한 과도기.',
                kitInfo: {
                    type: 'classic-thin-stripes',
                    homeColors: { base: '#004D98', stripe: '#A50044', accent: '#EDBB00', collar: '#EDBB00', campNou50: true },
                    awayColors: { base: '#8CAEC3', stripe: '#004D98', accent: '#A50044', collar: '#004D98' },
                    description: '캄 노우 50주년 패치 자수 및 클래식 가넷-블루 스트라이프 & 스카이 블루 어웨이.'
                }
            },
            {
                id: '2008-09',
                season: '2008-09',
                era: 'Pep Era',
                manager: '펩 과르디올라 (Pep Guardiola)',
                topScorer: '리오넬 메시 (38골)',
                trophies: ['스페인 클럽 최초 트레블 (라리가, 코파 델 레이, UCL)', '수페르코파, UEFA 슈퍼컵, 클럽 월드컵 (전무후무 6관왕)'],
                keyPlayers: ['리오넬 메시', '사비 에르난데스', '안드레스 이니에스타', '사뮈엘 에토', '카를레스 푸욜', '앙리'],
                summary: '축구 역사상 가장 완벽한 팀. 펩과 메시의 티키타카로 전 세계를 사로잡으며 스페인 최초 트레블과 역사상 유일한 단일 연도 6관왕 달성.',
                kitInfo: {
                    type: 'half-and-half',
                    homeColors: { left: '#A50044', right: '#004D98', accent: '#EDBB00', collar: '#004D98' },
                    awayColors: { base: '#FF9E1B', stripe: '#004D98', accent: '#A50044', collar: '#004D98' },
                    description: '좌우 50:50 반반(Half-and-Half) 배치의 레전드 홈 유니폼과 강렬한 샛노란/오렌지 어웨이.'
                }
            },
            {
                id: '2009-10',
                season: '2009-10',
                era: 'Pep Era',
                manager: '펩 과르디올라 (Pep Guardiola)',
                topScorer: '리오넬 메시 (47골)',
                trophies: ['라리가 우승 (승점 99점)', '수페르코파', 'UEFA 슈퍼컵', 'FIFA 클럽 월드컵'],
                keyPlayers: ['리오넬 메시', '즐라탄 이브라히모비치', '사비', '이니에스타', '페드로', '피케'],
                summary: '메시의 첫 발롱도르 수상과 함께 라리가 승점 99점 신기록 우승. 산티아고 베르나베우 원정 승리 등 막강한 지배력을 유지한 시즌.',
                kitInfo: {
                    type: 'classic-clean-stripes',
                    homeColors: { base: '#004D98', stripe: '#A50044', accent: '#EDBB00', collar: '#EDBB00' },
                    awayColors: { base: '#E05A17', stripe: '#004D98', accent: '#A50044', collar: '#E05A17' },
                    description: '노란 넥 테두리 포인트가 깔끔한 세로 스트라이프 및 매력적인망고 오렌지 어웨이.'
                }
            },
            {
                id: '2010-11',
                season: '2010-11',
                era: 'Pep Era',
                manager: '펩 과르디올라 (Pep Guardiola)',
                topScorer: '리오넬 메시 (53골)',
                trophies: ['UEFA 챔피언스 리그 우승', '라리가 우승', '수페르코파 데 에스파냐'],
                keyPlayers: ['리오넬 메시', '사비', '이니에스타', '다비드 비야', '페드로', '제라르 피케'],
                summary: '웸블리 챔피언스리그 결승에서 맨유를 3-1로 압도하며 완성된 펩 바르샤 축구학의 결정체이자 정점.',
                kitInfo: {
                    type: 'yellow-collar-stripes',
                    homeColors: { base: '#004D98', stripe: '#A50044', accent: '#EDBB00', collar: '#EDBB00', yellowSleeves: true },
                    awayColors: { base: '#3AAFA9', stripe: '#004D98', accent: '#A50044', collar: '#3AAFA9' },
                    description: '선명한 노란색 넥 칼라와 소매 시보리가 매력적인 정통 스트라이프 & 민트 티얼 어웨이.'
                }
            },
            {
                id: '2011-12',
                season: '2011-12',
                era: 'Pep Era',
                manager: '펩 과르디올라 (Pep Guardiola)',
                topScorer: '리오넬 메시 (73골 - 신기록)',
                trophies: ['코파 델 레이', '수페르코파', 'UEFA 슈퍼컵', 'FIFA 클럽 월드컵 (4관왕)'],
                keyPlayers: ['리오넬 메시', '세스크 파브레가스', '사비', '이니에스타', '알렉시스 산체스'],
                summary: '메시가 한 시즌 73골이라는 신의 영역에 달성한 해. 펩 과르디올라 감독과의 작별을 고하며 아름다운 마침표를 찍었습니다.',
                kitInfo: {
                    type: 'gradient-multi-stripes',
                    homeColors: { base: '#004D98', stripe: '#A50044', accent: '#EDBB00', collar: '#004D98' },
                    awayColors: { base: '#1C1C1C', stripe: '#EDBB00', accent: '#EDBB00', collar: '#1C1C1C' },
                    description: '중앙으로 모여드는 파격적인 얇은 그래디언트 스트라이프 및 스텔스 올 블랙 어웨이.'
                }
            },
            {
                id: '2012-13',
                season: '2012-13',
                era: 'Tito Era',
                manager: '티토 비라노바 (Tito Vilanova)',
                topScorer: '리오넬 메시 (60골)',
                trophies: ['라리가 우승 (승점 100점 달성)'],
                keyPlayers: ['리오넬 메시', '사비', '이니에스타', '세스크 파브레가스', '페드로', '부스케츠'],
                summary: '고(故) 티토 비라노바 감독의 지휘 아래 라리가 역사상 최고 타이기록인 승점 100점으로 압도적 우승을 일궈낸 감동의 시즌.',
                kitInfo: {
                    type: 'fade-gradient',
                    homeColors: { base: '#004D98', stripe: '#A50044', accent: '#EDBB00', collar: '#004D98' },
                    awayColors: { base: '#F7941D', stripe: '#A50044', accent: '#EDBB00', collar: '#F7941D' },
                    description: '경계선이 부드럽게 번지는 번짐 그라데이션 블라우그라나 & 오렌지-옐로우 그래디언트.'
                }
            },
            {
                id: '2013-14',
                season: '2013-14',
                era: 'Transition Era',
                manager: '헤라르도 타타 마르티노 (Gerardo Martino)',
                topScorer: '리오넬 메시 (41골)',
                trophies: ['수페르코파 데 에스파냐'],
                keyPlayers: ['네이마르 Jr', '리오넬 메시', '알렉시스 산체스', '사비', '이니에스타'],
                summary: '브라질 신성 네이마르의 합류. 무관의 위기 속 수페르코파 우승을 거두었으나 리그 마지막 경기 결승골 취소로 아쉬운 준우승을 거둔 해.',
                kitInfo: {
                    type: 'classic-clean-yellow-v',
                    homeColors: { base: '#004D98', stripe: '#A50044', accent: '#EDBB00', collar: '#EDBB00' },
                    awayColors: { base: '#EDBB00', stripe: '#A50044', accent: '#004D98', collar: '#EDBB00', senyera: true },
                    description: '노란 V넥 깃이 적용된 깔끔한 홈 킷과 카탈루냐 깃발(Senyera) 노랑-레드 어웨이.'
                }
            },
            {
                id: '2014-15',
                season: '2014-15',
                era: 'MSN Era',
                manager: '루이스 엔리케 (Luis Enrique)',
                topScorer: '리오넬 메시 (58골)',
                trophies: ['구단 역사상 두 번째 트레블 (라리가, 코파 델 레이, UCL)'],
                keyPlayers: ['리오넬 메시', '루이스 수아레스', '네이마르 Jr', '이반 라키티치', '마스체라노'],
                summary: '메시-수아레스-네이마르(MSN) 삼각 편대가 122골을 합작하며 축구 역사상 최초로 2회 트레블을 달성한 경이로운 전설의 시즌.',
                kitInfo: {
                    type: 'bold-vertical-vneck',
                    homeColors: { base: '#004D98', stripe: '#A50044', accent: '#EDBB00', collar: '#004D98', senyeraV: true },
                    awayColors: { base: '#E25B26', stripe: '#004D98', accent: '#A50044', collar: '#E25B26' },
                    description: '굵직한 세로 스트라이프와 목 카라 부분의 센에라 V자 디테일 & 크림슨 오렌지 어웨이.'
                }
            },
            {
                id: '2015-16',
                season: '2015-16',
                era: 'MSN Era',
                manager: '루이스 엔리케 (Luis Enrique)',
                topScorer: '루이스 수아레스 (59골 - 피치치)',
                trophies: ['라리가 우승', '코파 델 레이', 'UEFA 슈퍼컵', 'FIFA 클럽 월드컵 (4관왕)'],
                keyPlayers: ['루이스 수아레스', '리오넬 메시', '네이마르 Jr', '이니에스타', '세르지 로베르토'],
                summary: '구단 역사상 최초로 "가로 스트라이프" 디자인을 채택했던 파격의 해. 수아레스가 59골을 올리며 유러피언 골든슈를 차지했습니다.',
                kitInfo: {
                    type: 'horizontal-stripes',
                    homeColors: { base: '#004D98', stripe: '#A50044', accent: '#EDBB00', collar: '#EDBB00' },
                    awayColors: { base: '#EDBB00', stripe: '#A50044', accent: '#004D98', collar: '#EDBB00', senyeraBack: true },
                    description: '창단 이래 최초의 가로 방향 농구 킷 감성 스트라이프 & 뒷면 센에라 줄무늬 어웨이.'
                }
            },
            {
                id: '2016-17',
                season: '2016-17',
                era: 'MSN Era',
                manager: '루이스 엔리케 (Luis Enrique)',
                topScorer: '리오넬 메시 (54골)',
                trophies: ['코파 델 레이 우승', '수페르코파 데 에스파냐'],
                keyPlayers: ['리오넬 메시', '루이스 수아레스', '네이마르 Jr', '이반 라키티치', '부스케츠'],
                summary: '챔피언스리그 16강 파리 생제르맹전 6-1 기적의 역전승(Remontada)을 만들어낸 연출과 메시의 베르나베우 유니폼 세레머니의 해.',
                kitInfo: {
                    type: 'classic-retro-vertical',
                    homeColors: { base: '#004D98', stripe: '#A50044', accent: '#EDBB00', collar: '#004D98' },
                    awayColors: { base: '#5D3A9B', stripe: '#E25B26', accent: '#EDBB00', collar: '#5D3A9B' },
                    description: '1992년 첫 유러피언컵 우승 25주년 기념 레트로 세로 패턴 및 스포티 퍼플 어웨이.'
                }
            },
            {
                id: '2017-18',
                season: '2017-18',
                era: 'Valverde Era',
                manager: '에르네스토 발베르데 (Ernesto Valverde)',
                topScorer: '리오넬 메시 (45골)',
                trophies: ['라리가 우승 (무패 육박 우승)', '코파 델 레이 우승 (더블)'],
                keyPlayers: ['리오넬 메시', '루이스 수아레스', '파울리뉴', '필리피 코우치뉴', '테어슈테겐'],
                summary: '발베르데 감독의 실용주의 축구 아래 리그 36경기 무패 행진을 달리며 압도적인 국내 대회 더블(Double)을 달성한 시즌.',
                kitInfo: {
                    type: 'asymmetric-fading-stripes',
                    homeColors: { base: '#004D98', stripe: '#A50044', accent: '#EDBB00', collar: '#004D98' },
                    awayColors: { base: '#70C1B3', stripe: '#004D98', accent: '#A50044', collar: '#70C1B3' },
                    description: '중앙으로 갈수록 두꺼워지는 변형 세로 스트라이프와 매력적인 스카이 민트 어웨이.'
                }
            },
            {
                id: '2018-19',
                season: '2018-19',
                era: 'Valverde Era',
                manager: '에르네스토 발베르데 (Ernesto Valverde)',
                topScorer: '리오넬 메시 (51골)',
                trophies: ['라리가 우승', '수페르코파 데 에스파냐'],
                keyPlayers: ['리오넬 메시', '루이스 수아레스', '우스만 뎀벨레', '이반 라키티치', '피케'],
                summary: '캡틴 리오넬 메시의 독주로 라리가 2연패를 달성하였으나 챔피언스리그 안필드 비극으로 아쉬움을 삼켰던 해.',
                kitInfo: {
                    type: 'ten-stripes',
                    homeColors: { base: '#004D98', stripe: '#A50044', accent: '#EDBB00', collar: '#004D98' },
                    awayColors: { base: '#EDBB00', stripe: '#004D98', accent: '#A50044', collar: '#EDBB00' },
                    description: '바르셀로나 10개 구역을 상징하는 10개의 얇은 세로 스트라이프 & 형광 옐로우 어웨이.'
                }
            },
            {
                id: '2019-20',
                season: '2019-20',
                era: 'Transition Era',
                manager: '에르네스토 발베르데 / 키케 세티엔',
                topScorer: '리오넬 메시 (31골)',
                trophies: ['무관 (라리가 2위)'],
                keyPlayers: ['리오넬 메시', '앙투안 그리즈만', '프렝키 더용', '테어슈테겐', '아르투르'],
                summary: '크로아티아 체커보드 패턴을 도입한 파격적 유니폼 디자인. 코로나19 중단 및 감독 교체 등 혼란 속 무관으로 마감한 과도기.',
                kitInfo: {
                    type: 'checkerboard',
                    homeColors: { base: '#004D98', stripe: '#A50044', accent: '#EDBB00', collar: '#004D98' },
                    awayColors: { base: '#F4E8C1', stripe: '#004D98', accent: '#A50044', collar: '#F4E8C1', sash: true },
                    description: '전통을 깬 최초의 바둑판 체커보드 디자인 & 라마시아 40주년 노랑 사선(Sash) 어웨이.'
                }
            },
            {
                id: '2020-21',
                season: '2020-21',
                era: 'Koeman Era',
                manager: '로날트 쿠만 (Ronald Koeman)',
                topScorer: '리오넬 메시 (38골)',
                trophies: ['코파 델 레이 우승'],
                keyPlayers: ['리오넬 메시', '페드리', '프렝키 더용', '우스만 뎀벨레', '안수 파티'],
                summary: '페드리 등 신예들의 등장과 메시의 바르샤 공식 마지막 우승(코파 델 레이) 및 메시 시대의 감동적인 마침표.',
                kitInfo: {
                    type: 'gold-accent-stripes',
                    homeColors: { base: '#004D98', stripe: '#A50044', accent: '#EDBB00', collar: '#EDBB00' },
                    awayColors: { base: '#111111', stripe: '#EDBB00', accent: '#EDBB00', collar: '#111111' },
                    description: '줄무늬 사이에 클래식 골드 라인이 삽입된 명작 & 고급스러운 올블랙-메탈릭 골드 어웨이.'
                }
            },
            {
                id: '2021-22',
                season: '2021-22',
                era: 'Xavi Era',
                manager: '로날트 쿠만 / 사비 에르난데스',
                topScorer: '멤피스 데파이 / 피에르에메릭 오바메양 (각 13골)',
                trophies: ['무관 (라리가 2위 재도약)'],
                keyPlayers: ['페드리', '가비', '부스케츠', '오바메양', '멤피스 데파이', '아라우호'],
                summary: '메시의 이적 이후 사비 감독이 친정팀 구원투수로 복귀. 산티아고 베르나베우 4-0 대승 등을 이끌며 재건의 발판을 다진 시즌.',
                kitInfo: {
                    type: 'crest-inspired-stripes',
                    homeColors: { base: '#004D98', stripe: '#A50044', accent: '#EDBB00', collar: '#004D98' },
                    awayColors: { base: '#E3DBF2', stripe: '#A50044', accent: '#004D98', collar: '#E3DBF2' },
                    description: '클럽 엠블럼 형태를 유니폼 전면 그래픽으로 구현한 디자인 & 연보라 퍼플 어웨이.'
                }
            },
            {
                id: '2022-23',
                season: '2022-23',
                era: 'Xavi Era',
                manager: '사비 에르난데스 (Xavi Hernández)',
                topScorer: '로베르트 레반도프스키 (33골 - 피치치)',
                trophies: ['라리가 우승', '수페르코파 데 에스파냐'],
                keyPlayers: ['로베르트 레반도프스키', '페드리', '가비', '로날드 아라우호', '테어슈테겐'],
                summary: '레반도프스키의 폭발적 득점과 철벽 수비진(MATS, 아라우호, 쿤데 등)의 최저 실점 신화로 4년 만에 라리가 정상에 복귀한 왕의 귀환.',
                kitInfo: {
                    type: 'three-color-stripes',
                    homeColors: { base: '#041E42', stripe1: '#004D98', stripe2: '#A50044', accent: '#EDBB00', collar: '#041E42' },
                    awayColors: { base: '#D4AF37', stripe: '#004D98', accent: '#A50044', collar: '#D4AF37' },
                    description: '다크 네이비, 로열 블루, 가넷 레드가 결합된 3톤 세로 줄무늬 & 올림픽 올드 골드 어웨이.'
                }
            },
            {
                id: '2023-24',
                season: '2023-24',
                era: 'Xavi Era',
                manager: '사비 에르난데스 (Xavi Hernández)',
                topScorer: '로베르트 레반도프스키 (26골)',
                trophies: ['라리가 준우승', 'UCL 8강'],
                keyPlayers: ['라민 야말', '일카이 귄도안', '로베르트 레반도프스키', '파우 쿠바르시', '페르민'],
                summary: '16세 차오르는 신성 라민 야말과 파우 쿠바르시 등 라마시아 유스들의 찬란한 등장으로 클럽의 밝은 미래를 증명한 시즌.',
                kitInfo: {
                    type: 'classic-bold-diamond',
                    homeColors: { base: '#004D98', stripe: '#A50044', accent: '#EDBB00', collar: '#004D98' },
                    awayColors: { base: '#FFFFFF', stripe: '#004D98', accent: '#A50044', collar: '#FFFFFF' },
                    description: '여성팀 최초 엠블럼 속 다이아몬드 패턴 오마주 홈 킷과 요한 크루이프 시대 레트로 화이트 어웨이.'
                }
            },
            {
                id: '2024-25',
                season: '2024-25',
                era: 'Modern Era',
                manager: '한지 플릭 (Hansi Flick)',
                topScorer: '진행 중 (로베르트 레반도프스키 / 라민 야말 / 하피냐)',
                trophies: ['진행 중'],
                keyPlayers: ['라민 야말', '로베르트 레반도프스키', '하피냐', '페드리', '다니 올모', '쿠바르시'],
                summary: 'FC 바르셀로나 창단 125주년! 한지 플릭 감독의 강렬한 전방 압박과 화력 축구로 스페인과 유럽에서 대대적인 부활을 선언한 시즌.',
                kitInfo: {
                    type: 'half-and-half-125th',
                    homeColors: { left: '#A50044', right: '#004D98', accent: '#EDBB00', collar: '#004D98', centeredCrest: true },
                    awayColors: { base: '#111113', stripe: '#A50044', accent: '#004D98', collar: '#111113' },
                    description: '창단 125주년을 맞아 중앙 엠블럼과 1899-1999 100주년 반반 유산을 계승한 클래식 홈 킷.'
                }
            }
        ];

        // State Management
        let selectedEra = 'All';
        let selectedSeasonId = '2008-09';
        let searchQuery = '';

        const eras = ['All', 'Early 2000s', 'Rijkaard Era', 'Pep Era', 'Tito Era', 'MSN Era', 'Valverde Era', 'Transition Era', 'Koeman Era', 'Xavi Era', 'Modern Era'];

        // DOM Initialization
        window.addEventListener('DOMContentLoaded', () => {
            renderEraButtons();
            renderTimeline();
            renderSeasonDetail(selectedSeasonId);
        });

        // Render Era Filter Buttons
        function renderEraButtons() {
            const container = document.getElementById('eraButtons');
            container.innerHTML = eras.map(era => {
                const isActive = era === selectedEra;
                return `
                    <button onclick="filterByEra('${era}')" 
                        class="px-3 py-1.5 rounded-xl text-xs font-semibold transition-all duration-200 border ${
                            isActive 
                            ? 'bg-gradient-to-r from-blaugrana-blue to-blaugrana-red text-white border-blaugrana-yellow/60 shadow-md scale-105' 
                            : 'bg-gray-900/80 text-gray-400 border-gray-800 hover:border-gray-700 hover:text-gray-200'
                        }">
                        ${era}
                    </button>
                `;
            }).join('');
        }

        // Filter Functionality
        function filterByEra(era) {
            selectedEra = era;
            renderEraButtons();
            renderTimeline();
            
            const visibleSeasons = getFilteredSeasons();
            if (visibleSeasons.length > 0) {
                const exists = visibleSeasons.some(s => s.id === selectedSeasonId);
                if (!exists) {
                    selectSeason(visibleSeasons[0].id);
                }
            }
        }

        function handleSearch() {
            searchQuery = document.getElementById('searchInput').value.toLowerCase().trim();
            renderTimeline();
            const visible = getFilteredSeasons();
            if (visible.length > 0 && !visible.some(s => s.id === selectedSeasonId)) {
                selectSeason(visible[0].id);
            }
        }

        function resetFilters() {
            selectedEra = 'All';
            searchQuery = '';
            document.getElementById('searchInput').value = '';
            renderEraButtons();
            renderTimeline();
            selectSeason('2008-09');
        }

        function getFilteredSeasons() {
            return seasonsData.filter(s => {
                const matchesEra = selectedEra === 'All' || s.era === selectedEra;
                const matchesSearch = searchQuery === '' || 
                    s.season.toLowerCase().includes(searchQuery) ||
                    s.manager.toLowerCase().includes(searchQuery) ||
                    s.keyPlayers.some(p => p.toLowerCase().includes(searchQuery)) ||
                    s.trophies.some(t => t.toLowerCase().includes(searchQuery));
                return matchesEra && matchesSearch;
            });
        }

        // Render Timeline
        function renderTimeline() {
            const container = document.getElementById('timelineContainer');
            const filtered = getFilteredSeasons();
            
            document.getElementById('seasonCount').innerText = `${filtered.length} Seasons`;

            if (filtered.length === 0) {
                container.innerHTML = `<div class="text-xs text-gray-500 py-3 w-full text-center">검색 조건에 일치하는 시즌이 없습니다.</div>`;
                return;
            }

            container.innerHTML = filtered.map(s => {
                const isSelected = s.id === selectedSeasonId;
                const hasTreble = s.trophies.some(t => t.includes('트레블'));
                
                return `
                    <button onclick="selectSeason('${s.id}')" 
                        class="flex-shrink-0 px-3.5 py-2 rounded-xl transition-all duration-200 border flex flex-col items-center gap-1 ${
                            isSelected 
                            ? 'bg-gradient-to-b from-blaugrana-blue to-blaugrana-red text-white border-blaugrana-yellow shadow-lg shadow-blaugrana-blue/30 scale-105' 
                            : 'bg-gray-900/90 border-gray-800 text-gray-400 hover:border-gray-700 hover:text-gray-200'
                        }">
                        <span class="text-xs font-black tracking-wider ${isSelected ? 'text-blaugrana-yellow' : ''}">
                            ${s.season}
                        </span>
                        <div class="flex items-center gap-1">
                            ${hasTreble ? '<span class="text-[9px] bg-yellow-500/20 text-yellow-300 font-bold px-1 py-0.5 rounded border border-yellow-500/40">🏆 TREBLE</span>' : ''}
                            <span class="text-[9px] opacity-75">${s.era}</span>
                        </div>
                    </button>
                `;
            }).join('');
        }

        function selectSeason(id) {
            selectedSeasonId = id;
            renderTimeline();
            renderSeasonDetail(id);
        }

        // High Quality Realistic Vector Kit Illustration Generator
        function generateHighQualityKitSVG(kitInfo, isAway = false) {
            const colors = isAway ? kitInfo.awayColors : kitInfo.homeColors;
            const type = isAway ? 'away-style' : kitInfo.type;

            let bodyPattern = '';

            // Render Patterns with dynamic graphics
            if (!isAway) {
                if (type === 'half-and-half' || type === 'half-and-half-125th') {
                    bodyPattern = `
                        <rect x="25" y="25" width="25" height="85" fill="${colors.left}" />
                        <rect x="50" y="25" width="25" height="85" fill="${colors.right}" />
                        <path d="M 10,32 L 25,25 L 25,58 L 13,62 Z" fill="${colors.right}" />
                        <path d="M 90,32 L 75,25 L 75,58 L 87,62 Z" fill="${colors.left}" />
                    `;
                } else if (type === 'horizontal-stripes') {
                    bodyPattern = `
                        <rect x="25" y="25" width="50" height="85" fill="${colors.base}" />
                        <rect x="25" y="35" width="50" height="10" fill="${colors.stripe}" />
                        <rect x="25" y="55" width="50" height="10" fill="${colors.stripe}" />
                        <rect x="25" y="75" width="50" height="10" fill="${colors.stripe}" />
                        <rect x="25" y="95" width="50" height="10" fill="${colors.stripe}" />
                        <path d="M 10,32 L 25,25 L 25,58 L 13,62 Z" fill="${colors.base}" />
                        <path d="M 90,32 L 75,25 L 75,58 L 87,62 Z" fill="${colors.base}" />
                    `;
                } else if (type === 'checkerboard') {
                    bodyPattern = `
                        <rect x="25" y="25" width="50" height="85" fill="${colors.base}" />
                        <rect x="25" y="25" width="12.5" height="16" fill="${colors.stripe}" />
                        <rect x="50" y="25" width="12.5" height="16" fill="${colors.stripe}" />
                        <rect x="37.5" y="41" width="12.5" height="16" fill="${colors.stripe}" />
                        <rect x="62.5" y="41" width="12.5" height="16" fill="${colors.stripe}" />
                        <rect x="25" y="57" width="12.5" height="16" fill="${colors.stripe}" />
                        <rect x="50" y="57" width="12.5" height="16" fill="${colors.stripe}" />
                        <rect x="37.5" y="73" width="12.5" height="16" fill="${colors.stripe}" />
                        <rect x="62.5" y="73" width="12.5" height="16" fill="${colors.stripe}" />
                        <rect x="25" y="89" width="12.5" height="16" fill="${colors.stripe}" />
                        <rect x="50" y="89" width="12.5" height="16" fill="${colors.stripe}" />
                        <path d="M 10,32 L 25,25 L 25,58 L 13,62 Z" fill="${colors.base}" />
                        <path d="M 90,32 L 75,25 L 75,58 L 87,62 Z" fill="${colors.base}" />
                    `;
                } else if (type === 'three-color-stripes') {
                    bodyPattern = `
                        <rect x="25" y="25" width="50" height="85" fill="${colors.base}" />
                        <rect x="31" y="25" width="7" height="85" fill="${colors.stripe1}" />
                        <rect x="38" y="25" width="7" height="85" fill="${colors.stripe2}" />
                        <rect x="55" y="25" width="7" height="85" fill="${colors.stripe1}" />
                        <rect x="62" y="25" width="7" height="85" fill="${colors.stripe2}" />
                        <path d="M 10,32 L 25,25 L 25,58 L 13,62 Z" fill="${colors.base}" />
                        <path d="M 90,32 L 75,25 L 75,58 L 87,62 Z" fill="${colors.base}" />
                    `;
                } else if (type === 'gold-accent-stripes') {
                    bodyPattern = `
                        <rect x="25" y="25" width="50" height="85" fill="${colors.base}" />
                        <rect x="32" y="25" width="12" fill="${colors.stripe}" height="85"/>
                        <rect x="31" y="25" width="1" fill="${colors.accent}" height="85"/>
                        <rect x="44" y="25" width="1" fill="${colors.accent}" height="85"/>
                        <rect x="56" y="25" width="12" fill="${colors.stripe}" height="85"/>
                        <rect x="55" y="25" width="1" fill="${colors.accent}" height="85"/>
                        <rect x="68" y="25" width="1" fill="${colors.accent}" height="85"/>
                        <path d="M 10,32 L 25,25 L 25,58 L 13,62 Z" fill="${colors.base}" />
                        <path d="M 90,32 L 75,25 L 75,58 L 87,62 Z" fill="${colors.base}" />
                    `;
                } else {
                    // Standard Vertical Stripes
                    bodyPattern = `
                        <rect x="25" y="25" width="50" height="85" fill="${colors.base}" />
                        <rect x="34" y="25" width="10" height="85" fill="${colors.stripe}" />
                        <rect x="56" y="25" width="10" height="85" fill="${colors.stripe}" />
                        <path d="M 10,32 L 25,25 L 25,58 L 13,62 Z" fill="${colors.base}" />
                        <path d="M 90,32 L 75,25 L 75,58 L 87,62 Z" fill="${colors.base}" />
                    `;
                }
            } else {
                // Away Kit Graphics
                if (colors.sash) {
                    bodyPattern = `
                        <rect x="25" y="25" width="50" height="85" fill="${colors.base}" />
                        <polygon points="25,25 38,25 75,100 62,100" fill="${colors.stripe}" />
                        <polygon points="25,25 38,25 75,100 62,100" fill="${colors.accent}" opacity="0.3" />
                        <path d="M 10,32 L 25,25 L 25,58 L 13,62 Z" fill="${colors.base}" />
                        <path d="M 90,32 L 75,25 L 75,58 L 87,62 Z" fill="${colors.base}" />
                    `;
                } else if (colors.stripe) {
                    bodyPattern = `
                        <rect x="25" y="25" width="50" height="85" fill="${colors.base}" />
                        <rect x="47" y="25" width="6" height="85" fill="${colors.stripe}" />
                        <path d="M 10,32 L 25,25 L 25,58 L 13,62 Z" fill="${colors.base}" />
                        <path d="M 90,32 L 75,25 L 75,58 L 87,62 Z" fill="${colors.base}" />
                    `;
                } else {
                    bodyPattern = `
                        <rect x="25" y="25" width="50" height="85" fill="${colors.base}" />
                        <path d="M 10,32 L 25,25 L 25,58 L 13,62 Z" fill="${colors.base}" />
                        <path d="M 90,32 L 75,25 L 75,58 L 87,62 Z" fill="${colors.base}" />
                    `;
                }
            }

            const isCenteredCrest = !isAway && (type === 'half-and-half-125th' || type === 'half-and-half');
            const crestX = isCenteredCrest ? 50 : 37;

            return `
                <svg viewBox="0 0 100 120" class="w-full h-auto drop-shadow-xl select-none">
                    <defs>
                        <!-- Fabric Texture & Lighting Gradients -->
                        <linearGradient id="fabricShine" x1="0%" y1="0%" x2="100%" y2="100%">
                            <stop offset="0%" stop-color="#ffffff" stop-opacity="0.25" />
                            <stop offset="40%" stop-color="#ffffff" stop-opacity="0.05" />
                            <stop offset="70%" stop-color="#000000" stop-opacity="0.15" />
                            <stop offset="100%" stop-color="#000000" stop-opacity="0.4" />
                        </linearGradient>

                        <!-- Collar Shadow -->
                        <filter id="dropShadow" x="-10%" y="-10%" width="130%" height="130%">
                            <feDropShadow dx="0" dy="3" stdDeviation="2.5" flood-color="#000" flood-opacity="0.5"/>
                        </filter>
                    </defs>

                    <g filter="url(#dropShadow)">
                        <!-- Outer Base Body Clip Silhouette -->
                        <path d="M 25,25 L 38,20 C 45,23 55,23 62,20 L 75,25 L 90,32 L 87,62 L 75,58 L 75,108 C 75,110 73,112 70,112 L 30,112 C 27,112 25,110 25,108 L 25,58 L 13,62 L 10,32 Z" 
                            id="jerseyBody" fill="#004D98"/>

                        <!-- Kit Color & Pattern Render Group -->
                        <g clip-path="url(#bodyClip)">
                            <clipPath id="bodyClip">
                                <path d="M 25,25 L 38,20 C 45,23 55,23 62,20 L 75,25 L 90,32 L 87,62 L 75,58 L 75,108 C 75,110 73,112 70,112 L 30,112 C 27,112 25,110 25,108 L 25,58 L 13,62 L 10,32 Z"/>
                            </clipPath>
                            ${bodyPattern}
                            
                            <!-- 3D Fabric Lighting Overlay -->
                            <rect x="0" y="0" width="100" height="120" fill="url(#fabricShine)" />
                        </g>

                        <!-- Fold Lines & Detailed Seams -->
                        <path d="M 25,25 L 25,108" stroke="#000" stroke-width="0.75" opacity="0.25" />
                        <path d="M 75,25 L 75,108" stroke="#000" stroke-width="0.75" opacity="0.25" />
                        <path d="M 25,58 L 13,62" stroke="#000" stroke-width="0.75" opacity="0.2" />
                        <path d="M 75,58 L 87,62" stroke="#000" stroke-width="0.75" opacity="0.2" />

                        <!-- Detailed Sleeve Rib Cuffs -->
                        <path d="M 10,32 L 13,62" stroke="${colors.accent || '#EDBB00'}" stroke-width="2.5" opacity="0.9"/>
                        <path d="M 90,32 L 87,62" stroke="${colors.accent || '#EDBB00'}" stroke-width="2.5" opacity="0.9"/>

                        <!-- High Quality Neckline & Collar Rib -->
                        <path d="M 36,20 C 43,26 57,26 64,20 C 60,28 40,28 36,20 Z" fill="${colors.collar || colors.accent || '#EDBB00'}" stroke="#000" stroke-width="0.5"/>
                        <path d="M 38,21 C 44,26 56,26 62,21" fill="none" stroke="#000" stroke-width="1.2" opacity="0.4"/>

                        <!-- FC Barcelona Detailed Crest Shield Graphic -->
                        <g transform="translate(${crestX - 4.5}, 35) scale(0.23)">
                            <!-- Crest Shield Outline -->
                            <path d="M0 0 H40 V20 C40 35 20 45 20 45 C20 45 0 35 0 20 Z" fill="#EDBB00" stroke="#000" stroke-width="2"/>
                            <path d="M2 2 H38 V19 C38 32 20 42 20 42 C20 42 2 32 2 19 Z" fill="#FFF"/>
                            <!-- St George Cross (Top Left) -->
                            <rect x="4" y="6" width="12" height="3" fill="#A50044"/>
                            <rect x="8.5" y="3" width="3" height="9" fill="#A50044"/>
                            <!-- Senyera Catalunya Flags (Top Right) -->
                            <rect x="22" y="3" width="14" height="9" fill="#EDBB00"/>
                            <rect x="24" y="3" width="2" height="9" fill="#A50044"/>
                            <rect x="28" y="3" width="2" height="9" fill="#A50044"/>
                            <rect x="32" y="3" width="2" height="9" fill="#A50044"/>
                            <!-- Center Golden Football -->
                            <circle cx="20" cy="28" r="5" fill="#EDBB00" stroke="#000" stroke-width="1"/>
                            <!-- Blaugrana Stripes (Bottom Crest) -->
                            <rect x="5" y="20" width="4" height="15" fill="#A50044"/>
                            <rect x="9" y="20" width="4" height="15" fill="#004D98"/>
                            <rect x="13" y="20" width="4" height="15" fill="#A50044"/>
                            <rect x="23" y="20" width="4" height="15" fill="#004D98"/>
                            <rect x="27" y="20" width="4" height="15" fill="#A50044"/>
                            <rect x="31" y="20" width="4" height="15" fill="#004D98"/>
                        </g>

                        <!-- Golden Champion Badge or Sponsor Silhouette -->
                        <rect x="37" y="58" width="26" height="6" rx="2" fill="#FFFFFF" opacity="0.85"/>
                    </g>
                </svg>
            `;
        }

        // Render Detailed Profile Panel
        function renderSeasonDetail(seasonId) {
            const container = document.getElementById('seasonDetailContainer');
            const data = seasonsData.find(s => s.id === seasonId);

            if (!data) return;

            const homeKitSVG = generateHighQualityKitSVG(data.kitInfo, false);
            const awayKitSVG = generateHighQualityKitSVG(data.kitInfo, true);

            container.innerHTML = `
                <div class="bg-gray-900/95 border border-gray-800 rounded-3xl p-6 sm:p-8 backdrop-blur-md shadow-2xl relative overflow-hidden transition-all duration-300">
                    <!-- Background Accent Soft Glow -->
                    <div class="absolute -right-20 -top-20 w-80 h-80 bg-blaugrana-blue/20 rounded-full blur-3xl pointer-events-none"></div>
                    <div class="absolute -left-20 -bottom-20 w-80 h-80 bg-blaugrana-red/20 rounded-full blur-3xl pointer-events-none"></div>

                    <!-- Header Banner -->
                    <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-gray-800 pb-6 relative z-10">
                        <div>
                            <div class="flex items-center gap-3">
                                <span class="text-xs font-bold uppercase tracking-widest text-blaugrana-yellow bg-blaugrana-yellow/10 border border-blaugrana-yellow/30 px-3 py-1 rounded-full">
                                    ${data.era}
                                </span>
                                <span class="text-xs text-gray-400 font-mono">FC BARCELONA ARCHIVE</span>
                            </div>
                            <h2 class="text-3xl sm:text-5xl font-black text-white tracking-tight mt-2 flex items-center gap-3">
                                ${data.season} <span class="text-base sm:text-lg font-normal text-gray-400">시즌 프로필</span>
                            </h2>
                        </div>

                        <!-- Trophies Badges -->
                        <div class="flex flex-wrap gap-2">
                            ${data.trophies.map(t => `
                                <div class="flex items-center gap-2 bg-gradient-to-r from-yellow-500/20 to-amber-500/10 border border-yellow-500/40 text-yellow-300 text-xs font-bold px-3 py-1.5 rounded-xl shadow-sm">
                                    <i class="fa-solid fa-trophy text-yellow-400"></i>
                                    <span>${t}</span>
                                </div>
                            `).join('')}
                        </div>
                    </div>

                    <!-- Main Grid Content -->
                    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 mt-8 relative z-10">
                        
                        <!-- Left: Kits Display (5 cols) -->
                        <div class="lg:col-span-5 bg-gray-950/70 border border-gray-800/80 rounded-2xl p-6 flex flex-col items-center justify-between gap-6 shadow-inner">
                            <div class="w-full text-center border-b border-gray-800/80 pb-3 flex justify-between items-center">
                                <h3 class="text-xs font-bold uppercase text-gray-300 tracking-wider flex items-center gap-2">
                                    <i class="fa-solid fa-shirt text-blaugrana-yellow"></i> Detailed Kit Illustration
                                </h3>
                                <span class="text-[10px] text-gray-500 font-mono">Realistic Vector Rendering</span>
                            </div>

                            <!-- Kits Vector Display Grid -->
                            <div class="grid grid-cols-2 gap-4 w-full">
                                <!-- Home Kit -->
                                <div class="flex flex-col items-center group">
                                    <div class="w-full max-w-[160px] p-2 transition-transform duration-300 group-hover:scale-105 filter drop-shadow-lg">
                                        ${homeKitSVG}
                                    </div>
                                    <span class="text-xs font-bold text-gray-200 mt-2">HOME KIT</span>
                                    <span class="text-[10px] text-blaugrana-yellow font-medium">홈 유니폼</span>
                                </div>

                                <!-- Away Kit -->
                                <div class="flex flex-col items-center group">
                                    <div class="w-full max-w-[160px] p-2 transition-transform duration-300 group-hover:scale-105 filter drop-shadow-lg">
                                        ${awayKitSVG}
                                    </div>
                                    <span class="text-xs font-bold text-gray-200 mt-2">AWAY KIT</span>
                                    <span class="text-[10px] text-gray-400 font-medium">어웨이 유니폼</span>
                                </div>
                            </div>

                            <!-- Kit Description Note -->
                            <div class="bg-gray-900/90 border border-gray-800 rounded-xl p-3.5 text-xs text-gray-400 text-center w-full">
                                <p class="text-gray-200 font-semibold mb-1">유니폼 디자인 디테일</p>
                                ${data.kitInfo.description}
                            </div>
                        </div>

                        <!-- Right: Season Information & Summary (7 cols) -->
                        <div class="lg:col-span-7 flex flex-col justify-between gap-6">
                            
                            <!-- Key Stats Grid -->
                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                                <!-- Manager -->
                                <div class="bg-gray-950/50 border border-gray-800/80 p-4 rounded-2xl flex items-center gap-4">
                                    <div class="w-10 h-10 rounded-xl bg-blaugrana-blue/20 border border-blaugrana-blue/40 flex items-center justify-center text-blaugrana-blue">
                                        <i class="fa-solid fa-user-tie text-lg"></i>
                                    </div>
                                    <div>
                                        <div class="text-[11px] uppercase font-bold text-gray-500">Key Manager (감독)</div>
                                        <div class="text-sm font-bold text-gray-200 mt-0.5">${data.manager}</div>
                                    </div>
                                </div>

                                <!-- Top Scorer -->
                                <div class="bg-gray-950/50 border border-gray-800/80 p-4 rounded-2xl flex items-center gap-4">
                                    <div class="w-10 h-10 rounded-xl bg-blaugrana-red/20 border border-blaugrana-red/40 flex items-center justify-center text-blaugrana-red">
                                        <i class="fa-solid fa-futbol text-lg"></i>
                                    </div>
                                    <div>
                                        <div class="text-[11px] uppercase font-bold text-gray-500">Top Scorer (최다 득점자)</div>
                                        <div class="text-sm font-bold text-gray-200 mt-0.5">${data.topScorer}</div>
                                    </div>
                                </div>
                            </div>

                            <!-- Key Players -->
                            <div class="bg-gray-950/50 border border-gray-800/80 p-5 rounded-2xl">
                                <div class="text-xs uppercase font-bold text-gray-400 mb-3 flex items-center gap-2">
                                    <i class="fa-solid fa-star text-blaugrana-yellow"></i> Key Players (주요 선수)
                                </div>
                                <div class="flex flex-wrap gap-2">
                                    ${data.keyPlayers.map(player => `
                                        <span class="bg-gray-900 border border-gray-700/80 text-gray-300 text-xs font-medium px-3 py-1.5 rounded-lg flex items-center gap-1.5">
                                            <span class="w-1.5 h-1.5 rounded-full bg-blaugrana-red"></span>
                                            ${player}
                                        </span>
                                    `).join('')}
                                </div>
                            </div>

                            <!-- Season Summary -->
                            <div class="bg-gray-950/50 border border-gray-800/80 p-5 rounded-2xl flex-grow">
                                <div class="text-xs uppercase font-bold text-gray-400 mb-2 flex items-center gap-2">
                                    <i class="fa-solid fa-book-open text-blaugrana-yellow"></i> Season Summary (시즌 요약)
                                </div>
                                <p class="text-sm text-gray-300 leading-relaxed">
                                    ${data.summary}
                                </p>
                            </div>

                        </div>
                    </div>
                </div>
            `;
        }
    </script>
</body>
</html>
