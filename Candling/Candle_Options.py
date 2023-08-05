# %%
import numpy as np
import pandas as pd
from Options_NBBO_Candling import options_NBBO_candle
import pandas_market_calendars as mcal
import os

# %%
#get all the options contracts that we will be candling this batch
files = "/srv/sqc/volatility_exploration/temp_files.csv"
df = pd.read_csv(files)
all_files = df['all_files'].tolist()

# %%
#getting all market days from April 01 2022, to December 31 2022
nyse = mcal.get_calendar('NYSE')
dates = (nyse.schedule(start_date ='2022-04-01', end_date='2022-12-31'))['market_open'].to_list()

#make a directory for each market day
for num in range(len(dates)):
    date = dates[num].date().strftime('%Y%m%d')
    os.mkdir("/srv/sqc/volatility_exploration/fixed_candle/Options_Data/" + date)

# %%
print(all_files[0].split('.')[1].split('/')[0])

# %%
for ind in range(len(all_files)):
    path = "/srv/sqc/data/us-options-tanq/us-options-tanq-2022/" + all_files[ind]
    date = all_files[ind].split('.')[1].split('/')[0]
    file_name = date + "/" + all_files[ind].split('.')[-3] + ".csv"
    output_path = "/srv/sqc/volatility_exploration/fixed_candle/Options_Data/" + file_name
    print(ind)
    options_NBBO_candle(path, output_path)
# %%