# 🛰️ Avionics SRDB: Data Architecture & Visualization

## 📋 About the Project
This project simulates a **Satellite Reference Database (SRDB)** workflow, a critical component in aerospace engineering. It demonstrates a full-stack data engineering pipeline: from raw data generation to end-user visualization.

**Goal :** Ensure data consistency and accessibility for avionics subsystems (Thermal, Power, Propulsion, etc.).

## 🏗️ Architecture
The project follows a standard **ETL (Extract, Transform, Load)** pattern :

1.  **Data Generation :** Creation of mock satellite equipment data (`generator.py`).
2.  **ETL Pipeline :** Parsing JSON, validating integrity, and loading into a relational database (`main.py` -> SQLite).
3.  **Quality Assurance :** Automated unit testing to ensure physical constraints (e.g., Min < Max) (`test_consistency.py`).
4.  **Visualization :** An interactive dashboard for engineers to filter and analyze equipment limits (`dashboard.py`).

## 🛠️ Tech Stack
* **Language :** Python 3.11.6
* **Database :** SQLite
* **Data Analysis :** Pandas
* **Web App :** Streamlit
* **Testing :** Pytest

## 🚀 How to Run

### 1. Installation
Clone the repository and install the dependencies :
```bash
git clone [https://github.com/TonPseudo/Projet_Airbus_SRDB.git](https://github.com/TonPseudo/Projet_Airbus_SRDB.git)
pip install pandas streamlit pytest
```

### 2. Generate & Load Data
Initialize the database and generate fresh mock data :
```bash
python generator.py  # Creates massive_data.json
python main.py       # Loads data into avionics.db
```

### 3. Run Tests
Verify data consistency (physical limits check) :
```bash
pytest
```

### 4. Launch Dashboard
Start the interactive web interface :
```bash
streamlit run dashboard.py
```

## 📂 Project Structure
* **dashboard.py** : Streamlit application source code.

* **main.py** : ETL script for database ingestion.

* **generator.py** : Script to generate random mock data.

* **test_consistency.py** : Unit tests for data validation.

* **schema.sql** : SQL script defining the database architecture.

* **avionics.db** : The SQLite database file.