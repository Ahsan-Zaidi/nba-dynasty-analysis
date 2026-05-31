# NBA Dynasty Analysis Pipeline

An end-to-end Python data pipeline that ingests live NBA historical data via REST API, cleans and filters it across dynasty eras to produce comparative analysis and visualizations to uncover what made the greatest franchises in NBA history so dominant.

## Overview

A data pipeline built in Python that pulls live historical NBA data via the nba_api REST API to analyze what separates championship franchises from the rest. By comparing five of the greatest dynasties across different eras, this project explores the offensive and defensive traits that define sustained excellence and asks the question: does defense or offense win championships, and what is non-negotiable when building a winning franchise culture?

## Dynasty Eras Analyzed

**Boston Celtics**
The first true dynasty in NBA history, the Celtics established the standard for sustained excellence during the league's earliest years. The Bill Russell era (1957-1969) produced 11 championships in 13 seasons, a record that still stands today. Powered by Russell's unmatched defensive presence and the strategic mind of coach Red Auerbach, this dynasty defined what it meant to build a winning culture. In the 1980s, Larry Bird revived the franchise alongside Robert Parish, Kevin McHale, and Bill Walton, a team that dominated on both ends of the floor and served as the stepping stone to the Jordan era. Finally the 2008-2012 Celtics pioneered the modern superteam concept, assembling Paul Pierce, Kevin Garnett, and Ray Allen into the first true Big Three, a defensive powerhouse that brought a championship back to Boston.

**Los Angeles Lakers**
The Lakers are the Celtics' greatest rival and the second franchise to establish a dynasty in the NBA's early years. The Minneapolis Lakers (1948-1954) were one of the league's first dominant teams before relocating to Los Angeles. The franchise reached its cultural peak during the Showtime era (1980-1988), when Magic Johnson and Kareem Abdul-Jabbar with James Worthy as their running mate redefined basketball with an up-tempo fast break style that revolutionized the game. Then came the Shaq and Kobe era (2000-2004), arguably the hardest scoring environment in modern NBA history, where a dominant Shaquille O'Neal and a young hungry Kobe Bryant led the franchise to a three-peat.

**Chicago Bulls**
The Bulls dynasty of the 1990s (1991-1998) was built around arguably the greatest player to ever play the game, Michael Jordan. Alongside Scottie Pippen and under the guidance of coach Phil Jackson, the Bulls went a perfect 6-0 in the Finals across two three-peats. Their identity was defined by ferocious defense, elite athleticism, and a superhuman in Jordan who simply could not be stopped. The Bulls led all dynasties in steals per game, a testament to how suffocating their defensive scheme truly was.

**San Antonio Spurs**
The most consistent dynasty in NBA history. From 1999 to 2014 the Spurs won five championships across four different decades, a feat no other franchise has matched. Despite posting the lowest scoring averages among the dynasties analyzed, they maintained one of the strongest defensive identities of any era. The franchise was anchored by Tim Duncan, the greatest power forward of all time, and guided by Coach Gregg Popovich whose culture of selflessness and accountability became the blueprint for winning organizations. The Spurs dynasty cycled through generations, David Robinson, Tony Parker, Manu Ginobili, and Kawhi Leonard, all playing within the same system. That culture of excellence extends to this day with Victor Wembanyama carrying the torch in 2026.

**Golden State Warriors**
The most offensively efficient dynasty of the modern era. Led by Stephen Curry, the greatest shooter in NBA history, the Warriors (2015-2019) fundamentally changed how basketball is played, turning the three point shot from a secondary weapon into the foundation of an entire offensive system. Their 2015 championship came at the expense of LeBron James and the subsequent addition of Kevin Durant created one of the most talented rosters ever assembled, producing back to back titles in 2017 and 2018. What is often overlooked is that this was equally a defensive dynasty, with Draymond Green and Andre Iguodala anchoring a scheme that was as disruptive defensively as it was prolific offensively. The Warriors averaged 31.49 three point attempts per game during their dynasty years, nearly double any other franchise analyzed.

