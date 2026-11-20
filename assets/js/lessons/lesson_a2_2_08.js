/* Marugoto A2-2 Bài 8 (A2-2) - Extracted Data & Logic */
const VOCAB_DATA = [
  {
    "id": 1,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "にちじ",
    "kana": "にちじ",
    "kanji": "日時",
    "romaji": "nichiji",
    "vi": "Ngày giờ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_807cf1856124890b\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_807cf1856124890b)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🕒</text>\n</svg>"
  },
  {
    "id": 2,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "かいじょう",
    "kana": "かいじょう",
    "kanji": "会場",
    "romaji": "kaijou",
    "vi": "Hội trường, địa điểm tổ chức",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_68f5c16bf3de16e0\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_68f5c16bf3de16e0)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏛️</text>\n</svg>"
  },
  {
    "id": 3,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "にゅうじょうりょう",
    "kana": "にゅうじょうりょう",
    "kanji": "入場料",
    "romaji": "nyuujouryou",
    "vi": "Phí vào cửa",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_67614dd2aab47f54\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_67614dd2aab47f54)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎟️</text>\n</svg>"
  },
  {
    "id": 4,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "にゅうじょうむりょう",
    "kana": "にゅうじょうむりょう",
    "kanji": "入場無料",
    "romaji": "nyuujoumuryou",
    "vi": "Vào cửa miễn phí",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_53a5ad989a2cb9cc\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_53a5ad989a2cb9cc)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🆓</text>\n</svg>"
  },
  {
    "id": 5,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "さんかひ",
    "kana": "さんかひ",
    "kanji": "参加費",
    "romaji": "sankahi",
    "vi": "Phí tham gia",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_8bebc20bb11739e1\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_8bebc20bb11739e1)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💵</text>\n</svg>"
  },
  {
    "id": 6,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "はじまります",
    "kana": "はじまります",
    "kanji": "始まります",
    "romaji": "hajimarimasu",
    "vi": "Bắt đầu (tự động từ)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_515bed4871efedac\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_515bed4871efedac)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">▶️</text>\n</svg>"
  },
  {
    "id": 7,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "はじめます",
    "kana": "はじめます",
    "kanji": "始めます",
    "romaji": "hajimemasu",
    "vi": "Bắt đầu (tha động từ)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_483573edaad9c232\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_483573edaad9c232)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎬</text>\n</svg>"
  },
  {
    "id": 8,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "おわります",
    "kana": "おわります",
    "kanji": "終わります",
    "romaji": "owarimasu",
    "vi": "Kết thúc",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_35184912fa636159\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_35184912fa636159)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏁</text>\n</svg>"
  },
  {
    "id": 9,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "やります",
    "kana": "やります",
    "kanji": "やります",
    "romaji": "yarimasu",
    "vi": "Tổ chức, diễn ra",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_5bc655113c3f320f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_5bc655113c3f320f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎪</text>\n</svg>"
  },
  {
    "id": 10,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "プログラム",
    "kana": "プログラム",
    "kanji": "プログラム",
    "romaji": "puroguramu",
    "vi": "Chương trình, lịch trình",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_2f4a8afbb2e95c68\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_2f4a8afbb2e95c68)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📜</text>\n</svg>"
  },
  {
    "id": 11,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "うちわ",
    "kana": "うちわ",
    "kanji": "団扇",
    "romaji": "uchiwa",
    "vi": "Quạt giấy tròn",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_1008a64a148d92ad\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_1008a64a148d92ad)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🪭</text>\n</svg>"
  },
  {
    "id": 12,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "ひろば",
    "kana": "ひろば",
    "kanji": "広場",
    "romaji": "hiroba",
    "vi": "Quảng trường",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_34bca7a8b6186f52\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_34bca7a8b6186f52)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏞️</text>\n</svg>"
  },
  {
    "id": 13,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "ホール",
    "kana": "ホール",
    "kanji": "ホール",
    "romaji": "ho-ru",
    "vi": "Hội trường (hall)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_cf41c1f6df0ab67a\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_cf41c1f6df0ab67a)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏢</text>\n</svg>"
  },
  {
    "id": 14,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "デモンストレーション",
    "kana": "デモンストレーション",
    "kanji": "デモンストレーション",
    "romaji": "demonsutore-shon",
    "vi": "Biểu diễn mẫu",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_1fc9efde0fcd21ce\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_1fc9efde0fcd21ce)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🥋</text>\n</svg>"
  },
  {
    "id": 15,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "おねがい",
    "kana": "おねがい",
    "kanji": "お願い",
    "romaji": "onegai",
    "vi": "Yêu cầu, lời nhờ cậy",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_faece057e72bc70a\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_faece057e72bc70a)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🙏</text>\n</svg>"
  },
  {
    "id": 16,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "いんしょく",
    "kana": "いんしょく",
    "kanji": "飲食",
    "romaji": "inshoku",
    "vi": "Việc ăn uống",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_f9dc02f62a6e1d4a\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_f9dc02f62a6e1d4a)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍔</text>\n</svg>"
  },
  {
    "id": 17,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "ごえんりょください",
    "kana": "ごえんりょください",
    "kanji": "ご遠慮ください",
    "romaji": "goenryo kudasai",
    "vi": "Xin vui lòng tránh / không làm",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_4ae1b6f875e6b3a0\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_4ae1b6f875e6b3a0)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🚫</text>\n</svg>"
  },
  {
    "id": 18,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "おとな",
    "kana": "おとな",
    "kanji": "大人",
    "romaji": "otona",
    "vi": "Người lớn",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_c2516d6a18da9974\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_c2516d6a18da9974)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧑</text>\n</svg>"
  },
  {
    "id": 19,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "れんらくさき",
    "kana": "れんらくさき",
    "kanji": "連絡先",
    "romaji": "renrakusaki",
    "vi": "Thông tin liên lạc",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_ba70217ebf8a07de\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_ba70217ebf8a07de)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📱</text>\n</svg>"
  },
  {
    "id": 20,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "ほんじつ",
    "kana": "ほんじつ",
    "kanji": "本日",
    "romaji": "honjitsu",
    "vi": "Hôm nay (trang trọng)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_43dc4686ebf84c07\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_43dc4686ebf84c07)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📅</text>\n</svg>"
  }
];

