import random

str = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'

shuffled_words = []
for word in str.split():
	if len(word) > 4:
		shuffled_word = word[:1] + ''.join(random.sample(word[1:-1], len(word) - 2)) + word[-1:]
		shuffled_words.append(shuffled_word)
	else:
		shuffled_words.append(word)
	
print(' '.join(shuffled_words))

