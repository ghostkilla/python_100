import pandas as pd


df = pd.read_table('./popular-names.txt', header=None)

print(len(df.drop_duplicates(subset=0)))

# cut -f 1 popular-names.txt | sort | uniq | wc -l
