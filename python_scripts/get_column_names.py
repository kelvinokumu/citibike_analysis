import os
import csv

raw_data_dir = "C:\\Users\\Autochek\\Desktop\\kev\\projects\\data\\citibike_analysis\\raw_data"

def print_column_names(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".csv"):
                file_path = os.path.join(root, filename)
                print(f"Columns in file '{file_path}':")
                with open(file_path, 'r', newline='') as csvfile:
                    reader = csv.reader(csvfile)
                    column_names = next(reader)
                    print(", ".join(column_names))
                print()

# Call the function to print column names for each file in the raw_data directory
print_column_names(raw_data_dir)
