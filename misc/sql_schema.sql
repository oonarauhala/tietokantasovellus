DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS dinosaurs CASCADE;
DROP TABLE IF EXISTS feeding_times CASCADE;
DROP TABLE IF EXISTS areas;

CREATE TABLE areas (id SERIAL PRIMARY KEY, name TEXT);
CREATE TABLE dinosaurs (id SERIAL PRIMARY KEY, name TEXT, description TEXT, location INTEGER REFERENCES areas(id));
CREATE TABLE feeding_times (id SERIAL PRIMARY KEY, date DATE, available INTEGER, time TIME, dinosaur INTEGER REFERENCES dinosaurs(id));
CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT UNIQUE, admin BOOLEAN, password text, reserved_time INTEGER REFERENCES feeding_times(id)); 

INSERT INTO areas (name) VALUES ('Welcome'); -- 1
INSERT INTO areas (name) VALUES ('Field');   -- 2
INSERT INTO areas (name) VALUES ('Aquatic'); -- 3
INSERT INTO areas (name) VALUES ('Jungle');  -- 4

INSERT INTO dinosaurs (name, description, location) VALUES ('Velociraptor', 'A small predator with deadly claws', 4);
INSERT INTO dinosaurs (name, description, location) VALUES ('Tyrannosaurus', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', 4);
INSERT INTO dinosaurs (name, description, location) VALUES ('Spinosaurus', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', 3);
INSERT INTO dinosaurs (name, description, location) VALUES ('Hesperornis', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', 3);
INSERT INTO dinosaurs (name, description, location) VALUES ('Stegosaurus', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', 2);
INSERT INTO dinosaurs (name, description, location) VALUES ('Brachiosaurus', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', 2);
INSERT INTO dinosaurs (name, description, location) VALUES ('Nemicolopterus', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', 1);

INSERT INTO feeding_times(date, time, available, dinosaur) VALUES ('2021-10-22', '18:00', 10, 1);
INSERT INTO feeding_times(date, time, available, dinosaur) VALUES ('2021-10-22', '18:00', 10, 2);
INSERT INTO feeding_times(date, time, available, dinosaur) VALUES ('2021-10-22', '18:00', 10, 3);
INSERT INTO feeding_times(date, time, available, dinosaur) VALUES ('2021-10-22', '18:00', 10, 4);
INSERT INTO feeding_times(date, time, available, dinosaur) VALUES ('2021-10-22', '18:00', 10, 5);
INSERT INTO feeding_times(date, time, available, dinosaur) VALUES ('2021-10-22', '18:00', 10, 7);
INSERT INTO feeding_times(date, time, available, dinosaur) VALUES ('2021-10-22', '20:00', 10, 7);