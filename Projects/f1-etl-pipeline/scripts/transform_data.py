# import libraries
import psycopg2
import os
from dotenv import load_dotenv

# create mart in PostgreSQL
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
    DROP TABLE IF EXISTS f1_mart;""")
cur.execute("""
    CREATE TABLE f1_mart AS
        WITH meeting_session_agg AS (
        SELECT
            meeting_key,
            AVG(air_temperature) AS avg_air_temperature,
            AVG(humidity) AS avg_humidity,
            AVG(pressure) AS avg_pressure,
            SUM(rainfall) AS total_rainfall,
            AVG(track_temperature) AS avg_track_temperature,
            AVG(wind_speed) AS avg_wind_speed,
            MIN(date_weather) AS first_recorded_weather
        FROM
            f1_data
        GROUP BY
            meeting_key
)             
        SELECT 
            f.meeting_key,
            f.session_key,
            f.full_name,
            MAX(f.driver_number) AS driver_number,
            COUNT(f.headshot_url) AS headshot_count,
            MAX(f.team_name) AS team_name,
            MAX(f.team_colour) AS team_colour,
            MAX(f.country_code) AS driver_country,
            MAX(f.meeting_name) AS meeting_name,
            MAX(f.meeting_official_name) AS meeting_official_name,
            MAX(f.location) AS location,
            MAX(f.country_name) AS country_name,
            MAX(f.circuit_short_name) AS circuit_short_name,
            MIN(f.date_start) AS date_start,
            MAX(f.gmt_offset) AS gmt_offset,
            MAX(f.year) AS year,
            MAX(f.meeting_code) AS meeting_code,
            m.avg_air_temperature,
            m.avg_humidity,
            m.avg_pressure,
            m.total_rainfall,
            m.avg_track_temperature,
            m.avg_wind_speed,
            m.first_recorded_weather

        FROM 
            f1_data AS f
        LEFT JOIN 
            meeting_session_agg AS m
        ON 
            f.meeting_key = m.meeting_key

        GROUP BY 
            f.meeting_key, f.session_key, f.full_name, 
            m.avg_air_temperature, m.avg_humidity, m.avg_pressure, 
            m.total_rainfall, m.avg_track_temperature, m.avg_wind_speed, m.first_recorded_weather

        ORDER BY 
            f.meeting_key, f.session_key;
        ;""")
conn.commit()