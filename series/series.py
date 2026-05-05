import pandas as pd

# data = [100, 102, 104]
# things = [True, False, False]
# series = pd.Series(data) #this is a constructor not a function as the S is uppercased.
# series = pd.Series(data, index = ["a", "b", "c"])

# series.loc["c"] = 200 #we could also change the value at any given valid label using loc
# val = series.loc["a"]
# print(val)

# print(series)
# print(series.loc["a"]) #by this we will get the value which is in the label "a".
# print(series.iloc[0]) #by this we will get the value which are integer position
# print(series[series >= 101]) #by passing the series some condition we could make the series give output basis on that.

code = {"day 1" : 200, "day 2" : 300, "day 3" : 170 } 

series = pd.Series(code) #here we not passing any index as the values are labeled in the dictionary itself.
series.loc["day 3"] += 230

print(series[(series >= 200) & (series <= 400)])