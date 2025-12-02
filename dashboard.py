import streamlit as st
import pandas as pd
import sqlite3
from generator import systems

def load_data(sys_name):
    conn = sqlite3.connect('avionics.db')
    data = pd.read_sql(f"SELECT Equipments.Name_equipment, Subsystems.Name, Limits.measure_type, Limits.min_value, Limits.max_value \
                       FROM Equipments JOIN Subsystems ON Equipments.subsystem_id = Subsystems.id \
                       Join Limits ON Equipments.id = Limits.equipment_id \
                       WHERE Subsystems.Name = ?", conn, params=(sys_name,))
    return data

st.title("Equipments's table")
selected_system = st.sidebar.selectbox("Choose a system", systems)
df = load_data(selected_system)
st.dataframe(df)