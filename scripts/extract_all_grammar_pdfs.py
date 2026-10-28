# -*- coding: utf-8 -*-
"""
extract_all_grammar_pdfs.py
Extracts and OCRs all pages from the 5 Marugoto Grammar Summary PDFs.
"""

import os
import fitz
import subprocess
import json
import unicodedata

def main():
    pdf_files = [
        f for f in os.listdir(".")
        if "ngu" in unicodedata.normalize("NFD", f).lower() and f.endswith(".pdf")
    ]
    
    # Sort logically
    def sort_key(name):
        n = unicodedata.normalize("NFD", name)
        if "A1" in n and "11" in n: return 1
        if "A1" in n and "15" in n: return 2
        if "A2.1" in n and "L1" in n: return 3
        if "A2.1" in n and "L5" in n: return 4
        if "A2.1" in n and "L9" in n: return 5
        return 99

    pdf_files.sort(key=sort_key)
    
    os.makedirs("tmp_ocr", exist_ok=True)
    all_data = {}

    for pf in pdf_files:
        norm_name = unicodedata.normalize("NFC", pf)
        print(f"\nProcessing {norm_name}...")
        doc = fitz.open(pf)
        pages_text = []

        for p_idx in range(len(doc)):
            page = doc[p_idx]
            # Try get_text first
            raw_text = page.get_text("text").strip()
            
            # If raw_text is very short, perform OCR
            if len(raw_text) < 30:
                img_path = f"tmp_ocr/temp_page_{p_idx}.png"
                pix = page.get_pixmap(dpi=150)
                pix.save(img_path)
                
                try:
                    res = subprocess.run(["./ocr_bin", img_path], capture_output=True, text=True, check=True)
                    ocr_text = res.stdout.strip()
                    pages_text.append({
                        "page": p_idx + 1,
                        "method": "ocr",
                        "text": ocr_text
                    })
                    print(f"  P{p_idx+1} [OCR]: {ocr_text[:60].replace(chr(10), ' ')}...")
                except Exception as e:
                    print(f"  P{p_idx+1} OCR error: {e}")
                    pages_text.append({"page": p_idx + 1, "method": "error", "text": ""})
                finally:
                    if os.path.exists(img_path):
                        os.remove(img_path)
            else:
                pages_text.append({
                    "page": p_idx + 1,
                    "method": "native_text",
                    "text": raw_text
                })
                print(f"  P{p_idx+1} [Native]: {raw_text[:60].replace(chr(10), ' ')}...")

        all_data[norm_name] = pages_text

    with open("grammar_extracted_all.json", "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)

    print("\nExtracted all grammar data to grammar_extracted_all.json successfully!")

if __name__ == "__main__":
    main()
