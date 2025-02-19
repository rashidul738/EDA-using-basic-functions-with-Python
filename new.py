import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

df = pd.read_csv('eda_using_basic_data_functions_in_python_dataset1.csv')


df['date'] = pd.to_datetime(df['date'])

df.groupby(['date']).sum().sort_values('number_of_strikes', ascending=False).head(10)

df['month'] = df['date'].dt.month