import os
import re

folder_path = "ABV"  # Replace this with the actual path to your folder

def rename_files(folder_path):
    for filename in os.listdir(folder_path):
        old_path = os.path.join(folder_path, filename)

        # Extract information from the old filename using regular expressions
        # match = re.match(r'(\d{2}-[a-zA-Z]{3}-\d{4})-(\w+)-(\w+)-(\w+)( \(\d+\))?(\.\w+)?', filename)
        match = re.match(r'(\d{2}-[a-zA-Z]{3}-\d{4})-(\w+)-(\w+)-(\w+)(?: \((\d+)\))?(\.\w+)?', filename)
        if match:
            date, flight_number, location, code, count, extension = match.groups()

            # Create the new filename format
            new_filename = f"CSV {date} {flight_number} {location}-{code} P{count if count else ''}{extension if extension else ''}"
            
            new_path = os.path.join(folder_path, new_filename)
            
            # Rename the file
            os.rename(old_path, new_path)
            print(f"Renamed: {old_path} to {new_path}")

# Replace 'your_folder_path' with the actual path to your folder
rename_files(folder_path)