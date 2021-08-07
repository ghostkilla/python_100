from collections import defaultdict
import nlp_30


dic = defaultdict(int)
sentences = nlp_30.get_sentences()

for sentence in sentences:
    for morph in sentence:
        if morph['pos'] != '記号':
            dic[morph['base']] += 1

dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

print(dic)
