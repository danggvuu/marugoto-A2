/* Extracted page script for tests/On_Tap_Mini_Test_A2_5_8.html */
// ==========================================
// DỮ LIỆU GỐC TRÍCH XUẤT TỪ MINATO JF
// ==========================================
const minatoParticles = [
    { p: "か", ex: "かぞくは 何人ですか。", st: "Sか。", l: "L1", note: "Câu hỏi nghi vấn" },
    { p: "か", ex: "火よう日か木よう日は どうですか。", st: "N1かN2", l: "L9", note: "Lựa chọn hoặc/hay" },
    { p: "が", ex: "冬が好きです。", st: "N／イA‐いの／ナA‐なのが好きです。", l: "L3", note: "Đối tượng của tính từ yêu thích" },
    { p: "が", ex: "スキーができます。", st: "Nができます。", l: "L3", note: "Khả năng, có thể làm gì" },
    { p: "が", ex: "花がたくさん さきます。", st: "NがVます。", l: "L4", note: "Hiện tượng tự nhiên khách quan" },
    { p: "が", ex: "外は 強い 風が ふいています。", st: "NがVます。", l: "L4", note: "Gió thổi (Hiện tượng tự nhiên)" },
    { p: "が", ex: "この ホテルは 古いですが、きれいです。", st: "S1が、S2。", l: "L13", note: "Liên từ nối tương phản 'nhưng'" },
    { p: "が", ex: "すみません、JFビルに 行きたいんですが。", st: "～んですが", l: "L6", note: "Mào đầu câu chuyện nhờ vả/hỏi đường" },
    { p: "が", ex: "スペイン語は、たんごがかんたんです。", st: "N1は N2がイA／ナA です。", l: "L9", note: "Vị ngữ chỉ bộ phận / đặc điểm" },
    { p: "から", ex: "らいねんから びょういんで はたらきます。", st: "Nから", l: "L1", note: "Mốc thời gian bắt đầu (từ...)" },
    { p: "から", ex: "うちから かいしゃまで どうやって 行きますか。", st: "N1から N2まで", l: "L1", note: "Từ địa điểm A đến địa điểm B" },
    { p: "から", ex: "さとうさんは ジョイさんから 花を もらいます。", st: "Nから もらいます", l: "L17", note: "Nhận từ ai đó" },
    { p: "から", ex: "夏休みが ありますから、夏が いちばん 好きです。", st: "S1から、S2。", l: "L3", note: "Chỉ lý do, nguyên nhân (vì... nên...)" },
    { p: "ぐらい", ex: "でんしゃで 30分ぐらいです。", st: "Số lượng + ぐらい", l: "L1", note: "Khoảng chừng (thời gian/số lượng)" },
    { p: "ぐらい", ex: "年に 3回ぐらい マレーシアへ 行きます。", st: "Khoảng thời gian + ぐらい", l: "L10", note: "Mức độ tần suất (khoảng ~ lần)" },
    { p: "けど", ex: "この ゆうえんちは たのしいけど、とおいです。", st: "Nだけど／イA‐いけど／ナA‐だけど", l: "L5", note: "Liên từ nhưng (văn nói tự nhiên thân mật)" },
    { p: "で", ex: "東京で 日本語を べんきょうしています。", st: "Địa điểm + で + V", l: "L1", note: "Nơi diễn ra hành động cụ thể" },
    { p: "で", ex: "でんしゃで 行きます。", st: "Phương tiện + で", l: "L1", note: "Phương tiện đi lại / công cụ" },
    { p: "で", ex: "中国人の ともだちと 何語で 話しますか。", st: "Ngôn ngữ + で", l: "L2", note: "Phương tiện ngôn ngữ giao tiếp" },
    { p: "で", ex: "じゅうたいで おくれます。", st: "Nguyên nhân + で", l: "L7", note: "Nguyên nhân khách quan (tắc đường...)" },
    { p: "で", ex: "結婚の お祝いに 2人で 使う ものを あげます。", st: "Số người + で", l: "L17", note: "Phạm vi số lượng người thực hiện" },
    { p: "でも", ex: "６時半でも いいですか。", st: "Nでも いいですか", l: "L7", note: "Đưa ra gợi ý / dù là... cũng được chứ" },
    { p: "と", ex: "かぞくは 父と 母と 私です。", st: "N1 と N2", l: "L1", note: "Liệt kê toàn bộ (và/với)" },
    { p: "と", ex: "中国人の ともだちと 話します。", st: "Người + と", l: "L2", note: "Cùng làm gì với ai đó" },
    { p: "と", ex: "ドイツ語は 日本語と ちがいます。", st: "N1は N2と ちがいます", l: "L9", note: "So sánh khác với cái gì" },
    { p: "と", ex: "誕生日の お祝いは パーティーが いいと思います。", st: "～と 思います", l: "L18", note: "Trợ từ trích dẫn ý nghĩ / quan điểm" },
    { p: "と", ex: "夜 ねる 前に、おふろに 入ると いいですよ。", st: "V‐ると いいです", l: "L15", note: "Quy luật / Lời khuyên hễ... thì tốt" },
    { p: "など", ex: "この あたりに 高い ビルや ホテルなどが あります。", st: "N1や N2など", l: "L5", note: "Liệt kê không đầy đủ (vân vân...)" },
    { p: "や", ex: "この あたりは ゆうえんちや こうえんが あります。", st: "N1 や N2", l: "L5", note: "Liệt kê tiêu biểu đại diện" },
    { p: "に", ex: "東京に すんでいます。", st: "Địa điểm + に すんでいます", l: "L1", note: "Nơi cư trú, tồn tại cố định" },
    { p: "に", ex: "まいにち １０時に かいしゃに 行きます。", st: "Thời gian + に / Điểm đến + に", l: "L1", note: "Thời điểm xác định / Đích đến di chuyển" },
    { p: "に", ex: "春に なります。", st: "Nに / ナA‐に なります", l: "L3", note: "Biến đổi trạng thái (trở thành, sang)" },
    { p: "に", ex: "しんごうを みぎに まがってください。", st: "Hướng + に まがります", l: "L6", note: "Hướng rẽ / chuyển hướng" },
    { p: "に", ex: "ともだちに えいごを おしえています。", st: "Đối tượng + に", l: "L1", note: "Đối tượng tiếp nhận hành động" },
    { p: "に", ex: "ともだちと カラオケに 行きます。", st: "N / V-(bỏ masu) + に 行きます", l: "L8", note: "Mục đích của việc đi / đến" },
    { p: "に", ex: "週に １回 フラメンコを ならっています。", st: "Khoảng thời gian + に ～回", l: "L10", note: "Tần suất trong một khoảng thời gian" },
    { p: "ね", ex: "きのうは すごい 雨でしたね。", st: "Sね。", l: "L4", note: "Đồng tình / Tìm kiếm sự đồng cảm" },
    { p: "の", ex: "私の かぞく / でんしゃの かいしゃ", st: "N1の N2", l: "L1", note: "Sở hữu / Thuộc tính bổ nghĩa" },
    { p: "の", ex: "あついのが にがてです。", st: "Tính từ + の", l: "L3", note: "Danh từ hóa tính từ (cái nóng...)" },
    { p: "の", ex: "スペイン語は 読むのが ちょっと むずかしいです。", st: "V-る + のが Tính từ", l: "L9", note: "Danh từ hóa hành động (việc đọc...)" },
    { p: "は", ex: "私は ジョイ・カーターです。", st: "Nは", l: "L1", note: "Chủ đề chính của câu nói" },
    { p: "は", ex: "しごとは していません。", st: "Tân ngữ + は + Phủ định", l: "L1", note: "Đưa lên nhấn mạnh phủ định" },
    { p: "まで", ex: "うちから かいしゃまで", st: "Nまで", l: "L1", note: "Giới hạn điểm đến / thời gian kết thúc" },
    { p: "も", ex: "おじいちゃんも いっしょに 行きます。", st: "Nも", l: "L1", note: "Đồng nhất (cũng...)" },
    { p: "よ", ex: "らいしゅう、広島に 行きますよ。", st: "Sよ。", l: "L1", note: "Cung cấp thông tin mới cho người nghe" },
    { p: "を", ex: "日本語を べんきょうしています。", st: "Nを Vます", l: "L1", note: "Tân ngữ trực tiếp của ngoại động từ" },
    { p: "を", ex: "この とおりを まっすぐ 行きます。", st: "Đoạn đường + を 行きます", l: "L6", note: "Không gian đi qua / di chuyển xuyên qua" },
    { p: "を", ex: "ふじみえきで でんしゃを おります。", st: "Phương tiện + を おります", l: "L6", note: "Rời khỏi / bước xuống phương tiện" },
    { p: "（の）ために", ex: "けんこうの ために うんどうを しましょう。", st: "Nのために", l: "L15", note: "Vì mục đích / cho lợi ích của..." },
    { p: "について", ex: "らいしゅうの ピクニックに ついて れんらくします。", st: "Nについて", l: "L11", note: "Về chủ đề / nội dung gì đó" }
];

const minatoAdjectives = [
    { jp: "あつい (Nóng)", plain: "あついです", neg: "あつくないです", connect: "あつくて", connectNeg: "あつくなくて", contrast: "あつい けど (L5)", become: "あつく なります (L3)" },
    { jp: "おいしい (Ngon)", plain: "おいしいです", neg: "おいしくないです", connect: "おいしくて", connectNeg: "おいしくなくて", contrast: "おいしい けど (L5)", become: "おいしく なります" },
    { jp: "いたい (Đau)", plain: "いたいです", neg: "いたくないです", connect: "いたくて", connectNeg: "いたくなくて", contrast: "いたい けど", become: "いたく なります" },
    { jp: "いい / よい (Tốt)", plain: "いいです", neg: "よくないです", connect: "よくて", connectNeg: "よくなくて", contrast: "いい けど (L5)", become: "よく なります" },
    { jp: "すき (Thích)", plain: "すきです", neg: "すきじゃないです", connect: "すきで", connectNeg: "すきじゃなくて", contrast: "すき だけど (L5)", become: "すきに なります" },
    { jp: "きれい (Đẹp/Sạch)", plain: "きれいです", neg: "きれいじゃないです", connect: "きれいで", connectNeg: "きれいじゃなくて", contrast: "きれい だけど (L5)", become: "きれいに なります (L3)" },
    { jp: "べんり (Tiện lợi)", plain: "べんりです", neg: "べんりじゃないです", connect: "べんりで", connectNeg: "べんりじゃなくて", contrast: "べんり だけど (L5)", become: "べんりに なります" },
    { jp: "しずか (Yên tĩnh)", plain: "しずかです", neg: "しずかじゃないです", connect: "しずかで", connectNeg: "しずかじゃなくて", contrast: "しずか だけど (L5)", become: "しずかに なります" },
    { jp: "あめ (Mưa - N)", plain: "あめです", neg: "あめじゃないです", connect: "あめで", connectNeg: "あめじゃなくて", contrast: "あめ だけど (L5)", become: "あめに なります" },
    { jp: "こども (Trẻ em - N)", plain: "こどもです", neg: "こどもじゃないです", connect: "こどもで", connectNeg: "こどもじゃなくて", contrast: "こども だけど (L5)", become: "こどもに なります" }
];

