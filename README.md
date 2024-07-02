# Spotify Top Hip-Hop Artists Analysis Project

## Project Description

This project aims to analyze the top 50 hip-hop artists on Spotify based on their popularity and start year. The data is fetched using the Spotify API, processed, and stored in both SQLite database (`spotify_artists.db`) and CSV format (`spotify_artists_data.csv`). The goal is to determine if any of the top hip-hop artists emerged in the years 2020-2024 or the broader 2020s decade.

## Table of Contents

1. [How to Install and Run the Project](#how-to-install-and-run-the-project)
2. [How to Use the Project](#how-to-use-the-project)
3. [How to Do Tests](#how-to-do-tests)
4. [License](#license)

---

## How to Install and Run the Project

### Prerequisites

Before running the project, ensure you have Python installed on your system. You'll also need to set up a virtual environment (venv) to manage dependencies.

### Installation

1. **Clone the repository:**

   ```bash
   git clone <[https://github.com/sunilmakkar/data-projects.git]>
   cd data-projects/Spotify_API_Project

2. **Set up a virtual environment (optional but recommended):**

    python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`

SPOTIPY_CLIENT_ID=your_spotify_client_id
SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
SPOTIPY_REDIRECT_URI=http://localhost:8888/callback


4. **Install dependencies:**
    pip install spotipy python-dotenv



### How to RUN the project

1. **Configure your .env file:**

   ```bash
   Make sure your '.env' file is properly configured with your spotify client credentials.

2. **Execute the main script:**

    python spotify-api-project.py
    This script will fetch the top 50 hip-hop artists from Spotify, sort them by popularity, retrieve their start year, and store the data in spotify_artists.db and spotify_artists_data.csv.


### How to USE the project

    After running main.py, you will have two main files:

    - spotify_artists.db: SQLite database containing the top hip-hop artists data.
    - spotify_artists_data.csv: CSV file with the same data, suitable for further analysis or reporting.


### How to USE the project

    Currently, this project does not include automated tests. Testing can be implemented by creating test scripts or unit tests to validate data fetching, processing, and exporting functionalities.


### How to USE the project

    This project is licensed under the MIT License.


### Notes:
- Each section is clearly labeled and follows a logical order: Installation, Running the Project, Usage, Testing, and License.
- Commands are provided in a format that should work across different operating systems (Unix-like systems and Windows).
- Ensure to use `<rhttps://developer.spotify.com/documentation/web-api>` as the actual URL.
- Adjust paths and specific instructions based on your project's structure and requirements.