const VERB_DATA = [
  {
    "masu": "ならびます",
    "vi": "Xếp hàng",
    "te": "ならんで",
    "form1": "もうならびました (đã xếp hàng rồi)",
    "form2": "まだならんでいません (chưa xếp hàng)",
    "form3": "ならぶ"
  },
  {
    "masu": "はじまります",
    "vi": "Bắt đầu",
    "te": "はじまって",
    "form1": "もうはじまりました (đã bắt đầu rồi)",
    "form2": "まだはじまっていません (vẫn chưa)",
    "form3": "はじまる"
  },
  {
    "masu": "おわります",
    "vi": "Kết thúc",
    "te": "おわって",
    "form1": "もうおわりました",
    "form2": "まだおわっていません",
    "form3": "おわる"
  },
  {
    "masu": "つかれます",
    "vi": "Mệt",
    "te": "つかれて",
    "form1": "すこしつかれました (hơi mệt)",
    "form2": "つかれてから (sau khi mệt)",
    "form3": "つかれる"
  },
  {
    "masu": "かいます",
    "vi": "Mua",
    "te": "かって",
    "form1": "かってから (sau khi mua xong thì...)",
    "form2": "もうかいました",
    "form3": "かう"
  }
];

const QUIZ_DATA = [
  {
    "id": 1,
    "category": "Ngữ pháp",
    "q": "「コンサートは もう [____] か。」 ―― 「はい、10分前に 始まりました。」",
    "options": [
      "始まります",
      "始まって",
      "始まりました",
      "始まった"
    ],
    "correct": 2,
    "explain": "Đã bắt đầu chưa: もう ＋ V-ましたか ➔ 「始まりましたか」.",
    "grammarScope": "official"
  },
  {
    "id": 2,
    "category": "Ngữ pháp",
    "q": "「お昼ごはんは もう 食べましたか。」 ―― 「いいえ、まだ [____]。」",
    "options": [
      "食べていません",
      "食べませんでした",
      "食べます",
      "食べた"
    ],
    "correct": 0,
    "explain": "Trả lời 'vẫn chưa': 『いいえ、まだ V-ていません』 ➔ 「食べていません」.",
    "grammarScope": "official"
  },
  {
    "id": 3,
    "category": "Ngữ pháp",
    "q": "コンサートが何時に始まる [____]、知っていますか。",
    "options": [
      "と",
      "か",
      "ので",
      "まで"
    ],
    "correct": 1,
    "explain": "Câu hỏi gián tiếp dùng mệnh đề thường + か.",
    "grammarScope": "official"
  },
  {
    "id": 4,
    "category": "Từ vựng",
    "q": "たこ焼きを 買うために、長い [____] に 並びました。",
    "options": [
      "まつり",
      "えんそう",
      "コンサート",
      "ぎょうれつ"
    ],
    "correct": 3,
    "explain": "Xếp hàng trong hàng người đông đúc: 「行列 (ぎょうれつ)」."
  },
  {
    "id": 5,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「祭」 có nghĩa là gì?",
    "options": [
      "Lễ hội Nhật Bản",
      "Địa điểm tổ chức",
      "Lễ hội",
      "Phí vào cửa"
    ],
    "correct": 2,
    "explain": "祭 nghĩa là Lễ hội.",
    "scopeKanji": "祭"
  },
  {
    "id": 6,
    "category": "Từ vựng",
    "q": "水槽の 中の 赤い 魚を 紙の ポイですくう 遊びは [____] です。",
    "options": [
      "たこやき",
      "きんぎょすくい",
      "やきそば",
      "おめん"
    ],
    "correct": 1,
    "explain": "Trò chơi vớt cá vàng ngày hội là 「金魚すくい (きんぎょすくい)」."
  },
  {
    "id": 7,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「日本祭」 có nghĩa là gì?",
    "options": [
      "Lễ hội Nhật Bản",
      "Địa điểm tổ chức",
      "Phí vào cửa",
      "Người tham gia"
    ],
    "correct": 0,
    "explain": "日本祭 nghĩa là Lễ hội Nhật Bản.",
    "scopeKanji": "日本祭"
  },
  {
    "id": 8,
    "category": "Hội thoại",
    "q": "太鼓の かっこいい [____] が 遠くから 聞こえてきます。",
    "options": [
      "みず",
      "いろ",
      "あじ",
      "おと"
    ],
    "correct": 3,
    "explain": "Tiếng trống rền vang: 「太鼓の音 (おと)」."
  },
  {
    "id": 9,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「会場」 có nghĩa là gì?",
    "options": [
      "Phí vào cửa",
      "Người tham gia",
      "Vội, gấp",
      "Địa điểm tổ chức"
    ],
    "correct": 3,
    "explain": "会場 nghĩa là Địa điểm tổ chức.",
    "scopeKanji": "会場"
  },
  {
    "id": 10,
    "category": "Từ vựng",
    "q": "ずっと 歩いて いたので、足が [____] しまいました。",
    "options": [
      "ついた",
      "つかれて",
      "ならんで",
      "おわって"
    ],
    "correct": 1,
    "explain": "Mỏi mệt đôi chân: 疲れます ➔ thể TE: 「つかれて」."
  },
  {
    "id": 11,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「入場料」 có nghĩa là gì?",
    "options": [
      "Người tham gia",
      "Vội, gấp",
      "Phí vào cửa",
      "Quyết định"
    ],
    "correct": 2,
    "explain": "入場料 nghĩa là Phí vào cửa.",
    "scopeKanji": "入場料"
  },
  {
    "id": 12,
    "category": "Ngữ pháp",
    "q": "準備は [____] 終わりましたか。",
    "options": [
      "まだ",
      "まで",
      "もう",
      "しか"
    ],
    "correct": 2,
    "explain": "もう hỏi xem việc đã hoàn tất hay chưa.",
    "grammarScope": "official"
  },
  {
    "id": 13,
    "category": "Từ vựng",
    "q": "きつねや ひょっとこの 顔の 形を した かぶり物は [____] です。",
    "options": [
      "ぼうし",
      "おめん",
      "ゆかた",
      "めがね"
    ],
    "correct": 1,
    "explain": "Mặt nạ cáo đeo trong hội là 「お面 (おめん)」."
  },
  {
    "id": 14,
    "category": "Hội thoại",
    "q": "「ちょうど 今、花火が [____] よ！ 見て！」",
    "options": [
      "始まったところだ",
      "終わってしまった",
      "始まらない",
      "始める"
    ],
    "correct": 0,
    "explain": "Vừa đúng lúc pháo hoa khai màn: 「始まったところだ / 始まりましたよ」."
  },
  {
    "id": 15,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「参加者」 có nghĩa là gì?",
    "options": [
      "Người tham gia",
      "Vội, gấp",
      "Quyết định",
      "Biết"
    ],
    "correct": 0,
    "explain": "参加者 nghĩa là Người tham gia.",
    "scopeKanji": "参加者"
  }
];

