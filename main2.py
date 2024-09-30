import pandas as pd
import os
import glob
from zipfile import ZipFile 

zip_file_path = "Fwd_ ABUJA PAX MANIFEST JAN 27 - 31 2024 (1).zip"
extraction_path = "ABV"


if os.path.exists(zip_file_path):
    with ZipFile(zip_file_path, 'r') as zObject:
        zObject.extractall(path=extraction_path)
else:
    print(f"The specified zip file '{zip_file_path}' does not exist.")

# Set the path to the directory containing the CSV files
path = extraction_path
os.chdir(path)

# # Get a list of all CSV files in the directory
all_files = glob.glob('*.csv')
# # file = "C:/Users/nero.onose/OneDrive - Venture Garden Group/Desktop/dana-air/3-Nov-2023-9J332-QOW-LOS.csv"

for file in all_files:
    df = pd.read_csv(file, header=None)
    index_of_stations = df[df.apply(lambda row: 'Stations' in ' '.join(map(str, row)), axis=1)].index[0]

# Drop all rows before the row containing "Stations"
    df = df.iloc[index_of_stations:]
    
    # Shift all rows downwards by three positions
    # df = df.shift(periods=3)
    # # Add three new rows at the beginning
    # df.iloc[:3, :] = None  # You can use None or any value you want to fill these rows with

    # Add three new rows at the beginning
    new_rows = pd.DataFrame([[None] * df.shape[1]] * 3, columns=df.columns)
    df = pd.concat([new_rows, df], ignore_index=True)

    # Add 'CSV' in the first cell of the DataFrame
    df.iloc[0, 0] = 'CSV'

	# Save the modified DataFrame to a new CSV file in a different directory
    df.to_csv(f"C:/Users/nero.onose/OneDrive - Venture Garden Group/Desktop/dana-air/{extraction_path}/{file}", index=None, header=None)
