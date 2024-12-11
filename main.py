import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('QtAgg')

pd.set_option('display.precision', 2)
# pd.set_option('display.max_columns', None)  # or 1000
pd.set_option('display.max_rows', 20)  # or 1000
# pd.set_option('display.max_colwidth', None)  # or 199
heart = pd.read_csv("./data/heart.csv")


print(f"{list(heart.columns)}\n")
print(heart.info())
# print(heart_df.describe(include="all"))
print(heart.describe())

features = heart.iloc[:, :-1]
labels = heart.iloc[:, -1:]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(heart["age"])
ax.set_xticks(np.arange(20, 81, 10))

plt.show()
