import sys
import pandas as pd


args = sys.argv
head_num = args[1]
df = pd.read_table('./popular-names.txt', header=None)

if head_num.isdecimal():
    head_num = int(head_num)

    split_num = (len(df) // head_num)
    print(split_num)
    for i in range(head_num):
        split_df = df.iloc[i * split_num:(i + 1) * split_num]
        split_df.to_csv(f'split_{i}.txt', sep='\t', index=False, header=None)

# python nlp_16.py 5
# split -l 556 popular-names.txt command_
