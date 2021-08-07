import re


class Chunk:
    def __init__(self, morphs, dst):
        self.morphs = morphs
        self.dst = dst
        self.srcs = []


class Morph:
    def __init__(self, morph):
        # 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
        surface, attr = morph.split('\t')
        attributes = attr.split(',')
        self.surface = surface
        self.base = attributes[6]
        self.pos = attributes[0]
        self.pos1 = attributes[1]


cabocha_file = './ai.ja.txt.cabocha'


def get_chunked_sentences():
    sentences = []
    morphs = []
    chunks = []
    with open(cabocha_file, mode='r') as file:
        for line in file:
            if line[0] == '*':
                if len(morphs) > 0:
                    chunks.append(Chunk(morphs, dst))
                    morphs = []
                dst = int(line.split(' ')[2].rstrip('D'))
            elif not re.match(r'^EOS.*$', line):
                morphs.append(Morph(line))
            else:
                chunks.append(Chunk(morphs, dst))

                for index, chunk in enumerate(chunks):
                    if chunk.dst != -1:
                        chunks[chunk.dst].srcs.append(index)

                sentences.append(chunks)
                morphs = []
                chunks = []

    return sentences


# get_chunked_sentences()

# print(get_chunked_sentences())
