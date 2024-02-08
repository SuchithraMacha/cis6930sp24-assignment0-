from assignment0 import *
import argparse
import os
import urllib.parse
import pypdf
from pypdf import PdfReader

# Main function to orchestrate the process
def main():
    # Command-line argument parsing
    parser = argparse.ArgumentParser(description="Extract incident data from PDF or text file")
    parser.add_argument("--incidents", type=str, help="URL or path to the incident PDF file or text file")
    args = parser.parse_args()

    # Determine if the input is a URL or a local file path
    if urllib.parse.urlparse(args.incidents).scheme in ('http', 'https'):
        # It's a URL, so download the PDF file
        pdf_url = args.incidents
        download_pdf(pdf_url, "incident_data.pdf")
        pdf_file_path = "incident_data.pdf"
    else:
        # It's a local file path, use it directly
        pdf_file_path = args.incidents

    # Extract text from PDF or text file
    incident_data = []
    with open(pdf_file_path, "rb") as file:
        if pdf_file_path.endswith('.pdf'):
            reader = PdfReader(file)
            for page in reader.pages:
                text = page.extract_text()
                for line in text.split('\n'):
                    fields = extract_fields(line.strip())
                    if fields:
                        incident_data.append(fields)
        else:
            for line in file:
                fields = extract_fields(line.strip())
                if fields:
                    incident_data.append(fields)

    # Create SQLite database and table
    create_database()

    # Insert data into SQLite database
    insert_into_database(incident_data)

    # Print nature count
    status()

if __name__ == "__main__":
    main()