function escapeLessonText(value) {
    return String(value).replace(/&/g, '&amp;').replace(/</g, '&lt;')
        .replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&#39;');
}

// Render Verb Lab
function initVerbLab() {
    const row = document.getElementById('verbSelectorRow');
    if (!row || !VERB_DATA.length) return;
    row.innerHTML = '';
    VERB_DATA.forEach((v, idx) => {
        const btn = document.createElement('button');
        btn.type = 'button';
        btn.className = `btn-verb-chip ${idx === 0 ? 'active' : ''}`;
        btn.textContent = `${v.masu} (${v.vi})`;
        btn.onclick = () => selectVerb(idx);
        row.appendChild(btn);
    });
    selectVerb(0);
}

function selectVerb(idx) {
    const chips = document.querySelectorAll('.btn-verb-chip');
    chips.forEach((c, i) => c.classList.toggle('active', i === idx));
    const v = VERB_DATA[idx];
    if (!v) return;

    const elMasu = document.getElementById('morphMasu');
    const elVi = document.getElementById('morphVi');
    const elTe = document.getElementById('morphTe');
    const elForm1 = document.getElementById('morphTeIki');
    const elForm2 = document.getElementById('morphTeKi');
    const elForm3 = document.getElementById('morphMashou');

    if (elMasu) elMasu.textContent = v.masu || '---';
    if (elVi) elVi.textContent = v.vi || '---';
    if (elTe) elTe.textContent = v.te || '---';
    if (elForm1) elForm1.textContent = v.form1 || '---';
    if (elForm2) elForm2.textContent = v.form2 || '---';
    if (elForm3) elForm3.textContent = v.form3 || '---';
}

