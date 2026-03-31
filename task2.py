import pandas as pd
import glob

# Load all CSV files
files = glob.glob("data/*.csv")
df_list = [pd.read_csv(file) for file in files]

# Combine data
data = pd.concat(df_list)

# Filter only Pink Morsel
data = data[data["product"] == "pink morsel"]

# Remove $ sign and convert price to float
data["price"] = data["price"].replace('[\$,]', '', regex=True).astype(float)

# Create sales column
data["sales"] = data["quantity"] * data["price"]

# Keep only required columns
data = data[["sales", "date", "region"]]

# Save properly formatted CSV
data.to_csv("formatted_data.csv", index=False)

print("Fixed! File created correctly ✅")