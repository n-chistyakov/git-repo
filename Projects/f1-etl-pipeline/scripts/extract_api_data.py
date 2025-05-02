import pandas as pd
import requests

# extract F1 data from API
drivers_api = requests.get('https://api.openf1.org/v1/drivers').json()
meetings_api = requests.get('https://api.openf1.org/v1/meetings').json()
weather_api = requests.get('https://api.openf1.org/v1/weather').json()

# convert to DataFrames
drivers_df = pd.DataFrame(drivers_api)
meetings_df = pd.DataFrame(meetings_api)
weather_df = pd.DataFrame(weather_api)

# join DataFrames
f1_df = drivers_df.merge(meetings_df, on='meeting_key', how='inner').merge(weather_df, on=['meeting_key', 'session_key'], how='inner')

# preview columns
f1_df.columns