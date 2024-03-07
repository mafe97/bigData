-- Operaciones completas
-- Todas las tablas
-- DROP VIEW vista_data
CREATE VIEW vista_data AS
SELECT g.id_graduado,
    g.sexo,
    g.semestre,
    g.cantidad_graduados,
    g.anio,
    ies.nombre_institucion,
    ies.id_institucion,
    ies.sector_ies,
    ies.departamento_ies,
    ies.municipio_ies,
    pa.id_programa,
    pa.nivel_academico,
    pa.nombre_programa
   FROM graduados g
     JOIN programas_academicos pa ON g.id_programa = pa.id_programa
     JOIN ies ies ON pa.id_institucion = ies.id_institucion;