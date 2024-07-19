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

def visualize_oldest_sets(connection, queries):
    """Executes a query to get the oldest LEGO sets and visualizes their piece count.

    Args:
        connection: The established database connection.
        queries (dict): A dictionary containing the SQL queries.
    """

    query = queries['quantity_of_pieces_in_oldest_sets']  # Retrieve the query from the dictionary
    df_oldest_sets = query_to_dataframe(connection, query)

    # Determine the minimum year (oldest sets)
    min_year = df_oldest_sets['year'].min()

    # --- Visualization ---

    plt.figure(figsize=(12, 8))
    sns.barplot(data=df_oldest_sets, x='num_parts', y='name')
    plt.title(f'Number of Pieces in the Oldest LEGO Sets ({min_year})', fontsize=16)
    plt.xlabel('Number of Parts', fontsize=14)
    plt.ylabel('Set Name')

    # Add value labels to the bars
    for index, value in enumerate(df_oldest_sets['num_parts']):
        plt.text(value, index, str(value), color='black', va='center', ha='left')

    plt.show()

def visualize_year_variation(connection, queries):
    """
    Executes a query to get the variation of parts over time and visualizes it using a scatter plot with a trend line.
    
    Parameters:
    connection (sqlalchemy.engine.Engine): The SQLAlchemy engine connected to the database.
    queries (dict): A dictionary containing SQL queries.
    """
    
    query = queries['variation_num_part_over_year']
    df_parts_variation = query_to_dataframe(connection, query)

    # --- Visualization ---
    plt.figure(figsize=(12, 8))

    # Scatter plot with seaborn
    sns.scatterplot(x='year', y='part_range', data=df_parts_variation, color='skyblue', s=100, edgecolor='black')

    # Add labels and title (matching the example style)
    plt.title('Variation in Number of Parts Over Time', fontsize=14)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Range of Parts (Max - Min)', fontsize=12)
    
    # Optionally add a smoother line to show the trend
    sns.regplot(x='year', y='part_range', data=df_parts_variation, scatter=False, color='darkblue', lowess=True)

    plt.grid(True)
    plt.tight_layout()
    plt.show()


def visualize_new_themes_per_year(connection, queries):
    """Executes a query to get the number of new themes introduced each year
      and visualizes it with a scatter plot and trend line."""

    query_2 = queries['themes_introduced_each_year'] 
    df_new_themes = query_to_dataframe(connection, query_2)

    # --- Visualization ---
    plt.figure(figsize=(12, 8))

    # Scatter plot with Lego colors
    plt.scatter(df_new_themes['year'], df_new_themes['new_themes'], s=100, alpha=0.7, label='New Themes')

    # Trend line
    sns.regplot(x='year', y='new_themes', data=df_new_themes, scatter=False, lowess=True, label='Trend')

    # Add labels and title
    plt.title('Number of New Themes Introduced Each Year', fontsize=14)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Number of New Themes', fontsize=12)
    plt.legend(title='Legend') 

    # Show the plot
    plt.tight_layout()
    plt.show()

import matplotlib.pyplot as plt
import seaborn as sns



def visualize_most_common_colors(connection, queries):
    """Executes a query to get the most common colors in LEGO sets and visualizes it."""

    query = queries['most_common_color_in_sets']
    df_color_counts = query_to_dataframe(connection, query)

    # --- Visualization ---
    plt.figure(figsize=(12, 8))

    # Create a bar chart using Seaborn with Lego colors
    sns.barplot(x='Color', y='count', data=df_color_counts)

   

    # Set title and labels
    plt.title('Most Common Colors in LEGO Sets', fontsize=14)
    plt.xlabel('Color', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.xticks(rotation=45) 

    # Show the plot
    plt.tight_layout()
    plt.show()