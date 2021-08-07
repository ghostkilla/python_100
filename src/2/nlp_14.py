import sys
import pandas as pd


args = sys.argv
head_num = args[1]
df = pd.read_table('./popular-names.txt', header=None)

if head_num.isdecimal():
    print(df.head(int(head_num)))

# head -n 5 popular-names.txt
