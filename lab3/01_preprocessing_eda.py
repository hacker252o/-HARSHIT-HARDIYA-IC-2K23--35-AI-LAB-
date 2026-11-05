import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Kabir", "Sara", "Neha"],
    "Age": [20, 21, None, 22, 20],
    "Marks": [78, 91, 65, None, 84],
    "City": ["Indore", "Bhopal", "Indore", "Ujjain", "Bhopal"]
}
df = pd.DataFrame(data)

print("Original data:\n", df)
print("\nMissing values:\n", df.isnull().sum())

df["Age"] = df["Age"].fillna(df["Age"].median())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["City"] = df["City"].str.strip().str.title()

print("\nCleaned data:\n", df)
print("\nNumeric summary:\n", df.describe())
print("\nCity counts:\n", df["City"].value_counts())
