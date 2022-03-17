USE dojos_and_ninjas_schema;

SET SQL_SAFE_UPDATES = 0;
DELETE FROM dojos;

INSERT INTO dojos (name, created_at, updated_at)
VALUES ('little Dojo', NOW(), NOW()),
('Ninja time', NOW(), NOW()),
('Ninjitsu Academy', NOW(), NOW());

SET SQL_SAFE_UPDATES = 0;
DELETE FROM dojos;

DELETE FROM dojos WHERE (id = 46);
DELETE FROM dojos WHERE (id = 47);
DELETE FROM dojos WHERE (id = 48);

INSERT INTO dojos (name, created_at, updated_at)
VALUES ('little Dojo 2', NOW(), NOW()),
('Ninja time 2', NOW(), NOW()),
('Ninjitsu Academy 2', NOW(), NOW());

INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at)
VALUES ('Timmy', 'Turner', 34, 49, NOW(), NOW()),
('Limp', 'Biscut', 52, 49, NOW(), NOW()),
('Harry', 'Potter', 12, 49, NOW(), NOW());

INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at)
VALUES ('Johnny', 'Brown', 24, 50, NOW(), NOW()),
('JRR', 'Tolkein', 55, 50, NOW(), NOW()),
('Austin', 'Powers', 66, 50, NOW(), NOW());

INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at)
VALUES ('Jonah', 'Hill', 24, 51, NOW(), NOW()),
('Marty', 'McFly', 22, 51, NOW(), NOW()),
('Bat', 'Man', 13, 51, NOW(), NOW());

SELECT ninjas.first_name AS ninja FROM ninjas WHERE(dojo_id = 49);
SELECT ninjas.first_name AS ninja FROM ninjas WHERE(dojo_id = 50);
SELECT ninjas.first_name AS ninja FROM ninjas WHERE(dojo_id = 51);

SELECT * FROM dojos;
SELECT * FROM ninjas;
