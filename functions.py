from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def execute_query(query):
    """
    Executes a provided SQL query and 
    returns the results.
    """
    mycursor.execute(query)
    return mycursor.fetchall()

def create_bar_chart(data, x_label, y_label, title):
    """
    Creates a bar chart using Seaborn.
    """
    sns.barplot(x=x_label, y=y_label, data=data)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.xticks(rotation=45)  # Rotate x-axis labels for readability
    plt.tight_layout()
    plt.show()

def create_line_chart(data, x_label, y_label, title):
    """
    Creates a line chart using Matplotlib.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data[x_label], data[y_label])
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

