
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import fastf1

st.title("Scenario A: If Latifi Didnot Crash")

    # --- original notebook code ---
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# Gap data before crash
laps_before = np.arange(48, 53)
gap_to_ham = [11.5, 11.3, 11.2, 11.4, 11.6]

# Estimate average delta
avg_delta = np.mean(np.diff(gap_to_ham))

# Projected laps and gaps (no safety car)
projected_laps = np.arange(53, 59)
last_gap = gap_to_ham[-1]
projected_gaps = [last_gap + avg_delta * (i - 52) for i in projected_laps]

# Simulated SC actual gaps for context (optional visual contrast)
actual_sc_gap = [11.6, 8.4, 8.6, 2.5, 0.2, -0.1]

# Create plot
fig = go.Figure()

# Actual before crash
fig.add_trace(go.Scatter(
    x=laps_before,
    y=gap_to_ham,
    mode='lines+markers',
    name='Actual Gap (Before Lap 53)',
    line=dict(color='crimson', width=3)
))

# Actual SC impact (optional background)
fig.add_trace(go.Scatter(
    x=projected_laps,
    y=actual_sc_gap,
    mode='lines+markers',
    name='Actual With Safety Car',
    line=dict(color='lightgrey', dash='dot', width=2)
))

# Projected no crash scenario
fig.add_trace(go.Scatter(
    x=projected_laps,
    y=projected_gaps,
    mode='lines+markers',
    name='Projected Gap (No Crash)',
    line=dict(color='orange', dash='dash', width=4)
))

# Safety Car lap marker
fig.add_vline(x=53, line_dash="dash", line_color="lightgrey")

# Layout settings
fig.update_layout(
    # title="⚡ Scenario A: Projected Gap if No Latifi Crash (Laps 48–58)",
    xaxis_title="Lap",
    yaxis_title="Gap to Hamilton (seconds)",
    template="plotly_dark",
    plot_bgcolor="black",
    paper_bgcolor="black",
    font=dict(color="white"),
    xaxis=dict(dtick=1, range=[48, 58]),
    legend=dict(
        y=0.5,
        x=1.02,
        xanchor='left',
        bgcolor="rgba(0,0,0,0)",
        bordercolor="rgba(255,255,255,0.1)"
    )
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


