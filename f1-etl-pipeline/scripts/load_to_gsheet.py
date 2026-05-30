# import libraries
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from dotenv import load_dotenv

# create a Google Sheets spreadsheet with f1 data
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
load_dotenv()
creds = ServiceAccountCredentials.from_json_keyfile_name(os.getenv('GSHEET_CREDENTIALS'), scope)
client = gspread.authorize(creds)

# Open target Google Sheet
spreadsheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1_ITQ17SUBtdiacBrHBdl8H84pn9We1OSr2_9xZHXdeA")
sheet = spreadsheet.sheet1

# Clear existing data
sheet.clear()

# convert dates to strings
f1_mart_df['date_start'] = f1_mart_df['date_start'].astype(str)
f1_mart_df['first_recorded_weather'] = f1_mart_df['first_recorded_weather'].astype(str)

# Write headers
sheet.insert_row(f1_mart_df.columns.tolist(), index=1)

# Write data rows
sheet.insert_rows(f1_mart_df.values.tolist(), row=2)