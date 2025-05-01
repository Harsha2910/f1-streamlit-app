# # '''
# # import streamlit as st
# # import pandas as pd
# # import plotly.graph_objects as go
# # import plotly.express as px
# # import matplotlib.pyplot as plt
# # import fastf1

# # st.title("Step 3.2 Tyre Strategy")

# #     # --- original notebook code ---
# # import plotly.graph_objects as go

# # # Stint data for HAM and VER (Abu Dhabi 2021)
# # stints = [
# #     # Hamilton
# #     {"driver": "HAM", "compound": "Medium", "start": 1, "end": 14, "color": "gold"},
# #     {"driver": "HAM", "compound": "Hard", "start": 14, "end": 58, "color": "lightgray"},

# #     # Verstappen
# #     {"driver": "VER", "compound": "Soft", "start": 1, "end": 14, "color": "red"},
# #     {"driver": "VER", "compound": "Hard", "start": 14, "end": 36, "color": "lightgray"},
# #     {"driver": "VER", "compound": "Hard", "start": 36, "end": 54, "color": "lightgray"},
# #     {"driver": "VER", "compound": "Soft", "start": 54, "end": 58, "color": "red"},
# # ]

# # fig = go.Figure()

# # # Draw stint bars
# # for stint in stints:
# #     fig.add_trace(go.Bar(
# #         x=[stint["end"] - stint["start"]],
# #         y=[stint["driver"]],
# #         base=stint["start"],
# #         orientation="h",
# #         marker=dict(color=stint["color"]),
# #         name=f'{stint["driver"]} – {stint["compound"]}',
# #         hovertemplate=(
# #             f"{stint['driver']}<br>"
# #             f"Compound: {stint['compound']}<br>"
# #             f"Laps: {stint['start']}–{stint['end'] - 1}<extra></extra>"
# #         ),
# #         showlegend=False
# #     ))

# # # Annotate key pit stops
# # pit_labels = {
# #     "HAM": [14],
# #     "VER": [14, 36, 54]
# # }
# # for driver, laps in pit_labels.items():
# #     for lap in laps:
# #         fig.add_trace(go.Scatter(
# #             x=[lap],
# #             y=[driver],
# #             mode="markers+text",
# #             text=[f"Pit {lap}"],
# #             textposition="top center",
# #             marker=dict(size=10, color="white"),
# #             showlegend=False
# #         ))

# # # Layout
# # fig.update_layout(
# #     title="Abu Dhabi 2021: Tyre Strategy Timeline (HAM vs VER)",
# #     xaxis_title="Lap",
# #     yaxis=dict(title="", tickmode="array", tickvals=["HAM", "VER"]),
# #     template="plotly_dark",
# #     height=400
# # )

# #     # --- display logic ---
# # if 'fig' in locals():
# #     try:
# #         st.plotly_chart(fig, use_container_width=True)
# #     except Exception:
# #         pass
# # else:
# #         # fallback for matplotlib
# #     st.pyplot(plt.gcf())
# # '''

# # import streamlit as st
# # import pandas as pd
# # import plotly.graph_objects as go
# # import matplotlib.pyplot as plt
# # import fastf1

# # st.title("Step 3.2 Tyre Strategy")

# # # --- Stint data for HAM and VER (Abu Dhabi 2021) ---
# # stints = [
# #     {"driver": "HAM", "compound": "Medium", "start": 1, "end": 14, "color": "gold"},
# #     {"driver": "HAM", "compound": "Hard", "start": 14, "end": 58, "color": "lightgray"},
# #     {"driver": "VER", "compound": "Soft", "start": 1, "end": 14, "color": "red"},
# #     {"driver": "VER", "compound": "Hard", "start": 14, "end": 36, "color": "lightgray"},
# #     {"driver": "VER", "compound": "Hard", "start": 36, "end": 54, "color": "lightgray"},
# #     {"driver": "VER", "compound": "Soft", "start": 54, "end": 58, "color": "red"},
# # ]

# # fig = go.Figure()

