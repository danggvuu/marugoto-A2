import os
import re

base_dir = "Ke_Hoach_10_Ngay"

def md_to_html(md_text):
    html = md_text
    
    # Bold & Italic
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)
    html = re.sub(r'`(.*?)`', r'<code>\1</code>', html)
    
    lines = html.split('\n')
    out_lines = []
    in_list = False
    
    for line in lines:
        line_s = line.strip()
        if line_s.startswith('# '):
            if in_list: out_lines.append('</ul>'); in_list = False
            out_lines.append(f"<h1>{line_s[2:]}</h1>")
        elif line_s.startswith('## '):
            if in_list: out_lines.append('</ul>'); in_list = False
            out_lines.append(f"<h2>{line_s[3:]}</h2>")
        elif line_s.startswith('- '):
            if not in_list:
                out_lines.append('<ul>')
                in_list = True
            out_lines.append(f"<li>{line_s[2:]}</li>")
        elif line.startswith('1. ') or line.startswith('2. ') or line.startswith('3. '):
            if not in_list:
                out_lines.append('<ul>')
                in_list = True
            out_lines.append(f"<li>{line[3:]}</li>")
        elif line_s == '':
            if in_list:
                out_lines.append('</ul>')
                in_list = False
            out_lines.append("<br>")
        else:
            if line_s.startswith('1. '):
                if not in_list: out_lines.append('<ul>'); in_list = True
                out_lines.append(f"<li>{line_s[3:]}</li>")
            elif line_s.startswith('2. '):
                if not in_list: out_lines.append('<ul>'); in_list = True
                out_lines.append(f"<li>{line_s[3:]}</li>")
            elif line_s.startswith('3. '):
                if not in_list: out_lines.append('<ul>'); in_list = True
                out_lines.append(f"<li>{line_s[3:]}</li>")
            else:
                if in_list:
                    out_lines.append('</ul>')
                    in_list = False
                out_lines.append(f"<p>{line}</p>")
                
    if in_list:
        out_lines.append('</ul>')
        
    body = "\n".join(out_lines)
    return body

template = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nội dung học Ngày {day}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f4f7f6;
            color: #333;
        }}
        .container {{
            max-width: 800px;
            margin: 0 auto;
            background-color: #fff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #e67e22;
            margin-top: 30px;
        }}
        ul {{
            background-color: #f9f9f9;
            padding: 20px 40px;
            border-radius: 5px;
            border-left: 4px solid #3498db;
        }}
        li {{
            margin-bottom: 10px;
        }}
        code {{
            background-color: #eef;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: Consolas, monospace;
            color: #c0392b;
        }}
        em {{
            color: #16a085;
            font-weight: bold;
            font-style: normal;
        }}
    </style>
</head>
<body>
    <div class="container">
        {content}
    </div>
</body>
</html>"""

for i in range(1, 11):
    folder_name = os.path.join(base_dir, f"Ngay_{i}")
    md_file = os.path.join(folder_name, f"Noi_dung_hoc_Ngay_{i}.md")
    html_file = os.path.join(folder_name, f"Noi_dung_hoc_Ngay_{i}.html")
    
    if os.path.exists(md_file):
        with open(md_file, "r", encoding="utf-8") as f:
            md_text = f.read()
            
        html_body = md_to_html(md_text)
        html_content = template.format(day=i, content=html_body)
        
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html_content)
            
        os.remove(md_file)
        
print("Conversion complete!")
