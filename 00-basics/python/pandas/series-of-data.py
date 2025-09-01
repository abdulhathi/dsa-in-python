import pandas as pd

data = [x for x in range(10,101,10)]
print(data)

s = pd.Series(data)
print(s)

data = {'Name': ['Abdul','Abdul1','Abdul3'],
        'Age': [42,43,44],
        'City': ['CityA','CityB','CityC']
        }

df = pd.DataFrame(data)
print(df)

print(df.loc[1:2, 'Name'])