const minatoKanjiTopics = [
    { topic: "Topic 1: 私と家族 (Bài 1 - 2)", l1: "私 父 母 子 男 女 人 何", l2: "国 外 語 日 本 英 中 人 好 読 書 何", desc: "Bản thân, gia đình, ngôn ngữ và quốc tịch" },
    { topic: "Topic 2: 季節と天気 (Bài 3 - 4)", l1: "春 夏 秋 冬 今 花 海 山 川", l2: "今 日 天 気 晴 雨 雪 雲 風 空", desc: "Bốn mùa, thiên nhiên và hiện tượng thời tiết khí tượng" },
    { topic: "Topic 3: わたしの町 (Bài 5 - 6)", l1: "町 店 人 気 多 少 高 安 広", l2: "道 通 右 左 一 二 赤 青 黒 白", desc: "Phố xá, cửa hàng, chỉ đường và màu sắc" },
    { topic: "Topic 4: 出かける (Bài 7 - 8)", l1: "時 間 場 所 駅 日 出 待 止", l2: "食 事 仕 前 後 朝 昼 夜 乗", desc: "Thời gian, địa điểm, ga tàu và ăn uống" },
    { topic: "Topic 5: 日本語と文化 (Bài 9 - 10)", l1: "学 校 小 中 高 大 先 生 年 勉 強", l2: "文 化 音 楽 旅 行 留 学 友 週 回", desc: "Trường học, văn hóa, âm nhạc và du học" },
    { topic: "Topic 6: 外食 (Bài 11 - 12)", l1: "食 物 飲 茶 酒 作 持 願", l2: "料 理 味 色 野 菜 少 中 入", desc: "Đồ ăn, thức uống, gọi món và hương vị" },
    { topic: "Topic 7: 出張 (Bài 13 - 14)", l1: "会 社 本 支 出 張 空 港 発 到 着 午 前 後", l2: "自 分 電 話 気 車 送 使 借", desc: "Công ty, công tác, sân bay và phương tiện" },
    { topic: "Topic 8: 健康 (Bài 15 - 16)", l1: "体 頭 目 口 耳 手 足 上 下", l2: "毎 朝 日 週 末 元 気 外 起 歩 走 泳", desc: "Bộ phận cơ thể, sức khỏe và thể dục thể thao" },
    { topic: "Topic 9: お祝い (Bài 17 - 18)", l1: "祝 誕 生 日 結 婚 絵 写 真 時 計 着", l2: "先 週 今 月 来 年 去 家 思", desc: "Chúc mừng, sinh nhật, kết hôn và quà tặng" }
];

function renderMinatoData() {
    // Render Particles
    filterParticlesTable();

    // Render Adjectives
    const adjBody = document.getElementById('adjectivesTableBody');
    if (adjBody) {
        adjBody.innerHTML = minatoAdjectives.map(item => `
            <tr style="border-bottom: 1px solid #f1f5f9;">
                <td style="padding: 10px 14px; font-weight: 700; color: #1e293b;">${item.jp}</td>
                <td style="padding: 10px 14px;">${item.plain}</td>
                <td style="padding: 10px 14px;">${item.neg}</td>
                <td style="padding: 10px 14px; font-weight: 700; color: #854d0e; background: #fefce8;">${item.connect}</td>
                <td style="padding: 10px 14px; color: #dc2626;">${item.connectNeg}</td>
                <td style="padding: 10px 14px; font-weight: 700; color: #3730a3; background: #eef2ff;">${item.contrast}</td>
                <td style="padding: 10px 14px; color: #047857;">${item.become}</td>
            </tr>
        `).join('');
    }

    // Render Kanji Topics
    const kanjiBox = document.getElementById('kanjiTopicsContainer');
    if (kanjiBox) {
        kanjiBox.innerHTML = minatoKanjiTopics.map(t => `
            <div style="background: #f8fafc; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 18px;">
                <div style="font-weight: 800; color: var(--primary); font-size: 1.02rem; margin-bottom: 4px;">${t.topic}</div>
                <div style="font-size: 0.82rem; color: var(--gray-500); margin-bottom: 12px;">${t.desc}</div>
                <div style="background: white; border: 1px solid #cbd5e1; border-radius: 8px; padding: 10px 12px; margin-bottom: 8px;">
                    <span style="font-size: 0.78rem; font-weight: 700; color: #64748b;">BÀI LẺ:</span>
                    <div style="font-size: 1.25rem; font-weight: 800; color: #0f172a; letter-spacing: 4px; margin-top: 2px;">${t.l1}</div>
                </div>
                <div style="background: white; border: 1px solid #cbd5e1; border-radius: 8px; padding: 10px 12px;">
                    <span style="font-size: 0.78rem; font-weight: 700; color: #64748b;">BÀI CHẴN:</span>
                    <div style="font-size: 1.25rem; font-weight: 800; color: #0f172a; letter-spacing: 4px; margin-top: 2px;">${t.l2}</div>
                </div>
            </div>
        `).join('');
    }
}

function filterParticlesTable() {
    const query = (document.getElementById('particleSearchInput')?.value || '').trim().toLowerCase();
    const tbody = document.getElementById('particlesTableBody');
    if (!tbody) return;

    const filtered = minatoParticles.filter(item => {
        if (!query) return true;
        return item.p.toLowerCase().includes(query) ||
               item.ex.toLowerCase().includes(query) ||
               item.st.toLowerCase().includes(query) ||
               item.note.toLowerCase().includes(query) ||
               item.l.toLowerCase().includes(query);
    });

    if (filtered.length === 0) {
        tbody.innerHTML = '<tr><td colspan="5" style="text-align: center; padding: 25px; color: var(--gray-500);">Không tìm thấy trợ từ phù hợp.</td></tr>';
        return;
    }

    tbody.innerHTML = filtered.map(item => `
        <tr style="border-bottom: 1px solid #f1f5f9; transition: background 0.15s;" onmouseover="this.style.background='#f8fafc'" onmouseout="this.style.background='transparent'">
            <td style="padding: 10px 14px; font-weight: 800; color: var(--primary); font-size: 1.05rem;">${item.p}</td>
            <td style="padding: 10px 14px; font-family: inherit;" class="jp-text">${item.ex}</td>
            <td style="padding: 10px 14px; color: #475569; font-weight: 600; font-size: 0.88rem;"><code>${item.st}</code></td>
            <td style="padding: 10px 14px; color: #334155; font-size: 0.88rem;">${item.note}</td>
            <td style="padding: 10px 14px; text-align: center;"><span style="background: #e2e8f0; color: #334155; padding: 2px 8px; border-radius: 6px; font-weight: 700; font-size: 0.8rem;">${item.l}</span></td>
        </tr>
    `).join('');
}

