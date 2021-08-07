import pandas as pd


df = pd.read_table('./popular-names.txt', header=None)

col1 = df[0]
col1.to_csv('./col1.txt', index=False, header=None)
# cut -f 1 popular-names.txt

col2 = df[1]
col2.to_csv('./col2.txt', index=False, header=None)
# cut -f 2 popular-names.txt