# # # Draw stint bars
# # for stint in stints:
# #     fig.add_trace(go.Bar(
# #         x=[stint["end"] - stint["start"]],
# #         y=[stint["driver"]],
# #         base=stint["start"],
# #         orientation="h",
# #         marker=dict(color=stint["color"]),
# #         name=f'{stint["driver"]} – {stint["compound"]}',
# #         hovertemplate=(
# #             f"{stint['driver']}<br>"
# #             f"Compound: {stint['compound']}<br>"
# #             f"Laps: {stint['start']}–{stint['end'] - 1}<extra></extra>"
# #         ),
# #         showlegend=False
# #     ))

# # # Annotate key pit stops (with y-shifted text)
# # pit_labels = {
# #     "HAM": [14],
# #     "VER": [14, 36, 54]
# # }
# # for driver, laps in pit_labels.items():
# #     for lap in laps:
# #         fig.add_trace(go.Scatter(
# #             x=[lap],
# #             y=[driver],
# #             mode="markers+text",
# #             text=[f"Pit {lap}"],
# #             textposition="top center",
# #             textfont=dict(color="white", size=12),
# #             marker=dict(size=10, color="white"),
# #             showlegend=False
# #         ))

# # # Layout
# # fig.update_layout(
# #     title="Abu Dhabi 2021: Tyre Strategy Timeline (HAM vs VER)",
# #     xaxis_title="Lap",
# #     yaxis=dict(title="", tickmode="array", tickvals=["HAM", "VER"]),
# #     template="plotly_dark",
# #     height=400
# # )

# # # Display
# # if 'fig' in locals():
# #     try:
# #         st.plotly_chart(fig, use_container_width=True)
# #     except Exception:
# #         pass
# # else:
# #     st.pyplot(plt.gcf())
# import streamlit as st
# import pandas as pd
# import plotly.graph_objects as go
# import matplotlib.pyplot as plt

# st.set_page_config(layout="wide")
# st.title("Step 3.2 Tyre Strategy")

# # --- Stint data for HAM and VER (Abu Dhabi 2021) ---
# stints = [
#     {"driver": "HAM", "compound": "Medium", "start": 1, "end": 14, "color": "gold"},
#     {"driver": "HAM", "compound": "Hard", "start": 14, "end": 58, "color": "lightgray"},
#     {"driver": "VER", "compound": "Soft", "start": 1, "end": 14, "color": "red"},
#     {"driver": "VER", "compound": "Hard", "start": 14, "end": 36, "color": "lightgray"},
#     {"driver": "VER", "compound": "Hard", "start": 36, "end": 54, "color": "lightgray"},
#     {"driver": "VER", "compound": "Soft", "start": 54, "end": 58, "color": "red"},
# ]

# fig = go.Figure()

# # Draw stint bars
# for stint in stints:
#     fig.add_trace(go.Bar(
#         x=[stint["end"] - stint["start"]],
#         y=[stint["driver"]],
#         base=stint["start"],
#         orientation="h",
#         marker=dict(color=stint["color"]),
#         name=f'{stint["driver"]} – {stint["compound"]}',
#         hovertemplate=(f"{stint['driver']}<br>Compound: {stint['compound']}<br>Laps: {stint['start']}–{stint['end'] - 1}<extra></extra>"),
#         showlegend=False
#     ))

# # Annotate pit stops (adjust text offset for visibility)
# pit_labels = {
#     "HAM": [(14, "top left", -10, -5)],
#     "VER": [(14, "top right", 10, -5), (36, "bottom left", -10, 10), (54, "top center", 0, -10)]
# }

# for driver, labels in pit_labels.items():
#     for lap, pos, xshift, yshift in labels:
#         fig.add_trace(go.Scatter(
#             x=[lap],
#             y=[driver],
#             mode="markers+text",
#             text=[f"Pit {lap}"],
#             textposition=pos,
#             textfont=dict(color="white", size=12),
#             marker=dict(size=10, color="white"),
#             textangle=0,
#             showlegend=False,
#             hoverinfo="skip",
#             textfont_size=12,
#             textfont_family="Arial",
#             textfont_color="white",
#             textposition_="top center"
#         ))

