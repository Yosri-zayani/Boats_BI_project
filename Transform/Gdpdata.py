import pandas as pd 
file_path ='GDPfinal.json'
df = pd.read_json(file_path)
Columns_to_remove = ["Capital City","Anthem","Government","Land Area","Area",'Population Rank','Growth Rate',"World Percentage","Density","2020 Population Rank","2020 World Percentage","2020 Growth Rate"]
df = df.drop(columns=Columns_to_remove)

NewGdp_csv = 'new_gdp.csv'
df.to_csv(NewGdp_csv, index=False)

print(f"CSV file saved at: {NewGdp_csv}")