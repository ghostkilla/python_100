from itertools import combinations
import re
import nlp_41


sentences = nlp_41.get_chunked_sentences()
noun_indexes = []
for chunks in sentences:
    for index, chunk in enumerate(chunks):
        if '名詞' in [morph.pos for morph in chunk.morphs]:
            noun_indexes.append(index)
    if len(noun_indexes) > 1:
        for i, j in combinations(noun_indexes, 2):
            path_i = []
            path_j = []
            while i != j:
                if i < j:
                    path_i.append(i)
                    i = chunks[i].dst
                else:
                    path_j.append(j)
                    j = chunks[j].dst
            if len(path_i) == 0 and len(path_j) == 0:
                continue
            if len(path_j) == 0:
                chunk_x = ''.join([morph.surface if morph.pos != '名詞' else 'X' for morph in chunks[path_i[0]].morphs])
                chunk_y = ''.join([morph.surface if morph.pos != '名詞' else 'X' for morph in chunks[i].morphs])
                chunk_x = re.sub('X+', 'X', chunk_x)
                chunk_y = re.sub('Y+', 'Y', chunk_y)
                path_x_to_y = [chunk_x] + [''.join(morph.surface for morph in chunks[i].morphs) for i in path_i[1:]] + [chunk_y]
                print(' -> '.join(path_x_to_y))
            else:
                chunk_x = ''.join([morph.surface if morph.pos != '名詞' else 'X' for morph in chunks[path_i[0]].morphs])
                chunk_y = ''.join([morph.surface if morph.pos != '名詞' else 'X' for morph in chunks[path_j[0]].morphs])
                chunk_k = ''.join([morph.surface for morph in chunks[i].morphs])
                chunk_x = re.sub('X+', 'X', chunk_x)
                chunk_y = re.sub('Y+', 'Y', chunk_y)
                path_x = [chunk_x] + [''.join(morph.surface for morph in chunks[i].morphs) for i in path_i[1:]]
                path_y = [chunk_y] + [''.join(morph.surface for morph in chunks[i].morphs) for i in path_j[1:]]
                print(' | '.join([' -> '.join(path_x), ' -> '.join(path_y), chunk_k]))
