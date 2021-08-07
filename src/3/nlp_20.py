import json


def get_text_uk():
    with open('jawiki-country.json', mode='r') as file:
        for line in file:
            dic = json.loads(line)
            if dic['title'] == 'イギリス':
                text_uk = dic['text']
                break

    return text_uk


# 確認するときは下記のコメントを外してください
# print(get_text_uk())
