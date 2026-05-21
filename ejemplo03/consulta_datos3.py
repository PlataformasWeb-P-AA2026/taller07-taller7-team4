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

# Obtener un listado de todas las inscripciones
# que pertenezcan al departamento de
# Ciencias de la Computación

# para la solución se hace uso del método
# join aplicado a query
# se enlaza Inscripcion con Curso y Curso con Departamento

inscripciones = session.query(Inscripcion).join(Curso).join(Departamento).\
        filter(Departamento.nombre == "Ciencias de la Computación").all()

# Se recorre la lista a través de un ciclo
# repetitivo for en python
print("Presentación de Inscripciones - Ciencias de la Computación")
for i in inscripciones:
    # desde cada objeto de la lista
    # inscripcion
    # se puede acceder al estudiante, al curso
    # y desde el curso al instructor
    print("Estudiante : %s" % (i.estudiante.nombre))
    print("Curso      : %s" % (i.curso.titulo))
    print("Profesor   : %s" % (i.curso.instructor.nombre))
    print("---------")