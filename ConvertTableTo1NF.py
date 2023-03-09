import pandas as pd 
import numpy as np

df = pd.read_csv('data.csv',encoding='utf8')

#Separate String Data 
df['Course_ID']=df['Course_ID'].str.split(',')
df['Course_Name']=df['Course_Name'].str.split(",")
df.explode(['Course_ID','Course_Name'])

#Count the number of objects to flatten
lens = list(map(len, df['Course_ID'].values))

res = pd.DataFrame({
    'Student_ID': np.repeat(df['Student_ID'], lens), 
    'Program_Code': np.repeat(df['Program_Code'], lens), 
    'Term_ID': np.repeat(df['Term_ID'], lens), 
    'Term_Name': np.repeat(df['Term_Name'], lens), 
    'Start_Date': np.repeat(df['Start_Date'], lens), 
    'End_Date': np.repeat(df['End_Date'], lens), 
    'Program_Name': np.repeat(df['Program_Name'], lens), 
    'First_Name': np.repeat(df['First_Name'], lens), 
    'Last_Name': np.repeat(df['Last_Name'], lens), 
    'Course_ID': np.concatenate(df['Course_ID'].values),
    'Course_Name': np.concatenate(df['Course_Name'].values)
    })

res.to_csv("hello.csv",encoding = 'utf8',index=False)