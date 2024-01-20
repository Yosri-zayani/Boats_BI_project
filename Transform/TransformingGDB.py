import pandas as pd
file_path_1 ='GpdData.csv'
# Read the CSV file into a Pandas DataFrame
df_1 = pd.read_csv(file_path_1)

#remove empty rows 
for i in range(1996, 1960):
    df_1 =  df_1.drop(['${i}'])
# Save the transformed DataFrame to a new CSV file
output_file_path_1 = 'transformed_GDP.csv'
df_1.to_csv(output_file_path_1, index=False)
print(f'Transformed data saved to {output_file_path_1}')