-- Script de datos iniciales para pruebas
USE GestionDeEstudiantes;

-- Insertar administrador
INSERT INTO administradores (nombre, correo, contraseña) 
VALUES ('Admin Sistema', 'admin@example.com', 'pbkdf2:sha256:600000$...');

-- Insertar profesores
INSERT INTO profesores (nombre, correo, contraseña) 
VALUES 
('Prof. Carlos López', 'carlos@example.com', 'pbkdf2:sha256:600000$...'),
('Prof. María González', 'maria@example.com', 'pbkdf2:sha256:600000$...'),
('Prof. Juan Pérez', 'juan@example.com', 'pbkdf2:sha256:600000$...');

-- Insertar estudiantes
INSERT INTO estudiantes (nombre, correo, contraseña, puede_inscribirse) 
VALUES 
('Juan Diego Delgado Ramírez', 'juan.delgado@example.com', 'pbkdf2:sha256:600000$...', TRUE),
('María Rodríguez García', 'maria.rodriguez@example.com', 'pbkdf2:sha256:600000$...', TRUE),
('Carlos Martínez López', 'carlos.martinez@example.com', 'pbkdf2:sha256:600000$...', TRUE);

-- Insertar padres
INSERT INTO padres (nombre, correo, contraseña) 
VALUES 
('Padre Juan Delgado', 'padre.delgado@example.com', 'pbkdf2:sha256:600000$...'),
('Madre María Delgado', 'madre.delgado@example.com', 'pbkdf2:sha256:600000$...');

-- Asignar padres a estudiantes
INSERT INTO padres_estudiantes (id_padre, id_estudiante) 
VALUES 
(1, 1), (2, 1);

-- Insertar materias
INSERT INTO materias (nombre, descripcion) 
VALUES 
('Matemáticas', 'Álgebra, Geometría y Cálculo'),
('Física', 'Mecánica, Termodinámica y Óptica'),
('Química', 'Química General e Inorgánica'),
('Literatura', 'Análisis y Composición de Textos'),
('Historia', 'Historia Universal y Nacional');

-- Asignar profesores a materias
INSERT INTO asignaciones (id_profesor, id_materia) 
VALUES 
(1, 1), (2, 2), (3, 3), (1, 4), (2, 5);

-- Inscribir estudiantes en materias
INSERT INTO inscripciones (id_estudiante, id_materia) 
VALUES 
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
(2, 1), (2, 2), (2, 3),
(3, 1), (3, 4), (3, 5);

-- Insertar notas
INSERT INTO notas (id_estudiante, id_profesor, id_materia, nota, comentario) 
VALUES 
(1, 1, 1, 8.5, 'Excelente trabajo'),
(1, 2, 2, 8.0, 'Buen desempeño'),
(1, 3, 3, 7.5, 'Aceptable'),
(2, 1, 1, 7.8, 'Muy bien'),
(2, 2, 2, 8.2, 'Excelente'),
(3, 1, 1, 9.0, 'Sobresaliente');

-- Insertar notificaciones
INSERT INTO notificaciones (id_estudiante, titulo, mensaje) 
VALUES 
(1, 'Nueva tarea', 'Se ha publicado una nueva tarea en Matemáticas'),
(1, 'Calificación disponible', 'Tu calificación de Física está disponible'),
(2, 'Aviso importante', 'Recuerda enviar tus trabajos antes de la fecha límite');

-- Insertar tareas
INSERT INTO tareas (id_estudiante, titulo, descripcion, fecha_entrega, estado) 
VALUES 
(1, 'Tarea 1: Ecuaciones', 'Resolver 10 ecuaciones cuadráticas', DATE_ADD(NOW(), INTERVAL 7 DAY), 'pendiente'),
(1, 'Tarea 2: Redacción', 'Escribir un ensayo sobre un tema histórico', DATE_ADD(NOW(), INTERVAL 14 DAY), 'pendiente'),
(2, 'Proyecto final', 'Proyecto integrativo de ciencias', DATE_ADD(NOW(), INTERVAL 30 DAY), 'pendiente');

-- Insertar horarios
INSERT INTO horarios (id_estudiante, id_profesor, dia_semana, hora_inicio, hora_fin, id_materia) 
VALUES 
(1, 1, 'Lunes', '08:00', '09:30', 1),
(1, 2, 'Martes', '10:00', '11:30', 2),
(1, 3, 'Miércoles', '08:00', '09:30', 3),
(1, 1, 'Jueves', '10:00', '11:30', 4),
(1, 2, 'Viernes', '08:00', '09:30', 5);
