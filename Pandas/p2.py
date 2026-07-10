# Inspecting and Expanding our DataFrame
# Viewing Data: We can print specific columns by referencing their names, like inventory['Fruit'].
# Adding Columns: We can add a new column just like adding a new key to a Python dictionary.

import pandas as pd
data = {
    'Fruit': ['Apple', 'Orange', 'Mango'],
    'Quantity': [10, 15, 18]
}
inventory=pd.DataFrame(data)
# Adding a new col for price of each fruit
inventory['Price'] = [1.20, 0.80, 2.50]
print(inventory)
# Adding a new col for instock category
inventory['InStock']=['True', 'True', 'False']
print(inventory)