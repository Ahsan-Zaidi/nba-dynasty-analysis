import pandas as pd

# list of target teams in the data files
# empty dictionary to store each teams dataframes
teams = ["Lakers", "Bulls", "Spurs", "Warriors", "Celtics"]
dynasty_teams = {}

# loop through each teams data in cleaned csv
for team in teams:
    df = pd.read_csv(f"data/{team}_cleaned.csv")

    # save team data into dataframes
    dynasty_teams[team] = df

most_wins = []

for team, df in dynasty_teams.items():
    # calculate the average win percentage of every team
    wins = df["WIN_PCT"].mean().round(3)

    # append a key value pair to most_wins list for each team and their win percentage
    most_wins.append({"team": team, "win_pct": wins})

# sort most_wins list by dynasty with the highest to lowest win percentage
most_wins.sort(key=lambda x: x["win_pct"], reverse=True)

# OUTPUT HEADER
print("=" * 40)
print("DYNASTY TEAMS WIN PERCENTAGE RANKINGS")
print("=" * 40)
for item in most_wins:
    print(f"{item['team']}: {item['win_pct']}")

team_scores_avg = []

for team, df in dynasty_teams.items():
    # calculate avg pts per season by dividing total points by games played
    avgptsper_season = (df["PTS"] / df["GP"]).mean().round(2)

    # calculate avg 3pt attempted per season by dividing games played
    avg3pt_attempt = (df["FG3A"] / df["GP"]).mean().round(2)

    # calculate field goal percentage 
    # NBA didnt track fg percentage in the early years replace the values with Null to not skew data results
    avg_fg_pct = df["FG_PCT"].replace(0, pd.NA).mean().round(3)

    # append scoring results per team to list 
    team_scores_avg.append({
        "team": team,
        "avg_pts": avgptsper_season,
        "avg_3pt_attempts": avg3pt_attempt,
        "avg_fg_pct": avg_fg_pct
    })

# OUTPUT HEADER
print("=" * 45)
print("DYNASTY TEAMS SCORING COMPARISON ACROSS ERAS")
print("=" * 45)

# Diagnostic line to investigate why Bostons FG_PCT is so low compared to the other teams
# print(dynasty_teams["Celtics"][["YEAR", "FG_PCT"]].to_string())

# Iterate through the dynasty teams and avg points scored per season | avg 3pt attempts per season | avg fg pct per season
for item in team_scores_avg:
    print(f"{item['team']}: {item['avg_pts']} PTS | {item['avg_3pt_attempts']} 3PTA | {item['avg_fg_pct']} FG%")

def_stats_per_team = []

for team, df in dynasty_teams.items():
    # calculate avg steals per season by dividing games played
    # replace 0s with nulls to keep data fair & consistent for early dynasties
    avg_steals = (df["STL"].replace(0, pd.NA) / df["GP"]).mean().round(2)

    # calculate avg blocks per season by dividing games played
    # replace 0s with nulls to keep data fair & consistent for early dynasties
    avg_blocks = (df["BLK"].replace(0, pd.NA) / df["GP"]).mean().round(2)

    # calculate avg turnovers per season by dividing games played
    avg_turnovers = (df["TOV"] / df["GP"]).mean().round(2)

    # append the defensive averages to the defensive stats list
    def_stats_per_team.append({
        "team": team,
        "avg_steals": avg_steals,
        "avg_blocks": avg_blocks,
        "avg_tov": avg_turnovers
    })

# OUTPUT HEADER
print("=" * 55)
print("DYNASTY TEAMS DEFENSIVE STATS COMPARISON ACROSS ERAS")
print("=" * 55)

# Iterate through the dynasty teams and display avg steals per season | avg blocks per season | avg turnovers per season
for item in def_stats_per_team:
    print(f"{item['team']}: {item['avg_steals']} STL | {item['avg_blocks']} BLK | {item['avg_tov']} TOV")