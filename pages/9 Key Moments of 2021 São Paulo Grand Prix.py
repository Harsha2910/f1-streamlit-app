# 2.6  •  Key Moments — 2021 São Paulo GP (Brazil)
'''
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import pathlib

st.set_page_config(layout="wide")
st.title("2.6  •  Key Moments — 2021 São Paulo Grand Prix (Brazil)")

# ------------------------------------------------------------------
# Load prebuilt data
# ------------------------------------------------------------------
DATA_DIR = pathlib.Path("data")
ham_df = pd.read_parquet(DATA_DIR / "2021_brazil_ham.parquet")
ver_df = pd.read_parquet(DATA_DIR / "2021_brazil_ver.parquet")

laps = ham_df["LapNumber"]
ham_positions = ham_df["Position"]
ver_positions = ver_df["Position"]

# ------------------------------------------------------------------
# Plotly figure
# ------------------------------------------------------------------
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=laps, y=ham_positions,
    mode="lines+markers",
    name="Lewis Hamilton",
    line=dict(color="royalblue", width=3),
    marker=dict(size=6),
    hovertemplate="Hamilton<br>Lap %{x}<br>Pos %{y}"
))

fig.add_trace(go.Scatter(
    x=laps, y=ver_positions,
    mode="lines+markers",
    name="Max Verstappen",
    line=dict(color="orangered", width=3),
    marker=dict(size=6),
    hovertemplate="Verstappen<br>Lap %{x}<br>Pos %{y}"
))

# Battle phase shading (Laps 41–58)
fig.add_vrect(x0=40.5, x1=58.5, fillcolor="lightgrey", opacity=0.25,
              layer="below", line_width=0,
              annotation_text="Battle Phase", annotation_position="top left")

# Lap 59 overtake
fig.add_vline(x=59, line=dict(color="red", dash="dash", width=2))
fig.add_annotation(
    x=60, y=0.5, xref="x", yref="paper",
    text="Hamilton Overtakes", showarrow=False,
    font=dict(color="red", size=14)
)

# Lap 71 finish
fig.add_vline(x=71, line=dict(color="black", dash="dot"))
fig.add_annotation(
    x=71, y=0.05, xref="x", yref="paper",
    text="Lap 71: Finish", showarrow=False,
    font=dict(size=12)
)

# Grid, axes, layout
fig.update_yaxes(title="Race Position", autorange="reversed", dtick=1,
                 gridcolor="lightgray", gridwidth=1)
fig.update_xaxes(title="Lap Number", dtick=5, gridcolor="lightgray", gridwidth=1)
fig.update_layout(
    title="F1 2021 – Brazil GP: Hamilton vs Verstappen Race Positions",
    plot_bgcolor="white", hovermode="x unified",
    margin=dict(l=60, r=60, t=90, b=60)
)

# ------------------------------------------------------------------
# Display
# ------------------------------------------------------------------
st.plotly_chart(fig, use_container_width=True)
'''

# import streamlit as st
# import pandas as pd
# import plotly.graph_objects as go
# import pathlib

# st.set_page_config(layout="wide")
# st.title("Key Moments of 2021 São Paulo Grand Prix")

# # ------------------------------------------------------------------
# # Load prebuilt data
# # ------------------------------------------------------------------
# DATA_DIR = pathlib.Path("data")
# ham_df = pd.read_parquet(DATA_DIR / "2021_brazil_ham.parquet")
# ver_df = pd.read_parquet(DATA_DIR / "2021_brazil_ver.parquet")

# laps = ham_df["LapNumber"]
# ham_positions = ham_df["Position"]
# ver_positions = ver_df["Position"]

# # ------------------------------------------------------------------
# # Plotly figure
# # ------------------------------------------------------------------
# fig = go.Figure()

# fig.add_trace(go.Scatter(
#     x=laps, y=ham_positions,
#     mode="lines+markers",
#     name="Lewis Hamilton",
#     line=dict(color="royalblue", width=3),
#     marker=dict(size=6),
#     hovertemplate="Hamilton<br>Lap %{x}<br>Pos %{y}"
# ))

# fig.add_trace(go.Scatter(
#     x=laps, y=ver_positions,
#     mode="lines+markers",
#     name="Max Verstappen",
#     line=dict(color="orangered", width=3),
#     marker=dict(size=6),
#     hovertemplate="Verstappen<br>Lap %{x}<br>Pos %{y}"
# ))

