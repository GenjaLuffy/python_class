import pandas as pd
df = pd.read_csv('data.csv')
# # new_df = df.dropna()
# # print(df)
# # print(new_df.to_string())

df.fillna({"Calories": 130}, inplace=True)
# # print(df)


# # Remove NaN value and Corret the Format in data
df.dropna(subset=['Date'], inplace=True)
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
# print(df)



# # Claning value in data
# df.loc[7, 'Duration'] = 45
# print(df)


for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120
# print(df)


print(df.duplicated())
df.drop_duplicates(inplace = True)
print(df)


df.to_csv("data_new.csv",index=False)