
'''import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import fastf1

st.title("2.1 Total Season points progression")

    # --- original notebook code ---
import pandas as pd
import plotly.graph_objects as go

# Data
races = [
    "Bahrain", "Imola", "Portugal", "Spain", "Monaco", "Azerbaijan", "France",
    "Styria", "Austria", "Silverstone", "Hungary", "Belgium", "Netherlands",
    "Monza", "Russia", "Turkey", "USA", "Mexico", "Brazil", "Qatar", "Jeddah", "Abu Dhabi"
]
race_numbers = list(range(1, 23))
hamilton_points = [25, 44, 69, 94, 101, 101, 119, 138, 150, 177, 195, 202.5, 221.5, 221.5, 246.5, 256.5, 275.5, 293.5, 318.5, 343.5, 369.5, 387.5]
verstappen_points = [18, 43, 61, 80, 105, 105, 131, 156, 182, 182, 184, 196.5, 221.5, 221.5, 239.5, 257.5, 282.5, 307.5, 325.5, 344.5, 369.5, 395.5]

# DataFrame
df = pd.DataFrame({
    'RaceNumber': race_numbers,
    'RaceName': races,
    'Hamilton': hamilton_points,
    'Verstappen': verstappen_points
})

# Initialize base figure
fig = go.Figure()

# Add initial empty traces
fig.add_trace(go.Scatter(
    x=[], y=[], mode='lines+markers',
    name='Lewis Hamilton', line=dict(color='royalblue'),
    marker=dict(size=8),
    hovertemplate='<b>Race:</b> %{customdata[0]}<br><b>Hamilton:</b> %{y} pts',
    customdata=[]
))

fig.add_trace(go.Scatter(
    x=[], y=[], mode='lines+markers',
    name='Max Verstappen', line=dict(color='orangered'),
    marker=dict(size=8),
    hovertemplate='<b>Race:</b> %{customdata[0]}<br><b>Verstappen:</b> %{y} pts',
    customdata=[]
))

# Create animation frames
frames = []
for i in range(1, len(df) + 1):
    frames.append(go.Frame(
        name=str(i),
        data=[
            go.Scatter(
                x=df['RaceNumber'][:i],
                y=df['Hamilton'][:i],
                mode='lines+markers',
                line=dict(color='royalblue'),
                marker=dict(size=8),
                customdata=df[['RaceName']][:i]
            ),
            go.Scatter(
                x=df['RaceNumber'][:i],
                y=df['Verstappen'][:i],
                mode='lines+markers',
                line=dict(color='orangered'),
                marker=dict(size=8),
                customdata=df[['RaceName']][:i]
            )
        ]
    ))

fig.frames = frames

# Layout (NO SLIDER)
fig.update_layout(
    title="F1 2021: Animated Points Progression",
    xaxis=dict(title="Race Number", tickmode='linear', dtick=1),
    yaxis=dict(title="Cumulative Points", range=[0, 420]),
    template='plotly_white',
    hovermode='closest',
    updatemenus=[dict(
        type="buttons",
        showactive=False,
        buttons=[
            dict(label="Play", method="animate",
                 args=[None, {"frame": {"duration": 500, "redraw": True},
                              "fromcurrent": True, "transition": {"duration": 300}}]),
            dict(label="Pause", method="animate",
                 args=[[None], {"frame": {"duration": 0}, "mode": "immediate"}])
        ],
        x=0.1, y=1.15
    )]
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
'''

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("Total Season Points")

# --- Data ---
races = [
    "Bahrain", "Imola", "Portugal", "Spain", "Monaco", "Azerbaijan", "France",
    "Styria", "Austria", "Silverstone", "Hungary", "Belgium", "Netherlands",
    "Monza", "Russia", "Turkey", "USA", "Mexico", "Brazil", "Qatar", "Jeddah", "Abu Dhabi"
]
race_numbers = list(range(1, 23))
hamilton_points = [25, 44, 69, 94, 101, 101, 119, 138, 150, 177, 195, 202.5, 221.5, 221.5, 246.5, 256.5, 275.5, 293.5, 318.5, 343.5, 369.5, 387.5]
verstappen_points = [18, 43, 61, 80, 105, 105, 131, 156, 182, 182, 184, 196.5, 221.5, 221.5, 239.5, 257.5, 282.5, 307.5, 325.5, 344.5, 369.5, 395.5]

df = pd.DataFrame({
    'RaceNumber': race_numbers,
    'RaceName': races,
    'Hamilton': hamilton_points,
    'Verstappen': verstappen_points
})

# --- Animated Chart ---
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[], y=[], mode='lines+markers',
    name='Lewis Hamilton', line=dict(color='royalblue'),
    marker=dict(size=8),
    hovertemplate='<b>Race:</b> %{customdata[0]}<br><b>Hamilton:</b> %{y} pts',
    customdata=[]
))
fig.add_trace(go.Scatter(
    x=[], y=[], mode='lines+markers',
    name='Max Verstappen', line=dict(color='orangered'),
    marker=dict(size=8),
    hovertemplate='<b>Race:</b> %{customdata[0]}<br><b>Verstappen:</b> %{y} pts',
    customdata=[]
))

# --- Animation Frames ---
frames = []
for i in range(1, len(df) + 1):
    frames.append(go.Frame(
        name=str(i),
        data=[
            go.Scatter(
                x=df['RaceNumber'][:i],
                y=df['Hamilton'][:i],
                mode='lines+markers',
                line=dict(color='royalblue'),
                marker=dict(size=8),
                customdata=df[['RaceName']][:i]
            ),
            go.Scatter(
                x=df['RaceNumber'][:i],
                y=df['Verstappen'][:i],
                mode='lines+markers',
                line=dict(color='orangered'),
                marker=dict(size=8),
                customdata=df[['RaceName']][:i]
            )
        ]
    ))

fig.frames = frames

# --- Layout ---
fig.update_layout(
    # title="F1 2021: Animated Points Progression",
    xaxis=dict(
        title="Race Number",
        tickmode='linear',
        dtick=1,
        range=[0.5, 23.5],
        fixedrange=True
    ),
    yaxis=dict(
        title="Cumulative Points",
        range=[0, 420],
        fixedrange=True
    ),
    template='plotly_white',
    hovermode='closest',
    updatemenus=[dict(
        type="buttons",
        showactive=False,
        buttons=[
            dict(label="Play", method="animate",
                 args=[None, {"frame": {"duration": 500, "redraw": True},
                              "fromcurrent": True, "transition": {"duration": 300}}]),
            dict(label="Pause", method="animate",
                 args=[[None], {"frame": {"duration": 0}, "mode": "immediate"}])
        ],
        x=0.1, y=1.15
    )]
)

# --- Show in Streamlit ---
st.plotly_chart(fig, use_container_width=True)

