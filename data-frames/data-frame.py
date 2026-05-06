import pandas as pd

data = {
        "Name" : ["Robin", "Alex", "Tunip"],
        "Age" : [20, 21, 21]
}

df = pd.DataFrame(data, index = ["Emplpyee 1", "Emplpyee 2", "Emplpyee 3"])

#add a new column in the dataframe
df["job"] = ["Programer", "Tester", "N/A"]

#add a new row in the dataframe
new_rows = pd.DataFrame([{"Name" : "Cole", "Age" : 25, "job" : "Senior Developer"},
                        {"Name" : "Eugene", "Age" : 19, "job" : "Intern"}
                    ], index = ["Employee 4", "Intern"])
df = pd.concat([df, new_rows]) #we pass the all the dataframes that we need a python list to the method.


print(df)