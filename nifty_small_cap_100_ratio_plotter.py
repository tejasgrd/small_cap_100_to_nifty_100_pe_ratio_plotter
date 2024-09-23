import json
import matplotlib.pyplot as plt
import requests
from datetime import datetime
import argparse

# Company IDs for the URLs
small_cap_100_company_id = "1272791"
nifty_100_company_id = "1272675"

# Function to generate URL for the given company and days
def get_url(company_id, days):
    return f"https://www.screener.in/api/company/{company_id}/chart/?q=Index+PE-Median+Index+PE&days={days}"

# Argument parser to get days as a parameter
def get_script_params():
    parser = argparse.ArgumentParser(description='Fetch P/E data for companies and plot the ratio.')
    parser.add_argument('days', type=int, help='Number of days for the data range')
    return parser.parse_args()

# Script parameters (change these as required)
company_name_1 = "small_cap_100"  # First company name, either "small_cap_100" or "nifty_100"
company_name_2 = "nifty_100"      # Second company name

# Parse command-line arguments for the number of days
args = get_script_params()
days = args.days

# Map company names to their respective IDs
company_ids = {
    "small_cap_100": small_cap_100_company_id,
    "nifty_100": nifty_100_company_id
}

# Fetch data for both companies using requests
company_1_id = company_ids.get(company_name_1.lower())
company_2_id = company_ids.get(company_name_2.lower())

# Error handling for incorrect company names
if not company_1_id or not company_2_id:
    raise ValueError("Invalid company name. Please use 'small_cap_100' or 'nifty_100'.")

# Generate URLs for both companies based on the number of days
company_1_url = get_url(company_1_id, days)
company_2_url = get_url(company_2_id, days)

# Fetch data from the URLs
company_1_response = requests.get(company_1_url)
company_2_response = requests.get(company_2_url)

# Parse the JSON data from both companies
company_1_data = json.loads(company_1_response.content)
company_2_data = json.loads(company_2_response.content)

# Extract date and value arrays for both datasets
dates = []
values = []

for entry_1, entry_2 in zip(company_1_data['datasets'][0]['values'], company_2_data['datasets'][0]['values']):
    date_1 = entry_1[0]
    date_2 = entry_2[0]

    # Ensure the dates match
    if date_1 == date_2:
        value_ratio = float(entry_1[1]) / float(entry_2[1])
        
        # Convert date string to datetime object for plotting
        date = datetime.strptime(date_1, "%Y-%m-%d")
        dates.append(date)
        values.append(value_ratio)

# Create a plot with dates on the x-axis and values on the y-axis
plt.plot(dates, values, marker='o')

# Format the x-axis to display dates more clearly
plt.gcf().autofmt_xdate()

# Add labels to the axes
plt.xlabel('Date')
plt.ylabel('P/E Ratio')

# Add a title to the graph
plt.title(f'Ratio of {company_name_1.capitalize()} P/E to {company_name_2.capitalize()} P/E Over {days} Days')

# Show the graph
plt.show()
