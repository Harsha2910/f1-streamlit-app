# 2.2  •  Points progression for each race (Hamilton vs Verstappen)

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(layout="wide")
st.title("Points Earned in Each 2021 Race")

# ------------------------------------------------------------------
# ✅ Load pre-saved data from parquet (no FastF1 required)
# ------------------------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_parquet("data/2021_points_progression.parquet")

df = load_data()

# ------------------------------------------------------------------
# Plotly animated figure
# ------------------------------------------------------------------
fig = go.Figure(
    layout=go.Layout(
        # title="🏎️ 2021 F1: FIA Points per Round",
        xaxis=dict(title="Round", tick0=1, dtick=1, range=[1, 22]),
        yaxis=dict(title="Points", tickvals=[0, 1, 2, 4, 6, 8, 10, 12, 15, 18, 25], range=[0, 30]),
        template="plotly_dark",
        plot_bgcolor="black",
        paper_bgcolor="black",
        font=dict(color="white"),
        updatemenus=[dict(
            type="buttons", direction="left", x=0.1, y=0,
            showactive=False, pad=dict(r=10, t=85),
            buttons=[
                dict(label="Play",  method="animate",
                     args=[None, dict(frame=dict(duration=600, redraw=True), fromcurrent=True)]),
                dict(label="Pause", method="animate",
                     args=[[None], dict(frame=dict(duration=0, redraw=False), mode="immediate")]),
                dict(label="Reset", method="animate",
                     args=[[None], dict(frame=dict(duration=0, redraw=True), fromcurrent=False, mode="immediate")]),
            ]
        )]
    )
)

# Empty traces (for legend and layout)
fig.add_trace(go.Scatter(x=[], y=[], mode="lines+markers",
                         name="Lewis Hamilton", line=dict(color="#00D2BE", width=4)))
fig.add_trace(go.Scatter(x=[], y=[], mode="lines+markers",
                         name="Max Verstappen", line=dict(color="#1E41FF", width=4)))

# Create animation frames
frames = []
for i in range(1, 23):
    frames.append(go.Frame(
        name=str(i),
        data=[
            go.Scatter(x=df.Round[:i], y=df.Hamilton[:i]),
            go.Scatter(x=df.Round[:i], y=df.Verstappen[:i])
        ]
    ))
fig.frames = frames

# ------------------------------------------------------------------
# Show in Streamlit
# ------------------------------------------------------------------
st.plotly_chart(fig, use_container_width=True)


