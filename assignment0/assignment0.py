import requests
import sqlite3
import re


# Function to download PDF file given a URL
def download_pdf(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)

# Function to extract fields from incident data
def extract_fields(line):
    pattern = r'(\d+/\d+/\d+ \d+:\d+) (\d+-\d+) (.+) (.+) ([A-Z0-9]+)'
    match = re.match(pattern, line)
    if match:
        return match.groups()
    return None

# Function to create SQLite database and table
def create_database():
    conn = sqlite3.connect('incident_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Incidents
                 (Date_Time TEXT, Incident_Number TEXT, Location TEXT, Nature TEXT, Incident_ORI TEXT)''')
    conn.commit()
    conn.close()

# Function to insert data into SQLite database
def insert_into_database(data):
    conn = sqlite3.connect('incident_data.db')
    c = conn.cursor()
    c.executemany('INSERT INTO Incidents VALUES (?, ?, ?, ?, ?)', data)
    conn.commit()
    conn.close()

# Function to print each nature and the number of times it appears
def status():
    conn = sqlite3.connect('incident_data.db')
    c = conn.cursor()
    c.execute('SELECT Nature, COUNT(*) FROM Incidents GROUP BY Nature')
    for row in c.fetchall():
        print(row[0],"|",row[1])
    conn.close()