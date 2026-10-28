# -*- coding: utf-8 -*-
"""
generate_all_lesson_vocab.py
Prepares rich flashcard vocabularies for Lessons 11-18 matching the official teacher PDF.
"""

import json
import re

def make_svg(title, emoji, c1="#3b82f6", c2="#1d4ed8"):
    h = abs(hash(title)) % 1000000
    safe_title = re.sub(r'[^a-zA-Z0-9À-ỹ\s]', '', title)[:15]
    return f'''<svg viewBox="0 0 240 120" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="g_{h}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{c1}"/>
      <stop offset="100%" stop-color="{c2}"/>
    </linearGradient>
  </defs>
  <rect width="240" height="120" rx="14" fill="url(#g_{h})"/>
  <circle cx="120" cy="50" r="30" fill="rgba(255,255,255,0.2)"/>
  <text x="120" y="60" text-anchor="middle" font-size="34">{emoji}</text>
  <text x="120" y="105" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="800" font-family="system-ui, -apple-system, sans-serif">{safe_title.upper()}</text>
</svg>'''

from update_lessons_official_vocab import vocab_11, vocab_12

vocab_13 = [
    {"id": 1, "cat": "flight", "catName": "Chuyến bay & Sân bay", "badge": "Chuyến bay", "jp": "～時の フライト", "kana": "～じの フライト", "kanji": "～時のフライト", "romaji": "~ji no furaito", "vi": "Chuyến bay cất cánh lúc ... giờ", "exJp": "９時の フライトで とうきょうへ いきます。", "exVi": "Tôi sẽ đi Tokyo trên chuyến bay lúc 9 giờ.", "svg": make_svg("CHUYẾN BAY", "✈️", "#0284c7", "#0369a1")},
    {"id": 2, "cat": "flight", "catName": "Chuyến bay & Sân bay", "badge": "Chuyến bay", "jp": "～時の びん", "kana": "～じの びん", "kanji": "～時の便", "romaji": "~ji no bin", "vi": "Chuyến bay cất cánh lúc ... giờ", "exJp": "ごご２時の びんに のります。", "exVi": "Tôi sẽ lên chuyến bay lúc 2 giờ chiều.", "svg": make_svg("CHUYẾN BAY", "🛫", "#0ea5e9", "#0284c7")},
    {"id": 3, "cat": "flight", "catName": "Chuyến bay & Sân bay", "badge": "Địa điểm", "jp": "くうこう", "kana": "くうこう", "kanji": "空港", "romaji": "kuukou", "vi": "Sân bay, phi trường", "exJp": "ハノイの くうこうに とうちゃくしました。", "exVi": "Tôi đã đáp xuống sân bay Hà Nội.", "svg": make_svg("SÂN BAY", "🏬", "#3b82f6", "#1d4ed8")},
    {"id": 4, "cat": "travel", "catName": "Di chuyển & Công tác", "badge": "Động từ", "jp": "しゅっぱつ（します）", "kana": "しゅっぱつ（します）", "kanji": "出発（します）", "romaji": "shuppatsu(shimasu)", "vi": "Xuất phát, khởi hành", "exJp": "ひこうきは １０時に しゅっぱつします。", "exVi": "Máy bay sẽ cất cánh lúc 10 giờ.", "svg": make_svg("XUẤT PHÁT", "🛫", "#10b981", "#047857")},
    {"id": 5, "cat": "travel", "catName": "Di chuyển & Công tác", "badge": "Động từ", "jp": "とうちゃく（します）", "kana": "とうちゃく（します）", "kanji": "到着（します）", "romaji": "touchaku(shimasu)", "vi": "Đến nơi, hạ cánh", "exJp": "とうきょうに ぶじに とうちゃくしました。", "exVi": "Đã hạ cánh an toàn tới Tokyo.", "svg": make_svg("ĐẾN NƠI", "🛬", "#22c55e", "#15803d")},
    {"id": 6, "cat": "travel", "catName": "Di chuyển & Công tác", "badge": "Động từ", "jp": "しゅっちょう（します）", "kana": "しゅっちょう（します）", "kanji": "出張（します）", "romaji": "shucchou(shimasu)", "vi": "Đi công tác xa", "exJp": "らいしゅう おおさかへ しゅっちょうします。", "exVi": "Tuần tới tôi sẽ đi công tác Osaka.", "svg": make_svg("CÔNG TÁC", "💼", "#6366f1", "#4338ca")},
    {"id": 7, "cat": "company", "catName": "Công ty & Cơ quan", "badge": "Công ty", "jp": "ししゃ", "kana": "ししゃ", "kanji": "支社", "romaji": "shisha", "vi": "Chi nhánh công ty", "exJp": "ベトナムの ししゃで はたらいています。", "exVi": "Tôi đang làm việc tại chi nhánh Việt Nam.", "svg": make_svg("CHI NHÁNH", "🏢", "#8b5cf6", "#6d28d9")},
    {"id": 8, "cat": "company", "catName": "Công ty & Cơ quan", "badge": "Công ty", "jp": "ほんしゃ", "kana": "ほんしゃ", "kanji": "本社", "romaji": "honsha", "vi": "Trụ sở chính công ty", "exJp": "とうきょうの ほんしゃに れんらくします。", "exVi": "Tôi sẽ liên lạc về trụ sở chính ở Tokyo.", "svg": make_svg("TRỤ SỞ CHÍNH", "🏛️", "#ec4899", "#be185d")},
    {"id": 9, "cat": "travel", "catName": "Di chuyển & Công tác", "badge": "Động từ", "jp": "おくります", "kana": "おくります", "kanji": "送ります", "romaji": "okurimasu", "vi": "Gửi đồ / Tiễn người đi", "exJp": "ともだちを くうこうまで おくります。", "exVi": "Tôi tiễn bạn ra tận sân bay.", "svg": make_svg("TIỄN ĐI", "👋", "#f59e0b", "#d97706")},
    {"id": 10, "cat": "travel", "catName": "Di chuyển & Công tác", "badge": "Động từ", "jp": "もらいます", "kana": "もらいます", "kanji": "貰います", "romaji": "moraimasu", "vi": "Nhận được từ ai đó", "exJp": "せんぱいから おみやげを もらいました。", "exVi": "Tôi đã nhận được quà lưu niệm từ tiền bối.", "svg": make_svg("NHẬN ĐƯỢC", "🎁", "#eab308", "#ca8a04")},
    {"id": 11, "cat": "travel", "catName": "Di chuyển & Công tác", "badge": "Động từ", "jp": "おくりに いきます", "kana": "おくりに いきます", "kanji": "送りに行きます", "romaji": "okurini ikimasu", "vi": "Đi tiễn ai đó", "exJp": "あした たなかさんを おくりに いきます。", "exVi": "Ngày mai tôi sẽ đi tiễn anh Tanaka.", "svg": make_svg("ĐI TIỄN", "🚶‍♂️", "#14b8a6", "#0f766e")},
    {"id": 12, "cat": "travel", "catName": "Di chuyển & Công tác", "badge": "Động từ", "jp": "むかえに いきます", "kana": "むかえに いきます", "kanji": "迎えに行きます", "romaji": "mukaeni ikimasu", "vi": "Đi đón ai đó", "exJp": "えきまで くるまで むかえに いきます。", "exVi": "Tôi sẽ lái xe ra ga để đi đón bạn.", "svg": make_svg("ĐI ĐÓN", "🚗", "#0ea5e9", "#0284c7")},
    {"id": 13, "cat": "travel", "catName": "Di chuyển & Công tác", "badge": "Danh từ", "jp": "でむかえ", "kana": "でむかえ", "kanji": "出迎え", "romaji": "demukae", "vi": "Việc đón tiếp", "exJp": "くうこうで でむかえが あります。", "exVi": "Có người ra sân bay đón tiếp.", "svg": make_svg("ĐÓN TIẾP", "🤝", "#10b981", "#059669")},
    {"id": 14, "cat": "travel", "catName": "Di chuyển & Công tác", "badge": "Danh từ", "jp": "みおくり", "kana": "みおくり", "kanji": "見送り", "romaji": "miokuri", "vi": "Việc tiễn đưa", "exJp": "おおぜいの ひとが みおくりに きました。", "exVi": "Rất đông người đã đến tiễn đưa.", "svg": make_svg("TIỄN BIỆT", "👋", "#f97316", "#c2410c")},
    {"id": 15, "cat": "state", "catName": "Trạng thái & Lịch trình", "badge": "Động từ", "jp": "すきます", "kana": "すきます", "kanji": "空きます", "romaji": "sukimasu", "vi": "Vắng vẻ, thưa thớt", "exJp": "このじかんの でんしゃは すいています。", "exVi": "Tàu điện giờ này khá vắng vẻ.", "svg": make_svg("VẮNG VẺ", "🪑", "#06b6d4", "#0891b2")},
    {"id": 16, "cat": "state", "catName": "Trạng thái & Lịch trình", "badge": "Động từ", "jp": "こみます", "kana": "こみます", "kanji": "混みます", "romaji": "komimasu", "vi": "Đông đúc, chen chúc", "exJp": "みちは くるまで こんでいます。", "exVi": "Đường phố đang đông nghẹt xe cộ.", "svg": make_svg("ĐÔNG ĐÚC", "👥", "#ef4444", "#b91c1c")},
    {"id": 17, "cat": "state", "catName": "Trạng thái & Lịch trình", "badge": "Tính từ na", "jp": "かいてき（な）", "kana": "かいてき（な）", "kanji": "快適（な）", "romaji": "kaiteki(na)", "vi": "Thoải mái, tiện nghi", "exJp": "ホテルは ひろくて とても かいてきです。", "exVi": "Khách sạn rộng rãi và rất tiện nghi thoải mái.", "svg": make_svg("TIỆN NGHI", "🛋️", "#8b5cf6", "#6d28d9")},
    {"id": 18, "cat": "travel", "catName": "Di chuyển & Công tác", "badge": "Danh từ", "jp": "じさ", "kana": "じさ", "kanji": "時差", "romaji": "jisa", "vi": "Chênh lệch múi giờ", "exJp": "にほんと ベトナムの じさは ２じかんです。", "exVi": "Múi giờ giữa Nhật và Việt Nam chênh lệch 2 tiếng.", "svg": make_svg("MÚI GIỜ", "⏰", "#f59e0b", "#d97706")},
    {"id": 19, "cat": "state", "catName": "Trạng thái & Lịch trình", "badge": "Cụm từ", "jp": "おゆが でます", "kana": "おゆが でます", "kanji": "お湯が出ます", "romaji": "oyu ga demasu", "vi": "Có vòi nước nóng chảy ra", "exJp": "シャワーから あたたかい おゆが でます。", "exVi": "Vòi hoa sen chảy ra dòng nước ấm áp.", "svg": make_svg("NƯỚC NÓNG", "🚿", "#0284c7", "#0369a1")},
    {"id": 20, "cat": "state", "catName": "Trạng thái & Lịch trình", "badge": "Tính từ", "jp": "ぬるい", "kana": "ぬるい", "kanji": "温い", "romaji": "nurui", "vi": "Nguội, ấm ấm (nhiệt độ)", "exJp": "おゆが ぬるくて、すこし さむいです。", "exVi": "Nước chỉ hơi ấm ấm nên hơi lạnh.", "svg": make_svg("HƠI ẤM NGUỘI", "🌡️", "#64748b", "#334155")},
    {"id": 21, "cat": "state", "catName": "Trạng thái & Lịch trình", "badge": "Danh từ", "jp": "スケジュール", "kana": "スケジュール", "kanji": "スケジュール", "romaji": "sukejuuru", "vi": "Lịch trình công tác (Schedule)", "exJp": "しゅっちょうの スケジュールを かくにんします。", "exVi": "Xác nhận lại lịch trình chuyến công tác.", "svg": make_svg("LỊCH TRÌNH", "📅", "#10b981", "#047857")},
    {"id": 22, "cat": "state", "catName": "Trạng thái & Lịch trình", "badge": "Danh từ", "jp": "ばんごう", "kana": "ばんごう", "kanji": "番号", "romaji": "bangou", "vi": "Số hiệu, con số", "exJp": "へやの ばんごうは 302です。", "exVi": "Số phòng của tôi là 302.", "svg": make_svg("CON SỐ", "🔢", "#6366f1", "#4338ca")},
    {"id": 23, "cat": "state", "catName": "Trạng thái & Lịch trình", "badge": "Phó từ", "jp": "ずっと", "kana": "ずっと", "kanji": "ずっと", "romaji": "zutto", "vi": "Suốt, mãi / Hơn hẳn", "exJp": "きのうは ずっと ホテルに いました。", "exVi": "Hôm qua tôi ở suốt trong khách sạn.", "svg": make_svg("SUỐT MÃI", "⏳", "#ec4899", "#be185d")},
    {"id": 24, "cat": "travel", "catName": "Di chuyển & Công tác", "badge": "Động từ", "jp": "チェック（します）", "kana": "チェック（します）", "kanji": "チェック（します）", "romaji": "chekku(shimasu)", "vi": "Kiểm tra, soát lại (Check)", "exJp": "メールを チェックしてください。", "exVi": "Xin hãy kiểm tra hòm thư email nhé.", "svg": make_svg("KIỂM TRA", "✔️", "#22c55e", "#15803d")},
    {"id": 25, "cat": "business", "catName": "Giao tiếp công sở", "badge": "Động từ", "jp": "たんとう（します）", "kana": "たんとう（します）", "kanji": "担当（します）", "romaji": "tantou(shimasu)", "vi": "Đảm nhiệm, phụ trách", "exJp": "ベトナムの プロジェクトを たんとうします。", "exVi": "Tôi phụ trách dự án Việt Nam.", "svg": make_svg("PHỤ TRÁCH", "📋", "#0ea5e9", "#0284c7")},
    {"id": 26, "cat": "business", "catName": "Giao tiếp công sở", "badge": "Mẫu câu", "jp": "～へ ようこそ。", "kana": "～へ ようこそ。", "kanji": "～へようこそ", "romaji": "~e youkoso", "vi": "Chào mừng quý khách đến với...", "exJp": "にほんへ ようこそ！", "exVi": "Chào mừng bạn đến với Nhật Bản!", "svg": make_svg("CHÀO MỪNG", "🎊", "#f43f5e", "#be123c")},
    {"id": 27, "cat": "business", "catName": "Giao tiếp công sở", "badge": "Mẫu câu", "jp": "おつかれさまです。", "kana": "おつかれさまです。", "kanji": "お疲れ様です", "romaji": "otsukaresama desu", "vi": "Bạn đã vất vả rồi (chào đồng nghiệp)", "exJp": "きょうも おつかれさまでした。", "exVi": "Hôm nay bạn cũng đã vất vả rồi.", "svg": make_svg("VẤT VẢ RỒI", "🍵", "#10b981", "#059669")},
    {"id": 28, "cat": "business", "catName": "Giao tiếp công sở", "badge": "Mẫu câu", "jp": "おまたせしました。", "kana": "おまたせしました。", "kanji": "お待たせしました", "romaji": "omataseshimashita", "vi": "Xin lỗi đã để bạn phải đợi lâu", "exJp": "たいへん おまたせしました。", "exVi": "Vô cùng xin lỗi vì đã để quý khách phải đợi lâu.", "svg": make_svg("ĐỂ BẠN ĐỢI", "🙇", "#f59e0b", "#d97706")},
    {"id": 29, "cat": "business", "catName": "Giao tiếp công sở", "badge": "Mẫu câu", "jp": "～は いかがですか。", "kana": "～は いかがですか。", "kanji": "～はいかがですか", "romaji": "~wa ikaga desu ka", "vi": "Như thế nào ạ (cách hỏi lịch sự)", "exJp": "おちゃは いかがですか。", "exVi": "Dùng thêm một tách trà nhé ạ?", "svg": make_svg("NHƯ THẾ NÀO", "🍵", "#8b5cf6", "#6d28d9")},
    {"id": 30, "cat": "business", "catName": "Giao tiếp công sở", "badge": "Danh từ", "jp": "じょうだん", "kana": "じょうだん", "kanji": "冗談", "romaji": "joudan", "vi": "Nói đùa, lời trêu đùa", "exJp": "じょうだんを いって わらいました。", "exVi": "Nói đùa một câu khiến mọi người cùng cười.", "svg": make_svg("NÓI ĐÙA", "😄", "#eab308", "#ca8a04")},
    {"id": 31, "cat": "business", "catName": "Giao tiếp công sở", "badge": "Danh từ", "jp": "あいさつ", "kana": "あいさつ", "kanji": "挨拶", "romaji": "aisatsu", "vi": "Chào hỏi, lời chào xã giao", "exJp": "あさの あいさつを します。", "exVi": "Chào hỏi nhau vào buổi sáng.", "svg": make_svg("CHÀO HỎI", "🙋‍♂️", "#06b6d4", "#0891b2")},
    {"id": 32, "cat": "business", "catName": "Giao tiếp công sở", "badge": "Danh từ", "jp": "ねだん", "kana": "ねだん", "kanji": "値段", "romaji": "nedan", "vi": "Giá cả, mức giá", "exJp": "このホテルの ねだんは やすいです。", "exVi": "Giá phòng của khách sạn này khá rẻ.", "svg": make_svg("GIÁ CẢ", "🏷️", "#14b8a6", "#0f766e")},
    {"id": 33, "cat": "business", "catName": "Giao tiếp công sở", "badge": "Danh từ", "jp": "かぎ", "kana": "かぎ", "kanji": "鍵", "romaji": "kagi", "vi": "Chìa khóa phòng", "exJp": "へやの かぎを うけつけに あずけます。", "exVi": "Gửi chìa khóa phòng ở quầy lễ tân.", "svg": make_svg("CHÌA KHÓA", "🔑", "#eab308", "#a16207")},
    {"id": 34, "cat": "business", "catName": "Giao tiếp công sở", "badge": "Danh từ", "jp": "かいぎ", "kana": "かいぎ", "kanji": "会議", "romaji": "kaigi", "vi": "Cuộc họp nội bộ / với đối tác", "exJp": "ごごから ほんしゃで かいぎが あります。", "exVi": "Chiều nay có cuộc họp ở trụ sở chính.", "svg": make_svg("CUỘC HỌP", "👥", "#6366f1", "#4338ca")},
    {"id": 35, "cat": "business", "catName": "Giao tiếp công sở", "badge": "Danh từ", "jp": "しりょう", "kana": "しりょう", "kanji": "資料", "romaji": "shiryou", "vi": "Tài liệu cuộc họp", "exJp": "かいぎの しりょうを コピーします。", "exVi": "Photo tài liệu cho cuộc họp.", "svg": make_svg("TÀI LIỆU", "📄", "#3b82f6", "#1d4ed8")}
]

