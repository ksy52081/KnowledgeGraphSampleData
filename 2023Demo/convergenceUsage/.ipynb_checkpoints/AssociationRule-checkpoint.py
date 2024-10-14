from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd

# Load the mock data
df = pd.read_csv('/mnt/data/mock_shopping_cart.csv')

# Group by 'userId' and aggregate 'itemId' into a list for each user
user_transactions = df.groupby('userId')['itemId'].apply(list).tolist()

# Apply TransactionEncoder to convert the data into the format needed for apriori
te = TransactionEncoder()
te_ary = te.fit(user_transactions).transform(user_transactions)
df_encoded = pd.DataFrame(te_ary, columns=te.columns_)

# Apply the apriori algorithm to find frequent itemsets
frequent_itemsets = apriori(df_encoded, min_support=0.1, use_colnames=True)

# Generate the association rules from the frequent itemsets
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)

# Save the association rules to a CSV file
output_file_path = '/mnt/data/association_rules.csv'
rules.to_csv(output_file_path, index=False)

# Display the result to the user
import ace_tools as tools; tools.display_dataframe_to_user(name="Association Rules", dataframe=rules)

output_file_path
