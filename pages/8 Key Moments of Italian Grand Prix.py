import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ✅ Must be called first before any other Streamlit command
st.set_page_config(layout="wide")

st.title("Key Moments of Italian Grand Prix")
# st.caption("Synthetic lap-by-lap positions to illustrate the Lap-26 crash and pit-stop timing.")

# ------------------------------------------------------------------
# Sample lap data (for illustrative purpose)
# ------------------------------------------------------------------
lap_nums        = list(range(1, 27))
ham_positions   = [4]*10 + [3]*5 + [2]*8 + [1]*3
ver_positions   = [2]*26
ham_speeds      = [320 + (i % 5) for i in lap_nums]
ver_speeds      = [318 + (i % 4) for i in lap_nums]

ham_df = pd.DataFrame({"Lap": lap_nums, "Pos": ham_positions, "Speed": ham_speeds})
ver_df = pd.DataFrame({"Lap": lap_nums, "Pos": ver_positions, "Speed": ver_speeds})

# Fill any missing laps
ham_df = ham_df.set_index("Lap").reindex(range(1, 27)).ffill().reset_index()
ver_df = ver_df.set_index("Lap").reindex(range(1, 27)).ffill().reset_index()

# Merge & adjust overlap
merged = pd.merge(ham_df, ver_df, on="Lap", suffixes=("_HAM", "_VER"))
merged["Adj_Pos_HAM"] = merged["Pos_HAM"]
merged.loc[merged["Pos_HAM"] == merged["Pos_VER"], "Adj_Pos_HAM"] += 0.03

# ------------------------------------------------------------------
# Plotly figure
# ------------------------------------------------------------------
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=merged["Lap"], y=merged["Adj_Pos_HAM"],
    mode="lines+markers", name="Lewis Hamilton",
    line=dict(color="royalblue"),
    marker=dict(size=8, line=dict(width=1, color="black")),
    customdata=merged[["Lap", "Pos_HAM", "Speed_HAM"]],
    hovertemplate="<b>Hamilton</b><br>Lap %{customdata[0]}<br>"
                  "Position %{customdata[1]}<br>"
                  "Speed %{customdata[2]} km/h"
))

fig.add_trace(go.Scatter(
    x=merged["Lap"], y=merged["Pos_VER"],
    mode="lines+markers", name="Max Verstappen",
    line=dict(color="orangered"),
    marker=dict(size=8, line=dict(width=1, color="black")),
    customdata=merged[["Lap", "Pos_VER", "Speed_VER"]],
    hovertemplate="<b>Verstappen</b><br>Lap %{customdata[0]}<br>"
                  "Position %{customdata[1]}<br>"
                  "Speed %{customdata[2]} km/h"
))

# Vertical lines and annotations
fig.add_vline(x=23, line_dash="dot",  line_color="gray")
fig.add_annotation(x=22.5, y=3.8, text="Verstappen Pit", showarrow=False, font=dict(color="gray"))

fig.add_vline(x=25, line_dash="dot",  line_color="gray")
fig.add_annotation(x=24.5, y=3.4, text="Hamilton Pit", showarrow=False, font=dict(color="gray"))

fig.add_vline(x=26, line_dash="dash", line_color="red")
fig.add_annotation(x=26.5, y=2.1, text="Lap-26 Crash", showarrow=False, font=dict(color="red"))

# Layout settings
fig.update_yaxes(title="Race Position", autorange="reversed", tickmode="linear")
fig.update_xaxes(title="Lap Number", dtick=1)
fig.update_layout(
    template="plotly_white",
    hovermode="closest",
    height=600
)

# ------------------------------------------------------------------
# Display in Streamlit
# ------------------------------------------------------------------
st.plotly_chart(fig, use_container_width=True)