// Dữ liệu nhúng trực tiếp
const rawVocab = [{"l": "A2-5", "jp": "ばしょ", "vi": "Địa điểm"}, {"l": "A2-5", "jp": "ところ", "vi": "Nơi"}, {"l": "A2-5", "jp": "このあたり", "vi": "Khu vực này"}, {"l": "A2-5", "jp": "どうぶつえん", "vi": "Sở thú"}, {"l": "A2-5", "jp": "ゆうえんち", "vi": "Công viên giải trí"}, {"l": "A2-5", "jp": "でんきてん", "vi": "Cửa hàng đồ điện"}, {"l": "A2-5", "jp": "こうきょ", "vi": "Hoàng cung"}, {"l": "A2-5", "jp": "いざかや", "vi": "Quán nhậu"}, {"l": "A2-5", "jp": "うおいちば", "vi": "Chợ cá"}, {"l": "A2-5", "jp": "ゲームセンター", "vi": "Game center"}, {"l": "A2-5", "jp": "ちず", "vi": "Bản đồ"}, {"l": "A2-5", "jp": "ひろい", "vi": "Rộng"}, {"l": "A2-5", "jp": "せまい", "vi": "Hẹp, chật"}, {"l": "A2-5", "jp": "ちかい", "vi": "Gần"}, {"l": "A2-5", "jp": "とおい", "vi": "Xa"}, {"l": "A2-5", "jp": "べんり", "vi": "Tiện lợi"}, {"l": "A2-5", "jp": "ふべん", "vi": "Bất tiện"}, {"l": "A2-5", "jp": "はやい", "vi": "Nhanh, sớm"}, {"l": "A2-5", "jp": "おそい", "vi": "Chậm, muộn"}, {"l": "A2-5", "jp": "あかるい", "vi": "Sáng sủa"}, {"l": "A2-5", "jp": "くらい", "vi": "Tối tăm"}, {"l": "A2-5", "jp": "おおい", "vi": "Nhiều"}, {"l": "A2-5", "jp": "すくない", "vi": "Ít"}, {"l": "A2-5", "jp": "あぶない", "vi": "Nguy hiểm"}, {"l": "A2-5", "jp": "おとな", "vi": "Người lớn, trưởng thành"}, {"l": "A2-5", "jp": "わかいひと", "vi": "Người trẻ"}, {"l": "A2-5", "jp": "にんきがあります", "vi": "Được yêu thích, ưa chuộng"}, {"l": "A2-5", "jp": "おすすめ", "vi": "Đề xuất, gợi ý"}, {"l": "A2-5", "jp": "ジョギング", "vi": "Chạy bộ"}, {"l": "A2-5", "jp": "ぜひ", "vi": "Nhất định"}, {"l": "A2-5", "jp": "ぜひてください", "vi": "Nhất định hãy..."}, {"l": "A2-6", "jp": "たてもの", "vi": "Tòa nhà, kiến trúc"}, {"l": "A2-6", "jp": "ビル", "vi": "Tòa nhà"}, {"l": "A2-6", "jp": "ゆうびんきょく", "vi": "Bưu điện"}, {"l": "A2-6", "jp": "たいしかん", "vi": "Đại sứ quán"}, {"l": "A2-6", "jp": "びじゅつかん", "vi": "Bảo tàng mỹ thuật"}, {"l": "A2-6", "jp": "はくぶつかん", "vi": "Bảo tàng"}, {"l": "A2-6", "jp": "みち", "vi": "Con đường"}, {"l": "A2-6", "jp": "とおり", "vi": "Con đường, phố"}, {"l": "A2-6", "jp": "はし", "vi": "Cây cầu"}, {"l": "A2-6", "jp": "こうさてん", "vi": "Ngã tư"}, {"l": "A2-6", "jp": "かど", "vi": "Góc"}, {"l": "A2-6", "jp": "しんごう", "vi": "Đèn giao thông"}, {"l": "A2-6", "jp": "ひとつめのn", "vi": "N thứ nhất"}, {"l": "A2-6", "jp": "ふたつめのn", "vi": "N thứ hai"}, {"l": "A2-6", "jp": "みぎ", "vi": "Bên phải"}, {"l": "A2-6", "jp": "ひだり", "vi": "Bên trái"}, {"l": "A2-6", "jp": "まっすぐ", "vi": "Thẳng"}, {"l": "A2-6", "jp": "はしをわたります", "vi": "Đi qua, băng qua (cầu)"}, {"l": "A2-6", "jp": "まがります", "vi": "Rẽ"}, {"l": "A2-6", "jp": "こうさてんをまがります", "vi": "Rẽ phải/trái tại ngã tư"}, {"l": "A2-6", "jp": "nがみえます", "vi": "Có thể nhìn thấy..."}, {"l": "A2-6", "jp": "nがきこえます", "vi": "Có thể nghe thấy..."}, {"l": "A2-6", "jp": "たかい", "vi": "Cao"}, {"l": "A2-6", "jp": "ひくい", "vi": "Thấp"}, {"l": "A2-6", "jp": "まるい", "vi": "Tròn"}, {"l": "A2-6", "jp": "しろい", "vi": "Trắng"}, {"l": "A2-6", "jp": "くろい", "vi": "Đen"}, {"l": "A2-6", "jp": "あかい", "vi": "Đỏ"}, {"l": "A2-6", "jp": "あおい", "vi": "Xanh dương"}, {"l": "A2-6", "jp": "ほそながい", "vi": "Thon dài, dài và hẹp"}, {"l": "A2-7", "jp": "じかんにおくれます", "vi": "Muộn (giờ)"}, {"l": "A2-7", "jp": "バスをまちます", "vi": "Đợi, chờ (xe bus)"}, {"l": "A2-7", "jp": "じかんをまちがえます", "vi": "Nhầm, nhầm lẫn (giờ)"}, {"l": "A2-7", "jp": "でんしゃがとまります", "vi": "Tàu điện dừng lại, dừng chạy"}, {"l": "A2-7", "jp": "みちにまよいます", "vi": "Lạc đường"}, {"l": "A2-7", "jp": "かぞくとでかけます", "vi": "Ra ngoài (với gia đình)"}, {"l": "A2-7", "jp": "くるまにきをつけます", "vi": "Chú ý, cẩn thận (ô tô)"}, {"l": "A2-7", "jp": "ともだちにれんらくします", "vi": "Liên lạc (với bạn bè)"}, {"l": "A2-7", "jp": "くうこうにつきます", "vi": "Đến nơi (sân bay)"}, {"l": "A2-7", "jp": "まちあわせ", "vi": "Cuộc hẹn"}, {"l": "A2-7", "jp": "まちあわせをします", "vi": "Hẹn gặp"}, {"l": "A2-7", "jp": "じゅうたい", "vi": "Tắc đường"}, {"l": "A2-7", "jp": "じこ", "vi": "Tai nạn, sự cố"}, {"l": "A2-7", "jp": "ロビー", "vi": "Sảnh chờ (Lobby)"}, {"l": "A2-7", "jp": "いりぐち", "vi": "Lối vào, cửa vào"}, {"l": "A2-7", "jp": "ほんや", "vi": "Tiệm sách"}, {"l": "A2-7", "jp": "ちこくします", "vi": "Muộn (chỉ dùng cho người)"}, {"l": "A2-7", "jp": "はやくv", "vi": "Làm V nhanh, sớm"}, {"l": "A2-7", "jp": "たのしみ", "vi": "Mong chờ, mong đợi"}, {"l": "A2-7", "jp": "りゆう", "vi": "Lý do"}, {"l": "A2-8", "jp": "すいぞくかん", "vi": "Thủy cung"}, {"l": "A2-8", "jp": "やたい", "vi": "Quầy bán hàng lưu động"}, {"l": "A2-8", "jp": "タワー", "vi": "Tháp"}, {"l": "A2-8", "jp": "すいじょうバス", "vi": "Thuyền bus"}, {"l": "A2-8", "jp": "れきし", "vi": "Lịch sử"}, {"l": "A2-8", "jp": "どうぶつ", "vi": "Động vật"}, {"l": "A2-8", "jp": "やけい", "vi": "Cảnh đêm"}, {"l": "A2-8", "jp": "かんこう", "vi": "Tham quan"}, {"l": "A2-8", "jp": "かんこうち", "vi": "Địa điểm tham quan"}, {"l": "A2-8", "jp": "せかい", "vi": "Thế giới"}, {"l": "A2-8", "jp": "せかいいち", "vi": "Số một thế giới"}, {"l": "A2-8", "jp": "りょうがえ", "vi": "Đổi ngoại tệ"}, {"l": "A2-8", "jp": "おすすめ", "vi": "Đề xuất, gợi ý"}, {"l": "A2-8", "jp": "ライトアップ", "vi": "Lên đèn, chiếu sáng"}, {"l": "A2-8", "jp": "めずらしい", "vi": "Hiếm"}, {"l": "A2-8", "jp": "ちず", "vi": "Bản đồ"}, {"l": "A2-8", "jp": "てんぷら", "vi": "Món Tempura"}, {"l": "A2-8", "jp": "ふね", "vi": "Thuyền, tàu"}, {"l": "A2-8", "jp": "まだ", "vi": "Vẫn chưa..."}, {"l": "A2-8", "jp": "もうvました", "vi": "Đã làm V"}, {"l": "A2-8", "jp": "よてい", "vi": "Dự định"}, {"l": "A2-8", "jp": "イルカ", "vi": "Cá heo"}, {"l": "A2-8", "jp": "カラオケ", "vi": "Karaoke"}, {"l": "A2-8", "jp": "ショー", "vi": "Show, biểu diễn"}, {"l": "A2-8", "jp": "スカイツリー", "vi": "Tháp Skytree"}, {"l": "A2-8", "jp": "こんばん", "vi": "Tối nay"}, {"l": "A2-8", "jp": "おみやげ", "vi": "Quà lưu niệm"}, {"l": "A2-8", "jp": "しょくじのまえ", "vi": "Trước (bữa ăn)"}, {"l": "A2-8", "jp": "しょくじのあと", "vi": "Sau (bữa ăn)"}, {"l": "A2-8", "jp": "あとで", "vi": "Xíu nữa, sau đó..."}];
const rawKanji = [{"char": "町", "hv": "Đinh", "lesson": "L5", "lessonName": "Bài 5", "strokes": 7, "meaning": "Thị trấn, khu phố", "kun": "まち", "on": "ちょう", "examples": [{"word": "町", "reading": "まち", "vi": "Thị trấn, thành phố"}], "formula": "田 (Ruộng) ＋ 丁 (Đường)", "strokeGuide": "Trái trước phải sau: Bộ Điền (田 - 5 nét) bên trái ➔ chữ Đinh (丁 - 2 nét) bên phải.", "mnemonic": "Ruộng đồng (田) giao với con đường (丁) tạo nên thị trấn."}, {"char": "店", "hv": "Điếm", "lesson": "L5", "lessonName": "Bài 5", "strokes": 8, "meaning": "Cửa hàng", "kun": "みせ", "on": "てん", "examples": [{"word": "店", "reading": "みせ", "vi": "Cửa hàng"}], "formula": "广 (Mái hiên) ＋ 占 (Chiếm)", "strokeGuide": "Ngoài trước trong sau: Bộ Quảng (广 - 3 nét) bao ngoài ➔ chữ Chiêm (占 - 5 nét) ở trong.", "mnemonic": "Chiếm một mặt bằng dưới mái nhà để mở Cửa hàng."}, {"char": "多", "hv": "Đa", "lesson": "L5", "lessonName": "Bài 5", "strokes": 6, "meaning": "Nhiều, đông", "kun": "おお-い", "on": "た", "examples": [{"word": "多い", "reading": "おおい", "vi": "Nhiều, đông"}], "formula": "夕 ＋ 夕", "strokeGuide": "Trên trước dưới sau: Viết bộ Tịch (夕 - 3 nét) ở trên trước ➔ bộ Tịch thứ hai ở dưới.", "mnemonic": "Hai bộ Tịch chồng lên nhau biểu thị sự nhiều."}, {"char": "少", "hv": "Thiểu", "lesson": "L5", "lessonName": "Bài 5", "strokes": 4, "meaning": "Ít, một chút", "kun": "すく-ない、 すこ-し", "on": "しょう", "examples": [{"word": "少ない", "reading": "すくない", "vi": "Ít"}, {"word": "少し", "reading": "すこし", "vi": "Một chút"}], "formula": "小 (Nhỏ) ＋ 丿", "strokeGuide": "Giữa trước hai bên sau: Nét sổ móc giữa ➔ chấm trái ➔ chấm phải ➔ nét phẩy dài cắt chéo dưới.", "mnemonic": "Đã nhỏ (小) lại vơi đi nên chỉ còn rất ít."}, {"char": "高", "hv": "Cao", "lesson": "L5", "lessonName": "Bài 5", "strokes": 10, "meaning": "Cao, đắt", "kun": "たか-い", "on": "こう", "examples": [{"word": "高い", "reading": "たかい", "vi": "Cao, đắt"}, {"word": "高校", "reading": "こうこう", "vi": "Trường cấp 3"}], "formula": "亠 ＋ 口 ＋ 冂 ＋ 口", "strokeGuide": "Trên xuống dưới: Chấm ngang trên cùng ➔ bộ Khẩu nhỏ ➔ khung vòm dưới ➔ bộ Khẩu trong cùng.", "mnemonic": "Hình tòa tháp cao nhiều tầng."}, {"char": "安", "hv": "An", "lesson": "L5", "lessonName": "Bài 5", "strokes": 6, "meaning": "Rẻ, an tâm", "kun": "やす-い", "on": "あん", "examples": [{"word": "安い", "reading": "やすい", "vi": "Rẻ"}], "formula": "宀 (Mái nhà) ＋ 女 (Phụ nữ)", "strokeGuide": "Trên trước dưới sau: Bộ Miên (宀 - 3 nét) ở trên ➔ bộ Nữ (女 - 3 nét) ở dưới.", "mnemonic": "Người phụ nữ (女) dưới mái nhà (宀) luôn bình an."}, {"char": "広", "hv": "Quảng", "lesson": "L5", "lessonName": "Bài 5", "strokes": 5, "meaning": "Rộng rãi", "kun": "ひろ-い", "on": "こう", "examples": [{"word": "広い", "reading": "ひろい", "vi": "Rộng"}], "formula": "广 (Mái hiên) ＋ 厶", "strokeGuide": "Ngoài trước trong sau: Bộ Quảng (广 - 3 nét) trước ➔ bộ Khư (厶 - 2 nét) bên trong.", "mnemonic": "Ngôi nhà có mái hiên rộng thênh thang."}, {"char": "道", "hv": "Đạo", "lesson": "L6", "lessonName": "Bài 6", "strokes": 12, "meaning": "Con đường, đạo lý", "kun": "みち", "on": "どう、とう", "formula": "首 (Đầu) ＋ 辶 (Quai xước / Bước đi)", "strokeGuide": "Viết chữ Thủ (首 - 9 nét) trước ➔ bộ Quai xước (辶 - 3 nét) ôm bên ngoài sau.", "mnemonic": "Người dẫn đầu (首) cất bước (辶) khai mở ra con Đường (道).", "examples": [{"word": "道", "reading": "みち", "vi": "Con đường"}, {"word": "茶道", "reading": "さどう", "vi": "Trà đạo"}, {"word": "道路", "reading": "どうろ", "vi": "Đường cái, quốc lộ"}]}, {"char": "通", "hv": "Thông", "lesson": "L6", "lessonName": "Bài 6", "strokes": 10, "meaning": "Thông suốt, đi qua, đi lại", "kun": "とお-る、とお-り、かよ-う", "on": "つう、つ", "formula": "甬 (Dũng) ＋ 辶 (Quai xước / Bước đi)", "strokeGuide": "Viết chữ Dũng (甬 - 7 nét) trước ➔ bộ Quai xước (辶 - 3 nét) ôm bên ngoài sau.", "mnemonic": "Bước đi (辶) thông suốt qua con đường lớn.", "examples": [{"word": "通ります", "reading": "とおります", "vi": "Đi qua"}, {"word": "通り", "reading": "とおり", "vi": "Con phố, con đường"}, {"word": "交通", "reading": "こうつう", "vi": "Giao thông"}]}, {"char": "右", "hv": "Hữu", "lesson": "L6", "lessonName": "Bài 6", "strokes": 5, "meaning": "Bên phải", "kun": "みぎ", "on": "う、ゆう", "formula": "𠂇 (Tay) ＋ 口 (Miệng)", "strokeGuide": "Nét phẩy trước ➔ nét ngang dài ➔ bộ Khẩu (口 - 3 nét) ở dưới.", "mnemonic": "Tay phải (𠂇) cầm đũa gắp thức ăn đưa vào Miệng (口).", "examples": [{"word": "右", "reading": "みぎ", "vi": "Bên phải"}, {"word": "右手", "reading": "みぎて", "vi": "Tay phải"}, {"word": "右側", "reading": "みぎがわ", "vi": "Phía bên phải"}]}, {"char": "左", "hv": "Tả", "lesson": "L6", "lessonName": "Bài 6", "strokes": 5, "meaning": "Bên trái", "kun": "ひだり", "on": "さ、しゃ", "formula": "𠂇 (Tay) ＋ 工 (Thước thợ)", "strokeGuide": "Nét ngang trước ➔ nét phẩy ➔ bộ Công (工 - 3 nét) ở dưới.", "mnemonic": "Tay trái (𠂇) cầm cây thước thợ (工).", "examples": [{"word": "左", "reading": "ひだり", "vi": "Bên trái"}, {"word": "左手", "reading": "ひだりて", "vi": "Tay trái"}, {"word": "左側", "reading": "ひだりがわ", "vi": "Phía bên trái"}]}, {"char": "赤", "hv": "Xích", "lesson": "L6", "lessonName": "Bài 6", "strokes": 7, "meaning": "Màu đỏ, sắc đỏ", "kun": "あか、あか-い", "on": "せき、しゃく", "formula": "土 (Đất) ＋ 火 (Lửa)", "strokeGuide": "Bộ Thổ (土) ở trên ➔ 4 nét dưới tỏa ra như ngọn lửa.", "mnemonic": "Đất nung (土) trên ngọn lửa hồng (火) đỏ rực.", "examples": [{"word": "赤い", "reading": "あかい", "vi": "(Tính từ) Màu đỏ"}, {"word": "赤", "reading": "あか", "vi": "(Danh từ) Màu đỏ"}, {"word": "赤色", "reading": "あかいろ", "vi": "Màu đỏ"}]}, {"char": "青", "hv": "Thanh", "lesson": "L6", "lessonName": "Bài 6", "strokes": 8, "meaning": "Màu xanh dương, xanh thẫm", "kun": "あお、あお-い", "on": "せい、しょう", "formula": "生 (Sinh sôi) ＋ 月 (Trăng / Đan)", "strokeGuide": "Viết phần trên (3 nét ngang + 1 nét sổ) ➔ bộ Nguyệt (月 - 4 nét) ở dưới.", "mnemonic": "Cây cối sinh sôi tươi tốt dưới ánh trăng xanh biếc.", "examples": [{"word": "青い", "reading": "あおい", "vi": "(Tính từ) Màu xanh"}, {"word": "青", "reading": "あお", "vi": "(Danh từ) Màu xanh"}, {"word": "青色", "reading": "あおいろ", "vi": "Màu xanh"}]}, {"char": "黒", "hv": "Hắc", "lesson": "L6", "lessonName": "Bài 6", "strokes": 11, "meaning": "Màu đen, hắc ám", "kun": "くろ、くろ-い", "on": "こく", "formula": "里 (Làng) ＋ 灬 (Hỏa / Bốn chấm lửa)", "strokeGuide": "Viết phần trên giống bộ Lý (里) ➔ 4 chấm lửa (灬) ở dưới đáy.", "mnemonic": "Khói lửa (灬) đốt làng xóm bốc lên đen ngòm.", "examples": [{"word": "黒い", "reading": "くろい", "vi": "(Tính từ) Màu đen"}, {"word": "黒", "reading": "くろ", "vi": "(Danh từ) Màu đen"}, {"word": "黒色", "reading": "くろいろ", "vi": "Màu đen"}]}, {"char": "白", "hv": "Bạch", "lesson": "L6", "lessonName": "Bài 6", "strokes": 5, "meaning": "Màu trắng, trong sạch", "kun": "しろ、しろ-い、しら", "on": "はく、びゃく", "formula": "丿 (Chấm phẩy) ＋ 日 (Mặt trời)", "strokeGuide": "Nét phẩy trên đỉnh ➔ nét sổ trái ➔ nét gập phải ➔ 2 nét ngang trong và đáy.", "mnemonic": "Một tia nắng (丿) ló rạng từ mặt trời (日) tỏa ánh sáng trắng.", "examples": [{"word": "白い", "reading": "しろい", "vi": "(Tính từ) Màu trắng"}, {"word": "白", "reading": "しろ", "vi": "(Danh từ) Màu trắng"}, {"word": "白色", "reading": "しろいろ", "vi": "Màu trắng"}]}, {"char": "時", "hv": "Thời", "lesson": "L7", "lessonName": "Bài 7", "strokes": 10, "meaning": "Thời gian, mùa, giờ giấc", "kun": "とき、どき", "on": "じ", "formula": "日 (Mặt trời) ＋ 寺 (Chùa)", "strokeGuide": "Bộ Nhật (日 - 4 nét) bên trái ➔ chữ Tự (寺 - 6 nét) bên phải.", "mnemonic": "Nhìn bóng mặt trời (日) soi trên sân chùa (寺) để biết Thời gian.", "examples": [{"word": "あの時", "reading": "あのとき", "vi": "Lúc đấy, bấy giờ"}, {"word": "一時", "reading": "いちじ", "vi": "1 giờ, thời khắc / tạm thời"}, {"word": "時間", "reading": "じかん", "vi": "Thời gian"}]}, {"char": "間", "hv": "Gian", "lesson": "L7", "lessonName": "Bài 7", "strokes": 12, "meaning": "Khoảng (không gian, thời gian), ở giữa", "kun": "あいだ、ま", "on": "かん、けん", "formula": "門 (Cửa) ＋ 日 (Mặt trời)", "strokeGuide": "Bộ Môn (門 - 8 nét) bao ngoài ➔ bộ Nhật (日 - 4 nét) ở giữa.", "mnemonic": "Ánh nắng mặt trời (日) lọt qua khe Cửa (門) tạo thành Khoảng thời gian/không gian.", "examples": [{"word": "間", "reading": "あいだ", "vi": "Ở giữa (vị trí)"}, {"word": "この間", "reading": "このあいだ", "vi": "Gần đây, dạo này"}, {"word": "時間", "reading": "じかん", "vi": "Thời gian"}, {"word": "一時間", "reading": "いちじかん", "vi": "1 tiếng đồng hồ"}]}, {"char": "場", "hv": "Trường, Tràng", "lesson": "L7", "lessonName": "Bài 7", "strokes": 12, "meaning": "Địa điểm, nơi chốn, quảng trường", "kun": "ば", "on": "じょう、ちょう", "formula": "土 (Đất) ＋ 昜 (Ánh sáng)", "strokeGuide": "Bộ Thổ (土 - 3 nét) bên trái ➔ chữ Dương (昜 - 9 nét) bên phải.", "mnemonic": "Mảnh đất (土) chan hòa ánh nắng (昜) làm Quảng trường tụ họp.", "examples": [{"word": "広場", "reading": "ひろば", "vi": "Quảng trường"}, {"word": "会場", "reading": "かいじょう", "vi": "Hội trường"}, {"word": "場所", "reading": "ばしょ", "vi": "Địa điểm"}]}, {"char": "所", "hv": "Sở", "lesson": "L7", "lessonName": "Bài 7", "strokes": 8, "meaning": "Nơi chốn, địa điểm", "kun": "ところ、どころ、とこ", "on": "しょ", "formula": "戸 (Cánh cửa) ＋ 斤 (Cái rìu)", "strokeGuide": "Bộ Hộ (戸 - 4 nét) bên trái ➔ bộ Cân (斤 - 4 nét cái rìu) bên phải.", "mnemonic": "Cầm rìu (斤) đẽo cánh cửa (戸) dựng lên Nơi ở (所).", "examples": [{"word": "所", "reading": "ところ", "vi": "Nơi, chỗ"}, {"word": "場所", "reading": "ばしょ", "vi": "Địa điểm"}, {"word": "台所", "reading": "だいどころ", "vi": "Phòng bếp"}]}, {"char": "駅", "hv": "Dịch", "lesson": "L7", "lessonName": "Bài 7", "strokes": 14, "meaning": "Nhà ga tàu điện", "kun": "えき", "on": "えき", "formula": "馬 (Con ngựa) ＋ 尺 (Thước đo)", "strokeGuide": "Bộ Mã (馬 - 10 nét) bên trái ➔ chữ Xích (尺 - 4 nét) bên phải.", "mnemonic": "Trạm đổi Ngựa (馬) thời xưa chính là Nhà ga (駅) ngày nay.", "examples": [{"word": "駅", "reading": "えき", "vi": "Nhà ga"}, {"word": "東京駅", "reading": "とうきょうえき", "vi": "Ga Tokyo"}, {"word": "駅員", "reading": "えきいん", "vi": "Nhân viên nhà ga"}]}, {"char": "出", "hv": "Xuất", "lesson": "L7", "lessonName": "Bài 7", "strokes": 5, "meaning": "Ra ngoài, rời khỏi, xuất hiện", "kun": "で-る、だ-す、で-かける", "on": "しゅつ、すい", "formula": "山 ＋ 山 (Mầm cây nhú lên khỏi mặt đất)", "strokeGuide": "Sổ giữa ➔ gập trái ➔ sổ phải ➔ sổ dài giữa ➔ gập trái ➔ sổ phải.", "mnemonic": "Mầm cây nhú ra khỏi lòng đất vươn lên thành ngọn núi.", "examples": [{"word": "出かけます", "reading": "でかけます", "vi": "Ra ngoài (~に出かけます)"}, {"word": "出ます", "reading": "でます", "vi": "Rời khỏi (~を出ます)"}, {"word": "出口", "reading": "でぐち", "vi": "Cửa ra"}, {"word": "出張", "reading": "しゅっちょう", "vi": "Đi công tác"}]}, {"char": "待", "hv": "Đãi", "lesson": "L7", "lessonName": "Bài 7", "strokes": 9, "meaning": "Chờ đợi, đối đãi", "kun": "ま-つ", "on": "たい", "formula": "彳 (Bước chân) ＋ 寺 (Chùa)", "strokeGuide": "Bộ Xích (彳 - 3 nét) bên trái ➔ chữ Tự (寺 - 6 nét) bên phải.", "mnemonic": "Dừng bước chân (彳) trước cổng Chùa (寺) để Đợi chờ.", "examples": [{"word": "待ちます", "reading": "まちます", "vi": "Đợi, chờ"}, {"word": "待ち合わせ", "reading": "まちあわせ", "vi": "Cuộc hẹn"}]}, {"char": "止", "hv": "Chỉ", "lesson": "L7", "lessonName": "Bài 7", "strokes": 4, "meaning": "Dừng lại, đình chỉ", "kun": "と-まる、と-める", "on": "し", "formula": "Chữ tượng hình dấu chân dừng lại", "strokeGuide": "Sổ giữa ➔ nét ngang ngắn bên phải ➔ sổ ngắn bên trái ➔ nét ngang đáy dài khóa lại.", "mnemonic": "Bàn chân chạm đất đứng lại không đi nữa.", "examples": [{"word": "止まります", "reading": "とまります", "vi": "(Tàu, xe) Dừng lại (tự động từ)"}, {"word": "止めます", "reading": "とめます", "vi": "Dừng xe, đỗ lại (tha động từ)"}, {"word": "中止", "reading": "ちゅうし", "vi": "Hủy bỏ, hoãn"}]}, {"char": "食", "hv": "Thực", "lesson": "L8", "lessonName": "Bài 8", "strokes": 9, "meaning": "Ăn, bữa ăn, thực phẩm", "kun": "た-べる", "on": "しょく、じき", "formula": "亼 (Mái nhà) ＋ 艮 (Cái bát thức ăn)", "strokeGuide": "Nét phẩy và nét mác tạo mái ➔ nét ngang ➔ nét sổ gập ➔ các nét bên dưới.", "mnemonic": "Mọi người quây quần dưới mái nhà cùng nhau Ăn cơm.", "examples": [{"word": "食べます", "reading": "たべます", "vi": "Ăn"}, {"word": "食事", "reading": "しょくじ", "vi": "(Việc) Ăn uống, bữa ăn"}, {"word": "朝食", "reading": "ちょうしょく", "vi": "Bữa sáng (trang trọng)"}, {"word": "昼食", "reading": "ちゅうしょく", "vi": "Bữa trưa (trang trọng)"}]}, {"char": "事", "hv": "Sự", "lesson": "L8", "lessonName": "Bài 8", "strokes": 8, "meaning": "Sự việc, công việc", "kun": "こと", "on": "じ、ず", "formula": "Chữ tượng hình người cầm bút ghi chép sự việc", "strokeGuide": "Nét ngang trên ➔ nét khẩu nhỏ ➔ nét ngang dài ➔ bộ quyết ở dưới.", "mnemonic": "Bàn tay cầm bút ghi chép lại mọi Sự việc.", "examples": [{"word": "事", "reading": "こと", "vi": "Sự việc, điều"}, {"word": "食事", "reading": "しょくじ", "vi": "(Việc) Ăn uống, bữa ăn"}, {"word": "事故", "reading": "じこ", "vi": "Tai nạn, sự cố"}, {"word": "仕事", "reading": "しごと", "vi": "Công việc"}]}, {"char": "仕", "hv": "Sĩ", "lesson": "L8", "lessonName": "Bài 8", "strokes": 5, "meaning": "Làm việc, phục vụ", "kun": "つか-える", "on": "し、じ", "formula": "亻 (Người) ＋ 士 (Kẻ sĩ)", "strokeGuide": "Bộ Nhân đứng (亻 - 2 nét) bên trái ➔ chữ Sĩ (士 - 3 nét) bên phải.", "mnemonic": "Người (亻) kẻ sĩ (士) tận tâm phục vụ Công việc (仕事).", "examples": [{"word": "仕事", "reading": "しごと", "vi": "Công việc"}, {"word": "仕えます", "reading": "つかえます", "vi": "Phục vụ, phụng sự"}]}, {"char": "前", "hv": "Tiền", "lesson": "L8", "lessonName": "Bài 8", "strokes": 9, "meaning": "Phía trước, trước khi", "kun": "まえ", "on": "ぜん", "formula": "丷 ＋ 一 ＋ 月 ＋ 刂 (Đao)", "strokeGuide": "Phần trên (3 nét) ➔ bộ Nguyệt (月) bên dưới trái ➔ bộ Đao (刂) bên dưới phải.", "mnemonic": "Cầm dao (刂) tiến về phía Trước cắt cỏ mở đường.", "examples": [{"word": "前", "reading": "まえ", "vi": "Phía trước, trước khi"}, {"word": "午前", "reading": "ごぜん", "vi": "Buổi sáng (AM)"}]}, {"char": "後", "hv": "Hậu", "lesson": "L8", "lessonName": "Bài 8", "strokes": 9, "meaning": "Phía sau, sau đó", "kun": "のち、うし-ろ、あと", "on": "ご、こう", "formula": "彳 (Bước chân) ＋ 幺 (Sợi tơ) ＋ 夂 (Đi chậm)", "strokeGuide": "Bộ Xích (彳) bên trái ➔ bộ Yêu (幺) trên phải ➔ bộ Truy (夂) dưới phải.", "mnemonic": "Chân bước (彳) vướng sợi tơ (幺) nên tụt lại phía Sau (後).", "examples": [{"word": "その後", "reading": "そのあと", "vi": "Sau đó"}, {"word": "後で", "reading": "あとで", "vi": "Lát nữa, sau khi"}, {"word": "午後", "reading": "ごご", "vi": "Buổi chiều, tối (PM)"}, {"word": "後ろ", "reading": "うしろ", "vi": "Phía sau"}]}, {"char": "朝", "hv": "Triêu", "lesson": "L8", "lessonName": "Bài 8", "strokes": 12, "meaning": "Sớm, buổi sáng, triều đại", "kun": "あさ", "on": "ちょう", "formula": "十 ＋ 日 ＋ 十 ＋ 月", "strokeGuide": "Chữ Triêu (bên trái: thập, nhật, thập) ➔ bộ Nguyệt (月) bên phải.", "mnemonic": "Mặt trời (日) mọc giữa ngọn cỏ và mặt trăng (月) dần lặn là Buổi sáng.", "examples": [{"word": "朝", "reading": "あさ", "vi": "Buổi sáng"}, {"word": "朝ごはん", "reading": "あさごはん", "vi": "Cơm sáng, bữa sáng"}, {"word": "朝食", "reading": "ちょうしょく", "vi": "Bữa sáng (trang trọng)"}]}, {"char": "昼", "hv": "Trú", "lesson": "L8", "lessonName": "Bài 8", "strokes": 9, "meaning": "Ban ngày, buổi trưa", "kun": "ひる", "on": "ちゅう", "formula": "尺 ＋ 日 ＋ 一", "strokeGuide": "Chữ Xích (尺) ở trên bao lấy ➔ bộ Nhật (日) ở giữa ➔ nét ngang đáy.", "mnemonic": "Cây thước (尺) đo bóng mặt trời (日) đứng bóng giữa trưa.", "examples": [{"word": "昼", "reading": "ひる", "vi": "Buổi trưa"}, {"word": "昼ごはん", "reading": "ひるごはん", "vi": "Cơm trưa, bữa trưa"}, {"word": "昼食", "reading": "ちゅうしょく", "vi": "Bữa trưa (trang trọng)"}]}, {"char": "夜", "hv": "Dạ", "lesson": "L8", "lessonName": "Bài 8", "strokes": 8, "meaning": "Ban đêm, buổi tối", "kun": "よ、よる", "on": "や", "formula": "亠 ＋ 亻 ＋ 夕 (Tối)", "strokeGuide": "Bộ Đầu (亠) trên ➔ bộ Nhân đứng (亻) giữa trái ➔ bộ Tịch (夕) dưới.", "mnemonic": "Người (亻) trở về nhà dưới mái hiên (亠) khi trời Tối (夕).", "examples": [{"word": "夜", "reading": "よる", "vi": "Buổi tối, ban đêm"}, {"word": "夜景", "reading": "やけい", "vi": "Cảnh đêm"}, {"word": "夜勤", "reading": "やきん", "vi": "Làm ca đêm"}]}, {"char": "乗", "hv": "Thừa", "lesson": "L8", "lessonName": "Bài 8", "strokes": 9, "meaning": "Lên xe, cưỡi ngựa", "kun": "の-る、の-せる", "on": "じょう、しょう", "formula": "禾 (Cây lúa) ＋ 北 (Bắc)", "strokeGuide": "Nét phẩy trên ➔ nét ngang dài ➔ nét sổ giữa ➔ 4 nét phẩy mác hai bên.", "mnemonic": "Trèo lên cỗ xe chất đầy lúa (禾) để chở đi.", "examples": [{"word": "乗ります", "reading": "のります", "vi": "Lên xe, đi tàu"}, {"word": "乗り物", "reading": "のりもの", "vi": "Phương tiện đi lại"}]}];
const quizData = [{"id": 1, "category": "Tính từ đuôi い: Nối câu cùng chiều", "lesson": "A2-5", "q": "この 店の 料理は [____]、とても おいしいです。", "options": ["安いで", "安くては", "安い", "安くて"], "correct": 3, "explain": "Quy tắc nối tính từ đuôi い: Bỏ đuôi 「い」 và thêm 「くて」 (安[い] ➔ 安くて - vừa rẻ vừa ngon). Đuôi 「で」 chỉ dùng nối cho tính từ đuôi な và danh từ. Tuyệt đối không dùng 「安いで」."}, {"id": 2, "category": "Tính từ đuôi な: Nối câu cùng chiều", "lesson": "A2-5", "q": "この 辺りは [____]、おもしろい 町です。", "options": ["にぎやかくて", "にぎやかだ", "にぎやかで", "にぎやかに"], "correct": 2, "explain": "Quy tắc nối tính từ đuôi な: Bỏ 「な」 và thêm 「で」 (にぎやか[な] ➔ にぎやかで - náo nhiệt và thú vị). 「にぎやかくて」 là sai vì đây là tính từ đuôi な, không biến đổi như đuôi い."}, {"id": 3, "category": "Tính từ đuôi い: Nối tương phản đối lập", "lesson": "A2-5", "q": "この 遊園地は [____]、ちょっと 高いです。", "options": ["楽しいだけど", "楽しくて", "楽しいけど", "楽しいから"], "correct": 2, "explain": "Quy tắc nối mệnh đề tương phản đối lập (nhưng mà...): Tính từ đuôi い đi trực tiếp với 「けど」 (楽しい ＋ けど). Dạng 「だけど」 chỉ đi sau tính từ đuôi な và danh từ (ví dụ: 不便だけど)."}, {"id": 4, "category": "Tính từ đuôi な: Nối tương phản đối lập", "lesson": "A2-5", "q": "私の 町は ちょっと [____]、緑が多くて 好きです。", "options": ["不便けど", "不便で", "不便だけど", "不便くて"], "correct": 2, "explain": "Tính từ đuôi な (不便な) khi nối tương phản đối lập bắt buộc phải dùng 「～だけど」 (不便 ＋ だけど - hơi bất tiện nhưng nhiều cây xanh nên tôi thích). Không được nói 「不便けど」."}, {"id": 5, "category": "Trợ từ: Liệt kê tiêu biểu や～など", "lesson": "A2-5", "q": "この 辺りには 高い ビル [____] ホテルなどが あります。", "options": ["と", "も", "や", "を"], "correct": 2, "explain": "Cấu trúc liệt kê không toàn bộ: 「N1 や N2 (など) が あります」 (Có những thứ như N1, N2...). Khác với 「と」 là liệt kê toàn bộ đóng khung, 「や」 chỉ đưa ra một vài đại diện tiêu biểu (ngoài ra còn có những tòa nhà khác nữa)."}, {"id": 6, "category": "Trợ từ: Nhấn mạnh chủ đề / phạm vi には", "lesson": "A2-5", "q": "日本 [____] 東京や 大阪などの 有名な 町が あります。", "options": ["では", "へは", "には", "をは"], "correct": 2, "explain": "Trợ từ kép 「には」 = 「に」 (vị trí tồn tại khách quan) + 「は」 (đưa lên làm chủ đề / so sánh phạm vi: \"Còn riêng tại đất nước Nhật Bản thì có...\"). Tồn tại có danh từ chỉ vật thì đi với あります."}, {"id": 7, "category": "Trợ từ: Không gian di chuyển xuyên qua", "lesson": "A2-6", "q": "この とおり [____] まっすぐ 行って ください。", "options": ["で", "を", "に", "へ"], "correct": 1, "explain": "Trợ từ 「を」 trong trường hợp này chỉ không gian di chuyển xuyên qua: 「とおりを まっすぐ 行く」 (đi thẳng qua con phố này). Tương tự: 「道を あるく」 (đi trên đường), 「橋を わたる」 (băng qua cầu). Tuyệt đối không dùng 「で」."}, {"id": 8, "category": "Trợ từ: Rời khỏi phương tiện", "lesson": "A2-6", "q": "次の 駅で 電車 [____] おります。", "options": ["を", "に", "で", "へ"], "correct": 0, "explain": "Bẫy thi kinh điển của trợ từ di chuyển: Lên xe dùng に (電車に のる - tiếp xúc), còn xuống xe dùng を (電車を おりる - rời khỏi điểm xuất phát). Do đó câu này bắt buộc dùng 「を」."}, {"id": 9, "category": "Trợ từ: Tiếp xúc lên phương tiện", "lesson": "A2-6", "q": "駅で 電車 [____] のって ください。", "options": ["を", "で", "から", "に"], "correct": 3, "explain": "Động từ lên tàu xe 「乗る (のる)」 luôn luôn đi với trợ từ 「に」: 「電車に のる」, 「バスに のる」 (Trợ từ に chỉ điểm tiếp xúc đến của cơ thể)."}, {"id": 10, "category": "Trợ từ: Hướng rẽ tại điểm giao cắt", "lesson": "A2-6", "q": "2つ目の 信号を 右 [____] 曲がって ください。", "options": ["を", "で", "と", "に"], "correct": 3, "explain": "Cấu trúc chỉ đường: 「[Vị trí rẽ] を [Hướng rẽ: 右 / 左] に 曲がる」. Chỗ rẽ dùng 「を」 (信号を), còn hướng rẽ trái/phải dùng 「に」 (右に 曲がる)."}, {"id": 11, "category": "Giao tiếp: Đính chính thông tin じゃなくて", "lesson": "A2-6", "q": "「1つ目の 角ですか。」ー「いいえ、1つ目 [____]、2つ目ですよ。」", "options": ["で", "じゃなくて", "くて", "だけど"], "correct": 1, "explain": "Cấu trúc đính chính, phủ định thông tin sai để khẳng định thông tin đúng: 「A じゃなくて、B です」 (Không phải là A, mà là B cơ)."}, {"id": 12, "category": "Ngữ pháp: Cấm đoán lịch sự ないでください", "lesson": "A2-6", "q": "あぶないですから、ここには [____] ください。", "options": ["入って", "入らないで", "入らなくて", "入らない"], "correct": 1, "explain": "Mẫu câu yêu cầu không làm gì một cách lịch sự: 「V-ないで ください」. Động từ 「入る (はいる)」 là động từ Nhóm 1 kết thúc bằng đuôi -ru ➔ chuyển sang thể Nai là 「入らない (はいらない)」 ➔ 「入らないで ください」."}, {"id": 13, "category": "Giao tiếp: Thỏa thuận điều chỉnh giờ hẹn", "lesson": "A2-7", "q": "日曜日の 待ち合わせ、11時 [____] いいですか。", "options": ["にも", "でも", "とも", "へも"], "correct": 1, "explain": "Mẫu câu đề xuất / thỏa thuận một phương án thời gian hoặc địa điểm linh hoạt: 「[Thời gian / Địa điểm] ＋ でもいいですか」 (Khoảng... có được không ạ?)."}, {"id": 14, "category": "Trợ từ: Nguyên nhân khách quan gây trễ hẹn", "lesson": "A2-7", "q": "すみません、じゅうたい [____] 15分ぐらい 遅れます。", "options": ["に", "で", "を", "が"], "correct": 1, "explain": "Trợ từ 「で」 chỉ lý do / nguyên nhân khách quan (thiên tai, tai nạn, sự cố giao thông): 「渋滞で (do tắc đường)」, 「事故で (do tai nạn)」. Đi kèm với hậu quả phía sau: 「遅れます (bị trễ/muộn)」."}, {"id": 15, "category": "Thể TE: Nêu lý do sự cố trễ hẹn", "lesson": "A2-7", "q": "道に [____]、遅くなって すみません。", "options": ["まよって", "まよわないで", "まよう", "まよった"], "correct": 0, "explain": "Cụm từ 「道に 迷います (lạc đường)」 khi dùng thể TE 「道に まよって」 để nối câu nêu lý do dẫn tới kết quả trễ hẹn: \"Tôi bị lạc đường nên đến muộn, xin lỗi bạn nhiều nhé!\"."}, {"id": 16, "category": "Từ vựng: Tàu điện dừng chạy vì sự cố", "lesson": "A2-7", "q": "じこで 電車が [____] しまいました。", "options": ["おりて", "まよって", "まちがえて", "とまって"], "correct": 3, "explain": "Động từ 「止まる (とまる)」 nghĩa là dừng lại, ngừng hoạt động. 「電車が 止まる」 = tàu điện dừng chạy. 「おりる」 là người xuống xe, 「まよう」 là lạc đường, 「まちがえる」 là nhầm lẫn."}, {"id": 17, "category": "Văn hóa: Câu xin lỗi khi đến muộn", "lesson": "A2-7", "q": "「[____] すみませんでした！」ー「いいえ、大丈夫ですよ。」", "options": ["早くなって", "遅くなって", "元気になって", "寒くなって"], "correct": 1, "explain": "Câu xin lỗi chuẩn mực không thể thiếu khi đến muộn cuộc hẹn trong giao tiếp tiếng Nhật: 「遅くなって すみません (でした)」 (Tôi xin lỗi vì đã đến muộn). Tính từ 遅い ➔ 遅くなって."}, {"id": 18, "category": "Thỏa thuận địa điểm gặp gỡ", "lesson": "A2-7", "q": "待ち合わせの 場所は、ホテルの ロビー [____] いいですか。", "options": ["にも", "でも", "を", "へ"], "correct": 1, "explain": "Mẫu câu thương lượng địa điểm: 「[Địa điểm] ＋ でもいいですか」 (Hẹn ở sảnh khách sạn có được không bạn?). 「でも」 mang sắc thái gợi ý nhẹ nhàng, tôn trọng ý kiến người nghe."}, {"id": 19, "category": "Mục đích di chuyển: Động từ bỏ ます + に行きます", "lesson": "A2-8", "q": "上野公園へ 桜を [____] に 行きました。", "options": ["見る", "見て", "見", "見た"], "correct": 2, "explain": "Công thức chỉ mục đích di chuyển: 「[V-bỏ ます] ＋ に いきます / きます / 帰ります」. Động từ 「見ます」 bỏ ます còn 「見」 ghép với に ➔ 「見に 行きました」 (đã đi đến để ngắm)."}, {"id": 20, "category": "Mục đích di chuyển: Danh từ hành động + に行きます", "lesson": "A2-8", "q": "デパートへ [____] に 行きます。", "options": ["買う", "買って", "買い物", "買います"], "correct": 2, "explain": "Với danh từ chỉ hành vi (買い物 - mua sắm, 散歩 - đi dạo, 食事 - ăn uống), ta ghép thẳng với trợ từ 「に」: 「買い物に 行きます」. Không dùng dạng động từ chia dở."}, {"id": 21, "category": "Trình tự thời gian: Trước khi (V-る まえに)", "lesson": "A2-8", "q": "寝る [____]、本を 読みます。", "options": ["あとで", "まえに", "ときに", "あいだに"], "correct": 1, "explain": "Công thức chỉ trình tự TRƯỚC KHI: 「V-る ＋ まえに」. Quy tắc vàng: Động từ đứng trước まえに luôn ở thể từ điển V-る (寝る 前に = trước khi đi ngủ)."}, {"id": 22, "category": "Trình tự thời gian: Trước Danh từ (Nの まえに)", "lesson": "A2-8", "q": "食事 [____] まえに、お茶を 飲みます。", "options": ["の", "に", "で", "を"], "correct": 0, "explain": "Khi đi kèm Danh từ, cấu trúc trước khi bắt buộc phải có trợ từ 「の」: 「[Danh từ] ＋ の まえに」 (食事の 前に = trước bữa ăn). Phân biệt với động từ đi thẳng V-る 前に."}, {"id": 23, "category": "Trình tự thời gian: Sau khi (V-た あとで)", "lesson": "A2-8", "q": "映画を [____] あとで、カフェに 行きましょう。", "options": ["見た", "見る", "見て", "見ます"], "correct": 0, "explain": "Công thức chỉ trình tự SAU KHI: 「V-た ＋ あとで」. Hành động xem phim đã hoàn tất trước rồi mới đi cà phê nên động từ bắt buộc chia ở thể quá khứ Ta: 「見た あとで」."}, {"id": 24, "category": "Hội thoại: Phản hồi câu hỏi đã làm chưa もう", "lesson": "A2-8", "q": "「もう 美術館に 行きましたか。」ー「いいえ、[____]。」", "options": ["まだです", "行きませんでした", "行きます", "だめです"], "correct": 0, "explain": "Bẫy thi đắt giá nhất của Bài 8: Khi trả lời phủ định cho câu hỏi 「もう ～ましたか」 (Đã làm... chưa?), bắt buộc phải trả lời là 「いいえ、まだです」 (Chưa, tôi chưa làm). Nếu trả lời 「行きませんでした」 sẽ bị hiểu lầm là bạn từ chối không bao giờ muốn đi."}, {"id": 25, "category": "Kanji Bài 5: Chiết tự chữ 町", "lesson": "A2-5", "q": "Chữ Hán 「町」 (Đinh - thị trấn) được tạo nên từ 2 bộ thủ nào?", "options": ["Bộ Mộc (木) và bộ Thổ (土)", "Bộ Ngôn (言) và bộ Khẩu (口)", "Bộ Nhân (人) và bộ Nhật (日)", "Bộ Điền (田 - ruộng) và bộ Đinh (丁 - góc đường)"], "correct": 3, "explain": "Chữ 「町」 (Đinh) gồm bộ Điền (田 - ruộng lúa) ở bên trái và bộ Đinh (丁 - ngã ba đường) ở bên phải: Khu dân cư đông đúc cạnh cánh đồng tạo nên một thị trấn, góc phố."}, {"id": 26, "category": "Kanji Bài 5: Cặp từ trái nghĩa 高い vs 安い", "lesson": "A2-5", "q": "Cặp chữ Hán trái nghĩa 「高い」 (cao/đắt) và 「安い」 (rẻ/yên ổn) có âm Hán Việt tương ứng là gì?", "options": ["Cao - An", "Đa - Thiểu", "Quảng - Trắc", "Trường - Đoản"], "correct": 0, "explain": "Chữ 「高」 có âm Hán Việt là Cao (trong cao lớn, đắt đỏ), chữ 「安」 có âm Hán Việt là An (trong an toàn, an tâm, rẻ). Cả hai đều là tính từ trọng tâm của Bài 5."}, {"id": 27, "category": "Kanji Bài 6: Đạo & Thông", "lesson": "A2-6", "q": "Hai chữ Hán 「道」 và 「通」 trong cụm từ chỉ đường có cách đọc Kunyomi là gì?", "options": ["みぎ (bên phải) và ひだり (bên trái)", "あか (màu đỏ) và あお (màu xanh)", "しろ (màu trắng) và くろ (màu đen)", "みち (con đường) và とおり (đường phố)"], "correct": 3, "explain": "Chữ 「道」 (Đạo) có âm Kunyomi là 「みち」 (con đường), chữ 「通」 (Thông) có âm Kunyomi là 「とおり」 (con phố, tuyến đường). Cả hai chữ đều có bộ Quai xước (辶) chỉ sự di chuyển."}, {"id": 28, "category": "Kanji Bài 7: Nhà ga", "lesson": "A2-7", "q": "Chữ Hán 「駅」 (âm Hán Việt: Dịch) trong từ 「えき」 (nhà ga) gồm bộ thủ nào bên trái?", "options": ["Bộ Mã (馬 - con ngựa)", "Bộ Xích (彳- bước chân)", "Bộ Nhật (日 - mặt trời)", "Bộ Thổ (土 - đất đai)"], "correct": 0, "explain": "Chữ 「駅」 (Dịch) có bộ Mã (馬 - con ngựa) bên trái và chữ Xích (尺) bên phải. Thời xưa trạm bưu cục/ga ngựa là nơi đổi ngựa để chuyển công văn ➔ nay dùng làm Nhà ga tàu điện."}, {"id": 29, "category": "Kanji Bài 7: Động từ chờ đợi", "lesson": "A2-7", "q": "Chữ Hán 「待」 trong động từ 「待つ (まつ - chờ đợi)」 gồm những thành phần nào?", "options": ["Bộ Nhân (亻) ghép với chữ Mộc (木)", "Bộ Thủy (氵) ghép với chữ Thổ (土)", "Bộ Tâm (心) ghép với chữ Hỏa (火)", "Bộ Xích (彳 - bước chân đi) ghép với chữ Tự (寺 - ngôi chùa)"], "correct": 3, "explain": "Chữ 「待」 (Đãi) gồm bộ Xích (彳 - bước chân) đứng bên chữ Tự (寺 - ngôi chùa): Đứng dừng chân trước cổng chùa để chờ đợi ai đó."}, {"id": 30, "category": "Kanji Bài 8: Ghép từ 食事の 前に", "lesson": "A2-8", "q": "Cụm từ 「しょくじの まえに」 (trước bữa ăn) được viết bằng những chữ Hán nào?", "options": ["食事の 前に", "食言の 後に", "乗事の 前に", "朝昼の 後に"], "correct": 0, "explain": "Ghép chuẩn từ 3 chữ Hán trọng tâm Bài 8: 食 (Thực - ăn) + 事 (Sự - công việc/sự việc) ➔ 「食事 (しょくじ - bữa ăn)」 + 前 (Tiền - trước) ➔ 「食事の 前に (trước bữa ăn)」."}];

