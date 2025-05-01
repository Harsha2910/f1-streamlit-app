import fastf1
import pandas as pd
import os
import pathlib

print("✅ Script started")

# Enable FastF1 cache
fastf1.Cache.enable_cache("fastf1_cache")

# ✅ Create the /data folder if it doesn't exist
out_path = pathlib.Path("data")
out_path.mkdir(parents=True, exist_ok=True)

# Load the session
session = fastf1.get_session(2021, "Brazil", "R")
session.load()

# Get laps
ham_laps = session.laps.pick_driver("HAM")
ver_laps = session.laps.pick_driver("VER")

# Get first position per lap
ham_pos = ham_laps.groupby("LapNumber")["Position"].first().reset_index()
ver_pos = ver_laps.groupby("LapNumber")["Position"].first().reset_index()

# Insert Lap 1 manually for Hamilton (engine penalty)
ham_pos = pd.concat([
    pd.DataFrame({"LapNumber": [1], "Position": [10]}),
    ham_pos[ham_pos["LapNumber"] != 1]
], ignore_index=True)

# Create all lap numbers
all_laps = pd.DataFrame({"LapNumber": range(1, session.total_laps + 1)})

# Merge and fill gaps
ham_full = all_laps.merge(ham_pos, on="LapNumber", how="left").ffill().astype({"Position": int})
ver_full = all_laps.merge(ver_pos, on="LapNumber", how="left").ffill().astype({"Position": int})

out_path = pathlib.Path("data")

ham_file = out_path / "2021_brazil_ham.parquet"
ver_file = out_path / "2021_brazil_ver.parquet"

ham_full.to_parquet(ham_file, index=False)
ver_full.to_parquet(ver_file, index=False)

print(f"✅ Saved to {ham_file}")
print(f"✅ Saved to {ver_file}")