// Render Flashcards
function initFlashcards() {
    const grid = document.getElementById('flashcardGrid');
    if (!grid) return;
    grid.innerHTML = '';
    VOCAB_DATA.forEach(v => {
        const card = document.createElement('button');
        card.type = 'button';
        card.className = 'fc-item';
        card.setAttribute('aria-label', `Nghe ${v.jp}`);
        card.onclick = () => {
            if (typeof speakText === 'function') speakText(v.kana || v.jp);
        };
        card.innerHTML = `
            <span class="fc-svg-wrap" aria-hidden="true">${v.svg}</span>
            <span class="fc-content">
                <span class="fc-jp" lang="ja">${escapeLessonText(v.jp)}</span>
                <span class="fc-kana" lang="ja">${escapeLessonText(v.kana)}</span>
                <span class="fc-romaji">${escapeLessonText(v.romaji)}</span>
                <span class="fc-vi">${escapeLessonText(v.vi)}</span>
                <span class="fc-listen">🔊 Nghe phát âm</span>
            </span>
        `;
        grid.appendChild(card);
    });
}

// Render Quiz
function initQuiz() {
    const c = document.getElementById('quizContainer');
    if (!c) return;
    c.innerHTML = '';
    QUIZ_DATA.forEach((q, qIdx) => {
        const qBox = document.createElement('div');
        qBox.className = 'quiz-card';
        const optsHtml = q.options.map((opt, oIdx) => `
            <button type="button" class="quiz-opt" onclick="checkQuizAnswer(this, ${qIdx}, ${oIdx}, 'a22-reviewed-v2')">${escapeLessonText(opt)}</button>
        `).join('');
        qBox.innerHTML = `
            <div class="quiz-q"><b>Câu ${qIdx + 1}:</b> ${escapeLessonText(q.q)}</div>
            <div class="quiz-opts">${optsHtml}</div>
            <div class="quiz-explain" id="explain-${qIdx}">💡 ${escapeLessonText(q.explain)}</div>
        `;
        c.appendChild(qBox);
    });
}

function checkQuizAnswer(btn, qIdx, oIdx, revision) {
    if (revision !== 'a22-reviewed-v2' || btn.disabled) return;
    const q = QUIZ_DATA[qIdx];
    const parent = btn.parentElement;
    const allBtns = parent.querySelectorAll('.quiz-opt');
    allBtns.forEach(b => b.disabled = true);
    if (oIdx === q.correct) {
        btn.classList.add('correct');
    } else {
        btn.classList.add('wrong');
        allBtns[q.correct].classList.add('correct');
    }
    const exp = document.getElementById(`explain-${qIdx}`);
    if (exp) exp.style.display = 'block';
}

function initLessonInteractive() {
    initVerbLab();
    initFlashcards();
    initQuiz();
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initLessonInteractive);
} else {
    initLessonInteractive();
}

if (typeof VOCAB_DATA !== "undefined") window.VOCAB_DATA = VOCAB_DATA;
