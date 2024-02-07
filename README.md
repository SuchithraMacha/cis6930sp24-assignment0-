# Cis6930sp24 - Assignment 0 - Normanpd Project

## Project Description
This Python Project Focuses On Extracting Incident Data From The Norman, Oklahoma Police 
Department's Pdf Summaries, Storing It In An Sqlite Database, And Providing A Summary Of 
Incident Counts. The Code Is Organized As A Single Python File With Functions For Downloading, 
Extracting, And Working With The Data.

## how To Run
Pipenv Run Python Assignment0/main.py --incidents <url>


## Functions
# Download Pdf 
Downloads A Pdf File Containing Incident Data From A Specified Url.

# Extract Fields 
Extracts Relevant Fields From The Pdf Text Using Regular Expressions.

# Create Database 
Creates A Sqlite Database And Table To Store The Extracted Incident Data.

# Insert Into Database 
Inserts The Extracted Data Into The Sqlite Database.

# Print Status 
Prints The Count Of Each Nature Of Incident Stored In The Database.



## Tests
## How To Run Tests
Pipenv Run Python -m Pytest

# Test Download Pdf 
Verifies That The Download_pdf Function Correctly Downloads And Saves A Pdf File.

# Test Extract Fields 
Validates The Extract_fields Function's Ability To Extract Fields From A Given Line Of Text.

# Test Insert Into Database
Checks That The Insert_into_database Function Properly Inserts Data Into The Sqlite Database.

# Test Status
Verifies That The Status Function Correctly Prints The Count Of Each Incident Nature Stored 
In The Database.

### Note
In The Test_download_pdf Method, We Mock Requests.get And Open To Avoid Actual Network Requests 
And File Operations. Then, We Assert That The Functions Are Called Correctly.

In The Other Test Methods, We Mock Sqlite3.connect And Cursor To Avoid Actual Database Operations. 
We Also Mock Sys.stdout To Capture The Output Of The Status Function.