# # # # 2.4  •  Key Moments — 2021 British Grand Prix (Silverstone)

# # # import streamlit as st
# # # import pandas as pd
# # # import plotly.graph_objects as go

# # # st.set_page_config(layout="wide")
# # # st.title("Key Moments of British Grand Prix")

# # # # ✅ Load from prebuilt parquet files (no FastF1 needed)
# # # @st.cache_data
# # # def load_silverstone_data():
# # #     ham = pd.read_parquet("data/2021_silverstone_ham.parquet")
# # #     ver = pd.read_parquet("data/2021_silverstone_ver.parquet")
# # #     return ham, ver

# # # ham_df, ver_df = load_silverstone_data()

# # # # Plot
# # # fig = go.Figure()

# # # fig.add_trace(go.Scatter(
# # #     x=ham_df["LapNumber"],
# # #     y=ham_df["Position"],
# # #     mode="lines+markers",
# # #     name="Lewis Hamilton",
# # #     line=dict(color="royalblue"),
# # #     customdata=ham_df[["LapNumber", "Position", "SpeedST"]],
# # #     hovertemplate="<b>Hamilton</b><br>Lap %{customdata[0]}<br>"
# # #                   "Pos %{customdata[1]}<br>Speed %{customdata[2]:.0f} km/h"
# # # ))

# # # fig.add_trace(go.Scatter(
# # #     x=ver_df["LapNumber"],
# # #     y=ver_df["Position"],
# # #     mode="lines+markers",
# # #     name="Max Verstappen",
# # #     line=dict(color="orangered"),
# # #     customdata=ver_df[["LapNumber", "Position", "SpeedST"]],
# # #     hovertemplate="<b>Verstappen</b><br>Lap %{customdata[0]}<br>"
# # #                   "Pos %{customdata[1]}<br>Speed %{customdata[2]:.0f} km/h"
# # # ))

# # # # Events
# # # fig.add_vline(x=1, line_dash="dash", line_color="red")
# # # fig.add_vline(x=27, line_dash="dash", line_color="gray")
# # # fig.add_annotation(x=4.5, y=4, text="Verstappen Crash (Lap 1)", showarrow=False, font=dict(color="red"))
# # # fig.add_annotation(x=24, y=4, text="Hamilton 10 s Penalty", showarrow=False, font=dict(color="gray"))

# # # fig.update_yaxes(autorange="reversed", title="Race Position", tickmode="linear")
# # # fig.update_xaxes(title="Lap Number", tick0=1, dtick=1)
# # # fig.update_layout(
# # #     # title="2021 Silverstone GP • Lap-by-Lap Positions & Key Events",
# # #     hovermode="closest",
# # #     template="plotly_white",
# # #     height=600
# # # )

# # # st.plotly_chart(fig, use_container_width=True)
# # import streamlit as st
# # import pandas as pd
# # import plotly.graph_objects as go

# # st.set_page_config(layout="wide")
# # st.title("Key Moments of British Grand Prix")

# # # ✅ Load from prebuilt parquet files
# # @st.cache_data
# # def load_silverstone_data():
# #     ham = pd.read_parquet("data/2021_silverstone_ham.parquet")
# #     ver = pd.read_parquet("data/2021_silverstone_ver.parquet")
# #     return ham, ver

# # ham_df, ver_df = load_silverstone_data()

# # # ----------------------------------
# # # Plotly chart
# # # ----------------------------------
# # fig = go.Figure()

# # # Lewis Hamilton
# # fig.add_trace(go.Scatter(
# #     x=ham_df["LapNumber"],
# #     y=ham_df["Position"],
# #     mode="lines+markers",
# #     name="Lewis Hamilton",
# #     line=dict(color="royalblue"),
# #     marker=dict(size=6),
# #     customdata=ham_df[["LapNumber", "Position", "SpeedST"]],
# #     hovertemplate="<b>Hamilton</b><br>Lap %{customdata[0]}<br>"
# #                   "Pos %{customdata[1]}<br>"
# #                   "Speed %{customdata[2]:.0f} km/h<extra></extra>"
# # ))

