import nlp_30


result = set()
sentences = nlp_30.get_sentences()

for sentence in sentences:
    for index, morph in enumerate(sentence):
        if index + 1 != len(sentence):
            previous_pos = sentence[index - 1]['pos']
            previous_surface = sentence[index - 1]['surface']
            next_pos = sentence[index + 1]['pos']
            next_surface = sentence[index + 1]['surface']
            current_surface = morph['surface']

            if previous_pos == '名詞' and current_surface == 'の' and next_pos == '名詞':
                result.add(f'{previous_surface}{current_surface}{next_surface}')

print(result)
