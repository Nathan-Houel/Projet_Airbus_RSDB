import json
import pytest

# Opening and reading the json file
with open('massive_data.json','r') as f:
    data = json.load(f)

# Test function
def test_limits_coherence():
    """
    Verifies that all equipment limits are physically consistent (min <= max).
    """
    for elt in data :
        min_val = elt['limits']['min']
        max_val = elt['limits']['max']
        name_equipment = elt['name']
        # Ensure physical limits are logical to prevent system errors
        assert (min_val <= max_val), f"Incoherence for {name_equipment}"