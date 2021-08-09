import nlp_41


sentences = nlp_41.get_chunked_sentences()

with open('./nlp_result_46.txt', 'w') as file:
    for chunks in sentences:
        for chunk in chunks:
            for morph in chunk.morphs:
                if morph.pos == '動詞':
                    particles = []
                    items = []
                    for src in chunk.srcs:
                        _particles = [src_morph.surface for src_morph in chunks[src].morphs if src_morph.pos == '助詞']
                        if len(_particles) > 0:
                            particles += _particles
                            items.append(''.join(src_morph.surface for src_morph in chunks[src].morphs if src_morph.pos != '記号'))
                    if len(particles) > 0:
                        particles = sorted(list(set(particles)))
                        str_particles = ' '.join(particles)
                        str_items = ' '.join(items)
                        line = '{}\t{}\t{}'.format(morph.base, str_particles, str_items)
                        print(line, file=file)
                    break
