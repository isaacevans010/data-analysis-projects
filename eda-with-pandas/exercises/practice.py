import pandas as pd
import numpy as np

filepath = "C:/Users/fibdi/Downloads/iris_extended.csv"
irises_df = pd.read_csv(filepath)
print(irises_df.head())
most_common_soiltype = pd.Series.mode(irises_df["soil_type"])

## most_common_soiltype1 = pd.Series.groupby(irises_df["species"])[most_common_soiltype]

print(most_common_soiltype)
