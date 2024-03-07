-- BASE DE DATOS "bigdataStructure"

-- Tabla de Instituciones de Educación Superior (IES)
CREATE TABLE IF NOT EXISTS ies (
    id_institucion SERIAL NOT NULL PRIMARY KEY,
    nombre_institucion VARCHAR(255),
    sector_ies VARCHAR(255),
    departamento_ies VARCHAR(255),
    municipio_ies VARCHAR(255)
);

-- Tabla de Programas Académicos
CREATE TABLE IF NOT EXISTS programas_academicos (
    id_programa SERIAL NOT NULL PRIMARY KEY,
    nombre_programa VARCHAR(255),
    nivel_academico VARCHAR(255),
    departamento_programa VARCHAR(255),
    municipio_programa VARCHAR(255),
    id_institucion INTEGER REFERENCES ies (id_institucion)
);

-- Tabla de Graduados
CREATE TABLE IF NOT EXISTS graduados (
    id_graduado SERIAL NOT NULL PRIMARY KEY,
    sexo VARCHAR(255),
    semestre INT,
    cantidad_graduados INT,
    anio INT,
	id_institucion INTEGER REFERENCES ies (id_institucion),
	id_programa INTEGER REFERENCES programas_academicos (id_programa)
);