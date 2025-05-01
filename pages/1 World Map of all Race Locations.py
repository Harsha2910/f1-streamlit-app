
# # # # # import streamlit as st
# # # # # import pandas as pd
# # # # # import plotly.graph_objects as go
# # # # # import plotly.express as px
# # # # # import matplotlib.pyplot as plt
# # # # # import fastf1

# # # # # st.title("1.1 World Map of all Race Locations")

# # # # #     # --- original notebook code ---
# # # # # import pandas as pd
# # # # # import plotly.graph_objects as go

# # # # # # Full 2021 F1 Calendar with location and track info
# # # # # race_data = pd.DataFrame({
# # # # #     'Race': ["Bahrain GP", "Emilia Romagna GP", "Portuguese GP", "Spanish GP", "Monaco GP",
# # # # #              "Azerbaijan GP", "French GP", "Styrian GP", "Austrian GP", "British GP",
# # # # #              "Hungarian GP", "Belgian GP", "Dutch GP", "Italian GP", "Russian GP",
# # # # #              "Turkish GP", "United States GP", "Mexican GP", "Brazilian GP", "Qatar GP",
# # # # #              "Saudi Arabian GP", "Abu Dhabi GP"],
# # # # #     'Circuit': ["Bahrain International Circuit", "Imola", "Portimão", "Circuit de Barcelona-Catalunya", "Monte Carlo",
# # # # #                 "Baku City Circuit", "Circuit Paul Ricard", "Red Bull Ring", "Red Bull Ring", "Silverstone Circuit",
# # # # #                 "Hungaroring", "Spa-Francorchamps", "Zandvoort", "Monza", "Sochi Autodrom",
# # # # #                 "Istanbul Park", "Circuit of the Americas", "Autódromo Hermanos Rodríguez", "Interlagos", "Losail Circuit",
# # # # #                 "Jeddah Street Circuit", "Yas Marina Circuit"],
# # # # #     'Location': ["Sakhir, Bahrain", "Imola, Italy", "Portimão, Portugal", "Barcelona, Spain", "Monte Carlo, Monaco",
# # # # #                  "Baku, Azerbaijan", "Le Castellet, France", "Spielberg, Austria", "Spielberg, Austria", "Silverstone, UK",
# # # # #                  "Mogyoród, Hungary", "Spa, Belgium", "Zandvoort, Netherlands", "Monza, Italy", "Sochi, Russia",
# # # # #                  "Istanbul, Turkey", "Austin, USA", "Mexico City, Mexico", "São Paulo, Brazil", "Lusail, Qatar",
# # # # #                  "Jeddah, Saudi Arabia", "Abu Dhabi, UAE"],
# # # # #     'Laps': [57, 63, 66, 66, 78, 51, 53, 71, 71, 52, 70, 44, 72, 53, 53, 58, 56, 71, 71, 57, 50, 58],
# # # # #     'Length_km': [5.412, 4.909, 4.653, 4.675, 3.337, 6.003, 5.842, 4.318, 4.318, 5.891,
# # # # #                   4.381, 7.004, 4.259, 5.793, 5.848, 5.338, 5.513, 4.304, 4.309, 5.380, 6.174, 5.281],
# # # # #     'Length_miles': [3.363, 3.050, 2.892, 2.905, 2.074, 3.730, 3.630, 2.683, 2.683, 3.660,
# # # # #                      2.722, 4.352, 2.646, 3.600, 3.634, 3.315, 3.426, 2.674, 2.676, 3.343, 3.837, 3.281],
# # # # #     'Latitude': [26.0325, 44.3439, 37.2283, 41.57, 43.7347, 40.3725, 43.2508, 47.2197, 47.2197, 52.0786,
# # # # #                  47.5789, 50.4372, 52.3889, 45.6156, 43.4057, 40.9517, 30.1328, 19.4042, -23.7036, 25.49,
# # # # #                  21.6319, 24.4672],
# # # # #     'Longitude': [50.5106, 11.7167, -8.6268, 2.2611, 7.4206, 49.8533, 5.7858, 14.7647, 14.7647, -1.0169,
# # # # #                   19.2486, 5.9714, 4.5400, 9.2811, 39.9578, 29.405, -97.6411, -99.0886, -46.6997, 51.4542,
# # # # #                   39.1036, 54.6031]
# # # # # })

