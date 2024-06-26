import os
import datetime
from datetime import datetime
import pyfiglet
os.system("cls")

productos=[]
ventas = []

def buscar_id(id): 
    for a in productos:
        if a[0]==id:
            return a
    return -1

def validar_longitud_id(id):
    while len(id) != 4:
        print("\n Error, el ID del producto debe tener exactamente 4 caracteres.")
        id = input("Ingrese el ID del producto (debe tener 4 caracteres): ")
    return id 

def validar_id_unica(id):
    for producto in productos:
        if producto[0] == id:
            return False  
    return True

def validar_si_no(mensaje):                                
    while True:
        respuesta = input(mensaje).lower()
        if respuesta == "si" or respuesta == "no":
            return respuesta
        else:
            print("\n Error, la respuesta debe ser 'si' o 'no.")
            os.system("pause")

def obtener_fecha_actual(): 
    return datetime.now().strftime("%d-%m-%Y")

def buscar_fecha():
    while True:
        fechas_encontradas = []
        fecha = input("Ingrese la fecha (dd-mm-yyyy): ")
        if len(fecha) != 10 or fecha[2] != '-' or fecha[5] != '-':
            print("\nError, la fecha debe tener el formato dd-mm-yyyy.")
            os.system("pause")
            os.system("cls")
            continue
        validacion_fecha = validar_fecha_1(fecha)
        if validacion_fecha == 1:
            for venta in ventas:
                if venta[1] == fecha:
                    fechas_encontradas.append(venta)
        else:
            return -1
        if len(fechas_encontradas) != 0:
            return fechas_encontradas
        else:
            print("\nNo se encontraron ventas para la fecha ingresada.")
            os.system("pause")
            os.system("cls")
            return -1

def validar_fecha(venta):
    fecha=venta[1]
    if len(fecha)==10:
        if fecha[2] == "-" and fecha[5] == "-" :
            dia=int(fecha[0:2])
            mes=int(fecha[3:5])
            año=int(fecha[6:10])
            
            if año <= 2000:
                os.system("cls")
                print("ERROR\nAño ingresado fuera de parametros")
                os.system("pause")
                os.system("cls")
                return -1
            if mes < 1 or mes > 12:
                os.system("cls")
                print("ERROR\nMes Ingresado fuera de los parametros")
                os.system("pause")
                os.system("cls")
                return -1
            if mes == 2:  
                if bisiesto(año):
                    dias_febrero = 29
                else:
                    dias_febrero = 28
                if dia < 1 or dia > dias_febrero:
                    os.system("cls")
                    print("ERROR\nDía Ingresado fuera de los parametros")
                    os.system("pause")
                    os.system("cls")
                    return -1
            elif mes in [4, 6, 9, 11]:  
                if dia < 1 or dia > 30:
                    os.system("cls")
                    print("ERROR\nDía Ingresado fuera de los parametros")
                    os.system("pause")
                    os.system("cls")
                    return -1
            else:  
                if dia < 1 or dia > 31:
                    os.system("cls")
                    print("ERROR\nDía Ingresado fuera de los parametros")
                    os.system("pause")
                    os.system("cls")
                    return -1
            return 1
        return -1
    else:
        os.system("cls")
        print("ERROR\nFecha Ingresada con formato equivocado Formato(dd-mm-aaaa)")
        os.system("pause")
        os.system("cls")
        return -1

