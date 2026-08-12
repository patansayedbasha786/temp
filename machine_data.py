import pandas as pd
#load the engineering dataset
df=pd.read_csv("machine_data.csv")
#display complete dataset
print("ENGINEERING DATASET")
print(df)
#display first 5 records
print("\nFIRST 5 RECORDS")
print(df.haed())
#display last 5 records
print("\nLAST 5 RECORDS")
print(df.tail())
#display number of rows & columns
print("\nDATASET SHAPE")
print(df.shape)
#display column names
print("\nCOLUMN NAMES")
print(df.columns)
#display data types
print("\nDATA TYPES")
print(df.dtypes)
#diplay basic imformation
print("\nDATASET IMFORMATION")
df.info()
#check missing values
print("\nMISSING VALUES")
print(df.isnull().sum())
#generate statistical summary
print("\nSTATISTICAL SUMMARY")
print(df.describe())
#calculate mean values
print("\nAVERAGE VALUES")
print("Temperature:",df["temperature"].mean())
print("Pressure:",df["pressure"].mean())
print("Vibration:",df["vibration"].mean())
print("Operating_hours:",df["operating_hours"].mean())
#find maximum and minimum temperature
print("\nTEMPERATURE ANALYSIS")
print("MAXIMUM TEMPERATURE:",df["temperature"].max())
print("MINIMUM TEMPERATURE:",df["temperature"].min())
#count machine according to status
print("\nMACHINE STATUS")
print(df["status"].value_counts())
#display machines with high temperature
print("\nMACHINES WITH TEMPERATURE ABOVE 85")
print(df[df["temperature"]>85])
