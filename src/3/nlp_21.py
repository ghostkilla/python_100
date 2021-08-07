import re
import nlp_20


text_uk = nlp_20.get_text_uk()
text_uk_lines = text_uk.split('\n')
pattern = r'^\[\[Category:.+\]\]$'
categories = []

for line in text_uk_lines:
    if re.match(pattern, line):
        categories.append(line)

result = '\n'.join(categories)

print(result)