# # # # # # Tooltip formatting
# # # # # race_data['Tooltip'] = race_data.apply(
# # # # #     lambda row: f"<b>{row['Race']}</b><br>{row['Circuit']},<br>{row['Location']}<br>"
# # # # #                 f"Laps: {row['Laps']}<br>Course Length: {row['Length_km']} km ({row['Length_miles']} miles)",
# # # # #     axis=1
# # # # # )

# # # # # # Create 3D globe
# # # # # fig = go.Figure()

# # # # # fig.add_trace(go.Scattergeo(
# # # # #     lon=race_data['Longitude'],
# # # # #     lat=race_data['Latitude'],
# # # # #     text=race_data['Tooltip'],
# # # # #     mode='markers',
# # # # #     marker=dict(size=10, color='red', line=dict(width=1, color='white')),
# # # # #     hoverinfo='text'
# # # # # ))

# # # # # fig.update_geos(
# # # # #     projection_type='orthographic',
# # # # #     showland=True, landcolor='lightgray',
# # # # #     showocean=True, oceancolor='lightblue',
# # # # #     showcountries=True, countrycolor='gray',
# # # # #     showframe=False, lataxis_showgrid=True, lonaxis_showgrid=True,
# # # # # )

# # # # # fig.update_layout(
# # # # #     title='🌍 Formula 1 2021: All 22 Race Locations ',
# # # # #     margin=dict(l=0, r=0, t=50, b=0),
# # # # #     height=700
# # # # # )

# # # # #     # --- display logic ---
# # # # # if 'fig' in locals():
# # # # #     try:
# # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # #     except Exception:
# # # # #         pass
# # # # # else:
# # # # #         # fallback for matplotlib
# # # # #     st.pyplot(plt.gcf())
# # # # import streamlit as st
# # # # import pandas as pd
# # # # import plotly.graph_objects as go
# # # # import matplotlib.pyplot as plt

# # # # st.set_page_config(layout="wide")
# # # # st.title("1.1 World Map of all Race Locations")

