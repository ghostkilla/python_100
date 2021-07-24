def create_bi_gram(sequece_list):
	BI_GRAM_NUMBER = 2
	result = []
	for index, sequence in enumerate(sequece_list):
		if index != len(sequece_list) -1:
			result.append(tuple(sequece_list[index:BI_GRAM_NUMBER + index]))
			
	return result

str1 = 'paraparaparadise'
str2 = 'paragraph'

x = set(create_bi_gram(list(str1)))
y = set(create_bi_gram(list(str2)))

union = x | y
intersection = x & y
diff = x - y

print('x : ', x)
print('y : ', y)
print('和集合', union)
print('積集合', intersection)
print('差集合', diff)
print('seがxに含まれているか', {('s', 'e')} <= x)
print('seがyに含まれているか', {('s', 'e')} <= y)

