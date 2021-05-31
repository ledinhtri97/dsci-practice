import pandas as pd
from IPython.display import display

df_bh = pd.read_csv(
    "https://raw.githubusercontent.com/phamdinhkhanh/datasets/master/BostonHousing.csv", 
    sep=",", header = 0, index_col = None)

display(df_bh)

