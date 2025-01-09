import pandas as pd

# File paths
file_paths = [
    "/home/priyapragati/Downloads/Daily station report-June -24.xlsx",
    "/home/priyapragati/Downloads/Daily station report-May -24.xlsx",
    "/home/priyapragati/Downloads/Daily station report-Nov -24.xlsx"
]

# Month names corresponding to the files
months = ["June", "May", "November"]

# Placeholder for combined data
combined_data = []

# Loop over each file and apply the transformations
for file, month in zip(file_paths, months):
    # Load the "STATION" worksheet
    data = pd.read_excel(file, sheet_name="STATION")
    
    # Task 1: Drop the 1st, 2nd, 3rd, and 12th rows (0-based indexing)
    data = data.drop(index=[0, 1, 2, 11]).reset_index(drop=True)
    
    # Clear column names at indices 0, 1, and 2 with unique placeholders
    columns = list(data.columns)
    columns[0], columns[1], columns[2] = "Temp_0", "Temp_1", "Temp_2"  # Use temporary unique names
    data.columns = columns  # Reassign column names to the DataFrame
    
    # Task 2: Rename columns from index 3 to index 33 (inclusive) to "Day 1", "Day 2", ..., "Day 31"
    for i in range(3, len(data.columns)):  # Loop through from column index 3 to the last column
        if data.columns[i] not in ["Temp_0", "Temp_1", "Temp_2"]:  # Avoid renaming placeholders
            data.columns.values[i] = f"Day {i - 2}"  # Renaming columns to "Day 1", "Day 2", etc.
    
    # Add a new column for the month
    data["Month"] = month
    
    # Reorder columns to move "Month" to the first position
    cols = ["Month"] + [col for col in data.columns if col != "Month"]
    data = data[cols]
    
    # Append the transformed data to the list
    combined_data.append(data)

# Combine all datasets
final_data = pd.concat(combined_data, ignore_index=True)

# Restore blank column names after concatenation
final_data.rename(columns={"Temp_0": "", "Temp_1": "", "Temp_2": ""}, inplace=True)

# Save the combined result to a new Excel file
output_path = "/home/priyapragati/Downloads/Combined_Station_Report.xlsx"
final_data.to_excel(output_path, index=False)

print(f"File saved at: {output_path}")

# Save the combined result to a new Excel file
output_path = "/home/priyapragati/Downloads/Combined_Station_Report.xlsx"
final_data.to_excel(output_path, index=False)

print(f"File saved at: {output_path}")

# Loop over each file and apply the transformations
for file, month in zip(file_paths, months):
    # Load the "STATION" worksheet
    data = pd.read_excel(file, sheet_name="STATION")
    
    # Task 1: Drop the 1st, 2nd, 3rd, and 12th rows (0-based indexing)
    data = data.drop(index=[0, 1, 2, 11]).reset_index(drop=True)
    

# Loop over each file and apply the transformations
for file, month in zip(file_paths, months):
    # Load the "STATION" worksheet
    data = pd.read_excel(file, sheet_name="STATION")
    
    # Task 1: Drop the 1st, 2nd, 3rd, and 12th rows (0-based indexing)
    data = data.drop(index=[0, 1, 2, 11]).reset_index(drop=True)






