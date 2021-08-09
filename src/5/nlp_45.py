import nlp_41


sentences = nlp_41.get_chunked_sentences()

with open('./nlp_result_45.txt', 'w') as file:
    for chunks in sentences:
        for chunk in chunks:
            for morph in chunk.morphs:
                if morph.pos == '動詞':
                    particles = []
                    for src in chunk.srcs:
                        particles += [src_morph.surface for src_morph in chunks[src].morphs if src_morph.pos == '助詞']
                    if len(particles) > 0:
                        particles = sorted(list(set(particles)))
                        str_particles = ' '.join(particles)
                        line = '{}\t{}'.format(morph.base, str_particles)
                        print(line, file=file)
                    break
