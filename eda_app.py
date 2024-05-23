import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def perform_eda():
    st.header("Exploratory Data Analysis")
    
    # Load your data
    df = pd.read_csv('Train.csv')
    
    st.write("Dataset Overview")
    st.write(df.head())
    
    st.write("Statistical Summary")
    st.write(df.describe())
    
    # Categorical Columns
    categorical_cols = ['Gender', 'Ever_Married', 'Graduated', 'Profession', 'Spending_Score', 'Var_1', 'Segmentation']

    # Custom color palette
    colors = sns.color_palette("icefire")

    # Plot pie chart and bar chart for each categorical column
    for col in categorical_cols:
        st.subheader(f'{col} Distribution')
        fig, axes = plt.subplots(1, 2, figsize=(15, 6))

        # Pie chart
        value_counts = df[col].value_counts()
        axes[0].pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=90, colors=colors[:len(value_counts)])
        axes[0].axis('equal')
        axes[0].set_title(f'{col} Pie Chart')

        # Bar chart
        sns.barplot(x=value_counts.index, y=value_counts.values, palette=colors[:len(value_counts)], ax=axes[1])
        axes[1].set_xlabel(f'{col}')
        axes[1].set_ylabel('Count')
        axes[1].set_xticklabels(value_counts.index, rotation=45)
        axes[1].set_title(f'{col} Bar Chart')

        st.pyplot(fig)
    
    # Define numerical columns
    numerical_cols = ['Age', 'Work_Experience', 'Family_Size']

    # Plotting box plots and histograms for each numerical column
    for col in numerical_cols:
        st.subheader(f'{col} Distribution and Box Plot')
        fig, axes = plt.subplots(1, 2, figsize=(15, 6))

        # Box plot for numerical column
        sns.boxplot(y=df[col], color=colors[0], ax=axes[0])
        axes[0].set_title(f'{col} Box Plot')

        # Histogram for numerical column
        sns.histplot(df[col], bins=15, kde=True, color=colors[1], ax=axes[1])
        axes[1].set_title(f'{col} Distribution')
        axes[1].set_xlabel(col)
        axes[1].set_ylabel('Density')

        st.pyplot(fig)

    # Box plots for numerical columns by segmentation
    st.subheader('Numerical Columns by Segmentation')
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    sns.boxplot(x='Segmentation', y='Age', data=df, ax=axes[0])
    axes[0].set_title('Age')

    sns.boxplot(x='Segmentation', y='Family_Size', data=df, ax=axes[1])
    axes[1].set_title('Family Size')

    sns.boxplot(x='Segmentation', y='Work_Experience', data=df, ax=axes[2])
    axes[2].set_title('Work Experience')

    st.pyplot(fig)
