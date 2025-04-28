import streamlit as st
import pandas as pd
import plotly.express as px
from src.pipeline import fetch_data, clean_data, feature_engineering
from src import model

# Load and preprocess data
df = fetch_data.load_local_data('data/raw/baseball_stats.csv')
df = clean_data.clean_baseball_data(df)
df = feature_engineering.add_features(df)

# Sidebar for user input
st.sidebar.header('Filter Options')
selected_team = st.sidebar.selectbox('Select Team', options=df['team'].unique())
selected_player = st.sidebar.selectbox('Select Player', options=df[df['team'] == selected_team]['player'].unique())

# Filter data based on user selection
filtered_df = df[(df['team'] == selected_team) & (df['player'] == selected_player)]

# Display player statistics
st.header(f'Statistics for {selected_player}')
st.write(filtered_df)

# Visualizations
st.subheader('Home Runs Distribution')
fig = px.histogram(df, x='hr', nbins=20, title='Distribution of Home Runs')
st.plotly_chart(fig)

# Model Prediction
st.subheader('Predict Home Runs')
if st.button('Predict'):
    prediction = model.predict_home_runs(filtered_df)
    st.write(f'Predicted Home Runs: {prediction}')

