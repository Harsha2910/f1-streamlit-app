import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import fastf1

st.title("Scenario B: What if the safety car procedure was followed properly?")

    # --- original notebook code ---
import pandas as pd
import plotly.graph_objects as go

# Laps 48 to 58
laps = list(range(48, 59))

# Extend values
actual_gap_full = [11.4, 11.5, 11.6, 11.7, 11.75, None, None, None, None, None, None]
sc_gap_actual_full = [None, None, None, None, None, 11.8, 8.5, 2.5, 0.2, -0.1, 0.0]
scenario_b_projected_full = [None, None, None, None, None, 11.8, 11.8, 11.8, 11.8, 11.8, 11.8]

# DataFrame
df = pd.DataFrame({
    'Lap': laps,
    'Actual_Gap': actual_gap_full,
    'SC_Manipulated': sc_gap_actual_full,
    'Scenario_B_No_Pass': scenario_b_projected_full
})

# Plot
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df['Lap'],
    y=df['Actual_Gap'],
    mode='lines+markers',
    name='Actual Gap (Before Lap 53)',
    line=dict(color='firebrick', width=2),
    marker=dict(size=6)
))

fig.add_trace(go.Scatter(
    x=df['Lap'],
    y=df['SC_Manipulated'],
    mode='lines+markers',
    name='Actual With Lapped Cars Cleared',
    line=dict(color='white', width=2, dash='dot'),
    marker=dict(size=6, color='white')
))

fig.add_trace(go.Scatter(
    x=df['Lap'],
    y=df['Scenario_B_No_Pass'],
    mode='lines+markers',
    name='Projected (If Cars Not Cleared)',
    line=dict(color='deepskyblue', width=3, dash='dash'),
    marker=dict(size=6, color='deepskyblue')
))

fig.add_vline(x=53, line_width=1.5, line_dash='dot', line_color='gray')

fig.update_layout(
    # title='⚖️ Scenario B: Projected Gap if Proper Safety Car Protocol Followed (Laps 48–58)',
    xaxis_title='Lap',
    yaxis_title='Gap to Hamilton (seconds)',
    template='plotly_dark',
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    height=550
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