def validar_fecha_1(fecha_1):
    fecha=fecha_1
    if len(fecha)==10:
        if fecha[2] == "-" and fecha[5] == "-" :
            dia=int(fecha[0:2])
            mes=int(fecha[3:5])
            año=int(fecha[6:10])
            
            if año <= 2000:
                os.system("cls")
                print("ERROR\nAño ingresado fuera de parametros")
                os.system("pause")
                os.system("cls")
                return -1
            if mes < 1 or mes > 12:
                os.system("cls")
                print("ERROR\nMes Ingresado fuera de los parametros")
                os.system("pause")
                os.system("cls")
                return -1
            if mes == 2:  
                if bisiesto(año):
                    dias_febrero = 29
                else:
                    dias_febrero = 28
                if dia < 1 or dia > dias_febrero:
                    os.system("cls")
                    print("ERROR\nDía Ingresado fuera de los parametros")
                    os.system("pause")
                    os.system("cls")
                    return -1
            elif mes in [4, 6, 9, 11]:  
                if dia < 1 or dia > 30:
                    os.system("cls")
                    print("ERROR\nDía Ingresado fuera de los parametros")
                    os.system("pause")
                    os.system("cls")
                    return -1
            else:  
                if dia < 1 or dia > 31:
                    os.system("cls")
                    print("ERROR\nDía Ingresado fuera de los parametros")
                    os.system("pause")
                    os.system("cls")
                    return -1
            return 1
        else:
            return -1
    else:
        os.system("cls")
        print("ERROR\nFecha Ingresada con formato equivocado (dd-mm-aaaa)")
        os.system("pause")
        os.system("cls")
        return -1

def bisiesto(año):
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

def agregar_producto():
    print("\nAgregar Producto\n")
    while True:
        id = input("\n Ingrese el ID del producto (4 caracteres): ")
        id = validar_longitud_id(id)
        id = id.ljust(4)  
        if validar_id_unica(id):
            nombre = input("Ingrese el Nombre del Arma: ").strip()
            if len(nombre) == 0:
                print("\nError, el 'nombre' no puede estar vacío.")
                continue
            fabricante = input("Ingrese el Fabricante: ").strip()
            if len(fabricante) == 0:
                print("\nError, el 'fabricante' no puede estar vacío.")
                continue
            tipo = input("Ingrese el Tipo de Arma: ").strip()
            if len(tipo) == 0:
                print("\nError, el 'tipo de arma' no puede estar vacío.")
                continue
            calibre = input("Ingrese el Calibre: ").strip()
            if len(calibre) == 0:
                print("\nError, el 'calibre' no puede estar vacío.")
                continue
            try:
                stock = int(input("Ingrese el stock disponible: ").strip())
                if stock <= 0:
                    print("\nError, el 'stock' debe ser mayor o igual a 0.")
                    continue
            except ValueError:
                print("\nError, el 'stock' debe ser un número entero.")
                continue
            try:
                precio = float(input("Ingrese el precio: ").strip())
                if precio <= 0:
                    print("\nError, el 'precio' debe ser mayor o igual a 0.")
                    continue
            except ValueError:
                print("\nError, el precio debe ser un número.")
                continue
            lista_nueva = [id, nombre.ljust(15), fabricante.ljust(20), tipo.ljust(22), calibre.ljust(12), stock, precio]
            productos.append(lista_nueva)
            print("\nProducto agregado a la lista de productos.")
            os.system("pause")
            return
        else:
            print("\nError, la ID ingresada ya existe en el sistema.")
            os.system("pause")
            continue

def buscar_producto():
    os.system("cls")
    print("\n Buscar Producto\n")
    id = input("Ingrese el ID del producto: ")
    lista = buscar_id(id)
    if lista != -1:
        print("\n Producto encontrado: ")
        print("\n", lista)
    else:
        print("\n Error, la ID ingresada no existe...")
    os.system("pause")        
      
