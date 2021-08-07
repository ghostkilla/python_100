import json
import re
from urllib import request, parse
import nlp_20

mediawiki_imageinfo_api_url = 'https://www.mediawiki.org/w/api.php'

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
            flag_image_pattern = r'^国旗画像$'
            if re.match(flag_image_pattern, m.group(1)):
                # 国旗画像 = Flag of the United Kingdom.svg
                # ex) https://en.wikipedia.org/w/api.php?action=query&format=json&prop=imageinfo&titles=File:Billy_Tipton.jpg
                print(m.group(2))
                image_file_url = mediawiki_imageinfo_api_url + '?'\
                    + 'action=query&' \
                    + 'format=json&' \
                    + 'prop=imageinfo&' \
                    + 'iiprop=url&' \
                    + 'titles=File:' \
                    + parse.quote(m.group(2))
                print(image_file_url)
                req = request.urlopen(request.Request(image_file_url))
                res = json.loads(req.read().decode())
                print(res)
                print(res['query']['pages']['-1']['imageinfo'][0]['url'])
