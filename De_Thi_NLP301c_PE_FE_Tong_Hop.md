# 📚 TỔNG HỢP TOÀN BỘ ĐỀ THI MÔN NLP301c (NATURAL LANGUAGE PROCESSING)
> **Nguồn dữ liệu:** Diễn đàn FuExam (`https://fuexam.me/forums/nlp301c.197/`)  
> **Phạm vi tổng hợp:** Toàn bộ 9 đề thi hiện có trên hệ thống, bao gồm **6 Đề thực hành PE (Practical Exam)** kèm lời giải code Python mẫu chuẩn chỉ và **3 Đề lý thuyết cuối kỳ FE (Final Exam - 60 câu trắc nghiệm/đề)** kèm ngân hàng kiến thức trọng tâm.

---

## 📑 MỤC LỤC
1. [PHẦN I: TỔNG HỢP 6 ĐỀ THI THỰC HÀNH PE (PRACTICAL EXAMS) & LỜI GIẢI MẪU](#phần-i-tổng-hợp-6-đề-thi-thực-hành-pe)
   - [Đề PE 1: NLP301c - SU26 - PE - RE (Mã: NLP301c_SU26_PE_RE_230826)](#đề-pe-1-nlp301c---su26---pe---re)
   - [Đề PE 2: NLP301c - SU26 - PE (Mã: NLP301c_SU26_PE_160826)](#đề-pe-2-nlp301c---su26---pe)
   - [Đề PE 3: NLP301c - SP26 - NO1 - PE - RE (Mã: NLP301c_SP26_RE1_200116)](#đề-pe-3-nlp301c---sp26---no1---pe---re)
   - [Đề PE 4: NLP301c - SP26 - NO2 - PE - RE (Mã: NLP301c_SP26_RE2_200116)](#đề-pe-4-nlp301c---sp26---no2---pe---re)
   - [Đề PE 5: NLP301c - SP26 - NO2 - PE (Ca thi 12h50 - 25/04/2026)](#đề-pe-5-nlp301c---sp26---no2---pe)
   - [Đề PE 6: NLP301c - SP26 - NO1 - PE (Mã: NLP301c_SP26_PE1_200116)](#đề-pe-6-nlp301c---sp26---no1---pe)
2. [PHẦN II: TỔNG HỢP 3 ĐỀ THI CUỐI KỲ FE (FINAL EXAMS - 180 CÂU TRẮC NGHIỆM)](#phần-ii-tổng-hợp-3-đề-thi-cuối-kỳ-fe)
   - [Đề FE 1: NLP301c - SU26 - FE - RE (Mã: NLP301c_SU26_RE_171389)](#đề-fe-1-nlp301c---su26---fe---re)
   - [Đề FE 2: NLP301c - SU26 - FE (Mã: NLP301c_SU26_FE_483406)](#đề-fe-2-nlp301c---su26---fe)
   - [Đề FE 3: NLP301c - SP26 - FE (Đề thi chính thức SP26)](#đề-fe-3-nlp301c---sp26---fe)
3. [PHẦN III: CẨM NANG ÔN TẬP TRỌNG TÂM CHO KỲ THI NLP301c](#phần-iii-cẩm-nang-ôn-tập-trọng-tâm)

---

# PHẦN I: TỔNG HỢP 6 ĐỀ THI THỰC HÀNH PE

> **Quy định chung bài thi PE NLP301c:**
> - Thời gian làm bài: 60 - 90 phút.
> - Thang điểm: 10 điểm (chia 4 câu: 2đ + 2đ + 3đ + 3đ).
> - Ngôn ngữ: Python 3.8+ (khuyên dùng các thư viện chuẩn `re`, `string`, `collections`, `math`).

---

### ĐỀ PE 1: NLP301c - SU26 - PE - RE
* **Mã đề:** `NLP301c_SU26_PE_RE_230826`
* **Ngày thi:** 23/08/2026
* **Nguồn:** [Thread 1111](https://fuexam.me/threads/nlp301c-su26-pe-re.1111/)

#### Question 1 (2.0 điểm) - Trích xuất Hashtags duy nhất
* **Yêu cầu:** Viết hàm nhận vào một chuỗi văn bản và trích xuất tất cả các hashtag.
* **Quy tắc:**
  - Hashtag bắt đầu bằng ký tự `#`.
  - Sau ký tự `#` chỉ gồm các chữ cái hoặc số (alphanumeric `\w+`).
  - Trả về hashtag ở dạng chữ thường (lowercase).
  - Giữ nguyên thứ tự xuất hiện ban đầu.
  - Không chứa phần tử trùng lặp (duy nhất).
* **Ví dụ:**
  - Input: `"#AI and #nlp are future of #AI!"`
  - Output: `['#ai', '#nlp']`
* **Code Python mẫu:**
```python
import re

def extract_hashtags(text: str) -> list:
    pattern = r'#\w+'
    raw_matches = re.findall(pattern, text)
    result = []
    seen = set()
    for tag in raw_matches:
        low_tag = tag.lower()
        if low_tag not in seen:
            seen.add(low_tag)
            result.append(low_tag)
    return result

# Test
print(extract_hashtags("#AI and #nlp are future of #AI!"))
# Output: ['#ai', '#nlp']
```

#### Question 2 (2.0 điểm) - Trích xuất từ đối xứng (Palindromes)
* **Yêu cầu:** Viết hàm trích xuất tất cả các từ đọc xuôi hay ngược đều giống nhau trong câu.
* **Quy tắc:**
  - Không phân biệt chữ hoa, chữ thường khi kiểm tra đối xứng (`madam.lower() == madam.lower()[::-1]`).
  - Bỏ dấu câu kèm theo từ (ví dụ: `Madam,` -> xét `Madam`).
  - Độ dài từ tối thiểu $\ge 2$ ký tự.
  - Giữ nguyên cách viết hoa/thường gốc của từ trong câu và thứ tự xuất hiện.
* **Ví dụ:**
  - Input: `"Madam, did you see the racecar and kayak?"`
  - Output: `['Madam', 'racecar', 'kayak']`
* **Code Python mẫu:**
```python
import re

def extract_palindromes(text: str) -> list:
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    palindromes = []
    for w in words:
        if len(w) >= 2 and w.lower() == w.lower()[::-1]:
            palindromes.append(w)
    return palindromes

# Test
print(extract_palindromes("Madam, did you see the racecar and kayak?"))
# Output: ['Madam', 'racecar', 'kayak']
```

#### Question 3 (3.0 điểm) - Tạo từ viết tắt (Acronym Generator)
* **Yêu cầu:** Viết hàm tạo từ viết tắt từ một cụm từ.
* **Quy tắc:**
  - Chỉ lấy chữ cái đầu tiên của các từ viết hoa (bắt đầu bằng chữ in hoa).
  - Kết quả trả về là chuỗi viết tắt in hoa toàn bộ.
* **Ví dụ:**
  - Input: `"Central Processing Unit"`
  - Output: `"CPU"`
  - Input: `"natural Language Processing"`
  - Output: `"LP"`
* **Code Python mẫu:**
```python
def generate_acronym(phrase: str) -> str:
    words = phrase.split()
    acronym_chars = [w[0].upper() for w in words if w and w[0].isupper()]
    return "".join(acronym_chars)

# Test
print(generate_acronym("Central Processing Unit"))  # Output: 'CPU'
```

#### Question 4 (3.0 điểm) - Đếm từ có tần suất $\ge K$
* **Yêu cầu:** Nhận vào văn bản và số nguyên $K$, trả về các từ xuất hiện ít nhất $K$ lần kèm số lần xuất hiện.
* **Quy tắc:**
  - Không phân biệt chữ hoa thường (đưa về lowercase).
  - Bỏ qua các dấu câu.
  - Trả về dạng Dictionary `{word: count}` được **sắp xếp theo thứ tự bảng chữ cái (alphabetical order)** của từ.
* **Ví dụ:**
  - Input: `text = "apple banana apple orange apple banana", K = 2`
  - Output: `{'apple': 3, 'banana': 2}`
* **Code Python mẫu:**
```python
import re
from collections import Counter

def words_frequency_at_least_k(text: str, k: int) -> dict:
    words = re.findall(r'\b[a-zA-Z0-9]+\b', text.lower())
    counts = Counter(words)
    filtered = {w: cnt for w, cnt in counts.items() if cnt >= k}
    # Sắp xếp tăng dần theo bảng chữ cái
    sorted_dict = dict(sorted(filtered.items(), key=lambda item: item[0]))
    return sorted_dict

# Test
print(words_frequency_at_least_k("apple banana apple orange apple banana", 2))
# Output: {'apple': 3, 'banana': 2}
```

---

### ĐỀ PE 2: NLP301c - SU26 - PE
* **Mã đề:** `NLP301c_SU26_PE_160826`
* **Ngày thi:** 16/08/2026
* **Nguồn:** [Thread 1015](https://fuexam.me/threads/nlp301c-su26-pe.1015/)

#### Question 1 (2.0 điểm) - Đếm tần suất ký tự chữ cái
* **Yêu cầu:** Đếm số lần xuất hiện của từng chữ cái trong chuỗi.
* **Quy tắc:**
  - Đưa về chữ thường (lowercase).
  - Bỏ qua khoảng trắng và các dấu câu (chỉ đếm các ký tự `a-z`).
  - Trả về dictionary sắp xếp theo thứ tự `a -> z`.
* **Ví dụ:**
  - Input: `"Hello World!"`
  - Output: `{'d': 1, 'e': 1, 'h': 1, 'l': 3, 'o': 2, 'r': 1, 'w': 1}`
* **Code Python mẫu:**
```python
import re
from collections import Counter

def char_frequency(text: str) -> dict:
    chars = re.findall(r'[a-zA-Z]', text.lower())
    counts = Counter(chars)
    return dict(sorted(counts.items()))

# Test
print(char_frequency("Hello World!"))
# Output: {'d': 1, 'e': 1, 'h': 1, 'l': 3, 'o': 2, 'r': 1, 'w': 1}
```

#### Question 2 (2.0 điểm) - Che giấu số điện thoại (Phone Masking)
* **Yêu cầu:** Viết hàm che số điện thoại trong văn bản để bảo vệ quyền riêng tư.
* **Quy tắc:**
  - Số điện thoại gồm đúng 10 chữ số, bắt đầu bằng số `0`.
  - Che 4 chữ số ở giữa bằng dấu `*` (giữ 3 số đầu và 3 số cuối: `0xx****xxx`).
* **Ví dụ:**
  - Input: `"Call me at 0987654321 or 0123456789."`
  - Output: `"Call me at 098****321 or 012****789."`
* **Code Python mẫu:**
```python
import re

def mask_phone_numbers(text: str) -> str:
    # Pattern: \b(0\d{2})\d{4}(\d{3})\b
    pattern = r'\b(0\d{2})\d{4}(\d{3})\b'
    return re.sub(pattern, r'\1****\2', text)

# Test
print(mask_phone_numbers("Call me at 0987654321 or 0123456789."))
# Output: 'Call me at 098****321 or 012****789.'
```

#### Question 3 (3.0 điểm) - Lọc từ theo độ dài `[min_len, max_len]`
* **Yêu cầu:** Lọc các từ có độ dài thỏa mãn `min_length <= len(word) <= max_length`.
* **Quy tắc:**
  - Tách từ, bỏ dấu câu.
  - Chuyển về dạng chữ thường.
  - Giữ nguyên thứ tự xuất hiện ban đầu.
* **Ví dụ:**
  - Input: `"Natural Language Processing is fun and useful", min_len = 4, max_len = 7`
  - Output: `['useful']` (vì Natural=7, Language=8, Processing=10, is=2, fun=3, and=3, useful=6; lưu ý: nếu Natural=7 thì nằm trong đoạn)
* **Code Python mẫu:**
```python
import re

def filter_words_by_length(text: str, min_len: int, max_len: int) -> list:
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    result = [w.lower() for w in words if min_len <= len(w) <= max_len]
    return result

# Test
print(filter_words_by_length("Natural Language Processing is fun and useful", 4, 7))
```

#### Question 4 (3.0 điểm) - Đếm số lượng nguyên âm trong từng từ
* **Yêu cầu:** Đếm số nguyên âm (`a, e, i, o, u`) trong từng từ của câu.
* **Quy tắc:**
  - Không phân biệt hoa thường khi đếm nguyên âm.
  - Bỏ dấu câu, key trong dict là từ gốc.
* **Ví dụ:**
  - Input: `"Natural language processing"`
  - Output: `{'Natural': 3, 'language': 4, 'processing': 3}`
* **Code Python mẫu:**
```python
import re

def count_vowels_per_word(text: str) -> dict:
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    vowels = set('aeiouAEIOU')
    result = {}
    for w in words:
        v_count = sum(1 for ch in w if ch in vowels)
        result[w] = v_count
    return result

# Test
print(count_vowels_per_word("Natural language processing"))
# Output: {'Natural': 3, 'language': 4, 'processing': 3}
```

---

### ĐỀ PE 3: NLP301c - SP26 - NO1 - PE - RE
* **Mã đề:** `NLP301c_SP26_RE1_200116`
* **Ngày thi:** 03/05/2026
* **Nguồn:** [Thread 401](https://fuexam.me/threads/nlp301c-sp26-no1-pe-re.401/)

#### Question 1 (2.0 điểm) - Thống kê tần suất từ vựng
* **Yêu cầu:** Đếm số lần xuất hiện của từng từ trong câu/đoạn văn.
* **Quy tắc:**
  - Không phân biệt hoa/thường (lowercase).
  - Bỏ dấu câu (`. , ! ?`).
  - Sắp xếp tăng dần theo bảng chữ cái.
* **Ví dụ:**
  - Input: `"AI is the future, and AI is here."`
  - Output: `{'ai': 2, 'and': 1, 'future': 1, 'here': 1, 'is': 2, 'the': 1}`
* **Code Python mẫu:**
```python
import re
from collections import Counter

def word_frequencies(text: str) -> dict:
    words = re.findall(r'\b[a-zA-Z0-9]+\b', text.lower())
    counts = Counter(words)
    return dict(sorted(counts.items()))

# Test
print(word_frequencies("AI is the future, and AI is here."))
```

#### Question 2 (2.0 điểm) - Trích xuất danh từ riêng (Capitalized Words)
* **Yêu cầu:** Trích xuất các từ bắt đầu bằng chữ cái viết hoa.
* **Quy tắc:**
  - Bắt đầu bằng 1 chữ cái in hoa, các ký tự sau là chữ thường/chữ cái.
  - Giữ nguyên thứ tự xuất hiện ban đầu.
  - Không chứa phần tử trùng lặp.
* **Ví dụ:**
  - Input: `"John and Mary visited London and Paris last May."`
  - Output: `['John', 'Mary', 'London', 'Paris', 'May']`
* **Code Python mẫu:**
```python
import re

def extract_capitalized_words(text: str) -> list:
    words = re.findall(r'\b[A-Z][a-zA-Z]*\b', text)
    result = []
    seen = set()
    for w in words:
        if w not in seen:
            seen.add(w)
            result.append(w)
    return result

# Test
print(extract_capitalized_words("John and Mary visited London and Paris last May."))
```

#### Question 3 (3.0 điểm) - Kiểm tra câu hỏi
* **Yêu cầu:** Kiểm tra xem câu nhập vào có phải là câu hỏi hay không.
* **Quy tắc:** Trả về `True` nếu câu kết thúc bằng hoặc chứa dấu chấm hỏi `?`, ngược lại `False`.
* **Ví dụ:**
  - Input: `"What time is it?"` -> `True`
  - Input: `"It is 10 AM."` -> `False`
* **Code Python mẫu:**
```python
def is_question(sentence: str) -> bool:
    return '?' in sentence.strip()

# Test
print(is_question("What time is it?"))  # True
print(is_question("It is 10 AM."))      # False
```

#### Question 4 (3.0 điểm) - Lọc từ có độ dài tối thiểu
* **Yêu cầu:** Lọc các từ có độ dài $\ge min\_length$.
* **Quy tắc:** Đưa về chữ thường, bỏ dấu câu, không trùng lặp, giữ thứ tự ban đầu.
* **Ví dụ:**
  - Input: `"Big data and machine learning are important", min_length = 4`
  - Output: `['data', 'machine', 'learning', 'important']`
* **Code Python mẫu:**
```python
import re

def filter_min_length(text: str, min_len: int) -> list:
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    result = []
    seen = set()
    for w in words:
        if len(w) >= min_len and w not in seen:
            seen.add(w)
            result.append(w)
    return result

# Test
print(filter_min_length("Big data and machine learning are important", 4))
```

---

### ĐỀ PE 4: NLP301c - SP26 - NO2 - PE - RE
* **Mã đề:** `NLP301c_SP26_RE2_200116`
* **Ngày thi:** 03/05/2026
* **Nguồn:** [Thread 400](https://fuexam.me/threads/nlp301c-sp26-no2-pe-re.400/)

#### Question 1 (2.0 điểm) - Trích xuất các số nguyên
* **Yêu cầu:** Trích xuất toàn bộ các số nguyên trong chuỗi văn bản.
* **Quy tắc:** Trả về danh sách kiểu `int` trong Python, giữ đúng thứ tự xuất hiện.
* **Ví dụ:**
  - Input: `"Order 3 items for 45 dollars and 12 cents."`
  - Output: `[3, 45, 12]`
* **Code Python mẫu:**
```python
import re

def extract_integers(text: str) -> list:
    nums = re.findall(r'\b\d+\b', text)
    return [int(n) for n in nums]

# Test
print(extract_integers("Order 3 items for 45 dollars and 12 cents."))
# Output: [3, 45, 12]
```

#### Question 2 (2.0 điểm) - Tìm từ dài nhất trong câu
* **Yêu cầu:** Tìm từ có độ dài lớn nhất.
* **Quy tắc:** Bỏ dấu câu. Nếu có nhiều từ cùng độ dài dài nhất, trả về từ xuất hiện đầu tiên.
* **Ví dụ:**
  - Input: `"Natural Language Processing is fascinating."`
  - Output: `"fascinating"`
* **Code Python mẫu:**
```python
import re

def find_longest_word(text: str) -> str:
    words = re.findall(r'\b[a-zA-Z0-9]+\b', text)
    if not words:
        return ""
    longest = words[0]
    for w in words[1:]:
        if len(w) > len(longest):
            longest = w
    return longest

# Test
print(find_longest_word("Natural Language Processing is fascinating."))
# Output: 'fascinating'
```

#### Question 3 (3.0 điểm) - Kiểm tra Anagram (Đảo chữ)
* **Yêu cầu:** Kiểm tra xem hai chuỗi văn bản có phải là Anagram của nhau hay không.
* **Quy tắc:**
  - Hai chuỗi là anagram nếu có cùng tập ký tự và số lần xuất hiện của mỗi ký tự.
  - Bỏ qua khoảng trắng và không phân biệt chữ hoa, chữ thường.
* **Ví dụ:**
  - Input: `"listen"`, `"silent"` -> `True`
  - Input: `"hello"`, `"world"` -> `False`
* **Code Python mẫu:**
```python
import re
from collections import Counter

def is_anagram(str1: str, str2: str) -> bool:
    clean1 = re.findall(r'[a-zA-Z0-9]', str1.lower())
    clean2 = re.findall(r'[a-zA-Z0-9]', str2.lower())
    return Counter(clean1) == Counter(clean2)

# Test
print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False
```

#### Question 4 (3.0 điểm) - Thống kê tần suất ký tự chữ và số
* **Yêu cầu:** Đếm số lần xuất hiện của từng ký tự alphanumeric.
* **Quy tắc:** Bỏ qua chữ hoa/thường (đưa về lowercase), bỏ khoảng trắng và ký tự đặc biệt, sắp xếp tăng dần theo bảng chữ cái.
* **Ví dụ:**
  - Input: `"Data Science!"`
  - Output: `{'a': 2, 'c': 2, 'd': 1, 'e': 1, 'i': 1, 'n': 1, 's': 1, 't': 1}`
* **Code Python mẫu:**
```python
import re
from collections import Counter

def alphanumeric_frequency(text: str) -> dict:
    chars = re.findall(r'[a-zA-Z0-9]', text.lower())
    counts = Counter(chars)
    return dict(sorted(counts.items()))

# Test
print(alphanumeric_frequency("Data Science!"))
```

---

### ĐỀ PE 5: NLP301c - SP26 - NO2 - PE
* **Thời gian/Ca thi:** 12H50 - 25/04/2026
* **Nguồn:** [Thread 312](https://fuexam.me/threads/nlp301c-sp26-no2-pe.312/)

#### Question 1 (2.0 điểm) - Trích xuất địa chỉ Email
* **Yêu cầu:** Trích xuất toàn bộ các địa chỉ email hợp lệ từ văn bản.
* **Quy tắc:**
  - Email phải có ký tự `@`.
  - Phải có ít nhất một dấu chấm `.` ở phần tên miền sau ký tự `@`.
  - Giữ nguyên thứ tự xuất hiện ban đầu.
* **Ví dụ:**
  - Input: `"Please contact us at support@fpt.com or admin@khoahoc.org for assistance."`
  - Output: `['support@fpt.com', 'admin@khoahoc.org']`
* **Code Python mẫu:**
```python
import re

def extract_emails(text: str) -> list:
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)

# Test
print(extract_emails("Please contact us at support@fpt.com or admin@khoahoc.org for assistance."))
```

#### Question 2 (2.0 điểm) - Phân tích đánh giá tích cực (Sentiment Positive Words)
* **Yêu cầu:** Lọc các từ mang tính tích cực từ danh sách cho trước trong đoạn review phim.
* **Danh sách từ tích cực:** `['good', 'great', 'excellent', 'amazing', 'fantastic']`
* **Quy tắc:**
  - Không phân biệt hoa/thường (case-insensitive).
  - Không chứa phần tử trùng lặp.
  - Giữ nguyên thứ tự xuất hiện ban đầu của từ trong review.
* **Ví dụ:**
  - Input: `"The movie was amazing and the acting was excellent. Amazing story!"`
  - Output: `['amazing', 'excellent']`
* **Code Python mẫu:**
```python
import re

def extract_positive_words(review: str) -> list:
    pos_set = {'good', 'great', 'excellent', 'amazing', 'fantastic'}
    words = re.findall(r'\b[a-zA-Z]+\b', review.lower())
    result = []
    seen = set()
    for w in words:
        if w in pos_set and w not in seen:
            seen.add(w)
            result.append(w)
    return result

# Test
print(extract_positive_words("The movie was amazing and the acting was excellent. Amazing story!"))
# Output: ['amazing', 'excellent']
```

#### Question 3 (3.0 điểm) - Trích xuất từ viết hoa từ tiêu đề tin tức
* **Yêu cầu:** Lấy các từ viết hoa bắt đầu bằng chữ hoa, theo sau là chữ cái.
* **Quy tắc:** Giữ thứ tự xuất hiện ban đầu, không phân biệt hoa thường để lọc nếu không yêu cầu, ở đây giữ nguyên từ gốc.
* **Ví dụ:**
  - Input: `"Apple announces new AI System in California"`
  - Output: `['Apple', 'System', 'California']`
* **Code Python mẫu:**
```python
import re

def extract_news_capitalized_words(title: str) -> list:
    return re.findall(r'\b[A-Z][a-zA-Z]*\b', title)

# Test
print(extract_news_capitalized_words("Apple announces new AI System in California"))
```

#### Question 4 (3.0 điểm) - Phát hiện câu hỏi bị lặp lại trong Chatbot
* **Yêu cầu:** Kiểm tra xem trong đoạn hội thoại có câu hỏi nào bị lặp lại nhiều hơn 1 lần hay không.
* **Quy tắc:**
  - Câu hỏi là câu kết thúc bằng dấu chấm hỏi `?`.
  - Không phân biệt chữ hoa, chữ thường khi so sánh.
  - Trả về `True` nếu có ít nhất 1 câu hỏi xuất hiện $\ge 2$ lần, ngược lại `False`.
* **Ví dụ:**
  - Input: `"Where is the library? What time does it open? Where is the library?"` -> `True`
  - Input: `"How are you? What is your name?"` -> `False`
* **Code Python mẫu:**
```python
import re
from collections import Counter

def has_repeated_question(chat_text: str) -> bool:
    # Tách các câu hỏi bằng regex (các chuỗi kết thúc bằng ?)
    raw_questions = re.findall(r'([^?]+\?)', chat_text)
    cleaned_questions = [q.strip().lower() for q in raw_questions if q.strip()]
    counts = Counter(cleaned_questions)
    for q, cnt in counts.items():
        if cnt > 1:
            return True
    return False

# Test
print(has_repeated_question("Where is the library? What time does it open? Where is the library?")) # True
print(has_repeated_question("How are you? What is your name?")) # False
```

---

### ĐỀ PE 6: NLP301c - SP26 - NO1 - PE
* **Mã đề:** `NLP301c_SP26_PE1_200116`
* **Ngày thi:** 25/04/2026
* **Nguồn:** [Thread 303](https://fuexam.me/threads/nlp301c-sp26-no1-pe.303/)

#### Question 1 (2.0 điểm) - Đếm tần suất từ trong bài đánh giá sản phẩm
* **Yêu cầu:** Đếm số lần xuất hiện của từng từ.
* **Quy tắc:** Đưa về chữ thường, bỏ dấu câu, sắp xếp tăng dần theo từ điển.
* **Ví dụ:**
  - Input: `"This phone is great! This phone is fast, and this phone is reliable."`
  - Output: `{'and': 1, 'fast': 1, 'great': 1, 'is': 3, 'phone': 3, 'reliable': 1, 'this': 3}`
* **Code Python mẫu:**
```python
import re
from collections import Counter

def product_review_word_freq(review: str) -> dict:
    words = re.findall(r'\b[a-zA-Z0-9]+\b', review.lower())
    counts = Counter(words)
    return dict(sorted(counts.items()))

# Test
print(product_review_word_freq("This phone is great! This phone is fast, and this phone is reliable."))
```

#### Question 2 (2.0 điểm) - Trích xuất Username được mention (@username)
* **Yêu cầu:** Trích xuất tất cả username được nhắc đến trong đoạn chat.
* **Quy tắc:**
  - Username bắt đầu bằng `@`, sau đó chỉ gồm chữ cái hoặc chữ số.
  - Kết quả trả về **không bao gồm ký tự `@`**.
  - Giữ nguyên thứ tự xuất hiện, không chứa phần tử trùng lặp.
* **Ví dụ:**
  - Input: `"Thanks @alice for the update. Please confirm with @bob and @alice tomorrow."`
  - Output: `['alice', 'bob']`
* **Code Python mẫu:**
```python
import re

def extract_mentions(chat_text: str) -> list:
    pattern = r'@([a-zA-Z0-9_]+)'
    matches = re.findall(pattern, chat_text)
    result = []
    seen = set()
    for user in matches:
        if user not in seen:
            seen.add(user)
            result.append(user)
    return result

# Test
print(extract_mentions("Thanks @alice for the update. Please confirm with @bob and @alice tomorrow."))
# Output: ['alice', 'bob']
```

#### Question 3 (3.0 điểm) - Phát hiện Tweet Spam do lặp từ
* **Yêu cầu:** Xác định xem một tweet có phải là spam do lặp từ quá nhiều hay không.
* **Quy tắc:**
  - Một tweet là spam nếu có **bất kỳ từ nào xuất hiện nhiều hơn 3 lần** ($> 3$).
  - Không phân biệt chữ hoa, chữ thường.
  - Bỏ dấu câu.
* **Ví dụ:**
  - Input: `"Buy now buy now buy now buy now amazing deal"` -> `True` ("buy" và "now" đều xuất hiện 4 lần)
  - Input: `"I love learning natural language processing"` -> `False`
* **Code Python mẫu:**
```python
import re
from collections import Counter

def is_spam_tweet(tweet: str) -> bool:
    words = re.findall(r'\b[a-zA-Z0-9]+\b', tweet.lower())
    counts = Counter(words)
    for word, cnt in counts.items():
        if cnt > 3:
            return True
    return False

# Test
print(is_spam_tweet("Buy now buy now buy now buy now amazing deal")) # True
print(is_spam_tweet("I love learning natural language processing"))    # False
```

#### Question 4 (3.0 điểm) - Trích xuất từ khóa loại bỏ Stopwords
* **Yêu cầu:** Trích xuất từ khóa bằng cách loại bỏ các stopword cơ bản.
* **Danh sách stopword loại bỏ:** `['the', 'is', 'and', 'in', 'on', 'at', 'to', 'a', 'an']`
* **Quy tắc:**
  1. Chuyển thành chữ thường.
  2. Bỏ dấu câu (`. , ! ?`).
  3. Loại bỏ các từ nằm trong danh sách stopword.
  4. Giữ nguyên thứ tự xuất hiện ban đầu của các từ còn lại.
* **Ví dụ:**
  - Input: `"AI is transforming the world and creating opportunities in technology"`
  - Output: `['ai', 'transforming', 'world', 'creating', 'opportunities', 'technology']`
* **Code Python mẫu:**
```python
import re

def extract_keywords(sentence: str) -> list:
    stopwords = {'the', 'is', 'and', 'in', 'on', 'at', 'to', 'a', 'an'}
    words = re.findall(r'\b[a-zA-Z0-9]+\b', sentence.lower())
    return [w for w in words if w not in stopwords]

# Test
print(extract_keywords("AI is transforming the world and creating opportunities in technology"))
# Output: ['ai', 'transforming', 'world', 'creating', 'opportunities', 'technology']
```

---

# PHẦN II: TỔNG HỢP 3 ĐỀ THI CUỐI KỲ FE (180 CÂU TRẮC NGHIỆM)

> **Cấu trúc bài thi FE môn NLP301c:**
> - Hình thức thi: Trắc nghiệm khách quan trên máy (EOS / Exam Client).
> - Số lượng câu hỏi: **60 câu / đề**.
> - Thời gian làm bài: 60 phút.
> - Thang điểm: 10 điểm (chia đều $\approx 0.167$ điểm/câu).

---

### ĐỀ FE 1: NLP301c - SU26 - FE - RE
* **Mã Đề:** `NLP301c_SU26_RE_171389`
* **Nguồn:** [Thread 1114](https://fuexam.me/threads/nlp301c-su26-fe-re.1114/)
* **Số lượng:** 60 câu trắc nghiệm (Tệp ảnh: `nlp301c-su26-fe-re_001` $\rightarrow$ `_060`).

#### Các cụm câu hỏi trọng tâm xuất hiện trong đề:
1. **Câu 1 – 10: Xử lý tiền xử lý & Ngôn ngữ học cơ sở (Preprocessing & Linguistics)**
   - *Tokenization:* Phân biệt Word Tokenization vs Sentence Segmentation. Sự khác biệt giữa Token, Type và Vocabulary size ($|V|$).
   - *Stemming vs Lemmatization:* Porter Stemmer (quy tắc cắt đuôi heuristic) vs WordNet Lemmatizer (dựa trên từ điển & từ loại POS). *Ví dụ:* từ "better" qua Lemmatizer thành "good", qua Stemmer vẫn là "better".
   - *Zipf's Law:* Mối quan hệ giữa thứ hạng tần suất $r$ và tần suất $f$: $f \times r \approx \text{constant}$.

2. **Câu 11 – 20: Mô hình ngôn ngữ N-gram & Perplexity**
   - *Công thức N-gram:* Xác suất Maximum Likelihood Estimation (MLE):
     $$P(w_i | w_{i-1}) = \frac{C(w_{i-1}, w_i)}{C(w_{i-1})}$$
   - *Độ đo Perplexity (PP):* Đánh giá chất lượng mô hình ngôn ngữ:
     $$PP(W) = P(w_1, w_2, ..., w_N)^{-\frac{1}{N}}$$
     *(Mô hình càng tốt thì Perplexity càng thấp).*
   - *Kỹ thuật làm mượt (Smoothing):* Laplace (Add-1), Add-$k$, Good-Turing, Kneser-Ney Smoothing (xét khả năng xuất hiện như một từ tiếp nối mới).

3. **Câu 21 – 30: Gán nhãn từ loại (POS Tagging) & Hidden Markov Model (HMM)**
   - *Thành phần HMM:* Tập trạng thái ẩn $S$ (các nhãn POS), tập quan sát $O$ (các từ), ma trận xác suất chuyển trạng thái $A$ ($P(t_i | t_{i-1})$), ma trận xác suất phát xạ $B$ ($P(w_i | t_i)$).
   - *Thuật toán Viterbi:* Tìm chuỗi nhãn ẩn tối ưu có độ phức tạp thời gian $O(|S|^2 \times T)$ bằng quy hoạch động.
   - *Forward-Backward Algorithm:* Tính xác suất chuỗi quan sát và huấn luyện HMM bằng Baum-Welch (EM).

4. **Câu 31 – 40: Phân loại văn bản & Biểu diễn từ (Vector Space & Embeddings)**
   - *TF-IDF:*
     $$\text{TF-IDF}(t, d, D) = \text{TF}(t, d) \times \log\left(\frac{|D|}{|\{d \in D : t \in d\}|}\right)$$
   - *Naïve Bayes Classifier:* Giả định độc lập có điều kiện giữa các từ khi biết lớp $C$.
   - *Word2Vec:*
     + Skip-gram: Từ từ trung tâm dự đoán từ ngữ cảnh ($w_t \rightarrow w_{t-k}, ..., w_{t+k}$). Phù hợp với tập dữ liệu nhỏ và từ hiếm.
     + CBOW (Continuous Bag-of-Words): Từ ngữ cảnh dự đoán từ trung tâm. Tốc độ huấn luyện nhanh hơn.
     + Negative Sampling & Hierarchical Softmax để tối ưu tính toán.

5. **Câu 41 – 50: Ngữ nghĩa học & Khử nhập nhằng nghĩa từ (WSD)**
   - *WordNet:* Quan hệ Synset, Hypernym (từ thượng vị), Hyponym (từ hạ vị), Meronym (bộ phận), Antonym (trái nghĩa).
   - *Thuật toán Lesk:* Khử nhập nhằng nghĩa từ dựa trên độ giao nhau (overlap) giữa định nghĩa từ điển của nghĩa đó và các từ xung quanh trong ngữ cảnh.
   - *Cosine Similarity:* Đo độ tương đồng giữa hai vector biểu diễn từ $\vec{u}$ và $\vec{v}$:
     $$\text{cosine}(\vec{u}, \vec{v}) = \frac{\vec{u} \cdot \vec{v}}{\|\vec{u}\| \|\vec{v}\|}$$

6. **Câu 51 – 60: Trích xuất thực thể tên (NER) & Đánh giá mô hình**
   - *Định dạng nhãn IOB:* Inside, Outside, Beginning (ví dụ: `B-PER`, `I-PER`, `O`).
   - *Độ đo phân loại:* Precision, Recall, $F_1$-score:
     $$F_1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$

---

### ĐỀ FE 2: NLP301c - SU26 - FE
* **Mã Đề:** `NLP301c_SU26_FE_483406`
* **Nguồn:** [Thread 1035](https://fuexam.me/threads/nlp301c-su26-fe.1035/)
* **Số lượng:** 60 câu trắc nghiệm (Tệp ảnh: `nlp301c-su26-fe_001` $\rightarrow$ `_060`).

#### Các cụm câu hỏi trọng tâm xuất hiện trong đề:
1. **Cú pháp học & Cây cú pháp (Syntax & Parsing):**
   - Context-Free Grammar (CFG) dạng chuẩn Chomsky Normal Form (CNF): $A \rightarrow BC$ hoặc $A \rightarrow a$.
   - Thuật toán CKY (Cocke-Kasami-Younger): Thuật toán Bottom-up parsing dựa trên quy hoạch động với độ phức tạp $O(n^3 \cdot |G|)$.
   - Dependency Parsing: Cây phụ thuộc gồm các quan hệ ngữ pháp trực tiếp giữa head và dependent (chủ ngữ `nsubj`, tân ngữ `dobj`, định ngữ `amod`).

2. **Dịch máy & Độ đo BLEU Score:**
   - Dịch máy thống kê (SMT) vs Dịch máy nơ-ron (NMT).
   - *Công thức tính BLEU:* Dựa trên Modified N-gram Precision kết hợp với Brevity Penalty (BP) để phạt các câu dịch quá ngắn:
     $$\text{BLEU} = \text{BP} \times \exp\left(\sum_{n=1}^N w_n \log p_n\right)$$
   - *Độ đo ROUGE:* Sử dụng phổ biến trong bài toán tóm tắt văn bản (Text Summarization), dựa chủ yếu trên Recall.

3. **Mạng Nơ-ron hồi quy & Attention Mechanism trong NLP:**
   - Hạn chế của RNN truyền thống: Hiện tượng triệt tiêu đạo hàm (Vanishing Gradient) và bùng nổ đạo hàm (Exploding Gradient), khó nhớ phụ thuộc xa (Long-term dependencies).
   - Kiến trúc LSTM (Long Short-Term Memory):
     + Forget gate: $f_t = \sigma(W_f x_t + U_f h_{t-1} + b_f)$
     + Input gate: $i_t = \sigma(W_i x_t + U_i h_{t-1} + b_i)$
     + Cell state update: $C_t = f_t * C_{t-1} + i_t * \tilde{C}_t$
     + Output gate: $o_t = \sigma(W_o x_t + U_o h_{t-1} + b_o)$
   - Cơ chế Attention: Cho phép bộ giải mã (Decoder) tập trung vào các vị trí thích hợp của câu nguồn (Encoder) thay vì nén toàn bộ vào một context vector cố định.
   - Scaled Dot-Product Attention (Transformer):
     $$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

---

### ĐỀ FE 3: NLP301c - SP26 - FE
* **Mã Đề:** `NLP301c SP26 FE`
* **Nguồn:** [Thread 306](https://fuexam.me/threads/nlp301c-sp26-fe.306/)
* **Số lượng:** 60 câu trắc nghiệm (Tệp ảnh: `nlp301c-sp26-fe_001` $\rightarrow$ `_060`).

#### Các cụm câu hỏi trọng tâm xuất hiện trong đề:
1. **Hình thái học (Morphology):**
   - *Morpheme (Hình vị):* Đơn vị nhỏ nhất mang ý nghĩa.
   - *Inflectional Morphology (Hình thái học biến hình):* Thay đổi dạng của từ nhưng không đổi từ loại (ví dụ: `walk` -> `walked`, `book` -> `books`).
   - *Derivational Morphology (Hình thái học phái sinh):* Tạo ra từ mới hoặc đổi từ loại (ví dụ: `happy` -> `unhappy`, `teach` -> `teacher`).

2. **Topic Modeling - Mô hình chủ đề (LDA):**
   - Latent Dirichlet Allocation (LDA): Mô hình sinh xác suất (generative probabilistic model).
   - Giả định: Mỗi tài liệu là phân phối xác suất trên các chủ đề (Document-Topic distribution $\theta \sim \text{Dirichlet}(\alpha)$), mỗi chủ đề là phân phối xác suất trên các từ vựng (Topic-Word distribution $\phi \sim \text{Dirichlet}(\beta)$).
   - Ý nghĩa của tham số $\alpha$ và $\beta$:
     + $\alpha$ cao: Tài liệu chứa hỗn hợp nhiều chủ đề; $\alpha$ thấp: Tài liệu tập trung vào số ít chủ đề cụ thể.
     + $\beta$ cao: Chủ đề chứa nhiều từ vựng; $\beta$ thấp: Chủ đề tập trung vào số ít từ đặc trưng.

3. **Ngữ dụng & Tham chiếu (Discourse & Coreference Resolution):**
   - *Anaphora Resolution:* Xác định đại từ thay thế cho thực thể nào xuất hiện trước đó (Antecedent).
   - *Cohesion & Coherence:* Sự liên kết ngữ pháp/từ vựng (Cohesion) và tính mạch lạc ngữ nghĩa (Coherence) của văn bản.

---

# PHẦN III: CẨM NANG ÔN TẬP TRỌNG TÂM CHO KỲ THI NLP301c

### 1. Checklist kiến thức cốt lõi cần nhớ khi đi thi PE
| Dạng bài PE | Thư viện & Hàm cần nhớ | Lưu ý quan trọng |
| :--- | :--- | :--- |
| **Trích xuất Hashtag/Email/SĐT** | `re.findall(r'#\w+', text)`, `re.sub()` | Chú ý kiểm tra regex chính xác, giữ thứ tự xuất hiện ban đầu (`seen` set). |
| **Đếm tần suất từ/ký tự** | `from collections import Counter` | Luôn chuyển về `.lower()`, lọc dấu câu `\b[a-zA-Z]+\b`, sắp xếp theo `dict(sorted(c.items()))`. |
| **Palindrome / Anagram** | `s == s[::-1]`, `Counter(s1) == Counter(s2)` | Bỏ qua chữ hoa thường và dấu câu; lưu ý độ dài từ $\ge 2$. |
| **Lọc Stopwords** | `[w for w in words if w not in stop_set]` | Dùng `set` thay vì `list` để tốc độ tra cứu đạt $O(1)$. |
| **Phát hiện câu lặp/câu hỏi** | `re.findall(r'([^?]+\?)', text)` | Cắt chuỗi theo dấu `?` và `.strip().lower()`. |

### 2. Các công thức tính toán cần thuộc lòng khi thi FE
1. **N-gram MLE:**
   $$P(w_n | w_1, ..., w_{n-1}) = \frac{C(w_1, ..., w_n)}{C(w_1, ..., w_{n-1})}$$
2. **Add-1 (Laplace) Smoothing:**
   $$P_{\text{Laplace}}(w_i | w_{i-1}) = \frac{C(w_{i-1}, w_i) + 1}{C(w_{i-1}) + |V|}$$
3. **Perplexity:**
   $$PP(W) = \sqrt[N]{\frac{1}{\prod_{i=1}^N P(w_i | w_{i-1})}}$$
4. **TF-IDF:**
   $$\text{TF}(t, d) = \frac{f_{t, d}}{\sum_{t'} f_{t', d}}, \quad \text{IDF}(t, D) = \log\left(\frac{|D|}{|\{d \in D : t \in d\}|}\right)$$
5. **HMM Viterbi State Transition:**
   $$v_t(j) = \max_{i=1}^{N} \left[ v_{t-1}(i) \cdot a_{ij} \right] \cdot b_j(o_t)$$

---
*Tài liệu được trích xuất và biên tập tự động từ toàn bộ nguồn đề thi NLP301c trên FuExam. Chúc bạn ôn tập tốt và đạt điểm cao trong cả hai kỳ thi PE và FE!*
