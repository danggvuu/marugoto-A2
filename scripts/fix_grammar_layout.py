import re

def fix_grammar_layout():
    with open('Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Define the missing Hero section CSS and refined styles
    hero_css = '''
        /* -------------------------------------------------------------
           2. HERO HEADER & KPI STATS (PREMIUM CARD DESIGN)
        ------------------------------------------------------------- */
        .hero-section {
            background: linear-gradient(135deg, #1e1b4b 0%, #2e2a72 40%, #4338ca 100%);
            color: #ffffff;
            padding: 34px 28px 28px;
            border-radius: 20px;
            max-width: 1300px;
            margin: 0 auto 24px auto;
            position: relative;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(67, 56, 202, 0.22);
            border: 1px solid rgba(255, 255, 255, 0.12);
        }

        .hero-section::before {
            content: '';
            position: absolute;
            top: -70px;
            right: -70px;
            width: 320px;
            height: 320px;
            background: radial-gradient(circle, rgba(129, 140, 248, 0.28) 0%, transparent 70%);
            border-radius: 50%;
            pointer-events: none;
        }

        .hero-container {
            max-width: 1200px;
            margin: 0 auto;
            position: relative;
            z-index: 2;
        }

        .hero-badge-pill {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            padding: 5px 14px;
            border-radius: 999px;
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.05em;
            color: #e0e7ff;
            margin-bottom: 12px;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        .hero-title {
            font-size: 2.15rem;
            font-weight: 900;
            letter-spacing: -0.03em;
            margin-bottom: 8px;
            line-height: 1.25;
            color: #ffffff;
        }

        .hero-subtitle {
            font-size: 0.96rem;
            color: #c7d2fe;
            max-width: 860px;
            margin-bottom: 22px;
            line-height: 1.6;
        }
'''

    # Inject hero_css right before /* KPI STATS CARDS */
    target_kpi = '/* KPI STATS CARDS */'
    if target_kpi in content:
        content = content.replace(target_kpi, hero_css + '\n        ' + target_kpi, 1)
        print("Injected Hero CSS successfully")
    else:
        print("Warning: target_kpi not found")

    # 2. Fix .level-pill.active (change pitch black to primary brand color)
    old_level_active = """.level-pill.active {
            background: var(--text-dark);
            color: #ffffff;
            border-color: var(--text-dark);
        }"""
    new_level_active = """.level-pill.active {
            background: var(--primary);
            color: #ffffff;
            border-color: var(--primary);
            box-shadow: 0 2px 8px rgba(79, 70, 229, 0.3);
        }"""
    if old_level_active in content:
        content = content.replace(old_level_active, new_level_active, 1)
        print("Updated level-pill.active color")

    # 3. Fix .category-scroll-row to flex-wrap: wrap so tags aren't truncated
    old_cat_row = """.category-scroll-row {
            display: flex;
            align-items: center;
            gap: 6px;
            overflow-x: auto;
            padding-bottom: 4px;
        }"""
    new_cat_row = """.category-scroll-row {
            display: flex;
            align-items: center;
            gap: 6px;
            flex-wrap: wrap;
            padding-bottom: 4px;
        }"""
    if old_cat_row in content:
        content = content.replace(old_cat_row, new_cat_row, 1)
        print("Updated category-scroll-row to wrap")

    # 4. Remove duplicate .global-hub-nav CSS block before </style>
    duplicate_nav_pattern = r'/\* ==========================================\s*GLOBAL HUB NAVIGATION \(CLEAN & NON-STICKY\)\s*========================================== \*/.*?@media \(max-width: 768px\) \{.*?\.hub-nav-item \{.*?\}\s*\}'
    m = re.search(duplicate_nav_pattern, content, re.DOTALL)
    if m:
        content = content[:m.start()] + content[m.end():]
        print("Removed duplicate nav CSS block")

    # 5. Add mobile responsive rules for hero-section
    mobile_hero_css = '''
        @media (max-width: 768px) {
            .hero-section {
                padding: 22px 16px 18px;
                border-radius: 16px;
                margin: 0 10px 18px 10px;
            }
            .hero-title {
                font-size: 1.45rem;
            }
            .hero-subtitle {
                font-size: 0.85rem;
                margin-bottom: 16px;
            }
            .kpi-grid {
                grid-template-columns: repeat(2, 1fr);
                gap: 10px;
            }
            .kpi-card {
                padding: 10px 12px;
            }
            .kpi-value {
                font-size: 1.25rem;
            }
        }
'''
    content = content.replace('</style>', mobile_hero_css + '\n    </style>', 1)

    with open('Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("Completed fixing Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html")

if __name__ == '__main__':
    fix_grammar_layout()
