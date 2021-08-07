import re
import nlp_20


text_uk = nlp_20.get_text_uk()
text_uk_lines = text_uk.split('\n')

# {{基礎情報 国
template_pattern = r'^\{\{基礎情報.*?$(.*?)^\}\}'
templates = re.findall(template_pattern, text_uk, re.MULTILINE + re.DOTALL)
print(templates)

# |略名  =イギリス
# |日本語国名 = グレート
field_pattern = r'^\|(.+?)\s*=\s*(.+)'
fields = []

for template in templates:
    lines = template.split('\n')
    for line in lines:
        m = re.match(field_pattern, line)
        if m:
            fields.append((m.group(1), m.group(2)))

result_dic = dict(fields)
print(result_dic)
