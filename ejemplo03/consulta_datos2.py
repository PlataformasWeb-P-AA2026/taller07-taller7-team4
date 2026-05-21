from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

# se importa la clase(s) del 
# archivo clases
from clases import Departamento, Instructor, Curso, Estudiante, Inscripcion, Tarea, Entrega

# se importa información del archivo config
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Obtener un listado de todos los registros
# de la tabla Curso, que tengan un instructor
# con el nombre que contenga la cadena "Zam"

# para la solución se hace uso del método
# join aplicado a query

cursos = session.query(Curso).join(Instructor).\
        filter(Instructor.nombre.like("%Zam%")).all()

print("Consulta 1 ")
for c in cursos:
    print(c)

# Obtener un listado de todos los registros
# de la tabla Curso e Instructor, que tengan
# un instructor con el nombre que contenga
# la cadena "Zam"

# para la solución se hace uso del método
# join aplicado a query
# en el query se ubican las dos entidades involucradas

registros = session.query(Curso, Instructor).join(Instructor).\
        filter(Instructor.nombre.like("%Zam%")).all()

print("Consulta 2 ")
for registro in registros:
    # el registro contiene
    # dos valores en una tupla
    # posición 0 el curso
    # posición 1 el instructor
    # que cumplen con la condición
    print(registro[0]) # El curso
    print(registro[1]) # El instructor