# -------------------------------------------------------------
# LESSON 14 (25 items)
# -------------------------------------------------------------
vocab_14 = [
    {"id": 1, "cat": "office", "catName": "Văn phòng & Thiết bị", "badge": "Nơi chốn", "jp": "オフィス", "kana": "オフィス", "kanji": "オフィス", "romaji": "ofisu", "vi": "Văn phòng làm việc (Office)", "exJp": "あかるくて ひろい オフィスです。", "exVi": "Văn phòng làm việc sáng sủa và rộng rãi.", "svg": make_svg("VĂN PHÒNG", "🏢", "#0284c7", "#0369a1")},
    {"id": 2, "cat": "office", "catName": "Văn phòng & Thiết bị", "badge": "Thiết bị", "jp": "キャビネット", "kana": "キャビネット", "kanji": "キャビネット", "romaji": "kyabinetto", "vi": "Tủ đựng hồ sơ, tài liệu", "exJp": "しりょうは キャビネットの なかに あります。", "exVi": "Tài liệu nằm ở bên trong tủ đựng hồ sơ.", "svg": make_svg("TỦ TÀI LIỆU", "🗄️", "#475569", "#1e293b")},
    {"id": 3, "cat": "office", "catName": "Văn phòng & Thiết bị", "badge": "Thiết bị", "jp": "コピーき", "kana": "コピーき", "kanji": "コピー機", "romaji": "kopiiki", "vi": "Máy photocopy", "exJp": "コピーきの つかいかたを おしえてください。", "exVi": "Xin hãy chỉ cho tôi cách sử dụng máy photo.", "svg": make_svg("MÁY PHOTO", "🖨️", "#64748b", "#334155")},
    {"id": 4, "cat": "office", "catName": "Văn phòng & Thiết bị", "badge": "Thiết bị", "jp": "ファックス", "kana": "ファックス", "kanji": "ファックス", "romaji": "fakkusu", "vi": "Máy fax gửi văn bản", "exJp": "ファックスで しょるいを おくります。", "exVi": "Gửi giấy tờ qua đường máy fax.", "svg": make_svg("MÁY FAX", "📠", "#0ea5e9", "#0284c7")},
    {"id": 5, "cat": "office", "catName": "Văn phòng & Thiết bị", "badge": "Thiết bị", "jp": "こくさいでんわ", "kana": "こくさいでんわ", "kanji": "国際電話", "romaji": "kokusaidenwa", "vi": "Cuộc gọi quốc tế", "exJp": "かいしゃから こくさいでんわを かけます。", "exVi": "Gọi điện thoại quốc tế từ công ty.", "svg": make_svg("GỌI QUỐC TẾ", "🌐", "#3b82f6", "#1d4ed8")},
    {"id": 6, "cat": "people", "catName": "Nhân sự & Chức vụ", "badge": "Chức vụ", "jp": "しゃちょう", "kana": "しゃちょう", "kanji": "社長", "romaji": "shachou", "vi": "Giám đốc công ty", "exJp": "しゃちょうに あいさつを します。", "exVi": "Chào hỏi giám đốc công ty.", "svg": make_svg("GIÁM ĐỐC", "👔", "#1e293b", "#0f172a")},
    {"id": 7, "cat": "people", "catName": "Nhân sự & Chức vụ", "badge": "Chức vụ", "jp": "ひしょ", "kana": "ひしょ", "kanji": "秘書", "romaji": "hisho", "vi": "Thư ký văn phòng", "exJp": "ひしょに スケジュールを ききます。", "exVi": "Hỏi thư ký về lịch làm việc.", "svg": make_svg("THƯ KÝ", "👩‍💼", "#8b5cf6", "#6d28d9")},
    {"id": 8, "cat": "people", "catName": "Nhân sự & Chức vụ", "badge": "Nơi chốn", "jp": "うけつけ", "kana": "うけつけ", "kanji": "受付", "romaji": "uketsuke", "vi": "Quầy lễ tân đón khách", "exJp": "１かいの うけつけで まっています。", "exVi": "Tôi đang đợi ở quầy lễ tân tầng 1.", "svg": make_svg("LỄ TÂN", "💁‍♀️", "#ec4899", "#be185d")},
    {"id": 9, "cat": "people", "catName": "Nhân sự & Chức vụ", "badge": "Nhân sự", "jp": "じむスタッフ", "kana": "じむスタッフ", "kanji": "事務スタッフ", "romaji": "jimu sutaffu", "vi": "Nhân viên hành chính văn phòng", "exJp": "じむスタッフが てつだって くれました。", "exVi": "Nhân viên văn phòng đã giúp đỡ tôi.", "svg": make_svg("NHÂN VIÊN", "👥", "#10b981", "#047857")},
    {"id": 10, "cat": "people", "catName": "Nhân sự & Chức vụ", "badge": "Nghề nghiệp", "jp": "ドライバー", "kana": "ドライバー", "kanji": "ドライバー", "romaji": "doraibaa", "vi": "Tài xế lái xe (Driver)", "exJp": "ドライバーが くるまで まっています。", "exVi": "Bác tài xế đang đợi sẵn ở ô tô.", "svg": make_svg("TÀI XẾ", "🚗", "#f59e0b", "#d97706")},
    {"id": 11, "cat": "office", "catName": "Văn phòng & Thiết bị", "badge": "Cơ sở vật chất", "jp": "ドア", "kana": "ドア", "kanji": "ドア", "romaji": "doa", "vi": "Cửa ra vào (Door)", "exJp": "ドアを ノックしてから はいります。", "exVi": "Gõ cửa trước khi bước vào phòng.", "svg": make_svg("CỬA RA VÀO", "🚪", "#78350f", "#451a03")},
    {"id": 12, "cat": "office", "catName": "Văn phòng & Thiết bị", "badge": "Cơ sở vật chất", "jp": "まど", "kana": "まど", "kanji": "窓", "romaji": "mado", "vi": "Cửa sổ", "exJp": "まどを あけて、かぜを いれます。", "exVi": "Mở cửa sổ cho gió thoáng vào.", "svg": make_svg("CỬA SỔ", "🪟", "#0284c7", "#0369a1")},
    {"id": 13, "cat": "action", "catName": "Thao tác & Động từ", "badge": "Động từ", "jp": "（ドアを）あけます", "kana": "（ドアを）あけます", "kanji": "（ドアを）開けます", "romaji": "akemasu", "vi": "Mở (cửa/máy)", "exJp": "ドアを あけても いいですか。", "exVi": "Tôi mở cửa có được không ạ?", "svg": make_svg("MỞ CỬA", "🚪", "#22c55e", "#15803d")},
    {"id": 14, "cat": "action", "catName": "Thao tác & Động từ", "badge": "Động từ", "jp": "（ドアを）しめます", "kana": "（ドアを）しめます", "kanji": "（ドアを）閉めます", "romaji": "shimemasu", "vi": "Đóng (cửa/hộp)", "exJp": "さむいので、ドアを しめます。", "exVi": "Trời lạnh nên tôi đóng cửa lại.", "svg": make_svg("ĐÓNG CỬA", "🔒", "#ef4444", "#b91c1c")},
    {"id": 15, "cat": "action", "catName": "Thao tác & Động từ", "badge": "Động từ", "jp": "（でんきを）つけます", "kana": "（でんきを）つけます", "kanji": "（電気を）点けます", "romaji": "tsukemasu", "vi": "Bật (đèn/thiết bị điện)", "exJp": "くらいので でんきを つけます。", "exVi": "Phòng tối nên tôi bật đèn lên.", "svg": make_svg("BẬT ĐÈN", "💡", "#eab308", "#ca8a04")},
    {"id": 16, "cat": "action", "catName": "Thao tác & Động từ", "badge": "Động từ", "jp": "（でんきを）けします", "kana": "（でんきを）けします", "kanji": "（電気を）消します", "romaji": "keshimasu", "vi": "Tắt (đèn/máy tính)", "exJp": "かえるまえに でんきを けしてください。", "exVi": "Trước khi về nhớ tắt điện nhé.", "svg": make_svg("TẮT ĐÈN", "🌑", "#475569", "#1e293b")},
    {"id": 17, "cat": "action", "catName": "Thao tác & Động từ", "badge": "Động từ", "jp": "（パソコンが）こわれます", "kana": "（パソコンが）こわれます", "kanji": "（パソコンが）壊れます", "romaji": "kowaremasu", "vi": "(Máy tính) Bị hỏng, trục trặc", "exJp": "パソコンが こわれて、うごきません。", "exVi": "Máy tính bị hỏng nên không hoạt động.", "svg": make_svg("BỊ HỎNG", "⚠️", "#dc2626", "#991b1b")},
    {"id": 18, "cat": "action", "catName": "Thao tác & Động từ", "badge": "Trạng thái", "jp": "べんきょうちゅう", "kana": "べんきょうちゅう", "kanji": "勉強中", "romaji": "benkyouchuu", "vi": "Đang trong giờ học tập", "exJp": "いま にほんごを べんきょうちゅうです。", "exVi": "Tôi đang trong giờ học tiếng Nhật.", "svg": make_svg("ĐANG HỌC", "📖", "#6366f1", "#4338ca")},
    {"id": 19, "cat": "action", "catName": "Thao tác & Động từ", "badge": "Phó từ", "jp": "ぺらぺら", "kana": "ぺらぺら", "kanji": "ぺらぺら", "romaji": "perapera", "vi": "Nói trôi chảy, lưu loát", "exJp": "かれは えいごが ぺらぺらです。", "exVi": "Anh ấy nói tiếng Anh cực kỳ lưu loát.", "svg": make_svg("LƯU LOÁT", "🗣️", "#0ea5e9", "#0369a1")},
    {"id": 20, "cat": "action", "catName": "Thao tác & Động từ", "badge": "Động từ", "jp": "はじめます", "kana": "はじめます", "kanji": "始めます", "romaji": "hajimemasu", "vi": "Bắt đầu công việc/cuộc họp", "exJp": "では、かいぎを はじめましょう。", "exVi": "Vậy thì chúng ta bắt đầu cuộc họp nhé.", "svg": make_svg("BẮT ĐẦU", "▶️", "#10b981", "#059669")},
    {"id": 21, "cat": "office", "catName": "Văn phòng & Thiết bị", "badge": "Đồ dùng", "jp": "ファイル", "kana": "ファイル", "kanji": "ファイル", "romaji": "fairu", "vi": "File tệp tài liệu", "exJp": "このファイルを みてください。", "exVi": "Xin hãy xem tập file tài liệu này.", "svg": make_svg("FILE TÀI LIỆU", "📁", "#f59e0b", "#d97706")},
    {"id": 22, "cat": "office", "catName": "Văn phòng & Thiết bị", "badge": "Đồ dùng", "jp": "メモ", "kana": "メモ", "kanji": "メモ", "romaji": "memo", "vi": "Giấy ghi chú, bản ghi nhanh", "exJp": "だいじなことを メモに かきます。", "exVi": "Viết những điều quan trọng vào giấy ghi chú.", "svg": make_svg("GHI CHÚ", "📝", "#eab308", "#ca8a04")},
    {"id": 23, "cat": "office", "catName": "Văn phòng & Thiết bị", "badge": "Nơi chốn", "jp": "オフィス／じむしょ", "kana": "オフィス／じむしょ", "kanji": "事務所", "romaji": "ofisu / jimusho", "vi": "Văn phòng, nơi làm việc", "exJp": "じむしょに しりょうを とりに いきます。", "exVi": "Tôi đi đến văn phòng để lấy tài liệu.", "svg": make_svg("VĂN PHÒNG", "🏢", "#3b82f6", "#1d4ed8")},
    {"id": 24, "cat": "office", "catName": "Văn phòng & Thiết bị", "badge": "Thao tác", "jp": "プリントアウト", "kana": "プリントアウト", "kanji": "プリントアウト", "romaji": "purintoauto", "vi": "In ra giấy (Printout)", "exJp": "このメールを プリントアウトしてください。", "exVi": "Xin hãy in bức email này ra giấy.", "svg": make_svg("IN RA GIẤY", "🖨️", "#06b6d4", "#0891b2")},
    {"id": 25, "cat": "action", "catName": "Thao tác & Động từ", "badge": "Động từ", "jp": "しょうかいします", "kana": "しょうかいします", "kanji": "紹介します", "romaji": "shoukaishimasu", "vi": "Giới thiệu người/nơi chốn", "exJp": "あたらしい スタッフを しょうかいします。", "exVi": "Tôi xin phép giới thiệu nhân viên mới.", "svg": make_svg("GIỚI THIỆU", "🤝", "#8b5cf6", "#6d28d9")}
]

