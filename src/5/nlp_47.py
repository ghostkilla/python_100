import nlp_41


sentences = nlp_41.get_chunked_sentences()

with open('./nlp_result_47.txt', 'w') as file:
    for chunks in sentences:
        for chunk in chunks:
            for morph in chunk.morphs:
                if morph.pos == '動詞':
                    for index, src in enumerate(chunk.srcs):
                        src_morphs = chunks[src].morphs
                        # サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
                        if len(src_morphs) == 2 and src_morphs[0].pos1 == 'サ変接続' and src_morphs[1].surface == 'を':
                            predicate = ''.join([src_morphs[0].surface, src_morphs[1].surface, morph.base])
                            particles = []
                            items = []
                            for _src in chunk.srcs[:index] + chunk.srcs[index + 1:]:
                                _particles = [src_morph.surface for src_morph in chunks[_src].morphs if src_morph.pos == '助詞']
                                if len(_particles) > 0:
                                    particles += _particles
                                    items.append(''.join(src_morph.surface for src_morph in chunks[_src].morphs if src_morph.pos != '記号'))
                            if len(particles) > 0:
                                particles = sorted(list(set(particles)))
                                str_particles = ' '.join(particles)
                                str_items = ' '.join(items)
                                line = '{}\t{}\t{}'.format(predicate, str_particles, str_items)
                                print(line, file=file)
                            break
