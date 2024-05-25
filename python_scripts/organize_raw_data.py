import os
import shutil

raw_data_dir = "C:\\Users\\Autochek\\Desktop\\kev\\projects\\data\\citibike_analysis\\raw_data"

# Iterate over files in the raw_data directory
for filename in os.listdir(raw_data_dir):
    if filename.endswith(".csv"):
        
        # Extract the year from the filename
        year = filename[:4]
        
        # Create the year directory if it doesn't exist
        year_dir = os.path.join(raw_data_dir, year)
        if not os.path.exists(year_dir):
            os.makedirs(year_dir)
        
        file_path = os.path.join(raw_data_dir, filename)
        destination = os.path.join(year_dir, filename)

        shutil.move(file_path, destination)

