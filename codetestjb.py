import pandas as pd

# transaction data for calculation
data = pd.read_csv('transactions.csv')

# account data with calculated balances per account id and product
reconciliation_data = pd.read_csv('accounts.csv')

# Create dataframes and load data for analysis
df = pd.DataFrame(data)
reconciliation_df = pd.DataFrame(reconciliation_data)

# Create a new column 'adjusted_amount' where withdrawals are negative and deposits are positive
df['adjusted_amount'] = df.apply(
    lambda row: -row['amount'] if row['transaction_type'] == 'withdrawal' else row['amount'], axis=1)

# Group by 'account_id' and 'product_id' and sum the 'adjusted_amount'
result = df.groupby(['account_id', 'product_id']).agg(
    {'adjusted_amount': 'sum'}).reset_index()

# Merge the result with reconciliation_data
merged_df = pd.merge(result, reconciliation_df, on=[
                     'account_id', 'product_id'], how='outer', suffixes=('_calculated', '_expected'))

# Calculate the difference
merged_df['difference'] = merged_df['adjusted_amount'] - \
    merged_df['total_product_balance']

# Print the differences to a CSV file 
merged_df.to_csv('reconciliation_differences.csv', index=False)

print(merged_df)
