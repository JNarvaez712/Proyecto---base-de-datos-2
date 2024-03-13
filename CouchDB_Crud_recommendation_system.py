import couchdb

conn_string = "http://admin:admin@localhost:5984"
server = couchdb.Server(conn_string)
db_name = "recommendation_system"

if db_name in server:
    print("Conectado con la BD")
    db = server[db_name]
else:
    print("---Creando base de datos")
    db = server.create(db_name)

    #**** CRUD ****
#read: select all
id_doc = input("Ingrese el id del documento:") 
doc = db[id_doc]
print(doc)

### Funciones del crud ###
def Create(collection, data):
    doc_id, doc_rev = db.save(data)

def Update(doc_id, data):
    doc = db[doc_id]
    doc.update(data)
    db.save(doc)

def SelectAll(collection):
    docs = [doc for doc in db.view(f"{collection}/all")] #Sintaxis de consulta de couchDB

def Select_By_Criteria(collection, criteria):
    docs = [doc for doc in db.view(f"{collection}/by_criteria", key=criteria)]

def Delete(doc_id):
    doc = db[doc_id]
    db.delete(doc)

def Delete_Value(key, value):
    doc_idv = db.get()
    

guitarra = {
    "id":"G001",
    "Nombre": "Guitarra acustica",
    "Categoria": "Musica",
    "descripcion": "guitarra acustica basica",
    "duracion": 40,
    "precio": 0.0,
    "remoto":False
}

pintura1 = {
    "id":"P001",
    "Nombre": "Pintura al óleo",
    "Categoria": "Arte",
    "descripcion": "Pintura al óleo",
    "duracion": 30,
    "precio": 0.0,
    "remoto":False
}

pintura2 = {
    "id":"P002",
    "Nombre": "Pintura acrilica",
    "Categoria": "Arte",
    "descripcion": "Pintura acrilica",
    "duracion": 50,
    "precio": 0.0,
    "remoto":False
}

Create("cursos", guitarra)
Create("cursos", pintura1)
Create("cursos", pintura2)

### Revisar update ###
guitarra["duracion"] = 45
Update(guitarra)

listar_cursos = SelectAll("cursos")
for c in listar_cursos:
    print(c)

criterios = "Arte"
cursos_pintura = Select_By_Criteria("cursos",criterios)