# # # # # --- Race data ---
# # # # race_data = pd.DataFrame({
# # # #     'Race': ["Bahrain GP", "Emilia Romagna GP", "Portuguese GP", "Spanish GP", "Monaco GP",
# # # #              "Azerbaijan GP", "French GP", "Styrian GP", "Austrian GP", "British GP",
# # # #              "Hungarian GP", "Belgian GP", "Dutch GP", "Italian GP", "Russian GP",
# # # #              "Turkish GP", "United States GP", "Mexican GP", "Brazilian GP", "Qatar GP",
# # # #              "Saudi Arabian GP", "Abu Dhabi GP"],
# # # #     'Circuit': ["Bahrain International Circuit", "Imola", "Portimão", "Circuit de Barcelona-Catalunya", "Monte Carlo",
# # # #                 "Baku City Circuit", "Circuit Paul Ricard", "Red Bull Ring", "Red Bull Ring", "Silverstone Circuit",
# # # #                 "Hungaroring", "Spa-Francorchamps", "Zandvoort", "Monza", "Sochi Autodrom",
# # # #                 "Istanbul Park", "Circuit of the Americas", "Autódromo Hermanos Rodríguez", "Interlagos", "Losail Circuit",
# # # #                 "Jeddah Street Circuit", "Yas Marina Circuit"],
# # # #     'Location': ["Sakhir, Bahrain", "Imola, Italy", "Portimão, Portugal", "Barcelona, Spain", "Monte Carlo, Monaco",
# # # #                  "Baku, Azerbaijan", "Le Castellet, France", "Spielberg, Austria", "Spielberg, Austria", "Silverstone, UK",
# # # #                  "Mogyoród, Hungary", "Spa, Belgium", "Zandvoort, Netherlands", "Monza, Italy", "Sochi, Russia",
# # # #                  "Istanbul, Turkey", "Austin, USA", "Mexico City, Mexico", "São Paulo, Brazil", "Lusail, Qatar",
# # # #                  "Jeddah, Saudi Arabia", "Abu Dhabi, UAE"],
# # # #     'Laps': [57, 63, 66, 66, 78, 51, 53, 71, 71, 52, 70, 44, 72, 53, 53, 58, 56, 71, 71, 57, 50, 58],
# # # #     'Length_km': [5.412, 4.909, 4.653, 4.675, 3.337, 6.003, 5.842, 4.318, 4.318, 5.891,
# # # #                   4.381, 7.004, 4.259, 5.793, 5.848, 5.338, 5.513, 4.304, 4.309, 5.380, 6.174, 5.281],
# # # #     'Length_miles': [3.363, 3.050, 2.892, 2.905, 2.074, 3.730, 3.630, 2.683, 2.683, 3.660,
# # # #                      2.722, 4.352, 2.646, 3.600, 3.634, 3.315, 3.426, 2.674, 2.676, 3.343, 3.837, 3.281],
# # # #     'Latitude': [26.0325, 44.3439, 37.2283, 41.57, 43.7347, 40.3725, 43.2508, 47.2197, 47.2197, 52.0786,
# # # #                  47.5789, 50.4372, 52.3889, 45.6156, 43.4057, 40.9517, 30.1328, 19.4042, -23.7036, 25.49,
# # # #                  21.6319, 24.4672],
# # # #     'Longitude': [50.5106, 11.7167, -8.6268, 2.2611, 7.4206, 49.8533, 5.7858, 14.7647, 14.7647, -1.0169,
# # # #                   19.2486, 5.9714, 4.5400, 9.2811, 39.9578, 29.405, -97.6411, -99.0886, -46.6997, 51.4542,
# # # #                   39.1036, 54.6031]
# # # # })

# # # # # Tooltip formatting
# # # # race_data['Tooltip'] = race_data.apply(
# # # #     lambda row: f"<b>{row['Race']}</b><br>{row['Circuit']},<br>{row['Location']}<br>"
# # # #                 f"Laps: {row['Laps']}<br>Course Length: {row['Length_km']} km ({row['Length_miles']} miles)",
# # # #     axis=1
# # # # )

# # # # # Create 3D globe
# # # # fig = go.Figure()

# # # # fig.add_trace(go.Scattergeo(
# # # #     lon=race_data['Longitude'],
# # # #     lat=race_data['Latitude'],
# # # #     text=race_data['Tooltip'],
# # # #     mode='markers',
# # # #     marker=dict(size=10, color='red', line=dict(width=1, color='white')),
# # # #     hoverinfo='text'
# # # # ))

# # # # fig.update_geos(
# # # #     projection_type='orthographic',
# # # #     bgcolor='black',  # ✅ set background of the globe
# # # #     showland=True, landcolor='gray',
# # # #     showocean=True, oceancolor='black',  # ✅ black ocean
# # # #     showcountries=True, countrycolor='white',
# # # #     showframe=False
# # # # )

# # # # fig.update_layout(
# # # #     title='🌍 Formula 1 2021: All 22 Race Locations',
# # # #     paper_bgcolor='black',   # ✅ outer background
# # # #     plot_bgcolor='black',
# # # #     font=dict(color='white'),
# # # #     margin=dict(l=0, r=0, t=50, b=0),
# # # #     height=700
# # # # )

# # # # # Display
# # # # if 'fig' in locals():
# # # #     try:
# # # #         st.plotly_chart(fig, use_container_width=True)
# # # #     except Exception:
# # # #         pass
# # # # else:
# # # #     st.pyplot(plt.gcf())
# # # import streamlit as st
# # # import pandas as pd
# # # import plotly.graph_objects as go
# # # import matplotlib.pyplot as plt

