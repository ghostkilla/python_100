with open('./popular-names.txt') as file:
	text = file.read()
print(text.replace('\t', ' '))

# cat ./popular-names.txt | sed -e s/'\t'/' '/g
# cat ./popular-names.txt | tr '\t' ' '

