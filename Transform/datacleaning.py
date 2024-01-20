import pandas as pd 

file_path ='transformed_Boats.csv'
df = pd.read_csv(file_path)


df["Type"] = df['Type'].str.replace(',', '')
df["Boat Type"] = df['Boat Type'].str.replace(',', '')


# Save the modified DataFrame back to a CSV file
df.to_csv('finaleBoat.csv', index=False)