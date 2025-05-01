import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import fastf1

st.title("Chart for Pit Strategy and Position changes")

    # --- original notebook code ---
import plotly.graph_objects as go

# Hamilton Sankey data
ham_labels = [
    "1-Stop (HAM)", "2-Stop (HAM)", "Undercut (HAM)", "Overcut (HAM)", "Overtake (HAM)", "Defend (HAM)",
    "Gain Position", "Lose Position", "Position Swap", "No Change"
]
ham_source = [0, 0, 1, 1, 2, 3, 4, 5]
ham_target = [6, 9, 6, 7, 6, 7, 8, 9]
ham_value = [7, 2, 5, 4, 6, 4, 6, 5]

# Verstappen Sankey data
ver_labels = [
    "1-Stop (VER)", "2-Stop (VER)", "Undercut (VER)", "Overcut (VER)", "Overtake (VER)", "Defend (VER)",
    "Gain Position", "Lose Position", "Position Swap", "No Change"
]
ver_source = [0, 0, 1, 1, 2, 3, 4, 5]
ver_target = [6, 9, 6, 7, 6, 7, 8, 9]
ver_value = [5, 4, 4, 6, 5, 5, 7, 6]

# Color mapping
gain_color = "#6CC24A"
loss_color = "#FF6F61"
swap_color = "#FFD700"
no_change_color = "#7B8B8E"

ham_link_colors = [
    gain_color, no_change_color, gain_color, loss_color,
    gain_color, loss_color, swap_color, no_change_color
]

ver_link_colors = [
    gain_color, no_change_color, gain_color, loss_color,
    gain_color, loss_color, swap_color, no_change_color
]

# Build Hamilton Sankey
ham_sankey = go.Sankey(
    domain=dict(x=[0, 0.48]),
    node=dict(
        pad=20,
        thickness=20,
        line=dict(color="white", width=0.5),
        label=ham_labels,
        color=["#1f77b4"] * 6 + [gain_color, loss_color, swap_color, no_change_color]
    ),
    link=dict(
        source=ham_source,
        target=ham_target,
        value=ham_value,
        color=ham_link_colors,
        hovertemplate='Strategy: %{source.label} → %{target.label}<br>Moves: %{value}<extra></extra>'
    )
)

# Build Verstappen Sankey
ver_sankey = go.Sankey(
    domain=dict(x=[0.52, 1.0]),
    node=dict(
        pad=20,
        thickness=20,
        line=dict(color="white", width=0.5),
        label=ver_labels,
        color=["#d62728"] * 6 + [gain_color, loss_color, swap_color, no_change_color]
    ),
    link=dict(
        source=ver_source,
        target=ver_target,
        value=ver_value,
        color=ver_link_colors,
        hovertemplate='Strategy: %{source.label} → %{target.label}<br>Moves: %{value}<extra></extra>'
    )
)

# Layout
fig = go.Figure(data=[ham_sankey, ver_sankey])

fig.update_layout(
    # title_text="🏎️ Hamilton vs Verstappen — Pit Strategy & Position Changes (Refined Double Sankey)",
    font=dict(color='white', size=14),
    paper_bgcolor="black",
    plot_bgcolor="black",
    margin=dict(t=80, l=10, r=10, b=10),
    height=750
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


