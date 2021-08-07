import nlp_30


result = set()
sentences = nlp_30.get_sentences()

nouns = ''
noun_num = 0
for sentence in sentences:
    for morph in sentence:
        if morph['pos'] == '名詞':
            nouns = ''.join([nouns, morph['surface']])
            noun_num += 1
        elif noun_num >= 2:
            result.add(nouns)
            nouns = ''
            noun_num = 0
        else:
            nouns = ''
            noun_num = 0

print(result)
