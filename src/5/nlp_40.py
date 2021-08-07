import re


class Morph:
    def __init__(self, morph):
        # 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
        surface, attr = morph.split('\t')
        attributes = attr.split(',')
        self.surface = surface
        self.base = attributes[6]
        self.pos = attributes[0]
        self.pos1 = attributes[1]


# https://taku910.github.io/cabocha/
cabocha_file = './ai.ja.txt.cabocha'


sentences = []
morphs = []
with open(cabocha_file, mode='r') as file:
    for line in file:
        if line[0] == '*':
            continue
        elif not re.match(r'^EOS.*$', line):
            morphs.append(Morph(line))
        else:
            sentences.append(morphs)
            morphs = []


for sentence in sentences:
    for morph in sentence:
        print(vars(morph))