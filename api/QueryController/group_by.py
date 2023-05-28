import pandas as pd

# Create a sample DataFrame
data = {'Name': ['John', 'Alice', 'Bob', 'John', 'Alice'],
        'City': ['New York', 'London', 'Paris', 'New York', 'London'],
        'Salary': [5000, 6000, 4000, 5500, 6500]}
df = pd.DataFrame(data)

# Group the DataFrame by 'City'
grouped = df.groupby('City')

print(grouped.groups.items())

# Iterate over each group using groups() method
for city, indices in grouped.groups.items():
    print(indices)
    group = df.loc[indices]
    print(f"City: {city}")
    print(group)
    print()


