import pandas as pd
from sklearn.linear_model import LinearRegression
from skops.io import dump


# Load the data file
df=pd.read_csv("housing_data 3.csv")

df.info()

# Seperate features and target
X=df[['Area_sqft','Bedrooms','Age_years']]
y=df['Price_$']


# Load and train model
model=LinearRegression()
trained_model=model.fit(X,y)

# Save the trained model
dump(trained_model, "model/model.skops")