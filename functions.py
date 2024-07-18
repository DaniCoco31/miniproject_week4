import seaborn as sns
import matplotlib.pyplot as plt
import mysql.connector
import pandas as pd

##### CONNECTION
# Database connection function
def connect_to_database(host, user, password, database):
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

# Query execution function
def execute_query(connection, query):
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results


##### CREATE THE DF WITH THE QUERIES
# Function to create dataframes from query results
def query_to_dataframe(connection, query):
    results = execute_query(connection, query)
    return pd.DataFrame(results)



##### VISUALIZATION
# Visualization functions
def visualize_num_sets_per_theme(df):
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Number of sets', y='Theme', data=df)
    plt.title('Number of Sets per Theme')
    plt.show()

def visualize_top_sets_with_most_parts(df):
    plt.figure(figsize=(12, 8))
    sns.barplot(x='num_parts', y='name', data=df)
    plt.title('Top 10 Sets with the Most Parts')
    plt.show()

def visualize_top_sets_with_least_parts(df):
    plt.figure(figsize=(12, 8))
    sns.barplot(x='num_parts', y='name', data=df)
    plt.title('Top 10 Sets with the Least Parts')
    plt.show()

def visualize_themes_with_most_parts(df):
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Total amount of parts for the theme', y='Theme', data=df)
    plt.title('Themes with the Most Parts')
    plt.show()

def visualize_quantity_of_pieces_in_oldest_sets(df):
    plt.figure(figsize=(12, 8))
    sns.barplot(x='num_parts', y='name', data=df)
    plt.title('Quantity of Pieces in the Oldest Sets')
    plt.show()

def visualize_changes_in_quantity_of_pieces(df):
    plt.figure(figsize=(12, 8))
    sns.lineplot(x='year', y='avg_num_parts', data=df)
    plt.title('Changes in the Quantity of Pieces in LEGO Sets from 1950 to 2017')
    plt.show()

