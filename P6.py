# LAB_6 STREAMLIT

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

# Set page configuration
st.set_page_config(layout="wide", page_title="Retail Analytics Dashboard", page_icon=":bar_chart:", initial_sidebar_state="collapsed")

# Load sample dataset
df = pd.read_csv("shopping_behavior_updated.csv")

# Display the DataFrame
st.dataframe(df)

# Display the info of DataFrame
st.text(df.info())

# Display the description of DataFrame
st.write(df.describe())

# Sidebar for user input
st.sidebar.header('Visualization Selection')
visualization_type = st.sidebar.selectbox('Select Visualization Type', ['Dashboard', 'Bar Chart', 'Line Chart', 'Scatter Plot'])

# Function to create 3D graph for Dashboard
def create_dashboard():
    fig_dashboard = plt.figure(figsize=(8, 6))
    ax_dashboard = fig_dashboard.add_subplot(111, projection='3d')
    
    # Calculate key metrics
    total_sales = df['Purchase Amount (USD)'].sum()
    avg_purchase_amount = df['Purchase Amount (USD)'].mean()
    
    # Plotting customer demographics
    ax_dashboard.scatter(df['Age'], df['Purchase Amount (USD)'], df['Review Rating'], c='orange', label='Customer Demographics')
    
    ax_dashboard.set_xlabel('Age')
    ax_dashboard.set_ylabel('Purchase Amount (USD)')
    ax_dashboard.set_zlabel('Review Rating')
    ax_dashboard.set_title('Customer Demographics and Purchase Behavior')
    
    st.pyplot(fig_dashboard)
    st.write(f"Total Sales: {total_sales}")
    st.write(f"Average Purchase Amount: {avg_purchase_amount}")

# Function to create 2D/3D bar chart for product categories
def create_bar_chart():
    fig_bar = plt.figure(figsize=(8, 6))
    ax_bar = fig_bar.add_subplot()
    
    # Plotting distribution of purchases by product category
    purchase_by_category = df['Category'].value_counts()
    ax_bar.bar(purchase_by_category.index, purchase_by_category.values, color='orange')
    
    ax_bar.set_xlabel('Product Category')
    ax_bar.set_ylabel('Number of Purchases')
    ax_bar.set_title('Distribution of Purchases by Product Category')
    plt.xticks(rotation=45)
    
    st.pyplot(fig_bar)

# Function to create 2D/3D line chart for sales trend over time
def create_line_chart():
    fig_line = plt.figure(figsize=(8, 6))
    ax_line = fig_line.add_subplot()
    
    # Aggregating total sales by index (assuming it represents time)
    sales_trend = df['Purchase Amount (USD)'].cumsum()  # Cumulative sum for illustration
    
    ax_line.plot(sales_trend.index, sales_trend.values, color='orange')
    ax_line.set_xlabel('Index (Time)')
    ax_line.set_ylabel('Total Sales (USD)')
    ax_line.set_title('Sales Trend Over Time')
    
    st.pyplot(fig_line)

# Function to create 2D/3D scatter plot for customer age vs average purchase amount
def create_scatter_plot():
    fig_scatter = plt.figure(figsize=(8, 6))
    ax_scatter = fig_scatter.add_subplot()
    
    # Plotting relationship between customer age and average purchase amount
    avg_purchase_by_age = df.groupby('Age')['Purchase Amount (USD)'].mean()
    ax_scatter.scatter(avg_purchase_by_age.index, avg_purchase_by_age.values, color='orange')
    
    ax_scatter.set_xlabel('Age')
    ax_scatter.set_ylabel('Average Purchase Amount (USD)')
    ax_scatter.set_title('Relationship between Age and Average Purchase Amount')
    
    st.pyplot(fig_scatter)

# Main function to run the app
def main():
    if visualization_type == 'Dashboard':
        create_dashboard()
    elif visualization_type == 'Bar Chart':
        create_bar_chart()
    elif visualization_type == 'Line Chart':
        create_line_chart()
    elif visualization_type == 'Scatter Plot':
        create_scatter_plot()

if __name__ == "__main__":
    main()
