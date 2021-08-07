import re
import nlp_20


text_uk = nlp_20.get_text_uk()
text_uk_lines = text_uk.split('\n')
pattern = r'^(\={2,})\s*(.+?)\s*(\={2,}).*$'
sections = []

for line in text_uk_lines:
    m = re.match(pattern, line)
    if m:
        sections.append(f'{m.group(2)}:{len(m.group(1)) - 1}')

result = '\n'.join(sections)

print(result)
