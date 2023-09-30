from os import system
import time
import conexion as conn
db=conn.DB()
def create():
    cedula = 00
    while True:
        try:
            cedula = int(input("Ingrese la Cedula:"))
        except ValueError:
            print("Debes escribir un número.")
        break
    name=str(input("Ingrese el Nombre:"))
    primer_apellido=str(input("Ingrese el Primer Apellido:"))
    segundo_apellido=str(input("Ingrese el Segundo Apellido:"))
    email=str(input("Ingrese el Email: "))
    print("estoy aqui")
    
    
    print("estoy dentro del if")
    sql = "INSERT INTO sistema(cedula,name,primer_apellido, segundo_apellido, email) VALUES(?,?,?,?,?)"
    parametros=(cedula,name,primer_apellido,segundo_apellido,email)
    db.ejecutar_consulta(sql,parametros)
    print("Resgistros ingresados con exito")
        

def read ():
    sql="SELECT * FROM sistema"
    result = db.ejecutar_consulta(sql)
    for data in result:
        print("""
        ID:     {}
        NOMBRE: {}
        PRIMER APELLIDO: {}
        SEGUNDO APELLIDO: {}
        EMAIL:  {}
        """. format(data[0],data[1],data[2],data[3],data[4]))
def update():
    id = int(input("Seleccione el Id a actualizar: "))
    if(id != 0):
        name = str(input("Ingrese el nuevo nombre:"))
        primer_apellido = str (input("Ingrese el nuevo primer apellido:"))
        segundo_apellido = str (input("Ingrese el nuevo segundo apellido:"))
        email = str (input("Ingrese el nuevo email:"))
        if(len(name)>0 and len (primer_apellido)>0 and len (segundo_apellido)>0 and len (email)>0) :
            sql="UPDATE sistema SET name=?, primer_apellido=?, segundo_apellido=?, email=? WHERE id=?"
            parametros = (name,email,id)
            db.ejecutar_consulta(sql,parametros)
            print("Actualizado con exito")
        else:
            print ("Actualizado con exito")
def delete ():
    id = int(input("Seleccione el Id a Eliminar"))
    if(id != 0):
        sql = "DElETE FROM sistema WHERE id=?"
        parametros= (id,)
        db.ejecutar_consulta(sql,parametros)
    else:
        print ("Digite un id valido")
def search():
    nombre=str(input("Digite el nombre a consultar: "))
    if(len(nombre)>0):
        sql = "SELECT * FROM sistema WHERE name LIKE?"
        parametros = ('%{}%'.format(nombre),)
        result = db.ejecutar_consulta(sql,parametros)
        for data in result:
            print("""
            ID:     {}
            NOMBRE: {}
            PRIMER APELLIDO: {}
            SEGUNDO APELLIDO: {}
            EMAIL:  {}
            """. format(data[0],data[1],data[2],data[3],data[4]))
            
 
        
while True:
    print("*******************************")
    print("\tCRUD CON SQLITE")
    print("************************")
    print("\t[1] Insertar un registro.")
    print("\t[2] Consultar los registro.")
    print("\t[3] Actualizar registro.")
    print("\t[4] Eliminar un registro.")
    print("\t[5] Buscar registro.")
    print("\t[6] Salir del sistema.")
    print("*******************************")
    try:
        opcion = int(input("Seleccione una opcion: "))
        if (opcion == 1):
            create()
            system("clear")
        elif (opcion == 2):
            read()
            time.sleep(1)
            system("clear")
        elif (opcion == 3):
            update ()
            time.sleep(1)
            system("clear")
        elif (opcion == 4):
            delete ()
            time.sleep(1)
            system("clear")
        elif (opcion == 5):
            search ()
            time.sleep(1)
            system("clear")
        elif (opcion == 6):
            time.sleep(1)
            system("clear")
            break
         
    except:
        print("Seleccione una opcion correcta")
        system("clear")