# # # st.set_page_config(layout="wide")
# # # st.title("1.1 World Map of all Race Locations")

# # # # --- Race data ---
# # # race_data = pd.DataFrame({
# # #     'Race': ["Bahrain GP", "Emilia Romagna GP", "Portuguese GP", "Spanish GP", "Monaco GP",
# # #              "Azerbaijan GP", "French GP", "Styrian GP", "Austrian GP", "British GP",
# # #              "Hungarian GP", "Belgian GP", "Dutch GP", "Italian GP", "Russian GP",
# # #              "Turkish GP", "United States GP", "Mexican GP", "Brazilian GP", "Qatar GP",
# # #              "Saudi Arabian GP", "Abu Dhabi GP"],
# # #     'Circuit': ["Bahrain International Circuit", "Imola", "Portimão", "Circuit de Barcelona-Catalunya", "Monte Carlo",
# # #                 "Baku City Circuit", "Circuit Paul Ricard", "Red Bull Ring", "Red Bull Ring", "Silverstone Circuit",
# # #                 "Hungaroring", "Spa-Francorchamps", "Zandvoort", "Monza", "Sochi Autodrom",
# # #                 "Istanbul Park", "Circuit of the Americas", "Autódromo Hermanos Rodríguez", "Interlagos", "Losail Circuit",
# # #                 "Jeddah Street Circuit", "Yas Marina Circuit"],
# # #     'Location': ["Sakhir, Bahrain", "Imola, Italy", "Portimão, Portugal", "Barcelona, Spain", "Monte Carlo, Monaco",
# # #                  "Baku, Azerbaijan", "Le Castellet, France", "Spielberg, Austria", "Spielberg, Austria", "Silverstone, UK",
# # #                  "Mogyoród, Hungary", "Spa, Belgium", "Zandvoort, Netherlands", "Monza, Italy", "Sochi, Russia",
# # #                  "Istanbul, Turkey", "Austin, USA", "Mexico City, Mexico", "São Paulo, Brazil", "Lusail, Qatar",
# # #                  "Jeddah, Saudi Arabia", "Abu Dhabi, UAE"],
# # #     'Laps': [57, 63, 66, 66, 78, 51, 53, 71, 71, 52, 70, 44, 72, 53, 53, 58, 56, 71, 71, 57, 50, 58],
# # #     'Length_km': [5.412, 4.909, 4.653, 4.675, 3.337, 6.003, 5.842, 4.318, 4.318, 5.891,
# # #                   4.381, 7.004, 4.259, 5.793, 5.848, 5.338, 5.513, 4.304, 4.309, 5.380, 6.174, 5.281],
# # #     'Length_miles': [3.363, 3.050, 2.892, 2.905, 2.074, 3.730, 3.630, 2.683, 2.683, 3.660,
# # #                      2.722, 4.352, 2.646, 3.600, 3.634, 3.315, 3.426, 2.674, 2.676, 3.343, 3.837, 3.281],
# # #     'Latitude': [26.0325, 44.3439, 37.2283, 41.57, 43.7347, 40.3725, 43.2508, 47.2197, 47.2197, 52.0786,
# # #                  47.5789, 50.4372, 52.3889, 45.6156, 43.4057, 40.9517, 30.1328, 19.4042, -23.7036, 25.49,
# # #                  21.6319, 24.4672],
# # #     'Longitude': [50.5106, 11.7167, -8.6268, 2.2611, 7.4206, 49.8533, 5.7858, 14.7647, 14.7647, -1.0169,
# # #                   19.2486, 5.9714, 4.5400, 9.2811, 39.9578, 29.405, -97.6411, -99.0886, -46.6997, 51.4542,
# # #                   39.1036, 54.6031]
# # # })

