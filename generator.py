"""
Generates a JSON file containing mock satellite equipment data.

This script creates random equipment entries (sensors, batteries, etc.) 
associated with various subsystems and exports them to 'data.json' 
for testing purposes.
"""

import json
import random

# Lists
systems = ['Thermal', 'Power', 'Communication', 'Attitude and Orbit Control', 'Propulsion']
equip_types = ['Sensor', 'Valve', 'Battery', 'Computer', 'Tracker']
measure_types = ['Voltage', 'Power', 'Temperature', 'Pressure', 'Energy']
a, b = -100, 250


data = []

# Generating 50 equipments with random attributes
for i in range(50):
    chosen_system = random.choice(systems)
    chosen_type = random.choice(equip_types)
    equip_name = f"{chosen_type}_{i}"

    entry = {}
    entry["system"] = chosen_system
    entry["name"] = equip_name
    entry["limits"] = {"type" : random.choice(measure_types), "min": random.randint(a, -b//8), "max":random.randint(-a//2, b)}
    
    data.append(entry)

# Save data in the json file
with open('massive_data.json', 'w') as f:
    json.dump(data, f, indent=4)