// Trạng thái ứng dụng
let currentVocabFilter = 'ALL';
let currentKanjiFilter = 'ALL';
let isMeaningHidden = false;
let userAnswers = {};

// Switch Main Tabs
function switchMainTab(tabId) {
    document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));

    document.getElementById(tabId).classList.add('active');
    event.currentTarget.classList.add('active');
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Render Vocab
function renderVocab(list) {
    const container = document.getElementById('vocabContainer');
    if (!list || list.length === 0) {
        container.innerHTML = '<div style="grid-column: 1/-1; text-align: center; padding: 40px; color: var(--gray-500);">Không tìm thấy từ vựng phù hợp.</div>';
        return;
    }

    container.innerHTML = list.map((item, idx) => `
        <div class="vocab-card">
            <div class="vocab-top">
                <span class="vocab-badge">${item.l}</span>
                <button class="sound-btn" onclick="speakText('${item.jp.replace(/'/g, "\'")}')" title="Nghe phát âm">🔊</button>
            </div>
            <div class="vocab-jp jp-text">${item.jp}</div>
            <div class="vocab-vi ${isMeaningHidden ? 'hidden-meaning' : ''}" title="${isMeaningHidden ? 'Bấm để xem' : ''}" onclick="this.classList.toggle('hidden-meaning')">
                ${item.vi}
            </div>
        </div>
    `).join('');
}

