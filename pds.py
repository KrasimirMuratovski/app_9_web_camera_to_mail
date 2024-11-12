import pandas as pd

lst = [3,6,2]
ser = pd.Series(lst, index = ['s', 't', 'u'])
# print(ser)


calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)