import pandas as pd
df = pd.read_csv(r'C:\Users\Asmaa\IdeaProjects\Task3\Employees.csv')
print("Columns in the DataFrame:", df.columns)
if 'Salary(USD)' not in df.columns:
    raise ValueError("Column 'Salary(USD)' not found in the DataFrame.")
df = df.drop_duplicates()
df['Age'] = df['Age'].astype(int)
exchange_rate = 19.75
df['Salary in EGP'] = df['Salary(USD)'] * exchange_rate
average_age = df['Age'].mean()
print(f'Average Age: {average_age}')
median_salary = df['Salary in EGP'].median()
print(f'Median Salary in EGP: {median_salary}')
male_count = df[df['Gender'] == 'Male'].shape[0]
female_count = df[df['Gender'] == 'Female'].shape[0]
ratio_males_to_females = male_count / female_count if female_count != 0 else 'Undefined'
print(f'Ratio of Male to Female Employees: {ratio_males_to_females}')
df.to_csv('updated_data.csv', index=False)
