#!/bin/bash

# Step 1: Navigate to project directory (optional, assumed current directory)

# Step 2: Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # For Unix/Linux/macOS

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Set environment variables
export SPOTIFY_API_KEY='your_api_key'
export DATABASE_URL='your_database_connection_string'
# Add more environment variables as needed

# Step 5: Run your main script or application
python spotify-api-project.py