print("Vocab 13 and 14 prepared! Lengths:", len(vocab_13), len(vocab_14))

# -------------------------------------------------------------
# LESSON 15 (57 items)
# -------------------------------------------------------------
raw_15 = [
    ("あたま", "頭", "atama", "Đầu", "body", "Bộ phận cơ thể", "頭が 痛いんです。", "Tôi bị đau đầu.", "ĐẦU", "🧠"),
    ("かお", "顔", "kao", "Khuôn mặt", "body", "Bộ phận cơ thể", "朝、顔を 洗います。", "Rửa mặt vào buổi sáng.", "KHUÔN MẶT", "🙂"),
    ("め", "目", "me", "Mắt", "body", "Bộ phận cơ thể", "目が 疲れています。", "Mắt tôi đang bị mỏi.", "MẮT", "👀"),
    ("はな", "鼻", "hana", "Mũi", "body", "Bộ phận cơ thể", "鼻が つまっています。", "Mũi tôi đang bị nghẹt.", "MŨI", "👃"),
    ("くち", "口", "kuchi", "Miệng", "body", "Bộ phận cơ thể", "口を 大きく 開けてください。", "Xin hãy há to miệng ra.", "MIỆNG", "👄"),
    ("は", "歯", "ha", "Răng", "body", "Bộ phận cơ thể", "食後に 歯を みがきます。", "Đánh răng sau bữa ăn.", "RĂNG", "🦷"),
    ("みみ", "耳", "mimi", "Tai", "body", "Bộ phận cơ thể", "耳が 痛いです。", "Tai tôi bị đau.", "TAI", "👂"),
    ("かみ", "髪", "kami", "Tóc", "body", "Bộ phận cơ thể", "髪が 長くなりました。", "Tóc tôi đã dài rồi.", "TÓC", "💇"),
    ("からだ", "体", "karada", "Cơ thể", "body", "Bộ phận cơ thể", "体に 気をつけてください。", "Xin hãy chú ý giữ gìn cơ thể nhé.", "CƠ THỂ", "🏃"),
    ("くび", "首", "kubi", "Cổ", "body", "Bộ phận cơ thể", "首が こっています。", "Cổ tôi bị mỏi cứng.", "CỔ", "🧣"),
    ("かた", "肩", "kata", "Vai", "body", "Bộ phận cơ thể", "肩を まわします。", "Xoay bả vai.", "VAI", "💪"),
    ("むね", "胸", "mune", "Ngực", "body", "Bộ phận cơ thể", "胸が 苦しいです。", "Ngực tôi cảm thấy tức khó thở.", "NGỰC", "🫁"),
    ("おなか", "お腹", "onaka", "Bụng", "body", "Bộ phận cơ thể", "お腹が 痛いです。", "Tôi bị đau bụng.", "BỤNG", "🤰"),
    ("せなか", "背中", "senaka", "Lưng", "body", "Bộ phận cơ thể", "背中が 痛いです。", "Tôi bị đau lưng.", "LƯNG", "🚶"),
    ("こし", "腰", "koshi", "Eo, thắt lưng", "body", "Bộ phận cơ thể", "腰を まげないでください。", "Đừng cúi gập thắt lưng.", "THẮT LƯNG", "🧍"),
    ("て", "手", "te", "Bàn tay", "body", "Bộ phận cơ thể", "手を きれいに 洗います。", "Rửa tay thật sạch.", "BÀN TAY", "✋"),
    ("うで", "腕", "ude", "Cánh tay", "body", "Bộ phận cơ thể", "腕を 上にあげます。", "Giơ cánh tay lên trên.", "CÁNH TAY", "💪"),
    ("ゆび", "指", "yubi", "Ngón tay, ngón chân", "body", "Bộ phận cơ thể", "指を 切ってしまいました。", "Tôi lỡ cắt vào ngón tay mất rồi.", "NGÓN TAY", "☝️"),
    ("あし", "足", "ashi", "Bàn chân, cẳng chân", "body", "Bộ phận cơ thể", "足が つかれました。", "Chân tôi mỏi rã rời.", "BÀN CHÂN", "🦶"),
    ("ちょうし", "調子", "choushi", "Tình trạng sức khỏe", "health", "Sức khỏe & Khám bệnh", "体の 調子は どうですか。", "Tình trạng cơ thể bạn thế nào?", "TÌNH TRẠNG", "🩺"),
    ("たいちょう", "体調", "taichou", "Thể trạng cơ thể", "health", "Sức khỏe & Khám bệnh", "体調を くずしました。", "Tôi bị suy giảm thể trạng.", "THỂ TRẠNG", "🤒"),
    ("～が いたい", "～が痛い", "~ga itai", "Bị đau...", "health", "Sức khỏe & Khám bệnh", "のどが 痛いです。", "Cổ họng tôi bị đau.", "BỊ ĐAU", "😣"),
    ("きもちが いい", "気持ちがいい", "kimochi ga ii", "Tâm trạng thoải mái, sảng khoái", "health", "Sức khỏe & Khám bệnh", "おふろは 気持ちがいいです。", "Ngâm bồn tắm thật sảng khoái.", "SẢNG KHOÁI", "🍃"),
    ("たいちょうが いい", "体調がいい", "taichou ga ii", "Thể trạng sức khỏe tốt", "health", "Sức khỏe & Khám bệnh", "きょうは 体調がいいです。", "Hôm nay thể trạng tôi rất tốt.", "SỨC KHỎE TỐT", "😊"),
    ("たいちょうが わるい", "体調が悪い", "taichou ga warui", "Thể trạng sức khỏe không tốt", "health", "Sức khỏe & Khám bệnh", "体調が悪いので 休みます。", "Vì sức khỏe không tốt nên tôi xin nghỉ.", "SỨC KHỎE XẤU", "😷"),
    ("ねられません", "寝られません", "neraremasen", "Không ngủ được, mất ngủ", "health", "Sức khỏe & Khám bệnh", "ゆうべは ねられませんでした。", "Đêm qua tôi không tài nào chợp mắt được.", "MẤT NGỦ", "🥱"),
    ("つかれます", "疲れます", "tsukaremasu", "Mệt mỏi, kiệt sức", "health", "Sức khỏe & Khám bệnh", "しごとで つかれました。", "Mệt mỏi vì công việc.", "MỆT MỎI", "😫"),
    ("うでを あげます", "腕を上げます", "ude wo agemasu", "Giơ cánh tay lên", "exercise", "Vận động & Thể dục", "息をすいながら 腕を上げます。", "Vừa hít vào vừa giơ tay lên.", "GIƠ TAY", "🙆‍♂️"),
    ("かたを まわします", "肩を回します", "kata wo mawashimasu", "Xoay bả vai", "exercise", "Vận động & Thể dục", "ゆっくり 肩を回してください。", "Hãy xoay bả vai một cách từ từ.", "XOAY VAI", "🔄"),
    ("くびを まげます", "首を曲げます", "kubi wo magemasu", "Nghiêng bẻ cổ", "exercise", "Vận động & Thể dục", "左右に 首を曲げます。", "Nghiêng cổ sang hai bên trái phải.", "BẺ CỔ", "↔️"),
    ("いきを すいます", "息を吸います", "iki wo suimasu", "Hít không khí vào", "exercise", "Vận động & Thể dục", "はなから 息を吸います。", "Hít không khí vào bằng mũi.", "HÍT VÀO", "💨"),
    ("いきを はきます", "息を吐きます", "iki wo hakimasu", "Thở không khí ra", "exercise", "Vận động & Thể dục", "くちから 息を吐きます。", "Thở không khí ra bằng miệng.", "THỞ RA", "🌬️"),
    ("しんこきゅう", "深呼吸", "shinkokyuu", "Hít thở sâu", "exercise", "Vận động & Thể dục", "深呼吸を 3回 します。", "Hít thở sâu 3 lần.", "HÍT THỞ SÂU", "🧘"),
    ("けんこう", "健康", "kenkou", "Sức khỏe lành mạnh", "health", "Sức khỏe & Khám bệnh", "健康の ために 野菜を食べます。", "Ăn rau vì sức khỏe tốt.", "SỨC KHỎE", "🥗"),
    ("たいそう", "体操", "taisou", "Bài tập thể dục", "exercise", "Vận động & Thể dục", "毎朝 ラジオ体操を します。", "Mỗi sáng đều tập bài thể dục theo đài phát thanh.", "TẬP THỂ DỤC", "🤸"),
    ("アドバイス", "アドバイス", "adobaisu", "Lời khuyên y tế/sức khỏe", "advice", "Lời khuyên & Chăm sóc", "医者の アドバイスを 聞きます。", "Lắng nghe lời khuyên của bác sĩ.", "LỜI KHUYÊN", "💡"),
    ("ストレス", "ストレス", "sutoresu", "Căng thẳng, stress", "health", "Sức khỏe & Khám bệnh", "ストレスを たためないでください。", "Đừng để bị tích tụ căng thẳng quá nhé.", "STRESS", "⚡"),
    ("さいきん", "最近", "saikin", "Dạo gần đây", "advice", "Lời khuyên & Chăm sóc", "最近 忙しいです。", "Dạo gần đây tôi khá bận rộn.", "DẠO GẦN ĐÂY", "📅"),
    ("きゅうに", "急に", "kyuuni", "Đột ngột, bất thình lình", "advice", "Lời khuyên & Chăm sóc", "急に 熱が 出ました。", "Tôi đột ngột bị phát sốt.", "ĐỘT NGỘT", "⚡"),
    ("こうやって", "こうやって", "kou yatte", "Làm như thế này", "exercise", "Vận động & Thể dục", "こうやって 肩を おします。", "Bấm vào vai như thế này nè.", "LÀM THẾ NÀY", "👉"),
    ("まず", "先ず", "mazu", "Trước tiên, đầu tiên", "advice", "Lời khuyên & Chăm sóc", "まず 手を 洗いましょう。", "Trước tiên hãy rửa sạch tay nhé.", "TRƯỚC TIÊN", "1️⃣"),
    ("つぎ（に）", "次（に）", "tsugi (ni)", "Tiếp theo sau đó", "advice", "Lời khuyên & Chăm sóc", "次に 深呼吸を します。", "Tiếp theo là hít thở sâu.", "TIẾP THEO", "2️⃣"),
    ("さいご（に）", "最後（に）", "saigo (ni)", "Cuối cùng", "advice", "Lời khuyên & Chăm sóc", "最後に 水を 飲みます。", "Cuối cùng là uống một ngụm nước.", "CUỐI CÙNG", "🏁"),
    ("けんこうだいいち", "健康第一", "kenkou daiichi", "Sức khỏe là số một", "health", "Sức khỏe & Khám bệnh", "何よりも 健康第一ですね。", "Trên tất cả, sức khỏe là số một nhỉ.", "SỨC KHỎE SỐ 1", "🥇"),
    ("Nを おします", "Nを押します", "N wo oshimasu", "Ấn / bấm vào huyệt N", "exercise", "Vận động & Thể dục", "親指で ツボを 押します。", "Dùng ngón tay cái ấn vào huyệt đạo.", "ẤN BẤM", "👆"),
    ("ツボ", "ツボ", "tsubo", "Huyệt đạo cơ thể", "exercise", "Vận động & Thể dục", "肩の ツボを 押すと 楽になります。", "Ấn vào huyệt ở vai sẽ thấy nhẹ nhõm hẳn.", "HUYỆT ĐẠO", "🎯"),
    ("マッサージ", "マッサージ", "massaaji", "Mát-xa thư giãn (Massage)", "exercise", "Vận động & Thể dục", "首の マッサージを します。", "Thực hiện mát-xa phần cổ.", "MÁT XA", "💆"),
    ("リラックス", "リラックス", "rirakkusu", "Thư giãn tinh thần (Relax)", "health", "Sức khỏe & Khám bệnh", "音楽を聞いて リラックスします。", "Nghe nhạc để thư giãn tinh thần.", "THƯ GIÃN", "🎶"),
    ("エレベーター", "エレベーター", "erebeetaa", "Cầu thang máy (Elevator)", "advice", "Lời khuyên & Chăm sóc", "階段を使わず エレベーターに 乗ります。", "Đi thang máy thay vì leo thang bộ.", "THANG MÁY", "🛗"),
    ("ブルーベリー", "ブルーベリー", "buruuberii", "Quả việt quất tốt cho mắt", "health", "Sức khỏe & Khám bệnh", "目にいい ブルーベリーを食べます。", "Ăn quả việt quất rất tốt cho mắt.", "VIỆT QUẤT", "🫐"),
    ("ねむい", "眠い", "nemui", "Buồn ngủ", "health", "Sức khỏe & Khám bệnh", "夜遅いので とても 眠いです。", "Vì khuya rồi nên tôi rất buồn ngủ.", "BUỒN NGỦ", "😴"),
    ("ねつが あります", "熱があります", "netsu ga arimasu", "Bị phát sốt cao", "health", "Sức khỏe & Khám bệnh", "38度の 熱があります。", "Tôi đang bị sốt 38 độ.", "BỊ SỐT", "🌡️"),
    ("かぜ（を ひきます）", "風邪（をひきます）", "kaze (wo hikimasu)", "Bị cảm cúm", "health", "Sức khỏe & Khám bệnh", "風邪をひいて のどが痛いです。", "Bị cảm lạnh nên cổ họng tôi bị đau.", "BỊ CẢM CÚM", "🤧"),
    ("むりを します", "無理をします", "muri wo shimasu", "Làm việc quá sức", "advice", "Lời khuyên & Chăm sóc", "あまり 無理をしないでください。", "Đừng làm việc quá sức nhé.", "QUÁ SỨC", "⚠️"),
    ("どうしたんですか。", "どうしたんですか", "doushitan desu ka", "Bạn bị sao vậy? (hỏi thăm)", "advice", "Lời khuyên & Chăm sóc", "顔色が悪いですね。どうしたんですか。", "Sắc mặt bạn kém quá. Bạn bị sao vậy?", "BẠN SAO THẾ", "❓"),
    ("くすり", "薬", "kusuri", "Thuốc uống", "health", "Sức khỏe & Khám bệnh", "食後に 薬を 飲みます。", "Uống thuốc sau bữa ăn.", "THUỐC", "💊"),
    ("できるだけ", "できるだけ", "dekiru dake", "Càng... càng tốt, trong khả năng", "advice", "Lời khuyên & Chăm sóc", "できるだけ 早く 寝てください。", "Hãy đi ngủ càng sớm càng tốt nhé.", "TRONG KHẢ NĂNG", "⏳")
]

