import seaborn as sns
import matplotlib.pyplot as plt
import mysql.connector
import pandas as pd

##### CONNECTION
# Database connection function
"""
Establishes a connection to a MySQL database.

Args:
    host (str): The hostname or IP address of the MySQL server.
    user (str): The username for connecting to the database.
    password (str): The password associated with the username.
    database (str): The name of the specific database to connect to.

Returns:
    mysql.connector.connection object: The established connection object
        if successful, otherwise None.
"""
def connect_to_database(host, user, password, database):
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

# Query execution function
"""
Executes a provided SQL query on a MySQL database connection and returns the results.

Args:
    connection (mysql.connector.connection object): The established connection
        object to the database.
    query (str): The SQL query string to be executed.

Returns:
    list: A list of dictionaries representing the rows returned by the query.
        If the query doesn't return rows (e.g., DDL statements), an empty list 
        will be returned.
"""
def execute_query(connection, query):
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results

##### CREATE THE DF WITH THE QUERIES
# Function to create dataframes from query results
"""
Converts the results of an executed SQL query to a pandas DataFrame.

Args:
    connection (mysql.connector.connection object): The established connection
        object to the database.
    query (str): The SQL query string to be executed.

Returns:
    pandas.DataFrame: A DataFrame containing the data retrieved from the query.
        If the query doesn't return rows, an empty DataFrame will be returned.
"""
def query_to_dataframe(connection, query):
    results = execute_query(connection, query)
    return pd.DataFrame(results)

##### VISUALIZATION
# Visualization functions

#Visualization for themes
"""
Creates a bar chart visualizing the number of sets per theme in a pandas DataFrame.

Args:
    df (pandas.DataFrame): The DataFrame containing data on themes and their 
        corresponding number of sets. The DataFrame should have columns named 
        'Theme' and 'Number of sets'.
"""
def visualize_num_sets_per_theme(df):
    plt.figure(figsize=(12, 8))
    plot = sns.barplot(x='Number of sets', y='Theme', data=df)
    for index, row in df.iterrows():
        plot.text(row['Number of sets'], index, round(row['Number of sets'], 2), 
                  color='black', ha="center", va="center")
    plt.title('Number of Sets per Theme')
    plt.show()

#visualize top sets with most parts
"""
Creates a bar chart visualizing the top sets (potentially by a specified number) 
with the most parts in a pandas DataFrame.

Args:
    df (pandas.DataFrame): The DataFrame containing data on sets and their 
        corresponding number of parts. The DataFrame should have columns named 
        'name' and 'num_parts'.
"""
def visualize_top_sets_with_most_parts(df):
    plt.figure(figsize=(12, 8))
    plot = sns.barplot(x='num_parts', y='name', data=df)
    for index, row in df.iterrows():
        plot.text(row['num_parts'], index, round(row['num_parts'], 2), 
                  color='black', ha="center", va="center")
    plt.title('Top 10 Sets with the Most Parts')
    plt.xlabel('Number of Parts')
    plt.ylabel('Set Name')
    plt.show()

# visualize top sets with least parts
"""
Creates a bar chart visualizing the top sets (potentially by a specified number) 
with the least parts in a pandas DataFrame.

Args:
    df (pandas.DataFrame): The DataFrame containing data on sets and their 
        corresponding number of parts. The DataFrame should have columns named 
        'name' and 'num_parts'.
"""
def visualize_top_sets_with_least_parts(df):
    plt.figure(figsize=(12, 8))
    plot = sns.barplot(x='num_parts', y='name', data=df)
    for index, row in df.iterrows():
        plot.text(row['num_parts'], index, row['num_parts'], 
                  color='black', ha="center", va="center")
    plt.title('Top 10 Sets with the Least Parts')
    plt.xlabel('Number of Parts')
    plt.ylabel('Set Name')
    plt.show()

# visualize themes with most parts
"""
Creates a bar chart visualizing themes with the most parts in a pandas DataFrame.

Args:
    df (pandas.DataFrame): The DataFrame containing data on themes and their 
        corresponding total amount of parts. The DataFrame should have columns 
        named 'Theme' and 'Total amount of parts for the theme'.
"""
def visualize_themes_with_most_parts(df):
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Total amount of parts for the theme', y='Theme', data=df)
    plt.title('Themes with the Most Parts')
    plt.show()

# visualize quantity of pieces in oldest sets
"""
Creates a bar chart visualizing the quantity (number) of parts for each set 
in a pandas DataFrame.

Args:
    df (pandas.DataFrame): The DataFrame containing data on sets and their 
        corresponding number of parts. The DataFrame should have columns named 
        'name' and 'num_parts'.
"""
def visualize_quantity_of_pieces_in_oldest_sets(df):
    plt.figure(figsize=(12, 8))
    sns.barplot(x='num_parts', y='name', data=df)
    plt.title('Quantity of Pieces in the Oldest Sets')
    plt.show()

# visualize changes in quantity of pieces
"""
Creates a line chart visualizing the average number of pieces in LEGO sets 
across different years.

Args:
    df (pandas.DataFrame): The DataFrame containing data on LEGO sets with 
        columns named 'year' (likely representing the year the set was released) 
        and 'avg_num_parts' (likely representing the average number of pieces 
        per set for that year).

**Note:** This function assumes the DataFrame is already sorted by the 'year' 
column (ascending order) to ensure the line plot reflects the chronological 
changes in average number of pieces. 
"""
def visualize_changes_in_quantity_of_pieces(df):
    plt.figure(figsize=(12, 8))
    sns.lineplot(x='year', y='avg_num_parts', data=df)
    plt.title('Changes in the Quantity of Pieces in LEGO Sets from 1950 to 2017')
    plt.show()

