# 3.4  •  Lap-by-Lap Position Tracker – Abu Dhabi 2021

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import pathlib

st.set_page_config(layout="wide")
st.title("Lap-by-Lap Position Tracker of Abu Dhabi GP")

# ------------------------------------------------------------------
# Load prebuilt position data
# ------------------------------------------------------------------
DATA_FILE = pathlib.Path("data/2021_abudhabi_positions.parquet")
pos_df = pd.read_parquet(DATA_FILE)

# ------------------------------------------------------------------
# Plotly step plot
# ------------------------------------------------------------------
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=pos_df.LapNumber, y=pos_df.HAM,
    mode="lines", name="Hamilton",
    line=dict(shape="hv", color="#00D2BE", width=4),
    hovertemplate="Lap %{x}<br>Pos %{y}<extra></extra>"
))

fig.add_trace(go.Scatter(
    x=pos_df.LapNumber, y=pos_df.VER,
    mode="lines", name="Verstappen",
    line=dict(shape="hv", color="#1E41FF", width=4),
    hovertemplate="Lap %{x}<br>Pos %{y}<extra></extra>"
))

# Safety-car shading (Laps 53–57)
fig.add_vrect(
    x0=53, x1=56.8,
    line_width=2, line_dash="dash", line_color="yellow",
    fillcolor="rgba(0,0,0,0)",
    annotation_text="Safety Car", annotation_position="top left",
    annotation_font_color="yellow", annotation_font_size=12
)

# Pit-stop markers
for lap in (14, 15, 36, 54):
    fig.add_vline(
        x=lap, line_dash="dash", line_color="lightgrey", line_width=1,
        annotation_text="Pit stop" if lap == 14 else "", annotation_position="top left",
        annotation_font_color="lightgrey", annotation_font_size=11
    )

# Layout
fig.update_yaxes(title="Track Position", autorange="reversed", dtick=1, range=[0.5, 5.5])
fig.update_xaxes(title="Lap", dtick=5)
fig.update_layout(
    # title="Abu Dhabi 2021 – Lap-by-Lap Position Tracker (HAM vs VER)",
    template="plotly_dark", height=500,
    plot_bgcolor="black", paper_bgcolor="black",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5)
)

# ------------------------------------------------------------------
# Display in Streamlit
# ------------------------------------------------------------------
st.plotly_chart(fig, use_container_width=True)


