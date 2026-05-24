import pandas as pd
import time
from nba_api.stats.static import teams as nba_teams
from nba_api.stats.endpoints import teamyearbyyearstats

dynasty_teams = {
    "Lakers": 1610612747,
    "Bulls": 1610612741,
    "Spurs": 1610612759,
    "Warriors": 1610612744
}

# Loop used to get target team IDs from the API

# all_teams = nba_teams.get_teams()
# target_teams = {"Lakers", "Bulls", "Spurs", "Warriors"}
# for team in all_teams:
#     if team["nickname"] in target_teams:
#         print(team)

teams = {}

for team_name, team_id in dynasty_teams.items():
    stats = teamyearbyyearstats.TeamYearByYearStats(team_id)
    df = stats.get_data_frames()[0]
    teams[team_name] = df
    time.sleep(1)
    print(df.shape)
    print(df.head())
    print(df.isnull().sum())

for team_name, df in teams.items():
    df.to_csv(f"data/{team_name}.csv", index=False)
    print(f"Saved {team_name} data to data/{team_name}.csv")