## Project Structure

```
nba-dynasty-analysis/
├── data/
│   ├── Lakers.csv
│   ├── Bulls.csv
│   ├── Spurs.csv
│   ├── Warriors.csv
│   ├── Celtics.csv
│   ├── Lakers_cleaned.csv
│   ├── Bulls_cleaned.csv
│   ├── Spurs_cleaned.csv
│   ├── Warriors_cleaned.csv
│   └── Celtics_cleaned.csv
├── scripts/
│   ├── ingest.py
│   ├── clean.py
│   ├── report.py
│   └── visualize.py
├── visuals/
│   ├── win_pct_comparison.png
│   ├── avg_ppg_comparison.png
│   └── avg_3pta_by_team.png
├── reports/
├── requirements.txt
└── README.md
```

## Scripts

- **ingest.py** — Connects to the nba_api REST API and fetches year by year historical stats for all five dynasty franchises. Saves raw data as CSV files to the data folder.

- **clean.py** — Loads raw CSV files and filters each team's data to their defined dynasty era windows. Handles null values, drops irrelevant columns, and addresses early NBA data quality issues where stats were not tracked. Saves cleaned files with a _cleaned suffix.

- **report.py** — Loads cleaned data and generates descriptive statistics across three analytical questions: which dynasty had the highest win percentage, how did scoring evolve across eras, and which dynasty was the most defensively dominant.

- **visualize.py** — Produces three Matplotlib charts comparing dynasty performance across win percentage, points per game, and three point attempt trends over time.

## Key Insights

- The Spurs had the highest average win percentage at 0.704 across their dynasty years. They were also the lowest scoring team of the group which tells you everything about what Pop built in San Antonio. Defense and culture win championships.
- The Warriors averaged 31.49 three point attempts per game during their dynasty. That is nearly double the Spurs and more than seven times the early Lakers and Celtics who played before the three point line even existed. The game changed completely.
- The Bulls led every dynasty in steals per game at 8.94. That was Jordan's era and the numbers back it up. That team was built to take the ball from you.
- Early NBA data before 1980 had untracked stats for field goal percentage, steals, and blocks. Those showed up as zeros which would have completely skewed the cross era comparisons. Had to identify and clean those out before drawing any conclusions.
- The Celtics FG% went from 0.204 to 0.491 after replacing those untracked zeros with null values. One data cleaning decision completely changed the outcome of the analysis.

## Visualizations

- **Dynasty Win Percentage Comparison** — Bar chart comparing average win percentage across each franchise's dynasty era windows. The Spurs lead at 0.704 with the Warriors lowest at 0.668 despite their offensive dominance.

- **Dynasty Points Per Game Comparison** — Bar chart showing average points scored per game across dynasty seasons. The Warriors lead at 113.65 PPG followed by the Celtics at 111.37, reflecting the high scoring modern era vs the slower pace of earlier decades.

- **The 3 Point Revolution** — Line chart showing how three point attempts per game evolved across each dynasty's years. The most visually striking chart in the project, showing the flat zero line for pre-1980 teams, gradual adoption through the 90s and 2000s, and the Warriors exploding off the chart in 2015 with an unprecedented volume of three point attempts.

## How to Run

**1. Clone the repository:**
```bash
git clone https://github.com/Ahsan-Zaidi/nba-dynasty-analysis.git
cd nba-dynasty-analysis
```

**2. Create and activate a virtual environment:**
```bash
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Run the scripts in order:**
```bash
python scripts/ingest.py
python scripts/clean.py
python scripts/report.py
python scripts/visualize.py
```

Note: ingest.py makes live API calls to NBA.com. Run this first to generate the raw CSV files before running the remaining scripts.

## Tools & Libraries

- Python
- Pandas
- Matplotlib
- nba_api
- REST APIs
- Git & GitHub