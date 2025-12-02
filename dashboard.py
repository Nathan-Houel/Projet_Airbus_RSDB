"""
Streamlit Dashboard for Avionics Data Visualization.

This application connects to the SQLite database 'avionics.db' and provides 
an interactive interface to explore equipment data, joined with their 
subsystems and operational limits.
"""

import streamlit as st
import pandas as pd
import sqlite3
from generator import systems


def load_data(sys_name):
    """
    Fetches equipment data from the database for a specific subsystem.
    
    Performs a double JOIN to retrieve:
    - Equipment name (from Equipments table)
    - Subsystem name (from Subsystems table)
    - Limits info (Type, Min, Max from Limits table)
    """

    conn = sqlite3.connect('avionics.db')

    # We use a parameterized query (?) to prevent SQL injection
    query = """
        SELECT Equipments.Name_equipment, Subsystems.Name, 
               Limits.measure_type, Limits.min_value, Limits.max_value 
        FROM Equipments 
        JOIN Subsystems ON Equipments.subsystem_id = Subsystems.id 
        JOIN Limits ON Equipments.id = Limits.equipment_id 
        WHERE Subsystems.Name = ?
    """
    data = pd.read_sql(query, conn, params=(sys_name,))
    conn.close()
    return data


# Sidebar configuration
selected_system = st.sidebar.selectbox("Choose a system", systems)

st.sidebar.markdown("### Display Options")
show_type = st.sidebar.checkbox("Measure type")
show_min = st.sidebar.checkbox("Min value")
show_max = st.sidebar.checkbox("Max value")

st.title(f"🔍 Analysis : {selected_system} Subsystem")

df = load_data(selected_system)

# Dynamic filtering
if show_type == False :
    df = df.drop(columns=['measure_type'])
if show_min == False :
    df = df.drop(columns=['min_value'])
if show_max == False :
    df = df.drop(columns=['max_value'])

# Display dataframe
st.dataframe(df)