# # Layout
# fig.update_layout(
#     title="Abu Dhabi 2021: Tyre Strategy Timeline (HAM vs VER)",
#     xaxis_title="Lap",
#     yaxis=dict(title="", tickmode="array", tickvals=["HAM", "VER"]),
#     template="plotly_dark",
#     height=400
# )

# # Display
# if 'fig' in locals():
#     try:
#         st.plotly_chart(fig, use_container_width=True)
#     except Exception:
#         pass
# else:
#     st.pyplot(plt.gcf())
# import streamlit as st
# import pandas as pd
# import plotly.graph_objects as go
# import matplotlib.pyplot as plt

# st.set_page_config(layout="wide")
# st.title("Tyre Strategy")

# # --- Stint data for HAM and VER (Abu Dhabi 2021) ---
# stints = [
#     {"driver": "HAM", "compound": "Medium", "start": 1, "end": 14, "color": "gold"},
#     {"driver": "HAM", "compound": "Hard", "start": 14, "end": 58, "color": "lightgray"},
#     {"driver": "VER", "compound": "Soft", "start": 1, "end": 14, "color": "red"},
#     {"driver": "VER", "compound": "Hard", "start": 14, "end": 36, "color": "lightgray"},
#     {"driver": "VER", "compound": "Hard", "start": 36, "end": 54, "color": "lightgray"},
#     {"driver": "VER", "compound": "Soft", "start": 54, "end": 58, "color": "red"},
# ]

# fig = go.Figure()

# # Draw stint bars
# for stint in stints:
#     fig.add_trace(go.Bar(
#         x=[stint["end"] - stint["start"]],
#         y=[stint["driver"]],
#         base=stint["start"],
#         orientation="h",
#         marker=dict(color=stint["color"]),
#         name=f'{stint["driver"]} – {stint["compound"]}',
#         hovertemplate=(f"{stint['driver']}<br>Compound: {stint['compound']}<br>Laps: {stint['start']}–{stint['end'] - 1}<extra></extra>"),
#         showlegend=False
#     ))

# # Annotate key pit stops with offset positioning
# pit_labels = {
#     "HAM": [(14, "top right", 10, -10)],
#     "VER": [(14, "top left", -10, -10), (36, "bottom left", -10, 10), (54, "top right", 10, -10)]
# }

# for driver, label_list in pit_labels.items():
#     for lap, text_pos, xshift, yshift in label_list:
#         fig.add_trace(go.Scatter(
#             x=[lap],
#             y=[driver],
#             mode="markers+text",
#             text=[f"Pit {lap}"],
#             textposition=text_pos,
#             textfont=dict(color="white", size=12),
#             marker=dict(size=10, color="white"),
#             xaxis="x",
#             yaxis="y",
#             showlegend=False,
#             hoverinfo="skip",
#             # manually shifting the text
#             textfont_size=12,
#             customdata=[[xshift, yshift]],
#             hovertemplate=None
#         ))

# # Layout
# fig.update_layout(
#     # title="Tyre Strategy",
#     xaxis_title="Lap",
#     yaxis=dict(title="", tickmode="array", tickvals=["HAM", "VER"]),
#     template="plotly_dark",
#     height=400
# )

# # Display
# if 'fig' in locals():
#     try:
#         st.plotly_chart(fig, use_container_width=True)
#     except Exception:
#         pass
# else:
#     st.pyplot(plt.gcf())
# import streamlit as st
# import pandas as pd
# import plotly.graph_objects as go
# import matplotlib.pyplot as plt

# st.set_page_config(layout="wide")
# st.title("Tyre Strategy")

