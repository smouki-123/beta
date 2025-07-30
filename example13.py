import pandas as pd


#read file 
file = pd.read_excel("ventas_2025.xlsx")


#excel to dictionary
ventas = file.to_dict(orient="records")


#show data
print(ventas)

for venta in ventas:
    print(venta)