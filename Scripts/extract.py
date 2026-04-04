import requests
import pandas as pd

url = "https://dummyjson.com/products"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()

    # IMPORTANT: actual data is inside 'products'
    df = pd.DataFrame(data['products'])

    df.to_csv("../data/raw/products_raw.csv", index=False)

    print("✅ Data extracted and saved successfully!")

except requests.exceptions.RequestException as e:
    print("❌ API Request Failed:", e)

except ValueError:
    print("❌ Failed to parse JSON.")