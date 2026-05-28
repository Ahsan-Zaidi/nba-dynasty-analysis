import pandas as pd

# Dictionary defining each teams dynasty eras
# Teams with multiple eras have a list of era ranges
dynasty_eras = {
    "Lakers": [
        {"start": 1948, "end": 1954},
        {"start": 1980, "end": 1988},
        {"start": 2000, "end": 2004}
    ],
    "Celtics": [
        {"start": 1957, "end": 1969},
        {"start": 1981, "end": 1986},
        {"start": 2008, "end": 2012}
    ],
    "Bulls": [
        {"start": 1991, "end": 1998}
    ],
    "Spurs": [
        {"start": 1999, "end": 2014}
    ],
    "Warriors": [
        {"start": 2015, "end": 2019}
    ]
}


loaded_teams = {}

for team_name in dynasty_eras:
    # read CSV data from team data folder
    df = pd.read_csv(f"data/{team_name}.csv")

    # extract start year as an integer from YEAR string save it to start year variable
    df["start_year"] = df['YEAR'].str.split("-").str[0].astype(int)

    # store the data frame per team iteration
    loaded_teams[team_name] = df

filtered_teams = {}

for team_name in dynasty_eras:
    # retrieve loaded team data using df variable
    df = loaded_teams[team_name]
    
    # create a boolean mask initialized to false for every row in the dataframe
    # mark which seasons fall into dynasty season range
    mask = pd.Series([False] * len(df), index=df.index)

    # loop through each dynasty era for each current team
    # for each era, flip matching rows to true in the mask using OR to keep previously marked eras True
    for era in dynasty_eras[team_name]:
        mask |= (df["start_year"] >= era["start"]) & (df["start_year"] <= era["end"])
    
    # drop columns not necessary for analysis
    df = df.drop(columns=["TEAM_ID", "TEAM_CITY", "CONF_COUNT", "DIV_COUNT"])

    # fill missing finals appearance values with "N"
    df["NBA_FINALS_APPEARANCE"] = df["NBA_FINALS_APPEARANCE"].fillna("N")

    # apply the mask so that only dynasty era seasons are stored in filtered teams
    filtered_teams[team_name] = df[mask]

# check for any remaining null values in filtered_teams
for team_name in filtered_teams:
    print(f"\n{team_name} nulls:")
    print(filtered_teams[team_name].isnull().sum())

# save each cleaned and filtered dataframe as a CSV in the data folder
for team_name in filtered_teams:
    filtered_teams[team_name].to_csv(f"data/{team_name}_cleaned.csv", index=False)
    print(f"\nCleaned {team_name} data saved.")

    