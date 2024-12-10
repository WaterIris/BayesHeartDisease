import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df_health = pd.read_csv("./health.csv")

print(df_health.info())



