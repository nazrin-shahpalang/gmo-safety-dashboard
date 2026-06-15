import pandas as pd

# Dataseti yüklə
df = pd.read_csv('gmo_dataset.csv')

print("=== Əvvəlki vəziyyət ===")
print(f"Sətir sayı: {len(df)}")
print(f"Sütunlar: {list(df.columns)}")
print(f"Boş dəyərlər:\n{df.isnull().sum()}")
print(f"Dublikatlar: {df.duplicated().sum()}")

# Təmizləmə
df = df.drop_duplicates()
df = df.dropna()
df['gmo_name'] = df['gmo_name'].str.strip()
df['crop_type'] = df['crop_type'].str.strip()
df['approval_status'] = df['approval_status'].str.strip()

# Risk score 0-10 arasında olmalıdır
df = df[df['risk_score'].between(0, 10)]

# Approval year 1990-2030 arasında olmalıdır
df = df[df['approval_year'].between(1990, 2030)]

print("\n=== Təmizləndikdən sonra ===")
print(f"Sətir sayı: {len(df)}")
print(f"Boş dəyər yoxdur: {df.isnull().sum().sum() == 0}")

# Təmiz dataseti saxla
df.to_csv('gmo_dataset_clean.csv', index=False)
print("\nTəmiz dataset saxlandı: gmo_dataset_clean.csv")