# # --- Stint data for HAM and VER (Abu Dhabi 2021) ---
# stints = [
#     {"driver": "HAM", "compound": "Medium", "start": 1, "end": 14, "color": "gold"},
#     {"driver": "HAM", "compound": "Hard", "start": 14, "end": 58, "color": "lightgray"},
#     {"driver": "VER", "compound": "Soft", "start": 1, "end": 14, "color": "red"},
#     {"driver": "VER", "compound": "Hard", "start": 14, "end": 36, "color": "lightgray"},
#     {"driver": "VER", "compound": "Hard", "start": 36, "end": 54, "color": "lightgray"},
#     {"driver": "VER", "compound": "Soft", "start": 54, "end": 58, "color": "red"},
# ]

# fig = go.Figure()

# # Draw stint bars
# for stint in stints:
#     fig.add_trace(go.Bar(
#         x=[stint["end"] - stint["start"]],
#         y=[stint["driver"]],
#         base=stint["start"],
#         orientation="h",
#         marker=dict(color=stint["color"]),
#         name=f'{stint["driver"]} – {stint["compound"]}',
#         hovertemplate=(f"{stint['driver']}<br>Compound: {stint['compound']}<br>Laps: {stint['start']}–{stint['end'] - 1}<extra></extra>"),
#         showlegend=False
#     ))

# # Annotate key pit stops
# pit_labels = {
#     "HAM": [(14, "top right", 10, -10)],
#     "VER": [(14, "top left", -10, -10), (36, "bottom left", -10, 10), (54, "top right", 10, -10)]
# }

# for driver, label_list in pit_labels.items():
#     for lap, text_pos, xshift, yshift in label_list:
#         fig.add_trace(go.Scatter(
#             x=[lap],
#             y=[driver],
#             mode="markers+text",
#             text=[f"Pit {lap}"],
#             textposition=text_pos,
#             textfont=dict(color="white", size=12),
#             marker=dict(size=10, color="white"),
#             showlegend=False,
#             hoverinfo="skip"
#         ))

# # Add tyre legend on the side
# legend_x = 62
# legend_y_start = 1.5
# legend_gap = 0.3
# legend_items = [
#     {"label": "Soft Tyres", "color": "red"},
#     {"label": "Medium Tyres", "color": "gold"},
#     {"label": "Hard Tyres", "color": "lightgray"},
# ]

# for i, item in enumerate(legend_items):
#     fig.add_trace(go.Scatter(
#         x=[legend_x], y=[legend_y_start - i * legend_gap],
#         mode="markers+text",
#         marker=dict(color=item["color"], size=12),
#         text=[item["label"]],
#         textposition="middle right",
#         textfont=dict(color="white", size=12),
#         showlegend=False,
#         hoverinfo="skip"
#     ))

# # Layout
# fig.update_layout(
#     xaxis_title="Lap",
#     yaxis=dict(title="", tickmode="array", tickvals=["HAM", "VER"]),
#     template="plotly_dark",
#     height=400,
#     xaxis_range=[0, 70]  # add some room to the right for the legend
# )

# # Display
# if 'fig' in locals():
#     try:
#         st.plotly_chart(fig, use_container_width=True)
#     except Exception:
#         pass
# else:
#     st.pyplot(plt.gcf())
# import streamlit as st
# import pandas as pd
# import plotly.graph_objects as go
# import matplotlib.pyplot as plt

# st.set_page_config(layout="wide")
# st.title("Tyre Strategy")

# # --- Stint data for HAM and VER (Abu Dhabi 2021) ---
# stints = [
#     {"driver": "HAM", "compound": "Medium", "start": 1, "end": 14, "color": "gold"},
#     {"driver": "HAM", "compound": "Hard", "start": 14, "end": 58, "color": "lightgray"},
#     {"driver": "VER", "compound": "Soft", "start": 1, "end": 14, "color": "red"},
#     {"driver": "VER", "compound": "Hard", "start": 14, "end": 36, "color": "lightgray"},
#     {"driver": "VER", "compound": "Hard", "start": 36, "end": 54, "color": "lightgray"},
#     {"driver": "VER", "compound": "Soft", "start": 54, "end": 58, "color": "red"},
# ]

# fig = go.Figure()