# # # # Tooltip formatting
# # # race_data['Tooltip'] = race_data.apply(
# # #     lambda row: f"<b>{row['Race']}</b><br>{row['Circuit']},<br>{row['Location']}<br>"
# # #                 f"Laps: {row['Laps']}<br>Course Length: {row['Length_km']} km ({row['Length_miles']} miles)",
# # #     axis=1
# # # )

# # # # Create globe figure
# # # fig = go.Figure()

# # # fig.add_trace(go.Scattergeo(
# # #     lon=race_data['Longitude'],
# # #     lat=race_data['Latitude'],
# # #     text=race_data['Tooltip'],
# # #     mode='markers',
# # #     marker=dict(size=9, color='red', line=dict(width=1.5, color='white')),
# # #     hoverinfo='text'
# # # ))

# # # fig.update_geos(
# # #     projection_type='orthographic',
# # #     bgcolor='black',
# # #     showland=True, landcolor='gray',
# # #     showocean=True, oceancolor='black',
# # #     showcountries=True, countrycolor='white',
# # #     showlakes=False,
# # #     showcoastlines=True, coastlinecolor='deepskyblue',  # glow-like edge
# # #     showgrid=True,
# # #     lonaxis=dict(showgrid=True, gridcolor="white", gridwidth=0.5),
# # #     lataxis=dict(showgrid=True, gridcolor="white", gridwidth=0.5)
# # # )

# # # fig.update_layout(
# # #     title='🌍 Formula 1 2021: All 22 Race Locations',
# # #     paper_bgcolor='black',
# # #     plot_bgcolor='black',
# # #     font=dict(color='white'),
# # #     margin=dict(l=0, r=0, t=50, b=0),
# # #     height=720
# # # )

# # # # Display
# # # st.plotly_chart(fig, use_container_width=True)
# # import streamlit as st
# # import pandas as pd
# # import plotly.graph_objects as go

# # st.set_page_config(layout="wide")
# # st.title("1.1 World Map of all Race Locations")

# # # --- Race data ---
# # race_data = pd.DataFrame({
# #     'Race': ["Bahrain GP", "Emilia Romagna GP", "Portuguese GP", "Spanish GP", "Monaco GP",
# #              "Azerbaijan GP", "French GP", "Styrian GP", "Austrian GP", "British GP",
# #              "Hungarian GP", "Belgian GP", "Dutch GP", "Italian GP", "Russian GP",
# #              "Turkish GP", "United States GP", "Mexican GP", "Brazilian GP", "Qatar GP",
# #              "Saudi Arabian GP", "Abu Dhabi GP"],
# #     'Circuit': ["Bahrain International Circuit", "Imola", "Portimão", "Circuit de Barcelona-Catalunya", "Monte Carlo",
# #                 "Baku City Circuit", "Circuit Paul Ricard", "Red Bull Ring", "Red Bull Ring", "Silverstone Circuit",
# #                 "Hungaroring", "Spa-Francorchamps", "Zandvoort", "Monza", "Sochi Autodrom",
# #                 "Istanbul Park", "Circuit of the Americas", "Autódromo Hermanos Rodríguez", "Interlagos", "Losail Circuit",
# #                 "Jeddah Street Circuit", "Yas Marina Circuit"],
# #     'Location': ["Sakhir, Bahrain", "Imola, Italy", "Portimão, Portugal", "Barcelona, Spain", "Monte Carlo, Monaco",
# #                  "Baku, Azerbaijan", "Le Castellet, France", "Spielberg, Austria", "Spielberg, Austria", "Silverstone, UK",
# #                  "Mogyoród, Hungary", "Spa, Belgium", "Zandvoort, Netherlands", "Monza, Italy", "Sochi, Russia",
# #                  "Istanbul, Turkey", "Austin, USA", "Mexico City, Mexico", "São Paulo, Brazil", "Lusail, Qatar",
# #                  "Jeddah, Saudi Arabia", "Abu Dhabi, UAE"],
# #     'Latitude': [26.0325, 44.3439, 37.2283, 41.57, 43.7347, 40.3725, 43.2508, 47.2197, 47.2197, 52.0786,
# #                  47.5789, 50.4372, 52.3889, 45.6156, 43.4057, 40.9517, 30.1328, 19.4042, -23.7036, 25.49,
# #                  21.6319, 24.4672],
# #     'Longitude': [50.5106, 11.7167, -8.6268, 2.2611, 7.4206, 49.8533, 5.7858, 14.7647, 14.7647, -1.0169,
# #                   19.2486, 5.9714, 4.5400, 9.2811, 39.9578, 29.405, -97.6411, -99.0886, -46.6997, 51.4542,
# #                   39.1036, 54.6031]
# # })

