import pandas as pd

# Correct relative paths (from current script folder)
df_numeric = pd.read_csv('train_numeric.csv', nrows=1000)
df_date = pd.read_csv('train_date.csv', nrows=1000)
df_categorical = pd.read_csv('train_categorical.csv', nrows=1000)

df_numeric.to_csv('sample_train_numeric.csv', index=False)
df_date.to_csv('sample_train_date.csv', index=False)
df_categorical.to_csv('sample_train_categorical.csv', index=False)

print("Sample files saved successfully.")