# # Battle phase shading (Laps 41–58)
# fig.add_vrect(x0=40.5, x1=58.5, fillcolor="white", opacity=0.1,
#               layer="below", line_width=0,
#               annotation_text="Battle Phase", annotation_position="top left",
#               annotation=dict(font=dict(color="white")))

# # Lap 59 overtake
# fig.add_vline(x=59, line=dict(color="red", dash="dash", width=2))
# fig.add_annotation(
#     x=60, y=0.5, xref="x", yref="paper",
#     text="Hamilton Overtakes", showarrow=False,
#     font=dict(color="red", size=14)
# )

# # Lap 71 finish
# fig.add_vline(x=71, line=dict(color="white", dash="dot"))
# fig.add_annotation(
#     x=71, y=0.05, xref="x", yref="paper",
#     text="Lap 71: Finish", showarrow=False,
#     font=dict(color="white", size=12)
# )

# # Grid, axes, layout
# fig.update_yaxes(title="Race Position", autorange="reversed", dtick=1,
#                  gridcolor="gray", color="white")
# fig.update_xaxes(title="Lap Number", dtick=5, gridcolor="gray", color="white")

# fig.update_layout(
#     # title="F1 2021 – Brazil GP: Hamilton vs Verstappen Race Positions",
#     plot_bgcolor="black",
#     paper_bgcolor="black",
#     font=dict(color="white"),
#     hovermode="x unified",
#     margin=dict(l=60, r=60, t=90, b=60)
# )

# # ------------------------------------------------------------------
# # Display
# # ------------------------------------------------------------------
# st.plotly_chart(fig, use_container_width=True)

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import pathlib

st.set_page_config(layout="wide")
st.title("Key Moments of 2021 São Paulo Grand Prix")

# ------------------------------------------------------------------
# Load prebuilt data
# ------------------------------------------------------------------
DATA_DIR = pathlib.Path("data")
ham_df = pd.read_parquet(DATA_DIR / "2021_brazil_ham.parquet")
ver_df = pd.read_parquet(DATA_DIR / "2021_brazil_ver.parquet")

laps = ham_df["LapNumber"]
ham_positions = ham_df["Position"]
ver_positions = ver_df["Position"]

# ------------------------------------------------------------------
# Plotly figure
# ------------------------------------------------------------------
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=laps, y=ham_positions,
    mode="lines+markers",
    name="Lewis Hamilton",
    line=dict(color="#00D2BE", width=3),  # ✅ Mercedes teal
    marker=dict(size=6),
    hovertemplate="Hamilton<br>Lap %{x}<br>Pos %{y}"
))

fig.add_trace(go.Scatter(
    x=laps, y=ver_positions,
    mode="lines+markers",
    name="Max Verstappen",
    line=dict(color="#1E41FF", width=3),  # ✅ Red Bull blue
    marker=dict(size=6),
    hovertemplate="Verstappen<br>Lap %{x}<br>Pos %{y}"
))

# Battle phase shading (Laps 41–58)
fig.add_vrect(x0=40.5, x1=58.5, fillcolor="white", opacity=0.1,
              layer="below", line_width=0,
              annotation_text="Battle Phase", annotation_position="top left",
              annotation=dict(font=dict(color="white")))

# Lap 59 overtake
fig.add_vline(x=59, line=dict(color="red", dash="dash", width=2))
fig.add_annotation(
    x=60, y=0.5, xref="x", yref="paper",
    text="Hamilton Overtakes", showarrow=False,
    font=dict(color="red", size=14)
)

# Lap 71 finish
fig.add_vline(x=71, line=dict(color="white", dash="dot"))
fig.add_annotation(
    x=71, y=0.05, xref="x", yref="paper",
    text="Lap 71: Finish", showarrow=False,
    font=dict(color="white", size=12)
)

# Grid, axes, layout
fig.update_yaxes(title="Race Position", autorange="reversed", dtick=1,
                 gridcolor="gray", color="white")
fig.update_xaxes(title="Lap Number", dtick=5, gridcolor="gray", color="white")

fig.update_layout(
    plot_bgcolor="black",
    paper_bgcolor="black",
    font=dict(color="white"),
    hovermode="x unified",
    margin=dict(l=60, r=60, t=90, b=60)
)

# ------------------------------------------------------------------
# Display
# ------------------------------------------------------------------
st.plotly_chart(fig, use_container_width=True)
