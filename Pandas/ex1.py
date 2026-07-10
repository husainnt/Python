# Write the Python code to create a DataFrame named inventory from scratch. It should have two columns:
# Fruit and Quantity
import pandas as pd
data={
    'Fruit':['Apple','Orange','Mango'],
    'Quantity':[10,15,18]
}
df=pd.DataFrame(data)
print(df)