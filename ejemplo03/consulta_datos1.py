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

# Obtener todos los registros de
# la entidad Entrega
entregas = session.query(Entrega).all()

# Se recorre la lista a través de un ciclo
# repetitivo for en python
print("Presentación de Entregas")
for e in entregas:
    # desde cada objeto de la lista
    # entrega
    # se puede acceder al estudiante, a la tarea
    # y desde la tarea al curso y al instructor
    # como lo definimos en las relaciones
    print("Estudiante : %s" % (e.estudiante.nombre))
    print("Titulo     : %s" % (e.tarea.titulo))
    print("Profesor   : %s" % (e.tarea.curso.instructor.nombre))
    print("---------")