function filterVocab(lesson, btn) {
    currentVocabFilter = lesson;
    if (btn) {
        btn.parentElement.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
    }
    applyVocabFilter();
}

function handleVocabSearch() {
    applyVocabFilter();
}

let currentFilteredVocab = [...rawVocab];

function applyVocabFilter() {
    const keyword = document.getElementById('vocabSearchInput').value.trim().toLowerCase();
    let filtered = rawVocab;
    if (currentVocabFilter !== 'ALL') {
        filtered = filtered.filter(v => v.l === currentVocabFilter);
    }
    if (keyword) {
        filtered = filtered.filter(v => 
            v.jp.toLowerCase().includes(keyword) || 
            v.vi.toLowerCase().includes(keyword)
        );
    }
    currentFilteredVocab = filtered;
    const countEl = document.getElementById('quizletVocabCount');
    if (countEl) countEl.innerText = filtered.length;

    renderVocab(filtered);
}

function cleanJpTermForQuizlet(str) {
    if (!str) return "";
    let s = str;
    if (s === "まいつき、まいげつ") return "まいつき";
    if (s === "まいとし、まいねん") return "まいとし";
    s = s.replace(/[~～…\.]/g, "");
    s = s.replace(/めの[nN]/g, "め");
    s = s.replace(/^[nN]が/g, "");
    s = s.replace(/^[nNpPvV][をにへとがで]/g, "");
    s = s.replace(/^[pPnN]に/g, "");
    s = s.replace(/[vV]ましょう/g, "ましょう");
    s = s.replace(/[vV]ました/g, "");
    s = s.replace(/[vV]$/g, "");
    s = s.replace(/てください$/g, "");
    s = s.replace(/\([^)]*を\)/g, "").replace(/（[^）]*を）/g, "");
    s = s.replace(/\(お\)/g, "お").replace(/（お）/g, "お");
    s = s.replace(/\(します\)/g, "します").replace(/（します）/g, "します");
    s = s.replace(/\(さん\)/g, "").replace(/（さん）/g, "");
    s = s.replace(/\(な\)/g, "").replace(/（な）/g, "");
    s = s.replace(/[\(\)（）]/g, "");
    if (s.includes("/") || s.includes("／")) {
        s = s.split(/[\/／]/)[0];
    }
    s = s.replace(/[NPVnvp]/g, "");
    s = s.replace(/[。、,，\?？!！]/g, "");
    s = s.replace(/[\s　]+/g, "");
    return s.trim();
}

