import matplotlib.pyplot as plt
import japanize_matplotlib
import math
from collections import defaultdict
import nlp_30


dic = defaultdict(int)
sentences = nlp_30.get_sentences()

for sentence in sentences:
    for morph in sentence:
        if morph['pos'] != '記号':
            dic[morph['base']] += 1

dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

ranks = [index + 1 for index in range(len(dic))]
values = [item[1] for item in dic]

plt.figure()
plt.plot(ranks, values)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('出現頻度')
plt.ylabel('単語の頻度数')
plt.show()