def modificar_producto():
    print("\n Modificar Producto\n")
    while True:
        id = input("Ingrese el ID del producto a modificar: ")
        id = validar_longitud_id(id)
        id = id.ljust(4) 
        producto = buscar_id(id)
        if producto != -1:
            print("\n Producto encontrado: ", producto)
            print("\n Ingrese los nuevos datos:")
            nuevo_nombre = input("Ingrese el nuevo nombre: ").strip()
            if len(nuevo_nombre) == 0:
                print("\n El nuevo 'nombre' no puede estar vacío.")
                continue
            nuevo_fabricante = input("Ingrese el nuevo fabricante: ").strip()
            if len(nuevo_fabricante) == 0:
                print("\n El nuevo 'fabricante' no puede estar vacío.")
                continue
            nuevo_tipo = input("Ingrese el nuevo tipo de arma: ").strip()
            if len(nuevo_tipo) == 0:
                print("\n El nuevo 'tipo de arna' no puede estar vacío.")
                continue
            nuevo_calibre = input("Ingrese el nuevo calibre: ").strip()
            if len(nuevo_calibre) == 0:
                print("\n El nuevo 'calibre' no puede estar vacío.")
                continue
            nuevo_stock = producto[5]
            nuevo_precio = producto[6]
            stock_input = input("Ingrese el nuevo 'stock' disponible: ").strip()
            if stock_input:
                try:
                    nuevo_stock = int(stock_input)
                    if nuevo_stock <= 0:
                        print("\n Error, el 'stock' no puede ser negativo.")
                        continue
                    if len(nuevo_stock) == 0:
                        print("\n El nuevo 'stock' no puede estar vacío.")
                        continue
                except ValueError:
                    print("\n Error, el 'stock' debe ser un número entero.")
                    continue
            precio_input = input("Ingrese el nuevo 'precio' de venta: ").strip()
            if precio_input:
                try:
                    nuevo_precio = int(precio_input)
                    if nuevo_precio <= 0:
                        print("\n Error, el precio no puede ser negativo.")
                        continue
                    if len(nuevo_precio) == 0:
                        print("\n El nuevo precio no puede estar vacío.")
                        continue
                except ValueError:
                    print("\n Error, el precio debe ser un número entero.")
                    continue
            if nuevo_nombre:
                producto[1] = nuevo_nombre[:15].ljust(15)
            if nuevo_fabricante:
                producto[2] = nuevo_fabricante[:20].ljust(20)
            if nuevo_tipo:
                producto[3] = nuevo_tipo[:22].ljust(22)
            if nuevo_calibre:
                producto[4] = nuevo_calibre[:12].ljust(12)
            producto[5] = nuevo_stock
            producto[6] = nuevo_precio
            print("\n Datos modificados con éxito.")
            os.system("pause")
            break
        else:
            print("Error, el ID de producto no existe.")
            os.system("pause")
            break

def eliminar_producto():
    os.system("cls")
    print("\n Eliminar Producto\n")
    id = input("Ingrese el ID del producto a eliminar: ")
    lista = buscar_id(id)
    if lista != -1:
        productos.remove(lista)
        print("\n Producto eliminado con éxito.")
    else:
        print("Error, el ID de producto no existe.")
    os.system("pause")

def listar_productos():
    os.system("cls")
    if len(productos) != 0:
        print("\n Lista de armas\n")
        for i in productos:
            print(i[0], " ", i[1], " ", i[2], " ", i[3], " ", i[4], " ", i[5], " ", i[6], " ", )
        os.system("pause")
    else:
        print("Error, Lista no cargada, no hay datos para mostrar.")
        os.system("pause")

def cargar_datos_productos():
    global productos
    if len(productos) != 0:
        print("\n Error al cargar los datos, las listas ya contienen datos.")
        input("Presiona Enter para continuar...")
        os.system("pause")
        return
    try:
        with open("Productos.txt", "r") as f:
            for line in f:
                linea = line.strip().replace("_", " ").split(',')
                if len(linea) == 7:
                    id_producto = linea[0][:4].ljust(4) 
                    nombre = linea[1][:15].ljust(15)
                    fabricante = linea[2][:20].ljust(20)  
                    tipo = linea[3][:22].ljust(22) 
                    calibre = linea[4][:12].ljust(12) 
                    stock = int(linea[5]) 
                    precio = int(linea[6]) 
                    
                    productos.append([id_producto, nombre, fabricante, tipo, calibre, stock, precio])
                else:
                    print(f"Error: línea incorrecta en el archivo: {line}")
                    print("Se esperaban 7 campos separados por comas.")
    except FileNotFoundError:
        print("\n Error, El archivo Productos.txt no se encontró.")
    except ValueError as e:
        print(f"Error al procesar los datos: {str(e)}")

