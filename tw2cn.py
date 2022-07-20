from zhconv import convert
from pprint import pprint
import pandas as pd

raw_data = pd.read_csv('data/Gossiping-QA-Dataset-2_0-non-null.csv')
raw_data = raw_data.dropna()
print(type(raw_data))
pprint(raw_data.head())
total_rows = len(raw_data)
print('{} rows'.format(total_rows))
simp_data = pd.DataFrame(columns=['question', 'answer'])
for row in raw_data.itertuples():
    q = convert(row[1], 'zh-cn')
    a = convert(row[2], 'zh-cn')
    simp_data = pd.concat([simp_data, pd.DataFrame([[q, a]], columns=['question', 'answer'])], ignore_index=True)
    # print('{}:{}'.format(q, a))
    if (row[0] + 1) % 100 == 0:
        print("converted {}/{}".format(row[0] + 1, total_rows))
        # break

pprint(simp_data.head())

simp_data.to_csv('data/Gossiping-QA-Dataset-2_0-simple.csv')
