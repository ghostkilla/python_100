import re
import nlp_20


text_uk = nlp_20.get_text_uk()
text_uk_lines = text_uk.split('\n')

# |国章画像 = [[ファイル:Royal Coat of Arms of the United Kingdom.svg|85px|イギリスの国章]]
pattern = r'.*\[\[ファイル:(.+?)\|'
files = []

for line in text_uk_lines:
    m = re.match(pattern, line)
    if m:
        files.append(m.group(1))

result = '\n'.join(files)

print(len(files))
print(result)
