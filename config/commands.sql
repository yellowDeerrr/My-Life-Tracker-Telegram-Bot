CREATE TABLE params (
    id SERIAL PRIMARY KEY,
    health INTEGER,
    strength INTEGER,
    intelligence INTEGER,
    wisdom INTEGER,
    charisma INTEGER,
    confidence INTEGER,
    self_discipline INTEGER,
    skills INTEGER,
    happiness INTEGER,
    recovery INTEGER
);

-- Insert the initial data
INSERT INTO params (health, strength, intelligence, wisdom, charisma, confidence, self_discipline, skills, happiness, recovery)
VALUES (0, 0, 0, 0, 0, 0, 0, 0, 0, 0);



CREATE TABLE levels (
    id SERIAL PRIMARY KEY,
    health INTEGER,
    strength INTEGER,
    intelligence INTEGER,
    wisdom INTEGER,
    charisma INTEGER,
    confidence INTEGER,
    self_discipline INTEGER,
    skills INTEGER,
    happiness INTEGER,
    recovery INTEGER
);

-- Insert the initial data
INSERT INTO levels (health, strength, intelligence, wisdom, charisma, confidence, self_discipline, skills, happiness, recovery)
VALUES (0, 0, 0, 0, 0, 0, 0, 0, 0, 0);



CREATE TABLE history (
    id SERIAL PRIMARY KEY,
    type TEXT,
    param TEXT,
    amount INTEGER,
    description TEXT,
    date CURRENT_TIME TIMESTAMP,
    current_param_value INTEGER
);