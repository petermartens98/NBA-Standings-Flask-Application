# Necessary Imports
from flask import Flask, render_template
from functools import lru_cache
from datetime import datetime, timedelta
import pandas as pd

# Define Flask Application
app = Flask(__name__)

# Cache Standings
@lru_cache(maxsize=1)
def cached_standings():
    return scrape_standings()

# Main Landing Page
@app.route("/", methods=['GET', 'POST'])
def standings_page():
    # Cache Standings every hour
    global last_cached_time
    if not hasattr(cached_standings, 'cached_time') or datetime.now() - cached_standings.cached_time > timedelta(hours=1):
        standings = scrape_standings()
        cached_standings.cached_time = datetime.now()
        cached_standings.data = standings
    else:
        standings = cached_standings.data
    west_standings = standings[standings.Conference == 'West'].reset_index(drop=True)
    west_standings['Rk'] = west_standings.index + 1
    east_standings = standings[standings.Conference == 'East'].reset_index(drop=True)
    east_standings['Rk'] = east_standings.index + 1
    return render_template('standings_page.html', east_standings=east_standings, west_standings=west_standings)

# Function to Webscrape NBA Standings
def scrape_standings():
    df_east = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2023_standings.html')[0]
    df_east = df_east.rename(columns={'Eastern Conference': 'Team'})
    df_east['Conference']='East'
    df_west = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2023_standings.html')[1]
    df_west = df_west.rename(columns={'Western Conference': 'Team'})
    df_west['Conference']='West'
    df_all = pd.concat([df_east, df_west]).sort_values('W', ascending=False).reset_index(drop=True)
    df_all['Team'] = df_all['Team'].str.replace(r'\(\d+\)$', '', regex=True)
    return df_all

# Run Flask Application
if __name__ == '__main__':
    app.run(debug=True)