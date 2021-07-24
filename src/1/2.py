from itertools import zip_longest

str1 = 'パトカー'
str2 = 'タクシー'

result = ''.join([p + t for p, t in zip_longest(str1, str2, fillvalue='')])

print(result)

