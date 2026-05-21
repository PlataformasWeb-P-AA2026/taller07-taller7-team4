from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()


archivo = open("data/datos_clubs.txt", "r", encoding="utf-8")

for linea in archivo:
    datos = linea.strip().split(";")

    nombre = datos[0]
    deporte = datos[1]
    fundacion = int(datos[2])

    club_existe = session.query(Club).filter_by(nombre=nombre).first()
    
    if not club_existe:
        club = Club(
            nombre=nombre,
            deporte=deporte,
            fundacion=fundacion
        )
        session.add(club)

archivo.close()
session.commit()

archivo = open("data/datos_jugadores.txt", "r", encoding="utf-8")

for linea in archivo:
    datos = linea.strip().split(";")

    nombre_club = datos[0]
    posicion = datos[1]
    dorsal = int(datos[2])
    nombre = datos[3]

    club = session.query(Club).filter_by(nombre=nombre_club).first()

    if club: 
        jugador = Jugador(
            nombre=nombre,
            dorsal=dorsal,
            posicion=posicion,
            club=club
        )
        session.add(jugador)

archivo.close()
session.commit()

