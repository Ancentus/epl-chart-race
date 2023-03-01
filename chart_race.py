import pandas as pd
import pandas_alive

elec_df = pd.read_csv("points_table.csv",index_col=0,parse_dates=[0])

elec_df.fillna(0).plot_animated('pl_race.mp4',period_fmt="%Y-%m-%d",title='Premier League Race 2021-2022',fixed_max=True, enable_progress_bar=True)
