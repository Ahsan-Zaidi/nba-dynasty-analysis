import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# list of target teams in the data files
teams = ["Lakers", "Celtics", "Bulls", "Warriors", "Spurs"]

# empty dictionary to store each teams dataframes
dynasty_teams = {}

for team in teams:
    # read csv files for each team iteration
    df = pd.read_csv(f"data/{team}_cleaned.csv")
    # assign dataframe to its associated team
    dynasty_teams[team] = df

# EMpty lists to hold x & y values in the chart
team_names = []
win_pct = []

# loop through key value pairs in dynasty teamss
for team, df in dynasty_teams.items():
    # add the team names to the team_name list as the x values
    team_names.append(team)

    # add the average win percentage to the win_pct list as the y values
    win_pct.append(df['WIN_PCT'].mean().round(3))

colors = ["purple", "green", "red", "gold", "black"]

# create and style visuals for dynasty win percentage comparison chart
plt.figure(figsize=(12, 7))
plt.bar(team_names, win_pct, color=colors, width=0.5, edgecolor='white', linewidth=0.5)
plt.title("DYNASTY TEAM WIN PERCENTAGE COMP\n\nAverage win percentage across each franchise's golden era(s)", fontsize=14, fontweight='bold', pad=20)
plt.xlabel("")
plt.ylabel("Average Win %", fontsize=12, labelpad=15)
plt.ylim(0.6, 0.75)
for i, v in enumerate(win_pct):
    plt.text(i, v + 0.001, str(v), ha="center", fontsize=11, fontweight='bold')
plt.tight_layout()
plt.savefig("visuals/win_pct_comparison.png", dpi=150, bbox_inches='tight')
plt.close()

# empty list to hold y values for the points per game chart
avg_pts_per_game = []

for team, df in dynasty_teams.items():
    # calculate average points by dividing games played to append it to the list for plotting reference
    avg_pts_per_game.append((df['PTS'] / df['GP']).mean().round(2))

# create and style visuals for dynasty points per game percentage across all dynasty seasons
plt.figure(figsize=(12, 7))
plt.bar(team_names, avg_pts_per_game, color=colors, width=0.5, edgecolor='white', linewidth=0.5)
plt.title("DYNASTY TEAMS POINTS PER GAME COMP\n\nComparison of average points per game totals across each franchise's peak", fontsize=14, fontweight='bold', pad=20)
plt.xlabel("")
plt.ylabel("Average PPG", fontsize=12, labelpad=15)
plt.ylim(0, 130)
for i, v in enumerate(avg_pts_per_game):
    plt.text(i, v + 2, str(v), ha="center", fontsize=11, fontweight='bold')
plt.tight_layout()
plt.savefig("visuals/avg_ppg_comparison.png", dpi=150, bbox_inches='tight')
plt.close()

# Plotting the line chart for 3pt attempt comparisons across teams
plt.figure(figsize=(12, 7))

for i, (team, df) in enumerate(dynasty_teams.items()):
    # establish x and y values for line chart and add the correspoding colors to each team
    plt.plot(df["start_year"], df["FG3A"] / df["GP"], label=team, color=colors[i])

plt.title("THE 3PT REVOLUTION\n\nAverage 3-point attempts per game across dynasties", fontsize=14, fontweight='bold', pad=20)
plt.xlabel("")
plt.ylabel("Average 3-pointer attempted", fontsize=12, labelpad=15)
plt.legend(loc="upper left")
plt.tight_layout()
plt.savefig("visuals/avg_3pta_by_team.png", dpi=150, bbox_inches='tight')
plt.close()
