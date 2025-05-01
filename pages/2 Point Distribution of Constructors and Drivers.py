
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import fastf1
st.title("Point Distribution of Constructors and Drivers")

    # --- original notebook code ---
import plotly.express as px
import pandas as pd

# F1 2021 Driver and Team Summary
data = {
    'Constructor': [
        'Mercedes', 'Mercedes',
        'Red Bull Racing', 'Red Bull Racing',
        'Ferrari', 'Ferrari',
        'McLaren', 'McLaren',
        'Alpine', 'Alpine',
        'AlphaTauri', 'AlphaTauri',
        'Aston Martin', 'Aston Martin',
        'Williams', 'Williams',
        'Alfa Romeo', 'Alfa Romeo',
        'Haas', 'Haas'
    ],
    'Driver': [
        'Lewis Hamilton', 'Valtteri Bottas',
        'Max Verstappen', 'Sergio Pérez',
        'Carlos Sainz', 'Charles Leclerc',
        'Lando Norris', 'Daniel Ricciardo',
        'Esteban Ocon', 'Fernando Alonso',
        'Pierre Gasly', 'Yuki Tsunoda',
        'Sebastian Vettel', 'Lance Stroll',
        'George Russell', 'Nicholas Latifi',
        'Kimi Räikkönen', 'Antonio Giovinazzi',
        'Mick Schumacher', 'Nikita Mazepin'
    ],
    'Points': [
        387.5, 226,  # Mercedes
        395.5, 190,  # Red Bull
        164.5, 159,  # Ferrari
        160, 115,    # McLaren
        74, 81,      # Alpine
        110, 32,     # AlphaTauri
        43, 34,      # Aston Martin
        16, 7,       # Williams
        10, 3,       # Alfa Romeo
        0, 0         # Haas
    ],
    'Summary': [
        '2nd • 387.5 pts • 8 wins • 17 podiums', '3rd • 226 pts • 1 win • 11 podiums',
        '🏆 Champion • 395.5 pts • 10 wins • 18 podiums', '4th • 190 pts • 1 win • 5 podiums',
        '5th • 164.5 pts • 0 wins • 4 podiums', '7th • 159 pts • 0 wins • 1 podium',
        '6th • 160 pts • 0 wins • 4 podiums', '8th • 115 pts • 1 win • 1 podium',
        '9th • 74 pts • 1 win • 1 podium', '10th • 81 pts • 0 wins • 0 podiums',
        '11th • 110 pts • 0 wins • 1 podium', '14th • 32 pts • 0 wins • 0 podiums',
        '12th • 43 pts • 0 wins • 1 podium', '13th • 34 pts • 0 wins • 0 podiums',
        '15th • 16 pts • 0 wins • 1 podium', '17th • 7 pts • 0 wins • 0 podiums',
        '16th • 10 pts • 0 wins • 0 podiums', '18th • 3 pts • 0 wins • 0 podiums',
        '19th • 0 pts • 0 wins • 0 podiums', '20th • 0 pts • 0 wins • 0 podiums',
    ]
}

df = pd.DataFrame(data)

# Compute constructor totals for hover only
constructor_totals = df.groupby('Constructor')['Points'].sum().to_dict()
df['ConstructorSummary'] = df['Constructor'].map(lambda x: f'Total: {constructor_totals[x]} pts')

# Team colors
team_colors = {
    'Mercedes': '#00D2BE',
    'Red Bull Racing': '#1E41FF',
    'Ferrari': '#DC0000',
    'McLaren': '#FF8700',
    'Alpine': '#0090FF',
    'AlphaTauri': '#4E7C9B',
    'Aston Martin': '#006F62',
    'Williams': '#005AFF',
    'Alfa Romeo': '#900000',
    'Haas': '#FFFFFF'
}

# Sunburst chart
fig = px.sunburst(
    df,
    path=['Constructor', 'Driver'],
    values='Points',
    color='Constructor',
    color_discrete_map=team_colors,
    template='plotly_dark',
    hover_data=['Summary', 'ConstructorSummary']
)

# Custom hover: show summary for drivers, and constructor points when hovered
fig.update_traces(hovertemplate="""
<b>%{label}</b><br>
%{customdata[0]}%{customdata[1]}<extra></extra>
""")

# Layout polish
fig.update_layout(
    # title='F1 2021 Sunburst Chart: Constructor → Driver Season Summary',
    margin=dict(t=60, l=10, r=10, b=10),
    paper_bgcolor='black',
    font=dict(color='white')
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
