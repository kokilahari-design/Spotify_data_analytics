from spotipy.oauth2 import SpotifyClientCredentials
import pymysql
from pymysql import MySQLError
import spotipy
import re

#Setting up Spotify API Client credentials
sp = spotipy.Spotify(auth_manager = SpotifyClientCredentials (
    client_id = "ddd7c9abb2c842c3a44469076ac3c414",
    client_secret = "3e5fbcf74d154b38aa3bed0bdb719df6"
))

# MySQL database connection
dbconfig = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "spotify_db"
}

#Connect to spotify_db
connection = pymysql.connect(**dbconfig)
cursor = connection.cursor()
print("connection success")

#Read tarck URL List from track_urls.txt file
filepath = "spotify_data_analytics/track_urls.txt"
with open(filepath, 'r') as file:
    track_urls = file.readlines()
    
#Process each track URL
for track_url in track_urls:
    track_url = track_url.strip()
    print(f"Processing URL: {track_url}")
    try:
        #Extracting track ID from URL
        track_id = re.search(r'track/([a-zA-Z0-9]+)',track_url).group(1)
        print(track_id + "\n")
        
        #Fetching track details in JSON format
        track_info = sp.track(track_id)
        #print(track_info)

        #Extract Metadata
        track_metadata = {
            'Track Id' : track_info['id'],    
            'Track Name' : track_info['name'],
            'Artist' : track_info['artists'][0]['name'],
            'Album' : track_info['album']['name'],
            'Popularity' : track_info['popularity'],
            'Duration (ms)' : track_info['duration_ms'] / 60000
        }

        print(f"Track details:\n Track Id: {track_metadata['Track Id']}" + 
              f"\n Track Name: {track_metadata['Track Name']}" + f"\n Artist: {track_metadata['Artist']}" + 
              f"\n Album: {track_metadata['Album']}" + f"\n Popularity: {track_metadata['Popularity']}" + 
              f"\n Duration (minutes): {track_metadata['Duration (ms)']:.2f}\n")

        #Insert metadata into MySQL database
        insert_query = """
            INSERT INTO spotify_tracks (track_id, track_name, artist, album, popularity, duration_ms)
            values (%s, %s, %s, %s, %s, %s)
            """
        values = (track_metadata['Track Id'], track_metadata['Track Name'], track_metadata['Artist'], track_metadata['Album'],
          track_metadata['Popularity'], track_metadata['Duration (ms)'])
        cursor.execute(insert_query, values)
        connection.commit()
        
        print(f"Track {track_metadata['Track Name']} metadata inserted into database successfully.\n")

        #Fetch and display data from the database to verify insertion
        select_query = "SELECT * FROM spotify_tracks"   
        cursor.execute(select_query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except Exception as e:
        print(f"Error in processing URL:{track_url}, Error: {e}")
    
#Close the database connection
cursor.close()
connection.close()