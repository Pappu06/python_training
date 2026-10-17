# Pandas in python Pandas is a Python library used to manipulate, analyze, clean, and organize structured data.

# import pasdas as pd 
import pandas as pd

# print(pd.__version__) # verify installation 


# # Series in Pandas 
# marks = pd.Series([85,95,78,88,92])

# print(marks)

# marks2 = pd.Series([85,95,78,88,92],["Rahul","Pappu","praveen","sandeep","Suraj"])

# print(marks2)


# DataFrame in Pandas 
data = {
    "Names": ["Rahul","Pappu","praveen","sandeep","Suraj"],
    "Marks": [85,95,78,88,92],
    "age": [24,23,25,22,21]
}

df = pd.DataFrame(data)

print(df)


# # Access Elements 
# print(df["Names"])
# print(df["Marks"])
# print(df["age"])

# Access one particular element 
print(df.loc[1,"Names"])

# Access full row
print(df.iloc[1])

# Filtering Data in Pandas

result = df[df["Marks"] > 90]

print(result)


# head()
print(df.head(2))

# tail()
print(df.tail(2))

# info()

print(df.info())

# describe()

print(df.describe())