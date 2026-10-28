# -*- coding: utf-8 -*-
"""
sync_navigation_all.py
Synchronizes global floating dock pills (1-18), tools dropdown menu,
and mega drawer sheet (Topics 1-9, 18 Lessons) across all HTML pages in the project.
"""

import re

ICONS = {
    1: "🏠", 2: "🎨", 3: "🍁", 4: "⛅", 5: "🏙️", 6: "🗺️",
    7: "⏰", 8: "⛩️", 9: "🗣️", 10: "🌟", 11: "🍱", 12: "🍜",
    13: "✈️", 14: "💻", 15: "🏥", 16: "🏃", 17: "🎁", 18: "👘"
}

# The universal mega sheet covering Topics 1-9 and Lessons 1-18
MEGA_SHEET = """    <!-- MEGA DRAWER SHEET -->
    <div class="global-mega-sheet" id="globalMegaSheet" onclick="closeGlobalMegaSheet()">
        <div class="sheet-content" onclick="event.stopPropagation()">
            <div class="sheet-header">
                <div class="sheet-header-title">📚 Mục Lục Toàn Diện 18 Bài Học (Marugoto A2-1 & A2-2)</div>
                <button type="button" class="sheet-close-btn" onclick="closeGlobalMegaSheet()">✕</button>
            </div>
            <div class="sheet-topics-grid">
                <div class="sheet-topic-card">
                    <div class="sheet-topic-badge">Topic 1: Gia Đình & Bản Thân</div>
                    <a href="On_Tap_Mini_Test_A2_5_8.html#grammar-l1" class="sheet-lesson-link">
                        <div class="sheet-lesson-name">🏠 Bài 1: Nơi ở & Gia đình</div>
                        <div class="sheet-lesson-desc">～に住んでいます / Thể ている / で働いています</div>
                    </a>
                    <a href="On_Tap_Mini_Test_A2_5_8.html#grammar-l2" class="sheet-lesson-link">
                        <div class="sheet-lesson-name">🎨 Bài 2: Sở thích của tôi</div>
                        <div class="sheet-lesson-desc">V-ること / Thể từ điển (RU) / Năng khiếu</div>
                    </a>
                </div>
                <div class="sheet-topic-card">
                    <div class="sheet-topic-badge">Topic 2: Mùa & Thời Tiết</div>
                    <a href="On_Tap_Mini_Test_A2_5_8.html#grammar-l3" class="sheet-lesson-link">
                        <div class="sheet-lesson-name">🍁 Bài 3: Bốn mùa khí hậu</div>
                        <div class="sheet-lesson-desc">V-ると / になる・くなる (Thay đổi trạng thái)</div>
                    </a>
                    <a href="On_Tap_Mini_Test_A2_5_8.html#grammar-l4" class="sheet-lesson-link">
                        <div class="sheet-lesson-name">⛅ Bài 4: Dự báo thời tiết</div>
                        <div class="sheet-lesson-desc">～でしょう / ～かもしれません (Phán đoán)</div>
                    </a>
                </div>
                <div class="sheet-topic-card">
                    <div class="sheet-topic-badge">Topic 3: Thị Trấn Của Tôi</div>
                    <a href="On_Tap_Mini_Test_A2_5_8.html#grammar-l5" class="sheet-lesson-link">
                        <div class="sheet-lesson-name">🏙️ Bài 5: Nơi chốn & Phố xá</div>
                        <div class="sheet-lesson-desc">Địa điểm, phong cảnh và lối sống thị trấn</div>
                    </a>
                    <a href="On_Tap_Mini_Test_A2_5_8.html#grammar-l6" class="sheet-lesson-link">
                        <div class="sheet-lesson-name">🗺️ Bài 6: Mua sắm & Phương hướng</div>
                        <div class="sheet-lesson-desc">Chỉ đường, hỏi giá cả và mua hàng hóa</div>
                    </a>
                </div>
                <div class="sheet-topic-card">
                    <div class="sheet-topic-badge">Topic 4: Đi Lại & Ăn Uống</div>
                    <a href="On_Tap_Mini_Test_A2_5_8.html#grammar-l7" class="sheet-lesson-link">
                        <div class="sheet-lesson-name">⏰ Bài 7: Ra ngoài & Đi lại</div>
                        <div class="sheet-lesson-desc">Phương tiện giao thông, hẹn giờ và xuất phát</div>
                    </a>
                    <a href="On_Tap_Mini_Test_A2_5_8.html#grammar-l8" class="sheet-lesson-link">
                        <div class="sheet-lesson-name">⛩️ Bài 8: Bữa ăn & Thời gian</div>
                        <div class="sheet-lesson-desc">Món ăn thường ngày, thói quen ăn uống</div>
                    </a>
                </div>
                <div class="sheet-topic-card">
                    <div class="sheet-topic-badge">Topic 5: Ngôn Ngữ & Văn Hóa</div>
                    <a href="On_Tap_Mini_Test_A2_5_8.html#grammar-l9" class="sheet-lesson-link">
                        <div class="sheet-lesson-name">🗣️ Bài 9: Ngôn ngữ & Học tập</div>
                        <div class="sheet-lesson-desc">Năng khiếu ngôn ngữ, thời lượng học tập</div>
                    </a>
                    <a href="Marugoto_A2_Lesson_10.html" class="sheet-lesson-link">
                        <div class="sheet-lesson-name">🌟 Bài 10: Văn hóa & Du lịch ✨</div>
                        <div class="sheet-lesson-desc">V-たい / V-に行きます / Tần suất học & Du lịch</div>
                    </a>
                </div>
                <div class="sheet-topic-card">
                    <div class="sheet-topic-badge">Topic 6: Ăn Ngoài Trời</div>
                    <a href="Marugoto_A2_Lesson_11.html" class="sheet-lesson-link">
                        <div class="sheet-lesson-name">🍱 Bài 11: Dã ngoại & Đồ dùng ✨</div>
                        <div class="sheet-lesson-desc">V-ていきます/きます / Nghi vấn từ + でも / BBQ</div>
                    </a>
                    <a href="Marugoto_A2_Lesson_12.html" class="sheet-lesson-link">
                        <div class="sheet-lesson-name">🍜 Bài 12: Món ăn & Hương vị ✨</div>
                        <div class="sheet-lesson-desc">～そう (Trông ngon) / ～と似ています / A-くて</div>
                    </a>
                </div>
                <div class="sheet-topic-card">
                    <div class="sheet-topic-badge">Topic 7: Chuyến Đi Công Tác</div>
                    <a href="Marugoto_A2_Lesson_13.html" class="sheet-lesson-link">
                        <div class="sheet-lesson-name">✈️ Bài 13: Lịch trình công tác ✨</div>
                        <div class="sheet-lesson-desc">V-たことがあります / Sân bay, đưa đón & lịch trình</div>
                    </a>
                    <a href="Marugoto_A2_Lesson_14.html" class="sheet-lesson-link">
                        <div class="sheet-lesson-name">💻 Bài 14: Nơi làm việc ✨</div>
                        <div class="sheet-lesson-desc">V-てもいいですか (Xin phép) / V-てはいけません (Cấm)</div>
                    </a>
                </div>
                <div class="sheet-topic-card">
                    <div class="sheet-topic-badge">Topic 8: Cuộc Sống Khỏe Mạnh</div>
                    <a href="Marugoto_A2_Lesson_15.html" class="sheet-lesson-link">
                        <div class="sheet-lesson-name">🏥 Bài 15: Cơ thể & Bệnh tật ✨</div>
                        <div class="sheet-lesson-desc">～んです (Giải thích) / Triệu chứng & Khám bệnh</div>
                    </a>
                    <a href="Marugoto_A2_Lesson_16.html" class="sheet-lesson-link">
                        <div class="sheet-lesson-name">🏃 Bài 16: Giữ gìn sức khỏe ✨</div>
                        <div class="sheet-lesson-desc">V-たり V-たりします / V-たほうがいい / Lối sống</div>
                    </a>
                </div>
                <div class="sheet-topic-card">
                    <div class="sheet-topic-badge">Topic 9: Chúc Mừng & Kỷ Niệm</div>
                    <a href="Marugoto_A2_Lesson_17.html" class="sheet-lesson-link">
                        <div class="sheet-lesson-name">🎁 Bài 17: Quà tặng & Kỷ niệm ✨</div>
                        <div class="sheet-lesson-desc">あげます / もらいます / Các dịp lễ kỷ niệm</div>
                    </a>
                    <a href="Marugoto_A2_Lesson_18.html" class="sheet-lesson-link">
                        <div class="sheet-lesson-name">👘 Bài 18: Trang phục & Lễ hội ✨</div>
                        <div class="sheet-lesson-desc">V-ています (Mặc trang phục) / ～と思います / Lời chúc</div>
                    </a>
                </div>
            </div>
        </div>
    </div>"""

