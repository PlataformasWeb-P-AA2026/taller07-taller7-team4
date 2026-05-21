import csv
from datetime import datetime
from sqlalchemy.orm import sessionmaker

from clases import engine, Departamento, Instructor, Curso, Estudiante, Inscripcion, Tarea, Entrega

Session = sessionmaker(bind=engine)
session = Session()


def parse_fecha(valor):
    """Hubieron  problemas con la fecha por eso decidimos con mi compañero ver los distintos formatos para que funcione"""
    if valor is None or valor.strip() == '':
        return None
    formatos = [
        '%Y-%m-%d %H:%M:%S',
        '%Y-%m-%d',
        '%d/%m/%Y %H:%M:%S',
        '%d/%m/%Y',
    ]
    for fmt in formatos:
        try:
            return datetime.strptime(valor.strip(), fmt)
        except ValueError:
            continue
    raise ValueError(f"Formato de fecha no reconocido: {valor}")


def leer_csv(ruta):
    with open(ruta, encoding='utf-8') as f:
        lector = csv.DictReader(f)
        return list(lector)


# 1. Departamentos
print("Cargando departamentos...")
for fila in leer_csv('01_departamento.csv'):
    session.add(Departamento(
        id=int(fila['id']),
        nombre=fila['nombre']
    ))

# 2. Instructores
print("Cargando instructores...")
for fila in leer_csv('02_instructor.csv'):
    session.add(Instructor(
        id=int(fila['id']),
        nombre=fila['nombre']
    ))

# 3. Cursos
print("Cargando cursos...")
for fila in leer_csv('03_curso.csv'):
    session.add(Curso(
        id=int(fila['id']),
        titulo=fila['titulo'],
        departamento_id=int(fila['departamento_id']),
        instructor_id=int(fila['instructor_id'])
    ))

# 4. Estudiantes
print("Cargando estudiantes...")
for fila in leer_csv('04_estudiante.csv'):
    session.add(Estudiante(
        id=int(fila['id']),
        nombre=fila['nombre']
    ))

# Confirmamos hasta aquí para que las FK de las siguientes tablas
# encuentren los registros padres
session.commit()

# 5. Inscripciones
print("Cargando inscripciones...")
for fila in leer_csv('05_inscripcion.csv'):
    session.add(Inscripcion(
        estudiante_id=int(fila['estudiante_id']),
        curso_id=int(fila['curso_id']),
        fecha_inscripcion=parse_fecha(fila['fecha_inscripcion'])
    ))

# 6. Tareas
print("Cargando tareas...")
for fila in leer_csv('06_tarea.csv'):
    session.add(Tarea(
        id=int(fila['id']),
        curso_id=int(fila['curso_id']),
        titulo=fila['titulo'],
        fecha_entrega=parse_fecha(fila['fecha_entrega'])
    ))

session.commit()

# 7. Entregas
print("Cargando entregas...")
for fila in leer_csv('07_entrega.csv'):
    calificacion = fila.get('calificacion', '').strip()
    session.add(Entrega(
        id=int(fila['id']),
        tarea_id=int(fila['tarea_id']),
        estudiante_id=int(fila['estudiante_id']),
        fecha_envio=parse_fecha(fila['fecha_envio']),
        calificacion=float(calificacion) if calificacion else None
    ))

session.commit()
session.close()

print("¡Base de datos poblada correctamente!")