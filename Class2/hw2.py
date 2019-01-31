import pandas as pd

file_name = "/Users/MsBrilliant/Files/ucla_winter_2019/stats404/week3/employee_reviews.csv"
df = pd.read_csv(filepath_or_buffer=file_name)

df.shape
df.columns
df.head()
df.tail()
import matplotlib.pyplot as plt
df['helpful-count'].hist(bins=1)
df.describe()