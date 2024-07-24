import sqlite3
import pandas as pd

# Specify the path of your SQLite database
database_path = 'path_to_your_database.db'

# Connect to the SQLite database
conn = sqlite3.connect(database_path)

# Retrieve the list of tables
query = "SELECT name FROM sqlite_master WHERE type='table';"
tables_df = pd.read_sql_query(query, conn)

# Display the list of tables
print("Tables in the database:")
print(tables_df)

# If you want to display a specific table
if not tables_df.empty:
    table_name = tables_df['name'].iloc[0]  # Gets the name of the first table
    data_query = f'SELECT * FROM {table_name}'
    df = pd.read_sql_query(data_query, conn)
    print(f"\nData from the table '{table_name}':")
    print(df)

# Close the connection to the database
conn.close()