function formatQuizletVocabLine(item) {
    const term = cleanJpTermForQuizlet(item.kana || item.kanji || item.jp);
    let def = item.vi;
    if (item.jp && item.jp.includes('/')) {
        const alt = item.jp.split('/')[1].trim();
        def = `${item.vi} (hoặc ${alt})`;
    }
    return `${term}\t${def}`;
}

function copyVocabQuizletFormat() {
    if (!currentFilteredVocab || currentFilteredVocab.length === 0) {
        showToast("Không có từ vựng nào để sao chép!");
        return;
    }
    const text = currentFilteredVocab.map(formatQuizletVocabLine).join('\n');
    navigator.clipboard.writeText(text).then(() => {
        showToast(`✅ Đã copy ${currentFilteredVocab.length} từ vựng chuẩn Quizlet (Gõ mượt, không khoảng trắng, không ~)!`);
    }).catch(() => {
        fallbackCopyText(text, currentFilteredVocab.length);
    });
}

function copyFull121QuizletFormat() {
    const text = rawVocab.map(formatQuizletVocabLine).join('\n');
    navigator.clipboard.writeText(text).then(() => {
        showToast(`✅ Đã copy toàn bộ ${rawVocab.length} từ vựng (Bài 5 - 8) chuẩn Quizlet (Gõ mượt, không khoảng trắng, không ~)!`);
    }).catch(() => {
        fallbackCopyText(text, rawVocab.length);
    });
}

