str = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

str = str.replace(',', '')
str = str.replace('.', '')

words = str.split()

print([len(word) for word in words])