def generate_dock_pills(active_lesson_num=0):
    pills = []
    for i in range(1, 19):
        active_cls = " active" if i == active_lesson_num else ""
        icon = ICONS.get(i, "📘")
        if i >= 10:
            pills.append(f'            <a href="Marugoto_A2_Lesson_{i}.html" class="dock-pill{active_cls}" data-lesson="{i}"><span class="pill-ico">{icon}</span> Bài {i}</a>')
        else:
            pills.append(f'            <a href="On_Tap_Mini_Test_A2_5_8.html#grammar-l{i}" class="dock-pill{active_cls}" data-lesson="{i}"><span class="pill-ico">{icon}</span> Bài {i}</a>')
    
    return '<div class="dock-pill-track" id="dockPillTrack">\n' + "\n".join(pills) + "\n        </div>"

def generate_tools_menu(active_lesson_num=0):
    tools = []
    tools.append('                        <a href="Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html" class="dock-tool-item">📚 Tổng Hợp Ngữ Pháp A1-A2 (26 Bài) 🔥</a>')
    tools.append('                        <a href="index.html" class="dock-tool-item">🌸 Thể TE (～て)</a>')
    tools.append('                        <a href="the_ru.html" class="dock-tool-item">📘 Thể RU (Từ Điển)</a>')
    tools.append('                        <a href="kanji_a2.html" class="dock-tool-item">⛩️ Học Kanji & Nét Viết</a>')
    tools.append('                        <a href="Tu_Vung_Marugoto_A1_16_A2_1_10.html" class="dock-tool-item">📖 Kho Từ Vựng A1-A2 (600+ Từ)</a>')
    tools.append('                        <a href="On_Tap_Mini_Test_A2_5_8.html" class="dock-tool-item">🎯 Cẩm Nang Toàn Diện 10 Bài</a>')
    tools.append('                        <a href="De_Thi_Thu_Marugoto_A2_5_8.html" class="dock-tool-item">📝 5 Mã Đề Thi Thử</a>')
    for i in range(10, 19):
        active_cls = " active" if i == active_lesson_num else ""
        icon = ICONS.get(i, "📘")
        tools.append(f'                        <a href="Marugoto_A2_Lesson_{i}.html" class="dock-tool-item{active_cls}">{icon} Web Chuyên Sâu Bài {i} ✨</a>')
    return '<div class="dock-tools-menu" id="globalToolsMenu">\n' + "\n".join(tools) + "\n                    </div>"

