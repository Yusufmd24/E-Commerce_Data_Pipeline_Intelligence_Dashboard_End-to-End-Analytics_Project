import pandas as pd

# Load raw data
df = pd.read_csv("../data/raw/products_raw.csv")

# ---------------- CLEANING ---------------- #

# Rename columns (standardize)
df.rename(columns={
    'id': 'product_id',
    'title': 'product_name'
}, inplace=True)

# Handle missing values
df.dropna(inplace=True)

# ---------------- FEATURE ENGINEERING ---------------- #

# Create price bucket
def price_category(price):
    if price < 50:
        return "Low"
    elif price < 200:
        return "Medium"
    else:
        return "High"

df['price_category'] = df['price'].apply(price_category)

# Discount % (dummy but realistic)
if 'discountPercentage' in df.columns:
    df['discount_flag'] = df['discountPercentage'].apply(lambda x: 1 if x > 10 else 0)
else:
    df['discount_flag'] = 0

# Rating rounded
df['rating'] = df['rating'].round(1)

# ---------------- SAVE CLEAN DATA ---------------- #

df.to_csv("../data/processed/products_clean.csv", index=False)

print("✅ Products transformed successfully!")