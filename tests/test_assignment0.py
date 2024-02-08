import pytest
from unittest.mock import patch, mock_open
from io import StringIO
from assignment0.assignment0 import (
    download_pdf,
    extract_fields,
    create_database,
    insert_into_database,
    status,
)

@pytest.mark.parametrize("url, filename", [("http://example.com/incident_data.pdf", "test_pdf.pdf")])
@patch('requests.get')
@patch('builtins.open', new_callable=mock_open)
def test_download_pdf(mock_open, mock_get, url, filename):
    mock_get.return_value.content = b"PDF content"
    
    download_pdf(url, filename)

    mock_get.assert_called_once_with(url)
    mock_open.assert_called_once_with(filename, 'wb')
    mock_open.return_value.write.assert_called_once_with(b"PDF content")

def test_extract_fields():
    line = "01/01/2022 12:00 123-456 Location Nature ABC123"
    expected_output = ("01/01/2022 12:00", "123-456", "Location", "Nature", "ABC123")
    assert extract_fields(line) == expected_output


def test_insert_into_database():
    data = [("01/01/2022 12:00", "123-456", "Location", "Nature", "ABC123")]
    # Mock sqlite3.connect and cursor
    with patch('sqlite3.connect') as mock_connect:
        insert_into_database(data)
        mock_cursor = mock_connect.return_value.cursor.return_value
        mock_cursor.executemany.assert_called_once()

@patch('sys.stdout', new_callable=StringIO)
def test_status(mock_stdout):
    # Mock sqlite3.connect and cursor
    with patch('sqlite3.connect') as mock_connect:
        mock_cursor = mock_connect.return_value.cursor.return_value
        mock_cursor.fetchall.return_value = [("Nature", 1)]

        status()

        mock_cursor.execute.assert_called_once_with('SELECT Nature, COUNT(*) FROM Incidents GROUP BY Nature')
        output = mock_stdout.getvalue().strip()
        assert output == "Nature|1"
