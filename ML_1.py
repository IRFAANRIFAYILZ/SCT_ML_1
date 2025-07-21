# Import libraries
import pandas as pd
from sklearn.linear_model import LinearRegression

# Sample data (you can replace this with your own data or CSV file)
data = {
    'SquareFootage': [1000, 1500, 2000, 2500, 3000],
    'Bedrooms': [2, 3, 3, 4, 4],
    'Bathrooms': [1, 2, 2, 3, 3],
    'Price': [200000, 300000, 400000, 500000, 600000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Separate input (X) and output (y)
X = df[['SquareFootage', 'Bedrooms', 'Bathrooms']]
y = df['Price']

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Predict price for a new house
sqft=int(input("Enter square feet: "))
bedroom=int(input("Enter number of bedrooms: "))
bathroom=int(input("Enter number of bathrooms: "))
new_house = [[sqft,bedroom,bathroom]]

predicted_price = model.predict(new_house)
print("Predicted Price:", predicted_price[0])
