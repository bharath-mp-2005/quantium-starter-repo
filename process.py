import pandas as pd
import os

# folder containing your CSVs
data_folder = "data"

# list of csv files
csv_files = [
    "daily_sales_data_0.csv",
    "daily_sales_data_1.csv",
    "daily_sales_data_2.csv"
]

# empty list to hold DataFrames
dfs = []

for file in csv_files:
    file_path = os.path.join(data_folder, file)
    df = pd.read_csv(file_path)

    # 1. Filter for Pink Morsels
    df = df[df["product"] == "pink morsel"]

    # 2. Create sales column
    df["sales"] = df["price"] * df["quantity"]

    # 3. Keep only required columns
    df = df[["sales", "date", "region"]]

    dfs.append(df)

# 4. Combine into one file
final_df = pd.concat(dfs, ignore_index=True)

# 5. Save output file
output_path = os.path.join(data_folder, "processed_sales_data.csv")
final_df.to_csv(output_path, index=False)

print("Processing completed! Output saved to:", output_path)
