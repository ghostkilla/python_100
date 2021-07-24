# bi_gram: 2文字もしくは2単語ずつ
def create_bi_gram(sequece_list):
	BI_GRAM_NUMBER = 2
	result = []
	for index, sequence in enumerate(sequece_list):
		if index != len(sequece_list) -1:
			result.append(tuple(sequece_list[index:BI_GRAM_NUMBER + index]))
			
	return result
	
str = 'I am an NLPer'

print('単語bi-gram : ', create_bi_gram(str.split()))
print('文字bi-gram : ', create_bi_gram(list(str)))