# # # Tooltip
# # race_data['Tooltip'] = race_data.apply(
# #     lambda row: f"<b>{row['Race']}</b><br>{row['Circuit']},<br>{row['Location']}", axis=1
# # )

# # # --- Plotly globe ---
# # fig = go.Figure()

# # fig.add_trace(go.Scattergeo(
# #     lon=race_data['Longitude'],
# #     lat=race_data['Latitude'],
# #     text=race_data['Tooltip'],
# #     mode='markers',
# #     marker=dict(size=9, color='red', line=dict(width=1.5, color='white')),
# #     hoverinfo='text'
# # ))

# # fig.update_geos(
# #     projection_type='orthographic',
# #     bgcolor='black',
# #     showland=True, landcolor='gray',
# #     showocean=True, oceancolor='black',
# #     showcountries=True, countrycolor='white',
# #     showcoastlines=True, coastlinecolor='deepskyblue', coastlinewidth=2,
# #     showframe=False
# # )

# # fig.update_layout(
# #     title='🌍 Formula 1 2021: All 22 Race Locations',
# #     paper_bgcolor='black',
# #     plot_bgcolor='black',
# #     font=dict(color='white'),
# #     margin=dict(l=0, r=0, t=50, b=0),
# #     height=700
# # )

# # # --- Display ---
# # st.plotly_chart(fig, use_container_width=True)
# import streamlit as st
# import pandas as pd
# import plotly.graph_objects as go

# st.set_page_config(layout="wide")
# st.title("🌍 1.1 World Map of all Race Locations")

# # 2021 F1 Calendar data
# race_data = pd.DataFrame({
#     'Race': ["Bahrain GP", "Emilia Romagna GP", "Portuguese GP", "Spanish GP", "Monaco GP",
#              "Azerbaijan GP", "French GP", "Styrian GP", "Austrian GP", "British GP",
#              "Hungarian GP", "Belgian GP", "Dutch GP", "Italian GP", "Russian GP",
#              "Turkish GP", "United States GP", "Mexican GP", "Brazilian GP", "Qatar GP",
#              "Saudi Arabian GP", "Abu Dhabi GP"],
#     'Circuit': ["Bahrain International Circuit", "Imola", "Portimão", "Circuit de Barcelona-Catalunya", "Monte Carlo",
#                 "Baku City Circuit", "Circuit Paul Ricard", "Red Bull Ring", "Red Bull Ring", "Silverstone Circuit",
#                 "Hungaroring", "Spa-Francorchamps", "Zandvoort", "Monza", "Sochi Autodrom",
#                 "Istanbul Park", "Circuit of the Americas", "Autódromo Hermanos Rodríguez", "Interlagos", "Losail Circuit",
#                 "Jeddah Street Circuit", "Yas Marina Circuit"],
#     'Location': ["Sakhir, Bahrain", "Imola, Italy", "Portimão, Portugal", "Barcelona, Spain", "Monte Carlo, Monaco",
#                  "Baku, Azerbaijan", "Le Castellet, France", "Spielberg, Austria", "Spielberg, Austria", "Silverstone, UK",
#                  "Mogyoród, Hungary", "Spa, Belgium", "Zandvoort, Netherlands", "Monza, Italy", "Sochi, Russia",
#                  "Istanbul, Turkey", "Austin, USA", "Mexico City, Mexico", "São Paulo, Brazil", "Lusail, Qatar",
#                  "Jeddah, Saudi Arabia", "Abu Dhabi, UAE"],
#     'Laps': [57, 63, 66, 66, 78, 51, 53, 71, 71, 52, 70, 44, 72, 53, 53, 58, 56, 71, 71, 57, 50, 58],
#     'Length_km': [5.412, 4.909, 4.653, 4.675, 3.337, 6.003, 5.842, 4.318, 4.318, 5.891,
#                   4.381, 7.004, 4.259, 5.793, 5.848, 5.338, 5.513, 4.304, 4.309, 5.380, 6.174, 5.281],
#     'Latitude': [26.0325, 44.3439, 37.2283, 41.57, 43.7347, 40.3725, 43.2508, 47.2197, 47.2197, 52.0786,
#                  47.5789, 50.4372, 52.3889, 45.6156, 43.4057, 40.9517, 30.1328, 19.4042, -23.7036, 25.49,
#                  21.6319, 24.4672],
#     'Longitude': [50.5106, 11.7167, -8.6268, 2.2611, 7.4206, 49.8533, 5.7858, 14.7647, 14.7647, -1.0169,
#                   19.2486, 5.9714, 4.5400, 9.2811, 39.9578, 29.405, -97.6411, -99.0886, -46.6997, 51.4542,
#                   39.1036, 54.6031]
# })

