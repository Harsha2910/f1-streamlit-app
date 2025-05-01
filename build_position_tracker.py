# build_position_tracker.py

import fastf1
import pandas as pd
import pathlib

print("📊 Script started …")

# Setup FastF1 cache
fastf1.Cache.enable_cache("fastf1_cache")
out_path = pathlib.Path("data")
out_path.mkdir(exist_ok=True)

# Load race session
session = fastf1.get_session(2021, "Abu Dhabi", "R")
session.load()

# Get position data
laps = session.laps
ham = laps.pick_driver("HAM")[["LapNumber", "Position"]].dropna()
ver = laps.pick_driver("VER")[["LapNumber", "Position"]].dropna()

# Merge into a common frame
pos_df = (
    ham.rename(columns={"Position": "HAM"})
    .merge(ver.rename(columns={"Position": "VER"}), on="LapNumber")
)

# Save to Parquet
file = out_path / "2021_abudhabi_positions.parquet"
pos_df.to_parquet(file, index=False)
print(f"✅ Saved to {file}")
