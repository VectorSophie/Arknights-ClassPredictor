import requests
import pandas as pd

# Download JSON
url = "https://raw.githubusercontent.com/Aceship/AN-EN-Tags/master/json/gamedata/en_US/gamedata/excel/character_table.json"
data = requests.get(url).json()

# Prepare storage
rows = {
    "name": [],
    "unit_classes": [],
    "sub_classes": [],
    "hp": [],
    "atk": [],
    "def": [],
    "res": [],
    "rdp": [],
    "cost": [],
    "blk": [],
    "spe": []
}

for char_id, char in data.items():
    # Skip limited/unobtainable
    if char.get("isNotObtainable", False):
        continue
    
    unit_class = char.get("profession", "")
    sub_class = char.get("subProfessionId", "")
    
    # Skip invalid sub_class or token operators
    if sub_class in ["notchar1", "notchar2"] or unit_class == "TOKEN":
        continue

    # Optional: keep only advanced operators (rarity >= 3)
    if char.get("rarity", 0) < 3:
        continue

    rows["name"].append(char["name"])
    rows["unit_classes"].append(unit_class)
    rows["sub_classes"].append(sub_class)

    # Take last phase stats (usually max level)
    phases = char.get("phases", [])
    if not phases:
        continue  # skip characters with no phases
    last_phase = phases[-1]
    keyframes = last_phase.get("attributesKeyFrames", [])
    if not keyframes:
        continue
    stats = keyframes[-1].get("data", {})

    # Convert numeric stats explicitly
    rows["hp"].append(int(stats.get("maxHp", 0)))
    rows["atk"].append(int(stats.get("atk", 0)))
    rows["def"].append(int(stats.get("def", 0)))
    rows["res"].append(float(stats.get("magicResistance", 0)))
    rows["rdp"].append(int(stats.get("respawnTime", 0)))
    rows["cost"].append(int(stats.get("cost", 0)))
    rows["blk"].append(int(stats.get("blockCnt", 0)))
    rows["spe"].append(float(stats.get("baseAttackTime", 0.0)))

# Build DataFrame
df = pd.DataFrame(rows)
df = df.set_index("name")  # optional: set name as index

# Save CSV
df.to_csv("Database.csv", index=True)
print("Database.csv created with", len(df), "operators")
