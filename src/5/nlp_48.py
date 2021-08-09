import nlp_41


sentences = nlp_41.get_chunked_sentences()
for chunks in sentences:
    for chunk in chunks:
        if '名詞' in [morph.pos for morph in chunk.morphs]:
            path = [''.join(morph.surface for morph in chunk.morphs if morph.pos != '記号')]
            while chunk.dst != -1:
                path.append(''.join(morph.surface for morph in chunks[chunk.dst].morphs if morph.pos != '記号'))
                chunk = chunks[chunk.dst]
            if len(path) > 1:
                print(' -> '.join(path))
