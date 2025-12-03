# 🛰️ Avionics SRDB : Data Architecture & Visualization

## 📋 About the Project
This project simulates a **Satellite Reference Database (SRDB)** workflow, a critical component in aerospace engineering. It demonstrates a full-stack data engineering pipeline : from raw data generation to end-user visualization, including a robust audit system.

**Goal :** Ensure data consistency, accessibility, and traceability for avionics subsystems (Thermal, Power, Propulsion, etc.).

## 🌟 Key Features
* **ETL Pipeline :** Automates the ingestion of raw JSON data into a structured SQL architecture.
* **Data Consistency :** Automated unit testing (`pytest`) guarantees physical constraints (e.g., Min < Max).
* **Interactive Dashboard :** A Streamlit web app for engineers to filter and analyze equipment.
* **Time Machine (Audit Trail) :** A specialized `History` table tracks every modification (Old Value vs New Value, Timestamp) to ensure full traceability of specifications.
* **Full Automation :** A master script (`run_all.py`) orchestrates the entire lifecycle, from database cleanup to dashboard launch.

## 🏗️ Architecture
The project follows a standard **ETL (Extract, Transform, Load)** pattern:

1.  **Data Generation :** Creation of mock satellite equipment data (`generator.py`).
2.  **Ingestion :** Parsing and loading data into SQLite (`main.py`).
3.  **Validation :** Quality gates using automated tests (`test_consistency.py`).
4.  **Management :** Admin tools to update limits and log changes (`update_limits.py`).
5.  **Visualization :** User interface for data exploration (`dashboard.py`).

## 🛠️ Tech Stack
* **Language :** Python 3.13.9
* **Database :** SQLite
* **Data Analysis :** Pandas
* **Web App :** Streamlit
* **Testing :** Pytest
* **Orchestration :** Python `subprocess`

## 🚀 How to Run

### 1. Installation
Clone the repository and install dependencies :
```bash
git clone [https://github.com/TonPseudo/Projet_Airbus_SRDB.git](https://github.com/TonPseudo/Projet_Airbus_SRDB.git)
pip install -r requirements.txt
```

### 2. Launch (Automated Mode) ⚡
The easiest way to run the project. This script cleans the environment, rebuilds the database, runs tests, and launches the dashboard.
```bash
python run_all.py
```

### 3. Manual Mode (Dev)
If you prefer running steps individually :
```bash
python generator.py       # Generate mock data
python main.py            # Load data into DB
pytest                    # Run quality checks
streamlit run dashboard.py # Start the UI
```

### 📂 Project Structure
* `run_all.py` : Master script that orchestrates the entire workflow.

* `dashboard.py` : Streamlit application source code.

* `main.py` : ETL script for database ingestion.

* `generator.py` : Script to generate random mock data.

* `update_limits.py` : Module handling data updates and history logging.

* `test_consistency.py` : Unit tests for data validation.

* `schema.sql` : SQL script defining the DB architecture (Equipments, Subsystems, Limits, History).

* `requirements.txt` : List of external Python libraries.