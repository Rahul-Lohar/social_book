import pandas as pd

data = {
    'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'B': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
    'C': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

filtered_df = df[df['A'] > 5]
print("\nFiltered DataFrame (A > 5):")
print(filtered_df)

filtered_df_2 = df[(df['A'] > 5) & (df['C'] < 5)]
print("\nFiltered DataFrame (A > 5 and C < 5):")
print(filtered_df_2)

df.loc[df['A'] > 5, 'B'] = 'X'
print("\nDataFrame after replacing values in column 'B':")
print(df)

dummy_data = {
    'A': [11, 12, 13],
    'B': ['k', 'l', 'm'],
    'C': [0, -1, -2]
}

dummy_df = pd.DataFrame(dummy_data)

# Append the dummy DataFrame
appended_df = df._append(dummy_df, ignore_index=True)
print("\nAppended DataFrame:")
print(appended_df)

