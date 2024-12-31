# Task2
## Daily Station Report Transformer
This project provides a Python script to process and transform daily station reports for multiple months, consolidating them into a single output file for easier analysis.

### Description

The script performs the following tasks:

#### Loads data: 
Reads daily station report data from multiple Excel files, specifically the "STATION" worksheet.
#### Cleans data:
Drops specific rows (1st, 2nd, 3rd, and 12th) based on the task requirements.
Renames columns for clarity, including converting unnamed columns to unique placeholders.
Standardizes day column names as "Day 1", "Day 2", ..., "Day 31".
#### Adds metadata:
Adds a "Month" column for identifying data from different files.
Reorders columns to ensure the "Month" column appears first.
#### Combines datasets: 
Merges transformed data from all months into one consolidated file.
#### Outputs result: 
Saves the cleaned and combined data into a single Excel file.


   
