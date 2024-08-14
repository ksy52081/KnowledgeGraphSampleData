import pandas as pd
import random

# Parameters
user_ids = [str(i) for i in range(1, 51)]  # userId from "1" to "50"
item_ids = [f"Item{i}" for i in range(1, 15)]  # itemId from "Item1" to "Item14"
rows = 100  # Number of rows for the mock data

# Generate mock data
mock_data = {
    "userId": [random.choice(user_ids) for _ in range(rows)],
    "itemId": [random.choice(item_ids) for _ in range(rows)]
}

# Create DataFrame
df = pd.DataFrame(mock_data)

# Save to CSV
file_path = '/mnt/data/mock_shopping_cart.csv'
df.to_csv(file_path, index=False)

# Display the dataframe to the user
import ace_tools as tools; tools.display_dataframe_to_user(name="Mock Shopping Cart Data", dataframe=df)

file_path
