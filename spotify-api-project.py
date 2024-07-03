import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import sqlite3
import csv

# Load environment variables from .env file
load_dotenv()

# Initialize Spotipy with authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth())

# Function to establish SQLite connection and create table
def setup_database():
    try:
        # Establish connection to SQLite database
        conn = sqlite3.connect('spotify_artists.db')
        c = conn.cursor()

        # Create table if not exists
        c.execute('''
                  CREATE TABLE IF NOT EXISTS artists (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      artist_name TEXT,
                      start_year INTEGER,
                      popularity INTEGER
                  )
                  ''')

        # Commit changes and close connection
        conn.commit()
        conn.close()
        
    except sqlite3.Error as e:
        print(f"Error setting up SQLite database: {e}")

# Function to insert data into SQLite table
def insert_into_database(artists_data):
    try:
        # Establish connection to SQLite database
        conn = sqlite3.connect('spotify_artists.db')
        c = conn.cursor()

        # Insert data into SQLite table
        c.executemany('''
                      INSERT INTO artists (artist_name, start_year, popularity)
                      VALUES (?, ?, ?)
                      ''', artists_data)

        # Commit changes and close connection
        conn.commit()
        conn.close()
        
    except sqlite3.Error as e:
        print(f"Error inserting data into SQLite database: {e}")

# Function to fetch top hip-hop artists and process data
def fetch_top_artists():
    try:
        # Fetch top 50 hip-hop artists
        results = sp.search(q='genre:hip-hop', type='artist', limit=50)
        artists = results['artists']['items']

        # Sort artists by popularity (descending order)
        artists.sort(key=lambda x: x['popularity'], reverse=True)

        # Prepare data for insertion into SQLite and CSV export
        artists_data = []
        for artist in artists:
            artist_name = artist['name']
            artist_id = artist['id']
            start_year = get_first_track_year(artist_id)
            popularity_score = artist['popularity']
            
            artists_data.append((artist_name, start_year, popularity_score))
            
            # Print information (optional)
            print(f"Artist: {artist_name}")
            print(f"Start Year on Spotify: {start_year}")
            print(f"Popularity Score on Spotify: {popularity_score}")
            print("-" * 30)

        # Insert data into SQLite table
        insert_into_database(artists_data)

        # Export data to CSV file
        export_to_csv()

    except Exception as e:
        print(f"Error fetching top artists: {str(e)}")

# Function to retrieve the first track year for an artist
def get_first_track_year(artist_id):
    try:
        tracks = sp.artist_top_tracks(artist_id)['tracks']
        if tracks:
            tracks.sort(key=lambda x: x['album']['release_date'])
            first_track = tracks[0]
            if 'album' in first_track and 'release_date' in first_track['album']:
                return first_track['album']['release_date'][:4]
    except Exception as e:
        print(f"Error fetching data for artist ID {artist_id}: {str(e)}")
    return "Unknown"

# Function to export data from SQLite to CSV
def export_to_csv():
    try:
        # Establish connection to SQLite database
        conn = sqlite3.connect('spotify_artists.db')
        cursor = conn.cursor()

        # SQL query to fetch all data from artists table
        query = "SELECT * FROM artists ORDER BY popularity DESC"
        cursor.execute(query)

        # Fetch all rows
        rows = cursor.fetchall()

        # Define CSV file path
        csv_file = 'spotify_artists_data.csv'

        # Write to CSV
        with open(csv_file, 'w', newline='', encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            # Write header
            csv_writer.writerow([i[0] for i in cursor.description])
            # Write rows
            csv_writer.writerows(rows)

        print(f"Data exported to {csv_file} successfully.")

    except sqlite3.Error as e:
        print(f"Error exporting data to CSV: {e}")

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()

# Main function to orchestrate the process
def main():
    setup_database()
    print("Fetching top 50 hip-hop artists...")
    fetch_top_artists()

# Execute main function
if __name__ == "__main__":
    main()
