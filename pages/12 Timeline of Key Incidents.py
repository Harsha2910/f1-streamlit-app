
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import fastf1

st.title("Timeline of Key Incidents/Messages of Abu Dhabi GP")

    # --- original notebook code ---
import pandas as pd
import plotly.express as px

# Expanded key events from race article
events = [
    (1, "Lights out — HAM overtakes VER", "Racing Incident"),
    (1, "Turn 6 Incident: VER dives, HAM cuts corner", "Racing Incident"),
    (3, "Race Control: No investigation necessary", "Race Control"),
    (3, "Wheatley: 'Max was ahead at apex...'", "Red Bull"),
    (3, "Masi: 'HAM gave back all advantage'", "Race Control"),
    (3, "Verstappen: 'Incredible! What are they doing?!'", "Red Bull"),
    (3, "Horner: 'Total lack of consistency'", "Red Bull"),
    (3, "Rosberg: 'Max too aggressive...'", "Race Control"),
    (3, "Hill: 'I'm surprised they didn’t say give place back'", "Race Control"),
    (14, "VER pits (Soft → Hard)", "Red Bull"),
    (15, "HAM pits (Medium → Hard)", "Mercedes"),
    (20, "Perez defense — VER closes 8s gap", "Red Bull"),
    (20, "Wolff: 'Michael, warn them — it's dangerous'", "Mercedes"),
    (20, "Masi: 'They're racing hard, Toto'", "Race Control"),
    (20, "VER: 'Checo is a legend!'", "Red Bull"),
    (36, "Giovinazzi retires — VSC deployed", "Race Control"),
    (36, "VER pits again — fresher hards", "Red Bull"),
    (36, "Wolff: 'Please no safety car, it interferes...'", "Mercedes"),
    (36, "HAM: 'Are we in trouble? Can't keep up pace'", "Mercedes"),
    (36, "Bonnington: 'Risk of losing position too high'", "Mercedes"),
    (53, "Latifi crash — debris everywhere", "Race Control"),
    (54, "SC deployed — VER pits for Softs", "Red Bull"),
    (54, "HAM: 'Can't box? That's unbelievable man.'", "Mercedes"),
    (56, "Race Control: Lapped cars will NOT overtake", "Race Control"),
    (56, "Lambiase: 'Classic! Not surprised.'", "Red Bull"),
    (57, "Horner: 'You only need one racing lap!'", "Red Bull"),
    (57, "Wheatley: 'Let lapped cars go — we’ve got a race'", "Red Bull"),
    (57, "Race Control: Only 5 cars to unlap", "Race Control"),
    (57, "Wolff: 'Michael this isn't right!'", "Mercedes"),
    (57, "VER overtakes HAM — last lap", "Racing Incident"),
    (58, "HAM: 'This has been manipulated man!'", "Mercedes"),
    (58, "Wolff: 'Reinstate the lap before!'", "Mercedes"),
    (58, "Masi: 'Toto, we went car racing.'", "Race Control")
]

df = pd.DataFrame(events, columns=["Lap", "Event", "Category"])

# Color palette
category_colors = {
    "Racing Incident": "white",
    "Race Control": "lightgray",
    "Red Bull": "#1E41FF",   # Red Bull blue
    "Mercedes": "#00D2BE"    # Mercedes teal
}

# Create the beeswarm plot
fig = px.strip(
    df,
    x="Lap",
    y="Category",
    color="Category",
    hover_name="Event",
    stripmode="overlay",
    color_discrete_map=category_colors,
    template="plotly_dark"
)

# Style the markers
fig.update_traces(marker=dict(size=15, line=dict(width=1, color='black')))

# Layout tweaks with updated x-axis ticks
fig.update_layout(
    xaxis_title="Lap",
    yaxis_title="",
    height=420,
    plot_bgcolor="black",
    paper_bgcolor="black",
    font=dict(color="white"),
    xaxis=dict(tickmode="linear", dtick=5),
    legend=dict(orientation="h", y=1.15, x=0.5, xanchor="center")
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


