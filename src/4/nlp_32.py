import nlp_30


result = set()
sentences = nlp_30.get_sentences()

for sentence in sentences:
    for morph in sentence:
        if morph['pos'] == '動詞':
            result.add(morph['base'])

print(result)
