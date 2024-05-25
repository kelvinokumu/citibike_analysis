import os
import pandas as pd

raw_data_dir = "C:\\Users\\Autochek\\Desktop\\kev\\projects\\data\\citibike_analysis\\raw_data"

column_mapping = {
    "tripduration": "duration_seconds",
    "starttime": "start_time",
    "stoptime": "stop_time",
    "start station id": "start_station_id",
    "start station name": "start_station_name",
    "start station latitude": "start_station_latitude",
    "start station longitude": "start_station_longitude",
    "end station id": "end_station_id",
    "end station name": "end_station_name",
    "end station latitude": "end_station_latitude",
    "end station longitude": "end_station_longitude",
    "bikeid": "bike_id",
    "usertype": "user_type",
    "birth year": "birth_year",
    "gender": "gender",
    # Add mappings for columns from other files
    "ride_id": "trip_id",
    "rideable_type": "bike_type",
    "started_at": "start_time",
    "ended_at": "stop_time",
    "start_station_name": "start_station_name",
    "start_station_id": "start_station_id",
    "end_station_name": "end_station_name",
    "end_station_id": "end_station_id",
    "start_lat": "start_station_latitude",
    "start_lng": "start_station_longitude",
    "end_lat": "end_station_latitude",
    "end_lng": "end_station_longitude",
    "member_casual": "user_type"
}

def process_file(file_path):
    print(f"Processing file: {file_path}")
    # Read the file
    df = pd.read_csv(file_path)
    # Apply column mappings
    if df.columns[0] in column_mapping:
        df.rename(columns=column_mapping, inplace=True)
        # Example processing: Print first few rows with new column names
        print(df.head())

def traverse_files(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            # Check if the file is a CSV file
            if filename.endswith(".csv"):
                process_file(file_path)
            else:
                print(f"Skipping non-CSV file: {file_path}")


# Call the function to traverse files in the raw_data directory
traverse_files(raw_data_dir)
