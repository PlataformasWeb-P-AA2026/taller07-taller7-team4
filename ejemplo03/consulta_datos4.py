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
# la entidad Curso
cursos = session.query(Curso).all()

# Se recorre la lista a través de un ciclo
# repetitivo for en python
print("Presentación de Cursos y sus tareas")
for c in cursos:
    print("%s" % (c))
    # desde cada objeto de la lista
    # de tipo Curso
    # se puede acceder
    # a las tareas
    tareas = c.tareas # es una secuencia; es una lista
    # [objTarea1, objTarea2, objTarea3, ..., objTareaN]
    for t in tareas:
        print(t.titulo)

    print("---------")