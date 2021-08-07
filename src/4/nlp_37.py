import matplotlib.pyplot as plt
import japanize_matplotlib
from collections import defaultdict
import nlp_30


dic = defaultdict(int)
sentences = nlp_30.get_sentences()

for sentence in sentences:
    if '猫' in [morph['surface'] for morph in sentence]:
        for morph in sentence:
            if morph['pos'] != '記号':
                dic[morph['base']] += 1

del dic['猫']
dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

keys = [item[0] for item in dic[:10]]
values = [item[1] for item in dic[:10]]
plt.figure()
plt.bar(keys, values)
plt.show()