# # Draw stint bars (with thicker bars using width)
# for stint in stints:
#     fig.add_trace(go.Bar(
#         x=[stint["end"] - stint["start"]],
#         y=[stint["driver"]],
#         base=stint["start"],
#         orientation="h",
#         width=0.6,  # 👈 Thicker bars
#         marker=dict(color=stint["color"]),
#         name=f'{stint["driver"]} – {stint["compound"]}',
#         hovertemplate=(f"{stint['driver']}<br>Compound: {stint['compound']}<br>Laps: {stint['start']}–{stint['end'] - 1}<extra></extra>"),
#         showlegend=False
#     ))

# # Annotate pit stops
# pit_labels = {
#     "HAM": [(14, "top right", 10, -10)],
#     "VER": [(14, "top left", -10, -10), (36, "bottom left", -10, 10), (54, "top right", 10, -10)]
# }

# for driver, label_list in pit_labels.items():
#     for lap, text_pos, xshift, yshift in label_list:
#         fig.add_trace(go.Scatter(
#             x=[lap],
#             y=[driver],
#             mode="markers+text",
#             text=[f"Pit {lap}"],
#             textposition=text_pos,
#             textfont=dict(color="white", size=12),
#             marker=dict(size=10, color="white"),
#             showlegend=False,
#             hoverinfo="skip"
#         ))

# # Add tyre type legend at side
# legend_x = 65
# legend_y_start = 1.5
# legend_gap = 0.3
# legend_items = [
#     {"label": "Soft Tyres", "color": "red"},
#     {"label": "Medium Tyres", "color": "gold"},
#     {"label": "Hard Tyres", "color": "lightgray"},
# ]

# for i, item in enumerate(legend_items):
#     fig.add_trace(go.Scatter(
#         x=[legend_x], y=[legend_y_start - i * legend_gap],
#         mode="markers+text",
#         marker=dict(color=item["color"], size=12, symbol='circle'),
#         text=[item["label"]],
#         textposition="middle right",
#         textfont=dict(color="white", size=12),
#         showlegend=False,
#         hoverinfo="skip"
#     ))

# # Layout
# fig.update_layout(
#     xaxis_title="Lap",
#     yaxis=dict(title="", tickmode="array", tickvals=["HAM", "VER"]),
#     template="plotly_dark",
#     height=400,
#     xaxis_range=[0, 75]
# )

# # Display
# if 'fig' in locals():
#     try:
#         st.plotly_chart(fig, use_container_width=True)
#     except Exception:
#         pass
# else:
#     st.pyplot(plt.gcf())
# import streamlit as st
# import pandas as pd
# import plotly.graph_objects as go
# import matplotlib.pyplot as plt

# st.set_page_config(layout="wide")
# st.title("Tyre Strategy")

# # --- Stint data for HAM and VER (Abu Dhabi 2021) ---
# stints = [
#     {"driver": "HAM", "compound": "Medium", "start": 1, "end": 14, "color": "gold"},
#     {"driver": "HAM", "compound": "Hard", "start": 14, "end": 58, "color": "lightgray"},
#     {"driver": "VER", "compound": "Soft", "start": 1, "end": 14, "color": "red"},
#     {"driver": "VER", "compound": "Hard", "start": 14, "end": 36, "color": "lightgray"},
#     {"driver": "VER", "compound": "Hard", "start": 36, "end": 54, "color": "lightgray"},
#     {"driver": "VER", "compound": "Soft", "start": 54, "end": 58, "color": "red"},
# ]

# fig = go.Figure()

# # Keep track of compound types already added to legend
# legend_added = {"Soft": False, "Medium": False, "Hard": False}

# # Draw stint bars with proper legend
# for stint in stints:
#     compound = stint["compound"]
#     show_legend = not legend_added[compound]
#     legend_added[compound] = True

