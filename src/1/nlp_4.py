str = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

words = str.split()
word_num_get_one_char = [1, 5, 6, 7, 8, 9, 15, 16, 19]
result = {}

for index, word in enumerate(words):
	if index + 1 in word_num_get_one_char:
		result[word[:1]] = index + 1
	else:
		result[word[:2]] = index + 1
		
print(result)
