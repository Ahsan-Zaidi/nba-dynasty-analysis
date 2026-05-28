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