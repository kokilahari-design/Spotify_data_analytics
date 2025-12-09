import pandas as pd
import matplotlib.pyplot as plt
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import re

#Setting up Spotify API Client credentials
sp = spotipy.Spotify(auth_manager = SpotifyClientCredentials (
    client_id = "ddd7c9abb2c842c3a44469076ac3c414",
    client_secret = "3e5fbcf74d154b38aa3bed0bdb719df6"
))

#Full tarck URL
track_url = "https://open.spotify.com/track/6Z8oU8xMOie24Cflh2Sw6p?si=573f9bcbb9fa4e6a"

#Extracting track ID from URL
track_id = re.search(r'track/([a-zA-Z0-9]+)',track_url).group(1)
print(track_id + "\n")

#Fetching track details in JSON format
track_info = sp.track(track_id)
#print(track_info)

#Extract Metadata
track_metadata = {
    'Track Name' : track_info['name'],
    'Artist' : track_info['artists'][0]['name'],
    'Album' : track_info['album']['name'],
    'Popularity' : track_info['popularity'],
    'Duration (ms)' : track_info['duration_ms'] / 60000
}

print(f"Track details:\n Track Name: {track_metadata['Track Name']}" + f"\n Artist: {track_metadata['Artist']}" + 
      f"\n Album: {track_metadata['Album']}" + f"\n Popularity: {track_metadata['Popularity']}" + 
      f"\n Duration (minutes): {track_metadata['Duration (ms)']:.2f}")

#convert metadata to DataFrame
df = pd.DataFrame([track_metadata])
print(f"\nTrack data as DataFrame:\n {df}")

#save metadata to csv
df.to_csv("spotify_track_metadata.csv", index = False)

#visualization of track popularity and duration
features = ['Popularity', 'Duration (ms)']
values = [track_metadata['Popularity'], track_metadata['Duration (ms)']]
plt.figure(figsize=(8,5))
plt.bar(features, values, color = 'skyblue', edgecolor = 'black')
plt.title(f'Track Metadata for {track_metadata["Track Name"]} Song')
plt.ylabel('Values')
plt.show()

