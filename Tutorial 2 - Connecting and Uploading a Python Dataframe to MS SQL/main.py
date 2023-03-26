import pandas as pd
import pyodbc

# Define SQL Server connection parameters
server = 'LAPTOP-S1CGEN4M'
database = 'test_db'
username = 'sunny'
password = 'sunny123'
driver = '{ODBC Driver 17 for SQL Server}'

# Connect to SQL Server
cnxn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

# Define sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
    'Age': [25, 35, 30, 40, 28],
    'Work_Department': ['Sales', 'Marketing', 'IT', 'HR', 'Operations']
}

# Create DataFrame from sample data
df = pd.DataFrame(data)

# Define SQL Server table name
table_name = 'Employee'

# Upload DataFrame to SQL Server table
cursor = cnxn.cursor()

# Drop the table if it already exists (optional)
cursor.execute("IF OBJECT_ID('" + table_name + "', 'U') IS NOT NULL DROP TABLE " + table_name)

# Create the table
cursor.execute("CREATE TABLE " + table_name + " (Name VARCHAR(50), Age INT, Work_Department VARCHAR(50))")

# Insert the data into the table
for index, row in df.iterrows():
    cursor.execute("INSERT INTO " + table_name + " (Name, Age, Work_Department) values (?, ?, ?)",
                   row['Name'], row['Age'], row['Work_Department'])
    cnxn.commit()

# Close the cursor and connection
cursor.close()
cnxn.close()
