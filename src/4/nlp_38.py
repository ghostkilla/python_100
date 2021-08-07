import matplotlib.pyplot as plt
import japanize_matplotlib
from collections import defaultdict
import nlp_30


dic = defaultdict(int)
sentences = nlp_30.get_sentences()

for sentence in sentences:
    for morph in sentence:
        if morph['pos'] != '記号':
            dic[morph['base']] += 1

plt.figure()
plt.hist(dic.values(), bins=200)
plt.xlabel('出現頻度')
plt.ylabel('単語の頻度数')
plt.show()
