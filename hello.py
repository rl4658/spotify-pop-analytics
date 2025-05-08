import numpy as np
# Import necessary libraries
from preswald import Workflow, text, table, plotly, sidebar, WorkflowAnalyzer, connect, get_df
import pandas as pd
import plotly.express as px

# Create a workflow instance
workflow = Workflow()

# Define an atom for loading data
@workflow.atom()
def load_data():
    connect()  # Initialize data sources
    df = get_df('sample_csv')  # Retrieve data as DataFrame
    return df

# Define an atom for data analysis
@workflow.atom(dependencies=["load_data"])
def analyze_data(load_data):
    df = load_data
    text("## Data Analysis Results:")  # Section title

    # Display the structure of the DataFrame
    text("### Column Types")
    text("Column types:\n" + str(df.dtypes.to_string()))  # Display data types
    
    # Key metrics and statistics
    metrics = {
        "Total Rows": len(df),
        "Unique Artists": df['artist_name'].nunique(),
        "Average Followers": df['followers'].mean(),
        "Max Track Popularity": df['track_popularity'].max(),
        "Min Track Popularity": df['track_popularity'].min(),
    }
    
    for key, value in metrics.items():
        text(f"{key}: {value}")  # Display key metrics

    # Check for missing values
    missing_values = df.isnull().sum()
    text("### Missing Values:")
    text(missing_values[missing_values > 0].to_string())  # Display missing values

    # Display the first 10 records
    table(df.head(10))  # Display sample data

# Define an atom for visualizing data
@workflow.atom(dependencies=["load_data"])
def visualize_data(load_data):
    df = load_data
    text("## Recommended Visualizations")  # Section title
    
    # 1. Distribution of Track Popularity
    fig1 = px.histogram(df, x='track_popularity', title='Distribution of Track Popularity')  # Histogram
    plotly(fig1)  # Display the plot

    # 2. Followers vs. Track Popularity
    fig2 = px.scatter(df, x='followers', y='track_popularity', color='artist_name', title='Followers vs. Track Popularity')  # Scatter plot
    plotly(fig2)  # Display the plot

    # 3. Average Track Popularity by Genre
    avg_popularity_by_genre = df.groupby('genres')['track_popularity'].mean().reset_index()
    fig3 = px.bar(avg_popularity_by_genre, x='genres', y='track_popularity', title='Average Track Popularity by Genre')  # Bar chart
    plotly(fig3)  # Display the plot

    # 4. Track Duration Distribution
    fig4 = px.histogram(df, x='duration_ms', title='Distribution of Track Duration')  # Histogram
    plotly(fig4)  # Display the plot

# Define an atom for analyzing workflow
@workflow.atom()
def analyze_workflow():
    # Initialize analyzer
    analyzer = WorkflowAnalyzer(workflow)
    
    # Get critical path
    critical_path = analyzer.get_critical_path()
    text(f"Critical Path: {' → '.join(critical_path)}")

# Execute the workflow
workflow.execute()


# Generated plot
import numpy as np
# Import necessary libraries
from preswald import Workflow, text, table, plotly, sidebar, WorkflowAnalyzer, connect, get_df
import pandas as pd
import plotly.express as px

# Create a workflow instance
workflow = Workflow()

# Define an atom for loading data
@workflow.atom()
def load_data():
    connect()  # Initialize data sources
    df = get_df('sample_csv')  # Retrieve data as DataFrame
    return df

# Define an atom for data analysis
@workflow.atom(dependencies=["load_data"])
def analyze_data(load_data):
    df = load_data
    text("## Data Analysis Results:")  # Section title

    # Display the structure of the DataFrame
    text("### Column Types")
    text("Column types:\n" + str(df.dtypes.to_string()))  # Display data types
    
    # Key metrics and statistics
    metrics = {
        "Total Rows": len(df),
        "Unique Artists": df['artist_name'].nunique(),
        "Average Followers": df['followers'].mean(),
        "Max Track Popularity": df['track_popularity'].max(),
        "Min Track Popularity": df['track_popularity'].min(),
    }
    
    for key, value in metrics.items():
        text(f"{key}: {value}")  # Display key metrics

    # Check for missing values
    missing_values = df.isnull().sum()
    text("### Missing Values:")
    text(missing_values[missing_values > 0].to_string())  # Display missing values

    # Display the first 10 records
    table(df.head(10))  # Display sample data

# Define an atom for visualizing data
@workflow.atom(dependencies=["load_data"])
def visualize_data(load_data):
    df = load_data
    text("## Recommended Visualizations")  # Section title
    
    # 1. Distribution of Track Popularity
    fig1 = px.histogram(df, x='track_popularity', title='Distribution of Track Popularity')  # Histogram
    plotly(fig1)  # Display the plot

    # 2. Followers vs. Track Popularity
    fig2 = px.scatter(df, x='followers', y='track_popularity', color='artist_name', title='Followers vs. Track Popularity')  # Scatter plot
    plotly(fig2)  # Display the plot

    # 3. Average Track Popularity by Genre
    avg_popularity_by_genre = df.groupby('genres')['track_popularity'].mean().reset_index()
    fig3 = px.bar(avg_popularity_by_genre, x='genres', y='track_popularity', title='Average Track Popularity by Genre')  # Bar chart
    plotly(fig3)  # Display the plot

    # 4. Track Duration Distribution
    fig4 = px.histogram(df, x='duration_ms', title='Distribution of Track Duration')  # Histogram
    plotly(fig4)  # Display the plot

# Define an atom for analyzing workflow
@workflow.atom()
def analyze_workflow():
    # Initialize analyzer
    analyzer = WorkflowAnalyzer(workflow)
    
    # Get critical path
    critical_path = analyzer.get_critical_path()
    text(f"Critical Path: {' → '.join(critical_path)}")

# Execute the workflow
workflow.execute()


