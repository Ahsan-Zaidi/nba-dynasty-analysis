import pandas as pd
import time
from nba_api.stats.static import teams as nba_teams
from nba_api.stats.endpoints import teamyearbyyearstats

# Dictionary of dynasty franchises mapped to their NBA_API official IDs
dynasty_teams = {
    "Lakers": 1610612747,
    "Bulls": 1610612741,
    "Spurs": 1610612759,
    "Warriors": 1610612744,
    "Celtics": 1610612738
}

# Loop used to get target team IDs from the API
# all_teams = nba_teams.get_teams()
# target_teams = {"Lakers", "Bulls", "Spurs", "Warriors", "Celtics"}
# for team in all_teams:
#     if team["nickname"] in target_teams:
#         print(team)

# Empty dictionary to hold dynasty teams and their stats / df
teams = {}

for team_name, team_id in dynasty_teams.items():
    # Send API request for each individual team per iteration saving the returned data in stats
    stats = teamyearbyyearstats.TeamYearByYearStats(team_id)

    # Convert API response to pandas dataframe
    df = stats.get_data_frames()[0]

    # Store dataframe in teams dictionary using team_name as key
    teams[team_name] = df

    # Pause 1 second between requests to avoid rate limiting NBA.com
    time.sleep(1)
    print(df.shape)
    print(df.head())
    print(df.isnull().sum())

# Loop through teams dictionary and save each dataframe as a csv to the data folder
for team_name, df in teams.items():
    df.to_csv(f"data/{team_name}.csv", index=False)
    print(f"Saved {team_name} data to data/{team_name}.csv")
