print("\n✅ Starting POINTS script…\n")

import fastf1
import pandas as pd
import pathlib

# Enable FastF1 cache
fastf1.Cache.enable_cache("fastf1_cache")

# Create output folder
OUT = pathlib.Path("data")
OUT.mkdir(exist_ok=True)

# Initialize lists
ham_pts, ver_pts, event_names = [], [], []

# Loop through 22 races
for rnd in range(1, 23):
    print(f"🔄 Fetching Round {rnd}...")
    try:
        ses = fastf1.get_session(2021, rnd, "R")
        ses.load()

        res = ses.results
        ham_row = res.query("FullName == 'Lewis Hamilton'")
        ver_row = res.query("FullName == 'Max Verstappen'")

        ham_pts.append(int(ham_row.Points.iloc[0]) if not ham_row.empty else 0)
        ver_pts.append(int(ver_row.Points.iloc[0]) if not ver_row.empty else 0)
        event_names.append(ses.event.EventName)

    except Exception as e:
        print(f"⚠️ Round {rnd} failed: {e}")
        ham_pts.append(0)
        ver_pts.append(0)
        event_names.append(f"Round {rnd}")

# Create DataFrame
df = pd.DataFrame({
    "Round": range(1, 23),
    "Race": event_names,
    "Hamilton": ham_pts,
    "Verstappen": ver_pts
})

# Save to .parquet
OUT_FILE = OUT / "2021_points_progression.parquet"
df.to_parquet(OUT_FILE, index=False)

print(f"\n✔️ Data saved to: {OUT_FILE.resolve()}\n")
