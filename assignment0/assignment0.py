import requests
import sqlite3
import re
import os


# Function to download PDF file given a URL
def download_pdf(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)

# Function to extract fields from incident data
def extract_fields(line):
    fields = line.strip().split(' ')
    if len(fields) < 5:
        return None
    
    # Extract Date/Time
    date_time = fields[0] + ' ' + fields[1]
    
    # Extract Incident Number
    incident_number = fields[2]
    
    # Extract Location
    location = ' '.join(fields[3:-2])
    
    # Extract Nature
    nature = fields[-2]
    
    # Extract Incident ORI
    incident_ori = fields[-1]
    
    return (date_time, incident_number, location, nature, incident_ori)



# Function to create SQLite database and table
def create_database():
    directory = 'resources'

    if not os.path.exists(directory):
        os.mkdir(directory)

    db_file = os.path.abspath(os.path.join(directory, 'normanpd.db'))
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Incidents
                 (Date_Time TEXT, Incident_Number TEXT, Location TEXT, Nature TEXT, Incident_ORI TEXT)''')
    conn.commit()
    conn.close()

# Function to insert data into SQLite database
def insert_into_database(data):
    directory = 'resources'
    db_file = os.path.abspath(os.path.join(directory, 'normanpd.db'))

    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.executemany('INSERT INTO Incidents VALUES (?, ?, ?, ?, ?)', data)
    conn.commit()
    conn.close()


# Function to print each nature and the number of times it appears
def status():
    conn = sqlite3.connect('resources/normanpd.db')
    c = conn.cursor()
    c.execute('SELECT Nature, COUNT(*) FROM Incidents GROUP BY Nature')
    for row in c.fetchall():
        print(f"{row[0]}|{row[1]}")
    conn.close()