vocab_15 = []
for idx, item in enumerate(raw_15):
    vocab_15.append({
        "id": idx + 1,
        "cat": item[4],
        "catName": item[5],
        "badge": item[3].split(',')[0],
        "jp": item[0],
        "kana": item[0],
        "kanji": item[1],
        "romaji": item[2],
        "vi": item[3],
        "exJp": item[6],
        "exVi": item[7],
        "svg": make_svg(item[8], item[9], "#3b82f6", "#1d4ed8")
    })

# -------------------------------------------------------------
# LESSON 16 (30 items)
# -------------------------------------------------------------
raw_16 = [
    ("ジョギング（を）します", "ジョギングをします", "jogingu (wo) shimasu", "Chạy bộ thể dục (Jogging)", "exercise", "Môn thể thao & Tập luyện", "毎朝 公園で ジョギングをします。", "Mỗi sáng đều chạy bộ ở công viên.", "CHẠY BỘ", "🏃"),
    ("はしります", "走ります", "hashirimasu", "Chạy nhanh", "exercise", "Môn thể thao & Tập luyện", "駅まで 急いで 走りました。", "Chạy vội vã ra ga.", "CHẠY NHANH", "🏃‍♂️"),
    ("ウォーキング（を）します", "ウォーキングをします", "uookingu (wo) shimasu", "Đi bộ rèn luyện sức khỏe", "exercise", "Môn thể thao & Tập luyện", "夜 ウォーキングを しています。", "Buổi tối tôi thường đi bộ thể dục.", "ĐI BỘ", "🚶"),
    ("あるきます", "歩きます", "arukimasu", "Đi bộ bình thường", "exercise", "Môn thể thao & Tập luyện", "毎日 30分 歩きます。", "Mỗi ngày đi bộ 30 phút.", "ĐI BỘ", "🚶‍♂️"),
    ("キロメートル", "キロメートル", "kiromeetoru", "Kilomet (km)", "measure", "Đo lường & Cơ sở vật chất", "毎日 5キロメートル 走ります。", "Mỗi ngày chạy 5 km.", "KILOMET", "📏"),
    ("キログラム", "キログラム", "kiroguramu", "Kilogram (kg)", "measure", "Đo lường & Cơ sở vật chất", "体重が 2キログラム へりました。", "Cân nặng đã giảm được 2 kg.", "KILOGRAM", "⚖️"),
    ("およぎます", "泳ぎます", "oyogimasu", "Bơi dưới nước", "exercise", "Môn thể thao & Tập luyện", "夏は 海で 泳ぎます。", "Mùa hè đi bơi ở biển.", "BƠI", "🏊"),
    ("すいえい（を）します", "水泳をします", "suiei (wo) shimasu", "Môn bơi lội", "exercise", "Môn thể thao & Tập luyện", "週末に 水泳を 習っています。", "Cuối tuần tôi đi học bơi lội.", "BƠI LỘI", "🏊‍♂️"),
    ("プール", "プール", "puuru", "Bể bơi, hồ bơi", "measure", "Đo lường & Cơ sở vật chất", "近くの プールへ 行きます。", "Đi đến bể bơi gần nhà.", "BỂ BƠI", "🏊"),
    ("たいそう（を）します", "体操をします", "taisou (wo) shimasu", "Tập bài thể dục", "exercise", "Môn thể thao & Tập luyện", "運動の前に 体操をします。", "Tập thể dục trước khi vận động.", "TẬP THỂ DỤC", "🤸"),
    ("エアロビクス（を）します", "エアロビクスをします", "earobikusu (wo) shimasu", "Tập aerobic nhịp điệu", "exercise", "Môn thể thao & Tập luyện", "ジムで エアロビクスを します。", "Tập aerobic ở phòng gym.", "AEROBIC", "💃"),
    ("トレーニング（を）します", "トレーニングをします", "toreeningu (wo) shimasu", "Tập thể hình, rèn luyện thể lực", "exercise", "Môn thể thao & Tập luyện", "筋力 トレーニングを します。", "Tập luyện rèn cơ bắp.", "TẬP GYM", "🏋️"),
    ("ジム", "ジム", "jimu", "Phòng tập thể hình gym", "measure", "Đo lường & Cơ sở vật chất", "週に3回 ジムに 通っています。", "Đi tập gym 3 buổi một tuần.", "PHÒNG GYM", "🏋️‍♂️"),
    ("ヨガ（を）します", "ヨガをします", "yoga (wo) shimasu", "Tập yoga thiền định", "exercise", "Môn thể thao & Tập luyện", "朝起きて ヨガを します。", "Thức dậy buổi sáng rồi tập yoga.", "TẬP YOGA", "🧘"),
    ("たばこを すいます", "煙草を吸います", "tabako wo suimasu", "Hút thuốc lá", "health", "Sức khỏe & Thói quen", "たばこを 吸うのを やめました。", "Tôi đã bỏ hẳn hút thuốc lá.", "HÚT THUỐC", "🚭"),
    ("けんこう", "健康", "kenkou", "Sức khỏe tốt", "health", "Sức khỏe & Thói quen", "健康が いちばん 大切です。", "Sức khỏe là điều quý giá nhất.", "SỨC KHỎE", "💪"),
    ("けんこうに いい", "健康にいい", "kenkou ni ii", "Tốt cho sức khỏe", "health", "Sức khỏe & Thói quen", "野菜は 健康にいいです。", "Rau xanh rất tốt cho sức khỏe.", "TỐT SỨC KHỎE", "🥗"),
    ("からだに いい", "体にいい", "karada ni ii", "Tốt cho cơ thể", "health", "Sức khỏe & Thói quen", "お茶は 体にいい 飲み物です。", "Trà là thức uống tốt cho cơ thể.", "TỐT CƠ THỂ", "🍵"),
    ("けんこうに わるい", "健康に悪い", "kenkou ni warui", "Có hại cho sức khỏe", "health", "Sức khỏe & Thói quen", "お酒の 飲みすぎは 健康に悪いです。", "Uống quá nhiều rượu có hại sức khỏe.", "HẠI SỨC KHỎE", "⚠️"),
    ("からだに わるい", "体に悪い", "karada ni warui", "Có hại cho cơ thể", "health", "Sức khỏe & Thói quen", "夜更かしは 体に悪いです。", "Thức khuya rất có hại cho cơ thể.", "HẠI CƠ THỂ", "❌"),
    ("けんこうの ために", "健康のために", "kenkou no tameni", "Vì sức khỏe bản thân", "health", "Sức khỏe & Thói quen", "健康のために 毎日走っています。", "Tôi chạy mỗi ngày vì sức khỏe.", "VÌ SỨC KHỎE", "🏃"),
    ("リラックス（を）します", "リラックスをします", "rirakkusu (wo) shimasu", "Thư giãn, xả stress", "health", "Sức khỏe & Thói quen", "お風呂に入って リラックスします。", "Ngâm bồn tắm để thư giãn.", "THƯ GIÃN", "🛀"),
    ("アンケート", "アンケート", "ankeeto", "Bản khảo sát câu hỏi", "measure", "Đo lường & Cơ sở vật chất", "健康についての アンケートに 答えます。", "Trả lời bản khảo sát về sức khỏe.", "BẢN KHẢO SÁT", "📋"),
    ("けっか", "結果", "kekka", "Kết quả khảo sát/kiểm tra", "measure", "Đo lường & Cơ sở vật chất", "健康診断の 結果が よかったです。", "Kết quả khám sức khỏe định kỳ rất tốt.", "KẾT QUẢ", "📊"),
    ("ストレッチ（を）します", "ストレッチをします", "sutorecchi (wo) shimasu", "Tập giãn cơ, khởi động", "exercise", "Môn thể thao & Tập luyện", "お風呂の後に ストレッチをします。", "Giãn cơ sau khi tắm xong.", "GIÃN CƠ", "🤸‍♀️"),
    ("スポーツクラブ", "スポーツクラブ", "supootsu kurabu", "Câu lạc bộ thể thao", "measure", "Đo lường & Cơ sở vật chất", "スポーツクラブに 入会しました。", "Tôi đã đăng ký câu lạc bộ thể thao.", "CLB THỂ THAO", "🏟️"),
    ("トレーナー", "トレーナー", "toreenaa", "Huấn luyện viên, PT", "measure", "Đo lường & Cơ sở vật chất", "トレーナーに 運動を 教わります。", "Được huấn luyện viên hướng dẫn bài tập.", "HLV THỂ HÌNH", "👨‍🏫"),
    ("はじめて", "初めて", "hajimete", "Lần đầu tiên", "health", "Sức khỏe & Thói quen", "初めて マラソンに 参加しました。", "Lần đầu tiên tôi tham gia chạy marathon.", "LẦN ĐẦU TIÊN", "🌟"),
    ("マシン", "マシン", "mashin", "Máy móc tập luyện gym", "measure", "Đo lường & Cơ sở vật chất", "新しい トレーニングマシンです。", "Đây là máy tập gym đời mới.", "MÁY TẬP", "⚙️"),
    ("ラウンジ", "ラウンジ", "raunji", "Phòng chờ, sảnh nghỉ ngơi", "measure", "Đo lường & Cơ sở vật chất", "運動の後に ラウンジで 休みます。", "Nghỉ ngơi ở sảnh chờ sau khi tập.", "PHÒNG CHỜ", "🛋️")
]