#     fig.add_trace(go.Bar(
#         x=[stint["end"] - stint["start"]],
#         y=[stint["driver"]],
#         base=stint["start"],
#         orientation="h",
#         width=0.6,
#         marker=dict(color=stint["color"]),
#         name=f"{compound} Tyres",
#         legendgroup=compound,
#         showlegend=show_legend,
#         hovertemplate=(f"{stint['driver']}<br>Compound: {compound}<br>Laps: {stint['start']}–{stint['end'] - 1}<extra></extra>")
#     ))

# # Annotate pit stops
# pit_labels = {
#     "HAM": [(14, "top right")],
#     "VER": [(14, "top left"), (36, "bottom left"), (54, "top right")]
# }

# for driver, label_list in pit_labels.items():
#     for lap, text_pos in label_list:
#         fig.add_trace(go.Scatter(
#             x=[lap],
#             y=[driver],
#             mode="markers+text",
#             text=[f"Pit {lap}"],
#             textposition=text_pos,
#             textfont=dict(color="white", size=12),
#             marker=dict(size=10, color="white"),
#             showlegend=False,
#             hoverinfo="skip"
#         ))

# # Layout
# fig.update_layout(
#     xaxis_title="Lap",
#     yaxis=dict(title="", tickmode="array", tickvals=["HAM", "VER"]),
#     template="plotly_dark",
#     height=400,
#     legend=dict(
#         title="", 
#         orientation="v",
#         y=1, yanchor="top",
#         x=1.02, xanchor="left",
#         font=dict(size=12)
#     )
# )

# # Display
# st.plotly_chart(fig, use_container_width=True)
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("Tyre Strategy")

# --- Stint data for HAM and VER (Abu Dhabi 2021) ---
stints = [
    {"driver": "HAM", "compound": "Medium", "start": 1, "end": 14, "color": "gold"},
    {"driver": "HAM", "compound": "Hard", "start": 14, "end": 58, "color": "lightgray"},
    {"driver": "VER", "compound": "Soft", "start": 1, "end": 14, "color": "red"},
    {"driver": "VER", "compound": "Hard", "start": 14, "end": 36, "color": "lightgray"},
    {"driver": "VER", "compound": "Hard", "start": 36, "end": 54, "color": "lightgray"},
    {"driver": "VER", "compound": "Soft", "start": 54, "end": 58, "color": "red"},
]

fig = go.Figure()

# Track which compounds are already in the legend
legend_added = {"Soft": False, "Medium": False, "Hard": False}

# Plot stints
for stint in stints:
    compound = stint["compound"]
    show_legend = not legend_added[compound]
    legend_added[compound] = True

    fig.add_trace(go.Bar(
        x=[stint["end"] - stint["start"]],
        y=[stint["driver"]],
        base=stint["start"],
        orientation="h",
        width=0.2,  # 👈 Reduced from 0.6 to 0.4
        marker=dict(color=stint["color"]),
        name=f"{compound} Tyres",
        legendgroup=compound,
        showlegend=show_legend,
        hovertemplate=(f"{stint['driver']}<br>Compound: {compound}<br>Laps: {stint['start']}–{stint['end'] - 1}<extra></extra>")
    ))

# Annotate pit stops
pit_labels = {
    "HAM": [(14, "top right")],
    "VER": [(14, "top left"), (36, "bottom left"), (54, "top right")]
}

for driver, label_list in pit_labels.items():
    for lap, text_pos in label_list:
        fig.add_trace(go.Scatter(
            x=[lap],
            y=[driver],
            mode="markers+text",
            text=[f"Pit {lap}"],
            textposition=text_pos,
            textfont=dict(color="white", size=12),
            marker=dict(size=10, color="white"),
            showlegend=False,
            hoverinfo="skip"
        ))

# Layout
fig.update_layout(
    xaxis_title="Lap",
    yaxis=dict(title="", tickmode="array", tickvals=["HAM", "VER"]),
    template="plotly_dark",
    height=400,
    legend=dict(
        title="",
        orientation="v",
        y=1, yanchor="top",
        x=1.02, xanchor="left",
        font=dict(size=12)
    )
)

# Display
st.plotly_chart(fig, use_container_width=True)


