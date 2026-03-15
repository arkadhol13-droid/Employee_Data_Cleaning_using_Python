#importing necessary libaries
import pandas as pd
import numpy as np

#loading the dataset
df = pd.read_csv('Indian Empoyee Dataset project\Employe Dataset projecta\Indian_employee_data.csv')
print(df.head())
#cheking missing values each column
print('missing values in each column')
print(df.isnull().sum())

df['Salary (INR)'] = df['Salary (INR)'].str.replace(',', '')
df['Salary (INR)'] = pd.to_numeric(df['Salary (INR)'], errors='coerce')
df['Performance Rating'] = pd.to_numeric(df['Performance Rating'], errors='coerce')

df['Salary (INR)'].fillna(df['Salary (INR)'].mean())

df['Performance Rating'].fillna(df['Performance Rating'].median())

df.replace([np.inf, -np.inf], np.nan, inplace=True)
df = df.fillna(df.select_dtypes(include=np.number).mean())

#remove dupicate value
df.drop_duplicates(inplace=True)

#replace negative salary
df['Salary (INR)'] = np.where(df['Salary (INR)'] < 0, df['Salary (INR)'].mean(), df['Salary (INR)'])

salary_mean = df['Salary (INR)'].mean()
salary_std = df['Salary (INR)'].std()
lower_bound = salary_mean - (3 * salary_mean)
upper_bound = salary_mean + (3 * salary_mean)

#remove where salary to high or low
df =df[(df['Salary (INR)'] >= lower_bound) & (df['Salary (INR)'] <= upper_bound)]

df.to_csv('cleaned_indian_employee_data.csv', index=False)
print('Data cleaning complete! saved as "cleaned_indian_employee_data.csv"')