# # # Max Verstappen
# # fig.add_trace(go.Scatter(
# #     x=ver_df["LapNumber"],
# #     y=ver_df["Position"],
# #     mode="lines+markers",
# #     name="Max Verstappen",
# #     line=dict(color="orangered"),
# #     marker=dict(size=6),
# #     customdata=ver_df[["LapNumber", "Position", "SpeedST"]],
# #     hovertemplate="<b>Verstappen</b><br>Lap %{customdata[0]}<br>"
# #                   "Pos %{customdata[1]}<br>"
# #                   "Speed %{customdata[2]:.0f} km/h<extra></extra>"
# # ))

# # # Vertical event lines
# # fig.add_vline(x=1, line_dash="dash", line_color="red")
# # fig.add_vline(x=27, line_dash="dash", line_color="gray")

# # # Annotations
# # fig.add_annotation(
# #     x=5.3, y=4, text="Verstappen Crash (Lap 1)",
# #     showarrow=False, font=dict(color="red", size=12)
# # )
# # fig.add_annotation(
# #     x=23, y=4, text="Hamilton 10 s Penalty",
# #     showarrow=False, font=dict(color="gray", size=12)
# # )

# # # Axes and layout
# # fig.update_yaxes(
# #     title="Race Position",
# #     autorange="reversed",  # Keep this if you want 1 at top = better position
# #     tickmode="linear",
# #     dtick=1
# # )
# # fig.update_xaxes(
# #     title="Lap Number",
# #     tickangle=0,          # 👈 Keeps labels horizontal
# #     tickmode="linear",
# #     dtick=2,              # 👈 Shows every 2nd tick to reduce clutter
# #     tickfont=dict(size=10)
# # )
# # fig.update_layout(
# #     template="plotly_dark",
# #     hovermode="closest",
# #     height=600,
# #     margin=dict(l=40, r=40, t=60, b=40),
# #     title=dict(
# #         text="Lap-by-Lap Race Positions: British GP 2021",
# #         x=0.5,
# #         xanchor="center"
# #     )
# # )

# # # Display in Streamlit
# # st.plotly_chart(fig, use_container_width=True)
# import streamlit as st
# import pandas as pd
# import plotly.graph_objects as go

# st.set_page_config(layout="wide")
# st.title("Key Moments of British Grand Prix")  # ✅ Your exact title

# # ✅ Load from prebuilt parquet files
# @st.cache_data
# def load_silverstone_data():
#     ham = pd.read_parquet("data/2021_silverstone_ham.parquet")
#     ver = pd.read_parquet("data/2021_silverstone_ver.parquet")
#     return ham, ver

# ham_df, ver_df = load_silverstone_data()

# # ---------------------
# # Plotly Chart
# # ---------------------
# fig = go.Figure()

# # Lewis Hamilton trace
# fig.add_trace(go.Scatter(
#     x=ham_df["LapNumber"],
#     y=ham_df["Position"],
#     mode="lines+markers",
#     name="Lewis Hamilton",
#     line=dict(color="royalblue"),
#     marker=dict(size=6),
#     customdata=ham_df[["LapNumber", "Position", "SpeedST"]],
#     hovertemplate="<b>Hamilton</b><br>Lap %{customdata[0]}<br>"
#                   "Pos %{customdata[1]}<br>"
#                   "Speed %{customdata[2]:.0f} km/h<extra></extra>"
# ))

# # Max Verstappen trace
# fig.add_trace(go.Scatter(
#     x=ver_df["LapNumber"],
#     y=ver_df["Position"],
#     mode="lines+markers",
#     name="Max Verstappen",
#     line=dict(color="orangered"),
#     marker=dict(size=6),
#     customdata=ver_df[["LapNumber", "Position", "SpeedST"]],
#     hovertemplate="<b>Verstappen</b><br>Lap %{customdata[0]}<br>"
#                   "Pos %{customdata[1]}<br>"
#                   "Speed %{customdata[2]:.0f} km/h<extra></extra>"
# ))

