import pandas as pd
import seaborn as sns


data=sns.load_dataset('tips')

data.to_csv('data/tips.csv')