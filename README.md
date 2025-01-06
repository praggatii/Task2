# Task2
## Daily Station Report Transformer
This project provides a Python script to process and transform daily station reports for multiple months, consolidating them into a single output file for easier analysis.


## Description

The script performs the following tasks:

1. Loads data: Reads daily station report data from multiple Excel files, specifically the "STATION" worksheet.<br>
2. Cleans data:
 * Drops specific rows (1st, 2nd, 3rd, and 12th) based on the task requirements.
 * Renames columns for clarity, including converting unnamed columns to unique placeholders.
 * Standardizes day column names as "Day 1", "Day 2", ..., "Day 31".<br>
3. Adds metadata:
 * Adds a "Month" column for identifying data from different files.
 * Reorders columns to ensure the "Month" column appears first. <br>
4. Combines datasets: Merges transformed data from all months into one consolidated file. <br>
5. Outputs result: Saves the cleaned and combined data into a single Excel file.
  

## Requirements
Python 3.x
## Required libraries:
pandas
openpyxl (for working with Excel files)


## Usage
1. Clone this Repository
```
bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```
2. Install Dependencies
```
bash
pip install pandas openpyxl
```
3. File Setup
* Place the input Excel files in the appropriate directory.
* Update the file_paths variable in Task2.py with the file paths to your input Excel files.
4. Run the Script
```  
bash
python Task2.py
```
The script will process the data and save the output file as Combined_Station_Report.xlsx in the specified directory.


### Input Format
Excel files containing daily station report data. <br>
The script expects a worksheet named "STATION".
***

   
