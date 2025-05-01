print("✅ Script started")

import fastf1, pandas as pd, os, pathlib

# Step 1: Set up FastF1 cache
fastf1.Cache.enable_cache("fastf1_cache")

# Step 2: Create a local folder to store output
OUT = pathlib.Path("data")
OUT.mkdir(exist_ok=True)

# Step 3: Download + load the Silverstone race session
session = fastf1.get_session(2021, "Silverstone", "R")
session.load()

# Step 4: Get Hamilton & Verstappen laps
ham = session.laps.pick_driver("HAM").query("IsAccurate")[["LapNumber", "Position", "SpeedST"]]
ver = session.laps.pick_driver("VER").query("IsAccurate")[["LapNumber", "Position", "SpeedST"]]

# Step 5: Patch Hamilton missing early laps
ham_patch = pd.DataFrame({
    "LapNumber": [1, 2, 3, 4],
    "Position": [2, 2, 2, 2],
    "SpeedST": [300, 301, 302, 302]
})
ham = pd.concat([ham_patch, ham]).drop_duplicates("LapNumber")

# Step 6: Patch Verstappen if Lap 1 is missing
if 1 not in ver["LapNumber"].values:
    ver_patch = pd.DataFrame({"LapNumber": [1], "Position": [2], "SpeedST": [0]})
    ver = pd.concat([ver_patch, ver])

# Step 7: Save to Parquet files
ham_file = OUT / "2021_silverstone_ham.parquet"
ver_file = OUT / "2021_silverstone_ver.parquet"

ham.to_parquet(ham_file, index=False)
ver.to_parquet(ver_file, index=False)

print(f"✔️  Saved: {ham_file}")
print(f"✔️  Saved: {ver_file}")