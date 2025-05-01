# 3.1  •  Verstappen Gap to Hamilton – Abu Dhabi 2021

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import pathlib

st.set_page_config(layout="wide")
st.title("Verstappen Gap to Hamilton(Abu Dhabi)")

# ------------------------------------------------------------------
# Load prebuilt data
# ------------------------------------------------------------------
GAP_FILE = pathlib.Path("data/2021_abudhabi_gap.parquet")
df = pd.read_parquet(GAP_FILE)

# ------------------------------------------------------------------
# Plotly figure
# ------------------------------------------------------------------
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df["LapNumber"], y=df["Gap_to_HAM"],
    mode="lines+markers",
    name="Verstappen gap to Hamilton",
    line=dict(color="lightseagreen", width=3),
    hovertemplate="Lap %{x}<br>Gap %{y:.2f} s<extra></extra>"
))

# Annotate key events
key_events = [
    (1,  "Turn-6 incident",                     "white",       25.5),
    (14, "VER pit – Hard",                      "lightgray",   26),
    (20, "Perez defense",                       "dodgerblue",  24),
    (36, "VSC pit – fresher tyres",             "white",       21),
    (53, "Latifi crash",                        "red",         20),
    (54, "Safety Car",                          "yellow",      18.5),
    (54, "VER pit – Soft",                      "white",       17),
    (58, "Final-lap overtake",                  "limegreen",   15.5),
]

for lap, label, color, y in key_events:
    fig.add_vline(x=lap, line_dash="dot", line_color=color, line_width=2)
    fig.add_annotation(x=lap, y=y, text=label, showarrow=False,
                       font=dict(color=color, size=11), xanchor="left")

fig.update_layout(
    # title="🏁 Abu Dhabi 2021 – Verstappen Cumulative Gap to Hamilton",
    xaxis_title="Lap",  yaxis_title="Gap to HAM (s)",
    xaxis=dict(range=[1, 58], dtick=2),
    yaxis=dict(range=[-1, 27], autorange=False),
    template="plotly_dark",
    plot_bgcolor="black", paper_bgcolor="black",
    font=dict(color="white"), showlegend=False, height=560
)

# ------------------------------------------------------------------
# Display
# ------------------------------------------------------------------
st.plotly_chart(fig, use_container_width=True)


