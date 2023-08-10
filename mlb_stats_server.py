"""
============================
Extract MLB Team Data from Web
============================
This script extracts MLB team data from the Baseball Reference website and saves it to a CSV file.

This script requires that `requests`, `BeautifulSoup`, and `pandas` be installed within the Python
environment you are running this script in.    
    
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path
from util_logger import setup_logger

# Set up a file logger
logger, log_filename = setup_logger(__file__)

# URL of the webpage to scrape
url = "https://www.baseball-reference.com/teams/"

# Send an HTTP GET request to the URL
response = requests.get(url)
logger.info(f"response: {response}")

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")
logger.info(f"soup: {soup}")

# Find the table containing the data
table = soup.find('table', class_='sortable')
logger.info(f"table: {table}")

# Create a list to store the data
data = []
logger.info(f"data: {data}")

# Iterate through the table rows and extract data
for row in table.find_all('tr'):
    logger.info(f"row: {row}")
    cells = row.find_all(['th', 'td'])
    logger.info(f"cells: {cells}")
    row_data = [cell.get_text(strip=True) for cell in cells]
    if row_data:
        data.append(row_data)
        logger.info(f"row_data: {row_data}")

# Define the column headers
headers = data[0]

# Create a DataFrame from the data
df = pd.DataFrame(data[1:], columns=headers)
logger.info(f"df: {df}")

# Define the file path to save the CSV file
fp = Path(__file__).parent.joinpath("data").joinpath("team_data.csv")
logger.info(f"fp: {fp}")

# Save the DataFrame to a CSV file
df.to_csv(fp, index=False)
logger.info(f"Data has been extracted and saved to {fp}")

print(f"Data has been extracted and saved to {fp}")
