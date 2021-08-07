import re

# https://taku910.github.io/mecab/#parse
# 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
mecab_file = './neko.txt.mecab'


def get_sentences():
    sentences = []
    morphs = []
    with open(mecab_file, mode='r') as file:
        for line in file:
            if not re.match(r'^EOS.*$', line):
                fields = line.split('\t')
                if len(fields) > 1:
                    attributes = fields[1].split(',')
                    morph = {
                        'surface': fields[0],
                        'base': attributes[6],
                        'pos': attributes[0],
                        'pos1': attributes[1]
                    }
                    morphs.append(morph)
            else:
                sentences.append(morphs)
                morphs = []
    return sentences


# print(get_sentences())
