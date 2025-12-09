Developed a ETL pipeline that extracts detailed music metadata from the Spotify Web API using Spotipy, enabling automated retrieval of track, artist, and album attributes. Datasets were transformed and cleaned using Regex and loaded into a MySQL database via pymysql, creating a structured dataset of Spotify track metadata for analytical readiness.

spotify_mysql.py - Python script used for single-record testing, designed to process only a single, hardcoded track URL. It fetches the track metadata, truncates the MySQL table, inserts the single track, and displays the result.

spotify.py - Python script fetches metadata for a single, hardcoded track, converts the data into a Pandas DataFrame, saves the DataFrame to a CSV file (spotify_track_metadata.csv), and uses Matplotlib to generate and display a bar chart visualizing the track's popularity and duration.

spotify_mysql_urls.py - Python script reads a list of track URLs from the track_urls.txt file, iterates through each one, extracts the track ID, uses the Spotipy API to fetch the detailed metadata, and inserts the data into the DB table in MySQL.

track_urls.txt - Text file containing a list of Spotify track URLs. These URLs are used by spotify_mysql_urls.py to simulate a stream of tracks that need to be processed and logged.

spotify_database.sql - DDL for table ( It describes the table structure)
