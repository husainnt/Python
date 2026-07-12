import pandas as pd
# DF= tabular ds with rows and col (2D)
data={
    "Name":["Spongebob","Patrick","Squidward"],
    "Age":[30,35,50],
}
d=pd.DataFrame(data)
# d=pd.DataFrame(data,index=["Employee 1","Employee 2","Employee 3"])
# print(d)
# print(d.loc["Employee 2"])

# Adding a new col
d["Job"]=["Cook", "N/A", "Cashier"]
print(d)

# Adding a new row -> create a new DF and then concat
new_row=pd.DataFrame([{"Name":"Sandy", "Age": 28, "Job":"Engineer"}],index=["Employee 4"])
d=pd.concat([d,new_row])
print(d)
