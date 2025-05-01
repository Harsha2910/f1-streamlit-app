
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import fastf1

st.title("Wins vs Podiums for Top 5 Drivers")

    # --- original notebook code ---
import plotly.graph_objects as go
import pandas as pd

# Top 5 drivers manually based on 2021 standings
driver_data = {
    'Driver': ['Max Verstappen', 'Lewis Hamilton', 'Valtteri Bottas', 'Sergio Pérez', 'Carlos Sainz'],
    'Wins': [10, 8, 1, 1, 0],  # Actual 2021 wins
    'Podiums': [18, 17, 11, 5, 4]  # Podiums including wins
}

# Build dataframe
drivers_df = pd.DataFrame(driver_data)

# Plot
fig = go.Figure()

# Add bar for Podiums
fig.add_trace(go.Bar(
    x=drivers_df['Driver'],
    y=drivers_df['Podiums'],
    name='Podiums',
    marker_color='white'
))

# Add dot for Wins
fig.add_trace(go.Scatter(
    x=drivers_df['Driver'],
    y=drivers_df['Wins'],
    mode='markers+text',
    name='Wins',
    marker=dict(color='gold', size=14, symbol='circle'),
    text=drivers_df['Wins'],
    textposition='top center'
))

# Layout
fig.update_layout(
    # title="🏆 2021 F1 Top 5 Drivers - Wins vs Podiums",
    xaxis_title="Driver",
    yaxis_title="Count",
    yaxis=dict(range=[0, 20]),  # <<< SET Y-AXIS range manually from 0 to 20
    template='plotly_dark',
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    barmode='overlay'
)

    # --- display logic ---
if 'fig' in locals():
    try:
            st.plotly_chart(fig, use_container_width=True)
    except Exception:
        pass
else:
    # fallback for matplotlib
    st.pyplot(plt.gcf())


