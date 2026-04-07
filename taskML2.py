import pandas as pd
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv(r"C:\Users\Softlaptop\Downloads\data.csv")

print(df.head())

encoder = OneHotEncoder(sparse_output=False)
encoded = encoder.fit_transform(df[['Country']])

encoded_df = pd.DataFrame(
    encoded,
    columns=encoder.get_feature_names_out(['Country'])
)

df = df.drop('Country', axis=1)
df = pd.concat([df.reset_index(drop=True), encoded_df], axis=1)

print(df.isnull().sum())

df = df.fillna(df.mean(numeric_only=True))

print(df.head())