PAGES = [
    ("index.html", 0),
    ("the_ru.html", 0),
    ("kanji_a2.html", 0),
    ("Tu_Vung_Marugoto_A1_16_A2_1_10.html", 0),
    ("On_Tap_Mini_Test_A2_1_4.html", 0),
    ("On_Tap_Mini_Test_A2_5_8.html", 0),
    ("De_Thi_Thu_Marugoto_A2_5_8.html", 0),
    ("Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html", 0),
    ("Marugoto_A2_Lesson_10.html", 10),
    ("Marugoto_A2_Lesson_11.html", 11),
    ("Marugoto_A2_Lesson_12.html", 12),
    ("Marugoto_A2_Lesson_13.html", 13),
    ("Marugoto_A2_Lesson_14.html", 14),
    ("Marugoto_A2_Lesson_15.html", 15),
    ("Marugoto_A2_Lesson_16.html", 16),
    ("Marugoto_A2_Lesson_17.html", 17),
    ("Marugoto_A2_Lesson_18.html", 18)
]

def sync_page(filename, lesson_num):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            html = f.read()
    except Exception as e:
        print(f"Skipping {filename}: {e}")
        return

    # Replace dock-pill-track
    new_pills = generate_dock_pills(lesson_num)
    html = re.sub(r'<div class="dock-pill-track" id="dockPillTrack">[\s\S]*?</div>', new_pills, html)

    # Replace dock-tools-menu
    new_tools = generate_tools_menu(lesson_num)
    html = re.sub(r'<div class="dock-tools-menu" id="globalToolsMenu">[\s\S]*?</div>', new_tools, html)

    # Replace global-mega-sheet
    html = re.sub(r'<div class="global-mega-sheet" id="globalMegaSheet"[\s\S]*?</div>\s*</div>\s*</div>', MEGA_SHEET, html)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Synced {filename} successfully!")

def main():
    for fn, num in PAGES:
        sync_page(fn, num)

if __name__ == "__main__":
    main()
