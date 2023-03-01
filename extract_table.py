import pandas as pd

# Read the data from the file
df = pd.read_csv('eplmatches.csv')

# Filter the data for the 2021-2022 season
df = df[df['Season_End_Year'] == 2022]
df = df.sort_values(by='Date')  # sort the DataFrame by 'Date'
start_date = df['Date'].min()
end_date = df['Date'].max()

# Get a list of all teams in the 2021-2022 season
teams = sorted(set(df['Home']).union(set(df['Away'])))

# Create a new DataFrame to store the cumulative points for each team on each date of the season
new_df = pd.DataFrame(columns=['Date'] + teams)
new_df['Date'] = pd.date_range(start_date, end_date)
new_df = new_df.set_index('Date')  # set the index to the 'Date' column
new_df = new_df.sort_values(by='Date',ascending=False)  # sort the DataFrame by 'Date'

# Initialize all points to zero
for team in teams:
    new_df[team] = 0

# Loop through each match of the season
for index, match in df.iterrows():
    date = pd.to_datetime(match['Date'])
    print(date)
    home_team = match['Home']
    away_team = match['Away']
    home_goals = match['HomeGoals']
    away_goals = match['AwayGoals']

    if home_goals > away_goals:
        # Update points for home team
        new_df.loc[:date, home_team] += 3
        # Update points for away team
        new_df.loc[:date, away_team] += 0
    elif away_goals > home_goals:
        # Update points for home team
        new_df.loc[:date, home_team] += 0
        # Update points for away team
        new_df.loc[:date, away_team] += 3
    else:
        # Update points for both teams
        new_df.loc[:date, home_team] += 1
        new_df.loc[:date, away_team] += 1

new_df = new_df.sort_values(by='Date',ascending=True)  # sort the DataFrame by 'Date'

# Save the new DataFrame to a CSV file
new_df.to_csv('points_table.csv', index=True)