def cargar_datos_ventas():
    global ventas
    if len(ventas) != 0:
        print("\nError al cargar los datos, las listas ya contienen datos.")
        return   
    try:
        with open("Ventas.txt", "r") as f:
            for line in f:
                line = line.strip() 
                if line: 
                    datos = line.split(',')
                    if len(datos) == 5:
                        folio = int(datos[0])
                        fecha = datos[1]
                        id_producto = datos[2]
                        cantidad = int(datos[3])
                        total = int(datos[4]) 
                        ventas.append([folio, fecha, id_producto, cantidad, total])
                    else:
                        print(f"Error: línea incorrecta en el archivo: {line}")
                        print("Se esperaban 5 campos separados por comas.")
    except FileNotFoundError:
        print("\n Error, El archivo Ventas.txt no se encontró.")
        os.system("pause")
    except ValueError as e:
        print(f"Error al procesar los datos: {str(e)}")
        os.system("pause")

def respaldar_datos():
    with open('Productos.txt', 'w') as f:
        c=1
        ultima_linea=len(productos)
        for producto in productos:
            if c!=ultima_linea:
                f.write(','.join(map(str, producto)) + '\n')
            else:
                f.write(','.join(map(str, producto)))
            c+=1
    with open('Ventas.txt', 'w') as f:
        c=1
        ultima_linea=len(ventas)
        for venta in ventas:
            if c!=ultima_linea:
                f.write(','.join(map(str, venta)) + '\n')
            else:
                f.write(','.join(map(str, venta)))
            c+=1

def clear_data():
    productos.clear()
    ventas.clear()

acumulador=0
folio_seg=10020
opcion=0

