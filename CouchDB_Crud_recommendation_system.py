import couchdb

#Integrantes: 
#David Eduardo Quiceno - 2215539
#Jonathan Steven Narváez Navia - 2215983

# Conexión a la base de datos CouchDB
server = couchdb.Server("http://admin:admin@localhost:5984")
db = server["recommendation_system"]

# Operaciones CRUD

# Creación de Usuario, Tutor o Curso

def crear_usuario(usuario):
        db.save(usuario)
        
def crear_tutor(tutor):
        db.save(tutor)
        
def crear_curso(usuario):
        db.save(usuario)
        
# Consultar
        
def curso_por_calificacion_promedio(calificacion_promedio):
    return [doc.value for doc in db.view("cursos/por_calif", key=calificacion_promedio)]

def consultar_usuario_por_nombre(nombre):
    return [doc.value for doc in db.view("usuarios/por_nombre", key=nombre)]

def consultar_tutor_por_nombre(nombre):
    return [doc.value for doc in db.view("tutores/por_nombre", key=nombre)]
        
####################################

# Datos de usuario, tutor y curso
nuevo_usuario = {
    "id": "987654",
    "nombre": "Juan Garcia",
    "carrera": "Ingeniería Informática",
    "semestre": "5",
    "cursos_asistidos": ["2234567", "3208974"],
    "calificaciones_curso": [{"id_curso": "2234567", "calificacion": 4.8}],
    "calificaciones_tutor": [{"id_tutor": "2998373", "calificacion": 4.2}]
}

nuevo_tutor = {
    "id": "2298673",
    "nombre": "Ana Martínez",
    "carrera": "Psicología",
    "semestre": "10",
    "calificacionProm": 4.8,
    "cursos_dictados": [{"id_curso": "2234567"}]
}

nuevo_curso = {
    "id": "2234567",
    "nombre": "Introducción a la Historia del Arte",
    "categoria": "Artes y humanidades",
    "modalidad": "presencial",
    "gratuito": "F",
    "precio": 50,
    "duracion": 30,
    "certificado": "V",
    "calificacion_promedio": 4.5
}

#######################################################################################

# Crear un nuevo usuario, tutor y curso

a = int(input("Crear:\n"
              "1.Usuario"
              "2.Tutor"
              "3.Curso"))

if (a == 1):
    crear_usuario(nuevo_usuario)
elif (a == 2):   
    crear_tutor(nuevo_tutor)
elif (a == 3):    
    crear_curso(nuevo_curso)
else:
    print("Error")

########################################################

# Consultar usuario, tutor y curso por una llave

b = int(input("Consultar por llave:\n"
              "1.Usuario (Por nombre)"
              "2.Tutor (Por nombre)"
              "3.Curso (Por calificación promedio)"))

if (b == 1):
    # Consultar usuario por nombre
    usuarios_nombre = consultar_usuario_por_nombre("Juan")
    print("Usuarios: ")
    for usuario in usuarios_nombre:
        print(usuario)        
elif(b == 2):
    # Consultar tutor por nombre
    tutores_nombre = consultar_tutor_por_nombre("Ana")
    print("Tutores: ")
    for tutor in tutores_nombre:
        print(tutor)        
elif(b == 3):
    # Consultar curso por calificación promedio
    curso_calif= curso_por_calificacion_promedio(4.8)
    print("Cursos: ")
    for curso in curso_calif:
        print(curso)        
else:
    print("Error")