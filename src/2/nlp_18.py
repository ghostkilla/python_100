import pandas as pd


df = pd.read_table('./popular-names.txt', header=None)
sorted_df = df.sort_values(by=2, ascending=False)

sorted_df.to_csv('desc_number.txt', sep='\t', index=False, header=None)

# cat popular-names.txt | sort -rnk 3