# # Tooltip text
# race_data['Tooltip'] = race_data.apply(
#     lambda row: f"<b>{row['Race']}</b><br>{row['Circuit']},<br>{row['Location']}<br>"
#                 f"Laps: {row['Laps']}<br>Length: {row['Length_km']} km",
#     axis=1
# )

# # Create globe figure
# fig = go.Figure()

# # Soft glow background layer (larger transparent marker)
# fig.add_trace(go.Scattergeo(
#     lon=race_data['Longitude'],
#     lat=race_data['Latitude'],
#     mode='markers',
#     marker=dict(size=20, color='red', opacity=0.2),
#     hoverinfo='skip',
#     showlegend=False
# ))

# # Foreground race marker layer
# fig.add_trace(go.Scattergeo(
#     lon=race_data['Longitude'],
#     lat=race_data['Latitude'],
#     text=race_data['Tooltip'],
#     mode='markers',
#     marker=dict(size=8, color='red', line=dict(width=1, color='white')),
#     hoverinfo='text',
#     name="Race Locations"
# ))

# # Globe styling
# fig.update_geos(
#     projection_type='orthographic',
#     showland=True, landcolor='gray',
#     showocean=True, oceancolor='black',
#     showcountries=True, countrycolor='white',
#     coastlinecolor='deepskyblue',
#     coastlinewidth=2,
#     bgcolor='black',
#     showframe=False,
# )

# # Layout styling
# fig.update_layout(
#     title="🌍 Formula 1 2021: All 22 Race Locations",
#     paper_bgcolor='black',
#     plot_bgcolor='black',
#     font=dict(color='white'),
#     margin=dict(l=0, r=0, t=50, b=0),
#     height=700
# )

# # Display in Streamlit
# st.plotly_chart(fig, use_container_width=True)
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(layout="wide")
st.title("🌍 World Map of all Race Locations")