vocab_16 = []
for idx, item in enumerate(raw_16):
    vocab_16.append({
        "id": idx + 1,
        "cat": item[4],
        "catName": item[5],
        "badge": item[3].split(',')[0],
        "jp": item[0],
        "kana": item[0],
        "kanji": item[1],
        "romaji": item[2],
        "vi": item[3],
        "exJp": item[6],
        "exVi": item[7],
        "svg": make_svg(item[8], item[9], "#10b981", "#047857")
    })

# -------------------------------------------------------------
# LESSON 17 (29 items)
# -------------------------------------------------------------
raw_17 = [
    ("おいわい", "お祝い", "oiwai", "Quà chúc mừng, lời chúc", "event", "Sự kiện & Dịp lễ", "結婚の お祝いを あげました。", "Tôi đã tặng quà chúc mừng đám cưới.", "CHÚC MỪNG", "🎉"),
    ("にゅうがく", "入学", "nyuugaku", "Nhập học, vào trường", "event", "Sự kiện & Dịp lễ", "大学の 入学式に 出席しました。", "Tham dự lễ nhập học đại học.", "NHẬP HỌC", "🎓"),
    ("そつぎょう", "卒業", "sotsugyou", "Tốt nghiệp ra trường", "event", "Sự kiện & Dịp lễ", "高校を 卒業しました。", "Tôi đã tốt nghiệp trường cấp ba.", "TỐT NGHIỆP", "📜"),
    ("しゅうしょく", "就職", "shuushoku", "Bắt đầu đi làm, có việc làm", "event", "Sự kiện & Dịp lễ", "会社に 就職が 決まりました。", "Tôi đã xin được việc làm tại công ty.", "ĐI LÀM", "💼"),
    ("しゅっさん", "出産", "shussan", "Sinh em bé", "event", "Sự kiện & Dịp lễ", "出産の お祝いを えらびます。", "Chọn quà chúc mừng bạn sinh em bé.", "SINH CON", "👶"),
    ("あかちゃん", "赤ちゃん", "akachan", "Em bé sơ sinh", "event", "Sự kiện & Dịp lễ", "かわいい 赤ちゃんが 生まれました。", "Một em bé kháu khỉnh vừa chào đời.", "EM BÉ", "👶"),
    ("うまれます", "生まれます", "umaremasu", "Được sinh ra", "event", "Sự kiện & Dịp lễ", "先月 子どもが 生まれました。", "Tháng trước con tôi đã chào đời.", "SINH RA", "🐣"),
    ("けっこん", "結婚", "kekkon", "Kết hôn, cưới hỏi", "event", "Sự kiện & Dịp lễ", "ふたりは 来年 結婚します。", "Hai người họ sẽ kết hôn vào năm tới.", "KẾT HÔN", "💍"),
    ("ははの ひ", "母の日", "haha no hi", "Ngày của Mẹ (CN tuần 2 tháng 5)", "event", "Sự kiện & Dịp lễ", "母の日に カーネーションを 贈ります。", "Tặng hoa cẩm chướng vào Ngày của Mẹ.", "NGÀY CỦA MẸ", "👩"),
    ("ちちの ひ", "父の日", "chichi no hi", "Ngày của Bố (CN tuần 3 tháng 6)", "event", "Sự kiện & Dịp lễ", "父の日に ネクタイを プレゼントします。", "Tặng cà vạt cho bố nhân Ngày của Cha.", "NGÀY CỦA BỐ", "👨"),
    ("クリスマス", "クリスマス", "kurisumasu", "Lễ Giáng sinh (Christmas)", "event", "Sự kiện & Dịp lễ", "クリスマスに ケーキを 食べます。", "Ăn bánh kem vào dịp Giáng sinh.", "GIÁNG SINH", "🎄"),
    ("バレンタイン・デー", "バレンタインデー", "barentain dee", "Ngày lễ tình nhân Valentine", "event", "Sự kiện & Dịp lễ", "バレンタインデーに チョコを あげます。", "Tặng sô-cô-la vào ngày Valentine.", "VALENTINE", "🍫"),
    ("ネックレス", "ネックレス", "nekkuresu", "Vòng cổ, dây chuyền (Necklace)", "gift", "Quà tặng & Đồ dùng", "きれいな ネックレスを もらいました。", "Tôi nhận được sợi dây chuyền rất đẹp.", "VÒNG CỔ", "📿"),
    ("セーター", "セーター", "seetaa", "Áo len ấm mùa đông (Sweater)", "gift", "Quà tặng & Đồ dùng", "あたたかい セーターを 着ています。", "Đang mặc một chiếc áo len ấm áp.", "ÁO LEN", "🧶"),
    ("おもちゃ", "おもちゃ", "omocha", "Đồ chơi trẻ em", "gift", "Quà tặng & Đồ dùng", "子どもに おもちゃを 買いました。", "Mua đồ chơi tặng cho con.", "ĐỒ CHƠI", "🧸"),
    ("あみもの", "編み物", "amimono", "Đồ đan len thủ công", "gift", "Quà tặng & Đồ dùng", "母の 手編みの 編み物です。", "Đây là đồ đan len bằng tay của mẹ tôi.", "ĐỒ ĐAN LEN", "🧶"),
    ("にんぎょう", "人形", "ningyou", "Búp bê trang trí", "gift", "Quà tặng & Đồ dùng", "日本の 伝統的な 人形です。", "Đây là búp bê truyền thống của Nhật Bản.", "BÚP BÊ", "🎎"),
    ("（シャツを）きます", "（シャツを）着ます", "kimasu", "Mặc (áo sơ mi, áo khoác)", "action", "Hành động & Sử dụng", "新しい シャツを 着て 行きます。", "Mặc chiếc áo mới rồi đi dự tiệc.", "MẶC ÁO", "👔"),
    ("へやに かざります", "部屋に飾ります", "heya ni kazarimasu", "Trang trí trong phòng", "action", "Hành động & Sử dụng", "絵を 部屋に 飾ります。", "Treo tranh trang trí trong phòng.", "TRANG TRÍ", "🖼️"),
    ("しごとで つかいます", "仕事で使います", "shigoto de tsukaimasu", "Sử dụng trong công việc", "action", "Hành động & Sử dụng", "このペンは 仕事で 使います。", "Cây bút này tôi sử dụng trong công việc.", "DÙNG ĐI LÀM", "🖋️"),
    ("にあいます", "似合います", "niaimasu", "Rất hợp, vừa vặn phong cách", "action", "Hành động & Sử dụng", "その色の 服が よく 似合いますね。", "Bộ quần áo màu đó rất hợp với bạn đấy.", "RẤT HỢP", "✨"),
    ("あそびます", "遊びます", "asobimasu", "Vui chơi giải trí", "action", "Hành động & Sử dụng", "休みの日は 友だちと 遊びます。", "Ngày nghỉ tôi đi chơi cùng bạn bè.", "VUI CHƠI", "🎮"),
    ("きに いります", "気に入ります", "kini irimasu", "Ưa thích, vừa ý, ưng bụng", "action", "Hành động & Sử dụng", "このプレゼント、とても 気に入りました。", "Món quà này tôi ưng ý vô cùng.", "ƯA THÍCH", "💖"),
    ("～とか～とか", "～とか～とか", "~toka ~toka", "Chẳng hạn như ~ như là ~", "expr", "Cụm từ liên kết", "花とか お菓子とかを 買いました。", "Tôi đã mua chẳng hạn như hoa tươi và bánh kẹo.", "CHẲNG HẠN NHƯ", "🔗"),
    ("めいしいれ", "名刺入れ", "meishiire", "Hộp đựng danh thiếp lịch sự", "gift", "Quà tặng & Đồ dùng", "革の 名刺入れを 贈りました。", "Tôi đã tặng hộp đựng danh thiếp bằng da.", "HỘP DANH THIẾP", "💳"),
    ("ペア", "ペア", "pea", "Đồ đôi, cặp đôi (Pair)", "gift", "Quà tặng & Đồ dùng", "ペアの マグカップを プレゼントします。", "Tặng cặp cốc uống nước đôi.", "CẶP ĐÔI", "☕☕"),
    ("おなじ", "同じ", "onaji", "Giống nhau y hệt", "expr", "Cụm từ liên kết", "彼と 同じ時計を 持っています。", "Tôi đeo đồng hồ giống y hệt anh ấy.", "GIỐNG NHAU", "👥"),
    ("たとえば", "例えば", "tatoeba", "Ví dụ như là...", "expr", "Cụm từ liên kết", "例えば 写真立てなど どうですか。", "Ví dụ như khung ảnh thì bạn thấy sao?", "VÍ DỤ", "💡"),
    ("しゅうかん", "習慣", "shuukan", "Tập quán, phong tục thói quen", "event", "Sự kiện & Dịp lễ", "日本の 贈り物の 習慣を 学びます。", "Học hỏi về phong tục tặng quà của người Nhật.", "PHONG TỤC", "🎎")
]