# # Key event lines and annotations
# fig.add_vline(x=1, line_dash="dash", line_color="red")
# fig.add_vline(x=27, line_dash="dash", line_color="gray")

# fig.add_annotation(
#     x=5.3, y=4, text="Verstappen Crash (Lap 1)",
#     showarrow=False, font=dict(color="red", size=12)
# )
# fig.add_annotation(
#     x=23, y=4, text="Hamilton 10 s Penalty",
#     showarrow=False, font=dict(color="gray", size=12)
# )

# # Axes setup
# fig.update_yaxes(
#     title="Race Position",
#     autorange="reversed",
#     tickmode="linear",
#     dtick=1
# )
# fig.update_xaxes(
#     title="Lap Number",
#     tickangle=0,
#     tickmode="linear",
#     dtick=1,
#     tickfont=dict(size=10),
#     range=[1, 53]
# )

# # Layout
# fig.update_layout(
#     template="plotly_dark",
#     hovermode="closest",
#     height=600,
#     margin=dict(l=40, r=40, t=40, b=40)  # 👈 No extra title, tight layout
# )

# # Display in Streamlit
# st.plotly_chart(fig, use_container_width=True)


import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(layout="wide")
st.title("Key Moments of British Grand Prix")  # ✅ Keeping your original title

# ✅ Load from prebuilt parquet files
@st.cache_data
def load_silverstone_data():
    ham = pd.read_parquet("data/2021_silverstone_ham.parquet")
    ver = pd.read_parquet("data/2021_silverstone_ver.parquet")
    return ham, ver

ham_df, ver_df = load_silverstone_data()

# ---------------------
# Plotly Chart
# ---------------------
fig = go.Figure()

# Lewis Hamilton trace
fig.add_trace(go.Scatter(
    x=ham_df["LapNumber"],
    y=ham_df["Position"],
    mode="lines+markers",
    name="Lewis Hamilton",
    line=dict(color="#00D2BE"),  # Mercedes teal
    marker=dict(size=6),
    customdata=ham_df[["LapNumber", "Position", "SpeedST"]],
    hovertemplate="<b>Hamilton</b><br>Lap %{customdata[0]}<br>"
                  "Pos %{customdata[1]}<br>"
                  "Speed %{customdata[2]:.0f} km/h<extra></extra>"
))

# Max Verstappen trace
fig.add_trace(go.Scatter(
    x=ver_df["LapNumber"],
    y=ver_df["Position"],
    mode="lines+markers",
    name="Max Verstappen",
    line=dict(color="#1E41FF"),  # Red Bull blue
    marker=dict(size=6),
    customdata=ver_df[["LapNumber", "Position", "SpeedST"]],
    hovertemplate="<b>Verstappen</b><br>Lap %{customdata[0]}<br>"
                  "Pos %{customdata[1]}<br>"
                  "Speed %{customdata[2]:.0f} km/h<extra></extra>"
))

# Key event lines and annotations
fig.add_vline(x=1, line_dash="dash", line_color="red")
fig.add_vline(x=27, line_dash="dash", line_color="gray")

fig.add_annotation(
    x=5.3, y=4, text="Verstappen Crash (Lap 1)",
    showarrow=False, font=dict(color="red", size=12)
)
fig.add_annotation(
    x=23, y=4, text="Hamilton 10 s Penalty",
    showarrow=False, font=dict(color="gray", size=12)
)

# Axes config
fig.update_yaxes(
    title="Race Position",
    autorange="reversed",
    tickmode="linear",
    dtick=1
)
fig.update_xaxes(
    title="Lap Number",
    tickangle=0,
    tickmode="linear",
    dtick=1,
    tickfont=dict(size=10),
    range=[1, 53]
)

# Layout
fig.update_layout(
    template="plotly_dark",
    hovermode="closest",
    height=600,
    margin=dict(l=40, r=40, t=40, b=40)
)

# Show chart
st.plotly_chart(fig, use_container_width=True)
