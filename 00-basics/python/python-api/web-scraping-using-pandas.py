#
# ^ Optional dependency installation is required 'pip3 install lxml'
import pandas as pd

# url = "http://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
# tables = pd.read_html(url)
# df = tables[0]

# print(df)


URL = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"
tables = pd.read_html(URL)
# for table in tables:
# print(table)
df = tables[3]
print(df)

df.columns = range(df.shape[1])
# print(df[[0,2]])

print(df.iloc[1:11])
print(df.iloc[1:11,:])