vocab_17 = []
for idx, item in enumerate(raw_17):
    vocab_17.append({
        "id": idx + 1,
        "cat": item[4],
        "catName": item[5],
        "badge": item[3].split(',')[0],
        "jp": item[0],
        "kana": item[0],
        "kanji": item[1],
        "romaji": item[2],
        "vi": item[3],
        "exJp": item[6],
        "exVi": item[7],
        "svg": make_svg(item[8], item[9], "#ec4899", "#be185d")
    })

# -------------------------------------------------------------
# LESSON 18 (19 items)
# -------------------------------------------------------------
raw_18 = [
    ("けっこん", "結婚", "kekkon", "Kết hôn, lễ cưới", "event", "Sự kiện đời người", "友だちの 結婚式に 参加します。", "Tham dự lễ cưới của bạn thân.", "KẾT HÔN", "💍"),
    ("ひっこし", "引っ越し", "hikkoshi", "Chuyển nhà, dọn nhà mới", "event", "Sự kiện đời người", "来月 新しいアパートに 引っ越しします。", "Tháng sau tôi sẽ chuyển sang căn hộ mới.", "CHUYỂN NHÀ", "📦"),
    ("しゅうしょく", "就職", "shuushoku", "Bắt đầu đi làm, có việc làm", "event", "Sự kiện đời người", "息子の 就職が 決まりました。", "Con trai tôi đã nhận được việc làm ổn định.", "ĐI LÀM", "💼"),
    ("しゅっさん", "出産", "shussan", "Sinh con, chào đón thành viên mới", "event", "Sự kiện đời người", "出産の お祝いを 届けます。", "Gửi quà chúc mừng bạn sinh em bé.", "SINH CON", "👶"),
    ("よろこびます", "喜びます", "yorokobimasu", "Vui mừng, phấn khởi vô cùng", "feeling", "Cảm xúc & Tâm trạng", "プレゼントを とても 喜んでくれました。", "Bạn ấy đã vô cùng vui mừng khi nhận món quà.", "VUI MỪNG", "🥳"),
    ("しあわせ（な）", "幸せ（な）", "shiawase(na)", "Hạnh phúc ngập tràn", "feeling", "Cảm xúc & Tâm trạng", "いつまでも お幸せに！", "Chúc hai bạn mãi mãi hạnh phúc bên nhau nhé!", "HẠNH PHÚC", "🥰"),
    ("ひつよう（な）", "必要（な）", "hitsuyou(na)", "Cần thiết, thiết yếu", "necessity", "Nhu cầu & Đồ dùng", "パスポートが 必要です。", "Hộ chiếu là giấy tờ cần thiết.", "CẦN THIẾT", "❗"),
    ("N が ひつようです", "Nが必要です", "N ga hitsuyou desu", "Cần có N cho cuộc sống", "necessity", "Nhu cầu & Đồ dùng", "新しい 生活に 家具が 必要です。", "Cuộc sống mới cần có đồ nội thất.", "CẦN CÓ N", "🛋️"),
    ("あかちゃんの ものが ひつようです", "赤ちゃんの物が必要です", "akachan no mono ga hitsuyou desu", "Đồ dùng của em bé là rất cần thiết", "necessity", "Nhu cầu & Đồ dùng", "出産祝には 赤ちゃんの物が 必要です。", "Quà mừng sinh em bé thì các đồ dùng trẻ sơ sinh là rất cần thiết.", "ĐỒ EM BÉ CẦN", "🍼"),
    ("カードを かきます", "カードを書きます", "kaado wo kakimasu", "Viết thiệp chúc mừng", "gift", "Quà tặng & Lễ nghi", "お祝いの メッセージカードを 書きます。", "Viết thiệp gửi gắm thông điệp chúc phúc.", "VIẾT THIỆP", "💌"),
    ("おれい", "お礼", "orei", "Lời cảm ơn, quà đáp lễ", "gift", "Quà tặng & Lễ nghi", "お世話になった方に お礼を します。", "Tặng quà đáp lễ người đã giúp đỡ mình.", "LỜI CẢM ƠN", "🙇‍♂️"),
    ("おれいを いいます", "お礼を言います", "orei wo iimasu", "Nói lời cảm ơn chân thành", "gift", "Quà tặng & Lễ nghi", "先生に 直接 お礼を 言いました。", "Tôi đã trực tiếp nói lời cảm ơn tới thầy giáo.", "NÓI CẢM ƠN", "🗣️"),
    ("しゃしんたて", "写真立て", "shashintate", "Khung ảnh kỷ niệm", "gift", "Quà tặng & Lễ nghi", "結婚祝いに 写真立てを あげます。", "Tặng khung ảnh làm quà mừng cưới.", "KHUNG ẢNH", "🖼️"),
    ("かびん", "花瓶", "kabin", "Bình hoa, lọ hoa", "gift", "Quà tặng & Lễ nghi", "きれいな 花瓶に 花を かざります。", "Cắm hoa tươi vào chiếc bình hoa tuyệt đẹp.", "BÌNH HOA", "🏺"),
    ("ゆびわ", "指輪", "yubiwa", "Nhẫn đeo tay (nhẫn cưới)", "gift", "Quà tặng & Lễ nghi", "結婚指輪を 買いました。", "Chúng tôi đã mua nhẫn cưới.", "NHẪN ĐEO TAY", "💍"),
    ("きっと", "きっと", "kitto", "Chắc chắn là, nhất định là", "feeling", "Cảm xúc & Tâm trạng", "きっと 喜んでくれると 思います。", "Tôi tin chắc chắn bạn ấy sẽ rất thích.", "CHẮC CHẮN", "🌟"),
    ("スーツ", "スーツ", "suutsu", "Bộ âu phục, com-lê vest", "gift", "Quà tặng & Lễ nghi", "パーティーに 新しいスーツを 着て行きます。", "Mặc bộ com-lê mới đi dự tiệc.", "ÂU PHỤC", "🤵"),
    ("たいせつ（な）", "大切（な）", "taisetsu(na)", "Quan trọng, quý giá, trân quý", "feeling", "Cảm xúc & Tâm trạng", "友だちは 私の 大切な 宝物です。", "Bạn bè là báu vật vô cùng quý giá của tôi.", "QUÝ GIÁ", "💎"),
    ("たいせつに します", "大切にします", "taisetsu ni shimasu", "Trân trọng, giữ gìn cẩn thận", "feeling", "Cảm xúc & Tâm trạng", "いただいた プレゼントを 大切にします。", "Tôi sẽ trân trọng và giữ gìn cẩn thận món quà này.", "TRÂN TRỌNG", "🤲")
]

vocab_18 = []
for idx, item in enumerate(raw_18):
    vocab_18.append({
        "id": idx + 1,
        "cat": item[4],
        "catName": item[5],
        "badge": item[3].split(',')[0],
        "jp": item[0],
        "kana": item[0],
        "kanji": item[1],
        "romaji": item[2],
        "vi": item[3],
        "exJp": item[6],
        "exVi": item[7],
        "svg": make_svg(item[8], item[9], "#8b5cf6", "#6d28d9")
    })

print("All vocab arrays prepared:")
print(f"L11: {len(vocab_11)}, L12: {len(vocab_12)}, L13: {len(vocab_13)}, L14: {len(vocab_14)}, L15: {len(vocab_15)}, L16: {len(vocab_16)}, L17: {len(vocab_17)}, L18: {len(vocab_18)}")