function fallbackCopyText(text, count) {
    const ta = document.createElement('textarea');
    ta.value = text;
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    document.execCommand('copy');
    document.body.removeChild(ta);
    showToast(`✅ Đã copy ${count} từ vựng chuẩn Quizlet (Gõ mượt, không khoảng trắng, không ~)!`);
}

function showToast(msg) {
    let toast = document.getElementById('toast');
    if (!toast) {
        toast = document.createElement('div');
        toast.id = 'toast';
        toast.className = 'toast';
        document.body.appendChild(toast);
    }
    toast.innerText = msg;
    toast.style.display = 'block';
    setTimeout(() => { toast.style.display = 'none'; }, 2800);
}

function toggleHideMeaning() {
    isMeaningHidden = !isMeaningHidden;
    const btn = document.getElementById('hideMeaningBtn');
    if (isMeaningHidden) {
        btn.classList.add('active');
        btn.innerHTML = '👁️ Đang ẩn nghĩa (Chạm vào thẻ để xem)';
    } else {
        btn.classList.remove('active');
        btn.innerHTML = '👁️ Ẩn nghĩa tiếng Việt (Tự dò)';
    }
    document.querySelectorAll('.vocab-vi').forEach(el => {
        if (isMeaningHidden) el.classList.add('hidden-meaning');
        else el.classList.remove('hidden-meaning');
    });
}

