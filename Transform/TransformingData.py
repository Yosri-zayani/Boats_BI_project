import pandas as pd

file_path = 'boat_data1.csv'
file_path_1 ='API_NY.GDP.PCAP.CD_DS2_en_csv_v2_6298251.csv'
# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(file_path)

# Display the first 10 rows and columns
print(df.head(10))
# Define a mapping of currency codes to exchange rates
currency_exchange_rates = {'CHF': 1.08, 'EUR': 1.18, 'GBP': 1.38}  # Add more currencies as needed

df['Currency'] = df['Price'].str.extract('([A-Za-z]+)')
df['Amount'] = df['Price'].str.extract('(\d+)').astype(float)

# Convert prices to dollars using the exchange rates
df['Price_USD'] = df.apply(lambda row: row['Amount'] * currency_exchange_rates.get(row['Currency'], 1), axis=1)
# Drop the original 'Price', 'Currency', and 'Amount' columns
df = df.drop(['Price', 'Currency', 'Amount'], axis=1)

# Display the updated DataFrame
print(df.head(10))

# Extract the country name from the 'Location' column
df['Country'] = df['Location'].str.split(' Â» ').str[0]

# Drop the original 'Location' column
df = df.drop(['Location'], axis=1)


# Display the updated DataFrame
print(df.head(10))
# Save the transformed DataFrame to a new CSV file
output_file_path = 'transformed_Boats.csv'

df.to_csv(output_file_path, index=False)


print(f'Transformed data saved to {output_file_path}')
