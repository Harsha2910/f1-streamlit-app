# build_gap_abudhabi.py

import fastf1
import pandas as pd
import pathlib
import os

print("📊 Script started …")

fastf1.Cache.enable_cache("fastf1_cache")
out_path = pathlib.Path("data")
out_path.mkdir(exist_ok=True)

# Load session
ses = fastf1.get_session(2021, "Abu Dhabi", "R")
ses.load()

# Extract lap time data
laps = ses.laps
ham = laps.pick_driver("HAM")[["LapNumber", "LapTime"]].dropna()
ver = laps.pick_driver("VER")[["LapNumber", "LapTime"]].dropna()

ham["HAM_LapTime"] = ham.LapTime.dt.total_seconds()
ver["VER_LapTime"] = ver.LapTime.dt.total_seconds()

merged = (
    ham[["LapNumber", "HAM_LapTime"]]
    .merge(ver[["LapNumber", "VER_LapTime"]], on="LapNumber")
)
merged["HAM_CumTime"] = merged.HAM_LapTime.cumsum()
merged["VER_CumTime"] = merged.VER_LapTime.cumsum()
merged["Gap_to_HAM"] = merged.VER_CumTime - merged.HAM_CumTime

# Save to file
file = out_path / "2021_abudhabi_gap.parquet"
merged.to_parquet(file, index=False)
print(f"✅ Saved to {file}")
