CREATE TABLE Subsystems (
    ID INTEGER PRIMARY KEY,
    Name TEXT
);


CREATE TABLE Equipments (
    ID INTEGER PRIMARY KEY,
    Name_equipment TEXT,
    subsystem_id INTEGER REFERENCES Subsystems(ID)
);


CREATE TABLE Limits (
    ID INTEGER PRIMARY KEY,
    equipment_id INTEGER REFERENCES Equipments(ID),
    measure_type TEXT,
    min_value REAL,
    max_value REAL
);


CREATE TABLE History (
    ID INTEGER PRIMARY KEY,
    equipment_id INTEGER REFERENCES Equipments(ID),
    old_value REAL,
    new_value REAL,
    change_date TEXT
);
