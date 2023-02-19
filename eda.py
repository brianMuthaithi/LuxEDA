# set up environment
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# load the data and understand its structure
data = pd.read_csv(r'/home/brian/Downloads/IT_Salary_Survey_EU.csv')
df = pd.DataFrame(data)
df.head()
list(df.columns)  # list column names
df.shape
df.corr()   #correlation 

#----------------clean the data-------------
df.drop_duplicates(inplace=True)    #remove duplicates
print(df)
df.dropna(inplace=True) #remove blank rows
print(df)

#select the required columns
df.filter(items=['Age', 'Seniority level', 'City', 'Gender', 'Employment status',
          'Contract duration', 'Have you lost your job due to the coronavirus outbreak?'])

df.groupby('Gender').count()  # number of males and females
df.groupby('Employment status').count()  # tally of each employement status
df.groupby('Have you lost your job due to the coronavirus outbreak?').count()   
df.filter(['Have you lost your job due to the coronavirus outbreak?']).groupby(['Employment status']).count()

#metrics
df.groupby('Gender').agg({'Age': ['mean', 'max', 'min', 'count']})      #mean/max/min age per gender
df.groupby('Gender').agg({'Yearly brutto salary (without bonus and stocks) in EUR': ['mean', 'max', 'min']})    #mean/max/min salary per gender
df.filter(['Employment status', 'Yearly brutto salary (without bonus and stocks) in EUR',]).groupby(['Employment status']).agg({'Yearly brutto salary (without bonus and stocks) in EUR': ['mean', 'max', 'min']})


