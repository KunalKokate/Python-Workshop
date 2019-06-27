#import print_function
import matplotlib.pyplot as plt
import pandas as pd 
# print(pd.__version__)

# #The primary data structures in pandas are implemented as two classes:
# #DataFrame, which you can imagine as a relational data table, with rows and named columns.
# #Series, which is a single column. A DataFrame contains one or more Series and a name for each Series.
# #The data frame is a commonly used abstraction for data manipulation. 
# #One way to create a Series is to construct a Series object. 
# #For example:
# a = pd.Series(['India','San Francisco','San Jose','Sacremento'])
# print(a)

# #DataFrame objects can be created by passing a dict mapping string column names to their respective Series.
# #If the Series don't match in length, missing values are filled with special NA/NaN values.
# #Example:
city_names = pd.Series(['India','San Francisco','San Jose','Sacremento'])
population = pd.Series([98465269, 87546254, 75644588])
# b = pd.DataFrame({'City Names': city_names, 'Population': population})
# print(b)

# #But most of the time, you load an entire file into a DataFrame. The following example loads a file with California housing data.
# #Run the following cell to load the data and create feature definitions:
# california_housing_dataframe = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv")
# c = california_housing_dataframe.describe()
# print(c)
# d = california_housing_dataframe.head()
# print(d)
# e = california_housing_dataframe.hist('housing_median_age')
# print(e)
# plt.show(e)

# #Accessing Data
# #You can access DataFrame data using familiar Python dict/list operations:
cities = pd.DataFrame({'City Name':city_names, 'Population':population})
# print(type(cities['City Name']))
# print(cities['City Name'])
# print(type(cities['City Name'][1]))
# print(cities['City Name'][1])
# print(type(cities[0:3]))
# print(cities[0:3])

# # Manipulating Data
# # You may apply Python's basic arithmetic operations to Series. For example:
# f = population/1000
# print(f)
# import numpy as np 
# g = np.log(population)
# print(g)

# # Modifying DataFrames is also straightforward.
# # For example, the following code adds two Series to an existing DataFrame:
# cities['Area square miles'] = pd.Series([46.87, 187.54, 97.92])
# cities['Population Density'] = cities['Population'] / cities['Area square miles']
# print(cities)