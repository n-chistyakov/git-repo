# import libraries
import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv

#  connect to PostgreSQL (AWS RDS) and create a table
load_dotenv()
conn = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            port=os.getenv('DB_PORT')
            )
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS f1_data (
    meeting_key INT,
    session_key INT,
    driver_number INT,
    full_name TEXT,
    team_name TEXT,
    team_colour TEXT,
    headshot_url TEXT,
    country_code TEXT,
    meeting_name TEXT,
    meeting_official_name TEXT,
    location TEXT,
    country_name TEXT,
    circuit_short_name TEXT,
    date_start DATE,
    gmt_offset TEXT,
    year INT,
    meeting_code TEXT,
    air_temperature FLOAT,
    humidity FLOAT,
    pressure FLOAT,
    rainfall FLOAT,
    track_temperature FLOAT,
    wind_direction TEXT,
    wind_speed FLOAT,
    date_weather TIMESTAMP
);
""")


# load API data to PostgreSQL (AWS RDS)
cur.execute("""
        TRUNCATE TABLE f1_data;
""")
for index, row in f1_df.sample(10000).iterrows():
    cur.execute("""
        INSERT INTO f1_data (
            meeting_key, session_key, driver_number, full_name, team_name, team_colour,
            headshot_url, country_code, meeting_name, meeting_official_name, location,
            country_name, circuit_short_name, date_start, gmt_offset, year, meeting_code,
            air_temperature, humidity, pressure, rainfall, track_temperature, wind_direction,
            wind_speed, date_weather
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row['meeting_key'],
        row['session_key'],
        row['driver_number'],
        row['full_name'],
        row['team_name'],
        row['team_colour'],
        row['headshot_url'],
        row['country_code_x'],
        row['meeting_name'],
        row['meeting_official_name'],
        row['location'],
        row['country_name'],
        row['circuit_short_name'],
        row['date_start'],
        row['gmt_offset'],
        row['year'],
        row['meeting_code'],
        row['air_temperature'],
        row['humidity'],
        row['pressure'],
        row['rainfall'],
        row['track_temperature'],
        row['wind_direction'],
        row['wind_speed'],
        row['date']
    ))

