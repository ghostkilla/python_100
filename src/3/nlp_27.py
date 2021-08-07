import re
import nlp_20


text_uk = nlp_20.get_text_uk()
text_uk_lines = text_uk.split('\n')

# {{基礎情報 国
template_pattern = r'^\{\{基礎情報.*?$(.*?)^\}\}'
templates = re.findall(template_pattern, text_uk, re.MULTILINE + re.DOTALL)

# |略名  =イギリス
# |日本語国名 = グレート
field_pattern = r'^\|(.+?)\s*=\s*(.+)'
fields = []

for template in templates:
    lines = template.split('\n')
    for line in lines:
        m = re.match(field_pattern, line)
        if m:
            strong_markup_pattern = r'\'{2,5}'
            value = re.sub(strong_markup_pattern, '', m.group(2))

            internal_link_pattern = r'\[\[(?:[^|]*?\|)??([^|]*?)\]\]'
            value = re.sub(internal_link_pattern, r'\1', value)

            fields.append((m.group(1), value))

result_dic = dict(fields)
print(result_dic)
