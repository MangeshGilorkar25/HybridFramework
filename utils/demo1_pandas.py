"""Will be deleted later - not part of the framework"""

import pandas

df = pandas.read_excel(io="../test_data/open_emr_data.xlsx", sheet_name="test_valid_login")
print(df)
# print(df.loc[1])
# print(df.columns)
# print(df.index)
print(df.values.tolist())

# alernate way
ls = []
for i in df.index:
    print(df.loc[i].tolist())
    ls.append(df.loc[i].tolist())

print(ls)

df = pandas.read_csv(filepath_or_buffer="../test_data/test_valid_login.csv", delimiter=";")
print(df)
print(df.values.tolist())

json_dic = pandas.read_json(path_or_buf="../test_data/config.json", typ="dictionary")
print(json_dic)