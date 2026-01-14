# Author: Emin Arda Cakir
# Source: Transfermarkt (January 2026 Update)
# Project: Galatasaray High-Value Squad Analysis

# Professional dataset for the current 2026 squad
players = {
    "Victor Osimhen": {"age": 27, "position": "Center-Forward", "value": "75M €"},
    "Gabriel Sara": {"age": 26, "position": "Central Midfield", "value": "22M €"},
    "Baris Alper Yilmaz": {"age": 25, "position": "Right Winger", "value": "21M €"},
    "Davinson Sanchez": {"age": 29, "position": "Centre-Back", "value": "18M €"},
    "Mauro Icardi": {"age": 32, "position": "Center-Forward", "value": "12M €"},
    "Lucas Torreira": {"age": 29, "position": "Defensive Midfield", "value": "15M €"},
    "Ismail Jakobs": {"age": 26, "position": "Left-Back", "value": "10M €"},
    "Gunay Guvenc": {"age": 34, "position": "Goalkeeper", "value": "0.5M €"}
}

print("--- GALATASARAY MARKET VALUE ANALYSIS (2026 UPDATE) ---")
print(f"Analyzing {len(players)} active squad members...")
print("-" * 65)

# Formatting and displaying the data
for name, info in players.items():
    print(f"PLAYER: {name:20} | POSITION: {info['position']:18} | VALUE: {info['value']}")

print("-" * 65)
print("STATUS: 2026 Squad data successfully processed.")
print("MISSION: Working towards Data Science and iOS Development.")
