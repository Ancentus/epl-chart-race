import pandas as pd

# Read the data from the file
df = pd.read_csv('eplmatches.csv')

# Filter the data for the 2021-2022 season
df = df[df['Season_End_Year'] == 2022]
start_date = df['Date'].min()
end_date = df['Date'].max()

# Get a list of all teams in the 2021-2022 season
teams = sorted(set(df['Home']).union(set(df['Away'])))

# Create a new DataFrame to store the points for each team on each date of the season
new_df = pd.DataFrame(columns=['Date'] + teams)
new_df['Date'] = pd.date_range(start_date, end_date)

# Initialize all points to zero
for team in teams:
    new_df[team] = 0

new_df = new_df.set_index('Date')

# Loop through each date of the season
for date in pd.date_range(start_date, end_date):
    date_str = date.strftime('%Y-%m-%d')
    print('Current date:', date_str)
    if date_str in df['Date'].values:
        print('Date is matchday')
        # Get all matches played on this date
        matches = df.loc[df['Date'] == date_str]

        # Update points for each team in each match
        for index, match in matches.iterrows():
            home_team = match['Home']
            away_team = match['Away']
            home_goals = match['HomeGoals']
            away_goals = match['AwayGoals']

            if home_goals > away_goals:
                new_df.loc[date_str, home_team] += 3
            elif away_goals > home_goals:
                new_df.loc[date_str, away_team] += 3
            else:
                new_df.loc[date_str, home_team] += 1
                new_df.loc[date_str, away_team] += 1

# Save the new DataFrame to a CSV file
new_df.to_csv('points_table.csv', index=False)