// Render Kanji
function renderKanji(list) {
    const container = document.getElementById('kanjiContainer');
    if (!list || list.length === 0) {
        container.innerHTML = '<div style="grid-column: 1/-1; text-align: center; padding: 40px; color: var(--gray-500);">Không tìm thấy chữ Hán phù hợp.</div>';
        return;
    }

    container.innerHTML = list.map(item => `
        <div class="kanji-card">
            <div class="kanji-header">
                <div class="kanji-char-box jp-text">${item.char}</div>
                <div class="kanji-meta">
                    <div class="kanji-hv">${item.hv}</div>
                    <div class="kanji-meaning">${item.meaning}</div>
                    <div class="kanji-sub-row">
                        <span class="kanji-tag">${item.lessonName}</span>
                        <span class="kanji-tag">${item.strokes} nét</span>
                    </div>
                </div>
            </div>

            <div class="kanji-detail-box">
                <div class="kanji-reading-item">
                    <strong>KUN:</strong> <span class="jp-text">${item.kun || '—'}</span>
                </div>
                <div class="kanji-reading-item">
                    <strong>ON:</strong> <span class="jp-text">${item.on || '—'}</span>
                </div>
                <div class="kanji-reading-item">
                    <strong>Chiết tự:</strong> <span>${item.formula}</span>
                </div>
            </div>

            <div class="kanji-mnemonic">
                💡 <strong>Mẹo nhớ:</strong> ${item.mnemonic}
            </div>

            <ul class="kanji-words">
                ${(item.examples || []).map(ex => `
                    <li class="kanji-word-item">
                        <span class="kw-jp jp-text">${ex.word} (${ex.reading})</span>
                        <span class="kw-vi">${ex.vi}</span>
                    </li>
                `).join('')}
            </ul>
        </div>
    `).join('');
}

function filterKanji(lesson, btn) {
    currentKanjiFilter = lesson;
    if (btn) {
        btn.parentElement.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
    }
    applyKanjiFilter();
}

function handleKanjiSearch() {
    applyKanjiFilter();
}

function applyKanjiFilter() {
    const keyword = document.getElementById('kanjiSearchInput').value.trim().toLowerCase();
    let filtered = rawKanji;
    if (currentKanjiFilter !== 'ALL') {
        filtered = filtered.filter(k => k.lesson === currentKanjiFilter);
    }
    if (keyword) {
        filtered = filtered.filter(k => 
            k.char.includes(keyword) ||
            k.hv.toLowerCase().includes(keyword) ||
            k.meaning.toLowerCase().includes(keyword) ||
            (k.kun && k.kun.toLowerCase().includes(keyword)) ||
            (k.on && k.on.toLowerCase().includes(keyword))
        );
    }
    renderKanji(filtered);
}


    // ==========================================
    // 1. NATIVE JAPANESE VOICE ENGINE (Unified via audio-engine.js)
    // ==========================================



// Render Quiz Questions
function renderQuiz() {
    const container = document.getElementById('questionsContainer');
    container.innerHTML = quizData.map((item, idx) => `
        <div class="question-card" id="qCard_${item.id}">
            <div class="q-header">
                <span class="q-num">Câu ${idx + 1} / ${quizData.length}</span>
                <span class="q-category">${item.lesson} • ${item.category}</span>
            </div>
            <div class="q-text jp-text">${item.q}</div>
            <div class="options-list">
                ${item.options.map((opt, oIdx) => `
                    <button class="opt-btn" id="optBtn_${item.id}_${oIdx}" onclick="selectAnswer(${item.id}, ${oIdx})">
                        <span class="opt-key">${['A', 'B', 'C', 'D'][oIdx]}</span>
                        <span class="jp-text">${opt}</span>
                    </button>
                `).join('')}
            </div>
            <div class="q-explain" id="explain_${item.id}">
                💡 <strong>Giải thích chi tiết:</strong> ${item.explain}
            </div>
        </div>
    `).join('');
}

function selectAnswer(qId, selectedIdx) {
    if (userAnswers[qId] !== undefined) return; // Đã trả lời rồi thì không đổi

    userAnswers[qId] = selectedIdx;
    const qItem = quizData.find(q => q.id === qId);
    const correctIdx = qItem.correct;

    // Vô hiệu hóa các nút trong câu
    qItem.options.forEach((_, idx) => {
        const btn = document.getElementById(`optBtn_${qId}_${idx}`);
        btn.disabled = true;
        if (idx === correctIdx) {
            btn.classList.add('correct');
        } else if (idx === selectedIdx) {
            btn.classList.add('wrong');
        }
    });

    // Hiển thị giải thích
    const explainEl = document.getElementById(`explain_${qId}`);
    explainEl.style.display = 'block';

    // Cập nhật điểm
    updateScore();
}

function updateScore() {
    let correctCount = 0;
    let answeredCount = Object.keys(userAnswers).length;

    quizData.forEach(q => {
        if (userAnswers[q.id] === q.correct) {
            correctCount++;
        }
    });

    const percent = Math.round((correctCount / quizData.length) * 100);
    document.getElementById('scoreDisplay').innerText = correctCount;
    document.getElementById('quizProgressText').innerText = 
        `Đã làm: ${answeredCount}/${quizData.length} câu • Tỷ lệ đúng: ${percent}%`;

    if (answeredCount === quizData.length) {
        let rank = "🏆 XUẤT SẮC!";
        if (percent < 60) rank = "⚠️ CẦN ÔN TẬP THÊM!";
        else if (percent < 80) rank = "👍 KHÁ TỐT!";
        else if (percent < 90) rank = "🌟 RẤT GIỎI!";

        document.getElementById('quizStatusTitle').innerText = 
            `HOÀN THÀNH: ${correctCount}/${quizData.length} ĐIỂM (${percent}%) - ${rank}`;
    }
}

function resetQuiz() {
    userAnswers = {};
    document.getElementById('scoreDisplay').innerText = '0';
    document.getElementById('quizStatusTitle').innerText = 'Bài Thi Thử Trọng Tâm Bài 5 - 8 (30 Câu Chuẩn Sư Phạm)';
    document.getElementById('quizProgressText').innerText = `Đã làm: 0/${quizData.length} câu • Điểm số: 0%`;
    renderQuiz();
    window.scrollTo({ top: document.getElementById('tab-quiz').offsetTop - 60, behavior: 'smooth' });
}

// Khởi tạo ban đầu
document.addEventListener('DOMContentLoaded', () => {
    applyVocabFilter();
    renderKanji(rawKanji);
    renderQuiz();
    renderMinatoData();
});