# F1 2021 Race Data
race_data = pd.DataFrame({
    'Race': ["Bahrain GP", "Emilia Romagna GP", "Portuguese GP", "Spanish GP", "Monaco GP",
             "Azerbaijan GP", "French GP", "Styrian GP", "Austrian GP", "British GP",
             "Hungarian GP", "Belgian GP", "Dutch GP", "Italian GP", "Russian GP",
             "Turkish GP", "United States GP", "Mexican GP", "Brazilian GP", "Qatar GP",
             "Saudi Arabian GP", "Abu Dhabi GP"],
    'Circuit': ["Bahrain International Circuit", "Imola", "Portimão", "Circuit de Barcelona-Catalunya", "Monte Carlo",
                "Baku City Circuit", "Circuit Paul Ricard", "Red Bull Ring", "Red Bull Ring", "Silverstone Circuit",
                "Hungaroring", "Spa-Francorchamps", "Zandvoort", "Monza", "Sochi Autodrom",
                "Istanbul Park", "Circuit of the Americas", "Autódromo Hermanos Rodríguez", "Interlagos", "Losail Circuit",
                "Jeddah Street Circuit", "Yas Marina Circuit"],
    'Location': ["Sakhir, Bahrain", "Imola, Italy", "Portimão, Portugal", "Barcelona, Spain", "Monte Carlo, Monaco",
                 "Baku, Azerbaijan", "Le Castellet, France", "Spielberg, Austria", "Spielberg, Austria", "Silverstone, UK",
                 "Mogyoród, Hungary", "Spa, Belgium", "Zandvoort, Netherlands", "Monza, Italy", "Sochi, Russia",
                 "Istanbul, Turkey", "Austin, USA", "Mexico City, Mexico", "São Paulo, Brazil", "Lusail, Qatar",
                 "Jeddah, Saudi Arabia", "Abu Dhabi, UAE"],
    'Laps': [57, 63, 66, 66, 78, 51, 53, 71, 71, 52, 70, 44, 72, 53, 53, 58, 56, 71, 71, 57, 50, 58],
    'Length_km': [5.412, 4.909, 4.653, 4.675, 3.337, 6.003, 5.842, 4.318, 4.318, 5.891,
                  4.381, 7.004, 4.259, 5.793, 5.848, 5.338, 5.513, 4.304, 4.309, 5.380, 6.174, 5.281],
    'Latitude': [26.0325, 44.3439, 37.2283, 41.57, 43.7347, 40.3725, 43.2508, 47.2197, 47.2197, 52.0786,
                 47.5789, 50.4372, 52.3889, 45.6156, 43.4057, 40.9517, 30.1328, 19.4042, -23.7036, 25.49,
                 21.6319, 24.4672],
    'Longitude': [50.5106, 11.7167, -8.6268, 2.2611, 7.4206, 49.8533, 5.7858, 14.7647, 14.7647, -1.0169,
                  19.2486, 5.9714, 4.5400, 9.2811, 39.9578, 29.405, -97.6411, -99.0886, -46.6997, 51.4542,
                  39.1036, 54.6031]
})

race_data['Tooltip'] = race_data.apply(
    lambda row: f"<b>{row['Race']}</b><br>{row['Circuit']},<br>{row['Location']}<br>"
                f"Laps: {row['Laps']}<br>Length: {row['Length_km']} km",
    axis=1
)

fig = go.Figure()

# Glow marker behind main dot
fig.add_trace(go.Scattergeo(
    lon=race_data['Longitude'],
    lat=race_data['Latitude'],
    mode='markers',
    marker=dict(size=20, color='red', opacity=0.2),
    hoverinfo='skip',
    showlegend=False
))

# Foreground marker with tooltip
fig.add_trace(go.Scattergeo(
    lon=race_data['Longitude'],
    lat=race_data['Latitude'],
    text=race_data['Tooltip'],
    mode='markers',
    marker=dict(size=8, color='red', line=dict(width=1, color='white')),
    hoverinfo='text',
    name="Race Locations"
))

# Enhanced globe config
fig.update_geos(
    projection_type='orthographic',
    showland=True, landcolor='gray',
    showocean=True, oceancolor='#0a2542',  # Deep navy blue ocean
    showcountries=True, countrycolor='white',
    coastlinecolor='deepskyblue', coastlinewidth=2,
    lonaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)'),
    lataxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)'),
    bgcolor='black',
    showframe=False
)

# Final layout
fig.update_layout(
    # title="🌍 Formula 1 2021: All 22 Race Locations",
    paper_bgcolor='black',
    plot_bgcolor='black',
    font=dict(color='white'),
    margin=dict(l=0, r=0, t=50, b=0),
    height=720
)

st.plotly_chart(fig, use_container_width=True)
