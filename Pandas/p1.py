# Some Basics
# Series: A 1-dimensional labeled array. Think of it as a single column in a spreadsheet.
# DataFrame: A 2-dimensional labeled data structure. Think of it as the entire spreadsheet or table with rows and columns.

# Now here I create a Series
import pandas as pd
temp_list=[72,79,77,76]
tempratures=pd.Series(temp_list)
print(tempratures)

# Here I create DataFrame
data={
    'Name': ['Alice','Bob','Charlie'],
    'Age': [24,27,22],
    'City':['New York', 'Los Angeles', 'Chicago']
}
# Turning it into a Pandas DataFrame
df=pd.DataFrame(data)
print(df)