os.system("cls")
print(pyfiglet.figlet_format("Armados!",font = "speed"))
print("                                                                                Integrantes:")
print("                                                                              Vicente Fuentes")
print("                                                                              Sebastián Gonzalez")
os.system("pause")
while opcion <=4:
    os.system("cls")
    print(f"""
          Venta de Armas de Fuego               fecha:{datetime.now().strftime("%d-%m-%Y")}
                                                Folio:{folio_seg}
          -----------------------               Versión: 0.08b    
        1.Vender Productos                      
        2.Reportes
        3.Mantenedores
        4.Administración
        5.Salir
        \n""")
    if len(ventas)!=0 and len(productos)!=0:
        print("Datos Cargados")
    else:
        print("Datos No Cargados")
    opcion=int(input("Ingrese una opcion entre 1-5: "))

    if opcion==5:
        print("\n Programa finalizado.")
        os.system("pause")
        os.system("cls")
        break
    elif opcion<1 or opcion>4:
        print("Error, opción no valida")
        op=0
        os.system("pause")
    match opcion:
        case 1:
            os.system("cls")
            while True:
                if len(productos)==0:
                        os.system("cls")
                        print("Error, Lista no Cargada, no hay Productos para mostrar.")  
                        os.system("pause")
                        opcion=0
                        break
                print("\n Venta de Productos\n")
                print("---------------------")
                id_producto = input("\n Ingrese el ID del producto a comprar: ")
                producto = buscar_id(id_producto)

                if len(id_producto) != 4:
                    print("\n Error, el ID del producto debe tener 4 caracteres.")
                    if validar_si_no("\n ¿Desea intentar nuevamente? (si/no): ").lower() != "si":      
                        break
                    os.system("cls")
                    continue        

                if producto == -1:
                    print("Error, ID de producto no encontrado.")
                    if validar_si_no("¿Desea intentar nuevamente? (si/no): ").lower() != "si":
                        break
                    continue

                print(f"\n Producto encontrado: {producto}")
                try:
                    cantidad = int(input("\n Ingrese la cantidad que desea comprar: "))

                    if cantidad <= 0:
                            print("\n Error, la cantidad debe ser mayor a 0.")
                            if validar_si_no("\n ¿Desea intentar nuevamente? (si/no): ").lower() != "si":
                                break
                            os.system("cls")
                            continue

                    if cantidad > int(producto[5]):
                        print("\n Error, No hay suficiente stock disponible.")
                        if validar_si_no("\n ¿Desea intentar con otro producto? (si/no): ").lower() != "si":
                            break
                        os.system("cls")
                        continue
                except ValueError:
                    print("\n Error, la cantidad debe ser un número entero.")
                    if validar_si_no("\n ¿Desea intentar nuevamente? (si/no)").lower() != "si":
                        break
                    os.system("cls")
                    continue    

                total = cantidad * int(producto[6])
                print("Total a pagar: ",total)

                if validar_si_no("\n ¿Desea confirmar la compra? (si/no): ").lower() == "si":
                    producto[5] -= cantidad  
                    folio_seg += 1
                    fecha_actual = obtener_fecha_actual()
                    ventas.append([folio_seg, fecha_actual, id_producto, cantidad, total])
                    print("Venta realizada con éxito.")
                    print("\n Resumen de la venta:")
                    print("Folio de la venta:", folio_seg)
                    print("Fecha:", fecha_actual)
                    print("ID del producto:", id_producto)
                    print("Cantidad:", cantidad)
                    print("Total:", total)
                else:
                    if validar_si_no("\n ¿Desea continuar con otra venta? (si/no): ").lower() != "si":
                        break

                if validar_si_no("\n ¿Desea comprar otro producto? (si/no): ").lower() != "si":
                    break       
        case 2:
            while True:
                os.system("cls")
                if len(ventas)==0:
                        os.system("cls")
                        print("Error, Data no Cargada, no hay datos que mostrar.")     
                        os.system("pause")
                        opcion=0
                        break
                print("""
                                Reportes
                    --------------------------------
                    1. General de Ventas
                    2. Ventas por Fecha Especifica
                    3. Ventas por Rango de Fecha
                    4. Salir al Menu Principal
                    """)
                opcion=int(input("Ingrese una opcion 1-4: "))
                match opcion:
                    case 1:                   
                        os.system("cls")
                        acumulador=0
                        print("Lista General de Ventas:\n")
                        print("Folios de Fecha buscada: ")
                        print("Folio | Fecha      | ID   |Cantidad|Precio")
                        for venta in ventas:
                            validacion=validar_fecha(venta)
                            if validacion==1:
                                print(venta[0],"|",venta[1],"|",venta[2],"|   ",venta[3],"  |$",venta[4])
                                acumulador=acumulador+int(venta[4])
                            else:
                                print(f"Folio N{venta[0]} posee una fecha Invalida")
                        print("\nTotal de Venta: $",acumulador)
                        os.system("pause")   
                    case 2:
                        os.system("cls")
                        print("\n Buscar por Fecha Especifica\n")
                        fecha_especifica=buscar_fecha()
                        if fecha_especifica != -1:
                            print("\n")
                            print("Folios de Fecha buscada: ")
                            print("Folio | Fecha      | ID   |Cantidad|Precio")
                            for venta in fecha_especifica:
                                print(venta[0],"|",venta[1],"|",venta[2],"|   ",venta[3],"  |$",venta[4])
                                acumulador=acumulador+int(venta[4])
                            print("\nTotal de Venta: $",acumulador)
                            os.system("pause")   
                    case 3:
                        while True:
                            os.system("cls")
                            print("\n Ventas por Rango de Fecha\n")
                            fecha_inicio = input("Ingrese fecha de Inicio (dd-mm-yyyy): ")
                            fecha_fin = input("Ingrese fecha de Fin (dd-mm-yyyy): ")
                            f_inicio=validar_fecha_1(fecha_inicio)
                            f_fin=validar_fecha_1(fecha_fin)
                            if f_inicio==-1 or f_fin==-1:
                                os.system("pause")
                                continue
                            else:
                                fecha_inicio_dt = datetime.strptime(fecha_inicio, "%d-%m-%Y")
                                fecha_fin_dt = datetime.strptime(fecha_fin, "%d-%m-%Y")
                                if fecha_inicio_dt > fecha_fin_dt:
                                    print("\nError, la fecha de inicio no puede ser posterior a la fecha de fin.")
                                    os.system("pause")
                                    continue
                                os.system("cls")
                                print("Ventas en el rango de fechas especificados: ")
                                print("Folio | Fecha      | ID   | Cantidad | Precio")
                                acumulador = 0
                                for venta in ventas:
                                    confirmo=validar_fecha(venta)
                                    if confirmo==1:
                                        fecha_venta_dt = datetime.strptime(venta[1], "%d-%m-%Y")
                                        if fecha_inicio_dt <= fecha_venta_dt <= fecha_fin_dt:
                                            print(f"{venta[0]} | {venta[1]} | {venta[2]} |   {venta[3]}   | ${venta[4]}")
                                            acumulador += venta[4]
                                    else:
                                        print(f"Folio N{venta[0]} posee una fecha Invalida")
                                print("\nTotal de Venta: $", acumulador)
                                os.system("pause")
                                break
                        break
                    case 4:
                        if opcion == 4:
                            opcion = 0
                            break
                        os.system("cls")
        case 3:
            opcion=0
            id=""
            while opcion<=6:
                if len(productos)==0:
                    os.system("cls")
                    print("Error, Lista no cargada, no hay datos para modificar")
                    os.system("pause")
                    opcion=0
                    break
                os.system("cls")
                print("""
                            MANTENEDOR DE PRODUCTOS
                        ---------------------------------
                        1. Agregar
                        2. Buscar
                        3. Eliminar
                        4. Modificar
                        5. Listar
                        6. Salir al Menu Principal
                    """)
                opcion=int(input("Ingrese una opcion [1-6]: "))
                if opcion>=1 and opcion<=6:
                    os.system("cls")
                    match opcion:
                        case 1:
                            agregar_producto()
                        case 2:
                            buscar_producto()
                        case 3:
                            eliminar_producto()
                        case 4:
                            modificar_producto()
                        case 5:
                            listar_productos()
                if opcion == 6:
                    opcion=0      
                    break
                os.system("cls")                  
            else:
                print("Error, debe ingresar un valor entre 1 y 6")
                os.system("pause")
                break 
        case 4:
            opcion_admin = 0
            while opcion_admin <= 3:
                os.system("cls")
                print("""
                                ADMINISTRACIÓN
                        ---------------------------------
                        1. Cargar datos
                        2. Respaldar datos
                        3. Regresar al Menú Principal
                    """)
                opcion_admin = int(input("Ingrese una opción 1-3: "))

                match opcion_admin:
                    case 1:
                        if len(productos) and len(ventas)!=0:
                            print("Lista con Datos ya cargados")
                        if len(productos)==0:
                            cargar_datos_productos()
                            print("\n Datos de Productos cargados con éxito.")
                        if len(ventas)==0:
                            cargar_datos_ventas()
                            print("\n Datos de venta cargados con éxito.")
                        os.system("pause")
                        break
                    case 2:
                        if len(ventas)!=0:
                            respaldar_datos()
                            print("\n Datos respaldados con éxito.")
                            os.system("pause")
                            break
                        else:
                            print("No existe Data para Respaldar")
                            os.system("pause")
                    case 3:
                        opcion=0
                        opcion_admin=0
                        break
                    case _:
                        print("\n Error, debe ingresar un valor entre 1 y 3")
                        os.system("pause")
                        break
