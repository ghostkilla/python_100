import nlp_41


sentences = nlp_41.get_chunked_sentences()

for chunks in sentences:
    for chunk in chunks:
        if int(chunk.dst) != -1:
            source = ''.join([morph.surface if morph.pos != '記号' else '' for morph in chunk.morphs])
            source_pos = [morph.pos for morph in chunk.morphs]
            target = ''.join([morph.surface if morph.pos != '記号' else '' for morph in chunks[int(chunk.dst)].morphs])
            target_pos = [morph.pos for morph in chunks[int(chunk.dst)].morphs]
            if '名詞' in source_pos and '動詞' in target_pos:
                print(source, target, sep='\t')
