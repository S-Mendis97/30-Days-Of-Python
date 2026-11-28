print("\n### Exercise 25: Pandas ###")
print("-------------------------------")

import pandas as pd
import numpy as np

hacker_news = pd.read_csv('data/hacker_news.csv')

print("First five rows:\n", hacker_news.head())

print("\nLast five rows:\n", hacker_news.tail())

title_column = hacker_news['title']
print("\nTitle column as a series:\n", title_column)

print("\nNumber of rows and columns:", hacker_news.shape)

#python_in_title = pd.Series(title for title in hacker_news['title'] if 'python' in title.lower()) # or 'Python' in title)
python_in_title = title_column[title_column.str.contains('python', case=False, na=False)] # case: ignore capitalization, na: treat missing values as non-matches
print("\nTitles with python in them:\n", python_in_title)

'''
for title in hacker_news['title']:
    if 'python' in title or 'Python' in title:
        python_in_title.append(title)
'''
js_in_title = title_column[title_column.str.contains('JavaScript', case=False, na=False)]
#js_in_title = pd.Series(title for title in hacker_news['title'] if 'JavaScript' in title)
print("\nTitles with JavaScript in them:\n", js_in_title)

print("\nColumn names:\n", hacker_news.columns)

print("\nDataset information:")
hacker_news.info()

print("\nStatistical summary:\n", hacker_news.describe())

print("\nMissing values:\n", hacker_news.isnull().sum())

print("\nNumber of Python titles:", len(python_in_title))

print("\nNumber of JavaScript titles:", len(js_in_title))