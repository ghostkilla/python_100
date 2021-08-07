import re
import nlp_20


text_uk = nlp_20.get_text_uk()
text_uk_lines = text_uk.split('\n')

# 取り出したい部分（カテゴリの値）をグループ化することでその値のみ取り出せる
pattern = r'^\[\[Category:(.*?)(?:\|.*)?\]\]$'
category_values = []

for line in text_uk_lines:
    m = re.match(pattern, line)
    if m:
        category_values.append(m.group(1))

result = '\n'.join(category_values)

print(result)
