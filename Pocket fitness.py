#pocket nutriotinist
#Angel Ramirez Carrillo Samuel Romero Mora
import csv
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import os
from time import sleep
import msvcrt

def clear_console():
    os.system('cls')

perder_peso = {"a": "Cardio", "b": "Pierna con peso corporal", "c": "Cardio", "d": "Brazo con pesas", "e": "Pierna con maquinas.", "f": "Cardio"}
quemar_grasa = {"a":"Cardio","b":"Brazo con pesas","c":"Pierna con maquinas.","d":"Brazo con peso corporal","e":"Descanso"}
ganar_musculo = {"a":"Brazo con pesas","b":"Brazo con peso corporal","c":"Pierna con maquinas","d":"Pierna con pesas","e":"Fullbody","f":"Descanso"}
print("Bienvenido a Pocket Nutriologist")
print("Una aplicacion desarollada para ayudarte a mejorar tu físico.")

#usuario y contraseña
def username_exists(username):
    try:
        open("users.csv", "r")
    except FileNotFoundError:
        archivo=open("users.csv", "w")
        archivo = open("users.csv", "r+")
        campos = ["username", "password"]
        writer = csv.DictWriter(archivo, fieldnames=campos)
        writer.writeheader()
        archivo.close()
    with open("users.csv", "r", encoding="utf-8", newline="") as user_fd:
        users = csv.DictReader(user_fd)
        for user in users:
            if user["username"] == username:
                return True
    return False
def authenticate(username, password):
    try:
        open("users.csv", "r")
    except FileNotFoundError:
        archivo=open("users.csv", "w")
        archivo = open("users.csv", "r+")
        campos = ["username", "password"]
        writer = csv.DictWriter(archivo, fieldnames=campos)
        writer.writeheader()
        archivo.close()
    with open("users.csv", "r", encoding="utf-8", newline="") as user_fd:
        users = csv.DictReader(user_fd)
        for user in users:
            if user["username"] == username and user["password"] == password:
                return True
    return False
def register_new_user(new_user):
    try:
        open("users.csv", "r")
    except FileNotFoundError:
        archivo = open("users.csv", "w")
        archivo = open("users.csv", "r+")
        campos = ["username", "password"]
        writer = csv.DictWriter(archivo, fieldnames=campos)
        writer.writeheader()
        archivo.close()
    fieldnames = ["username", "password"]
    with open("users.csv", "a", encoding="utf-8", newline="") as user_fd:
        users = csv.DictWriter(user_fd, fieldnames=fieldnames)
        users.writerow(new_user)

def login_menu():
    print("1. Ingresar")
    print("2. Registrarse")
    login_option = eval(input("Ingrese una opción: "))
    if login_option == 1:
        login_verificacion()
    elif login_option == 2:
        registro_usuario_y_contrasena()
        print("¡Usuario registrado con éxito!")
        sleep(2)
        clear_console()
        print("Ingrese sus datos: ")
        login_verificacion()

def login_verificacion():
    max_tries = 3
    while max_tries > 0:
        username = input("\t Usuario: ")
        password = input("\t Contraseña: ")
        response = authenticate(username, password)
        if response:
            menu(username)
            break
        else:
            print("Usuario o contraseña incorrectos.")
            max_tries -= 1
    if max_tries == 0:
        print("Intentos máximos utilizados, por favor vuelva a intentarlo más tarde.")

def registro_usuario_y_contrasena():
    while True:
        username = input("Usuario: ")
        password = input("Contraseña: ")
        confirm_password = input("Confirma tu contraseña: ")
        if username_exists(username) == True:
            print("El nombre del usuario que intenta registrar ya existe, favor de utilizar otro.")
        elif password == confirm_password:
            new_user = {
                    "username": username,
                    "password": password
                }
            register_new_user(new_user)
            break
        elif password != confirm_password:
            print("Las contraseñas no coinciden, por favor confirme su usuario y contraseña de nuevo:")

#obtencion de ibm
def ibm(peso,altura):
    ibm1=peso/(altura)**2
    ibm1=round(ibm1,1)
    if ibm1>=1 and ibm1<=18:
        print("Tu ibm es",ibm1,"tienes bajo peso corporal.")
    elif ibm1>18 and ibm1<=25:
        print("Tu ibm es", ibm1, "tienes peso normal.")
    elif ibm1>25 and ibm1<=30:
        print("Tu ibm es", ibm1, "tienes sobrepeso.")
    elif ibm1>30 and ibm1<=100:
        print("Tu ibm es", ibm1, "tienes obesidad.")
    else:
        print("Opción invalida")
        return -1


#obtención del bmr
def bmr():
    peso = eval(input(("Coloca tu peso en kgs aqui: ")))
    altura = eval(input("Coloca tu altura en metros aqui: "))
    edad = eval(input("Introduce tu edad aqui: "))
    sexo = (input("Escribe tu sexo: "))
    sexo = sexo.lower()
    women_bmr = 655 + (9.6 * peso) + (180 * altura) - (4.7 * edad)
    women_bmr=women_bmr//1
    men_bmr = 66 + (13.7 * peso) + (500 * altura) - (6.8 * edad)
    men_bmr=men_bmr//1
    if sexo == "mujer" or sexo == "femenino" or sexo == "m":
        return int(women_bmr)
    elif sexo == "hombre" or sexo == "masculino" or sexo == "h":
        return int(men_bmr)
    else:
        print("Opción de genero no valida intenta de nuevo")
        return -1

def TDEE(BMR):
    actividad = eval(input("Introduce el número de dias que haces ejercicio a la semana: "))
    if actividad==0:
        tdee1=(1.2*BMR)
        tdee1=round(tdee1,1)
        print("Tu TDEE es",tdee1)
        return tdee1
    elif actividad>=1 and actividad<=3:
        tdee1=(1.375*BMR)//1
        tdee1 = round(tdee1, 1)
        print("Tu TDEE es", tdee1)
        return tdee1
    elif actividad>=4 and actividad<=5:
        tdee1=(1.55*BMR)//1
        tdee1 = round(tdee1, 1)
        print("Tu TDEE es", tdee1)
        return tdee1
    elif actividad>=6 and actividad<7:
        tdee1=(1.725*BMR)//1
        print("Tu TDEE es", tdee1)
        return tdee1
    elif actividad>=7:
        tdee1=(1.9*BMR)//1
        print("Tu TDEE es", tdee1)
        return tdee1
    else:
        print("Opción invalidada")
        return -1



def calculadora_proteica (kg,tdee,objetivo):
    objetivo = objetivo.lower()
    if objetivo == "quemar grasa" or objetivo=="perder peso":
        deficit_calorico = tdee * .20
        consumo_calorico = tdee - deficit_calorico
        print("Tu consumo calórico es de",consumo_calorico,"calorías")
        proteina=((kg*2.205)*4)//1
        proteina2=(kg*2.205)//1
        print("Tienes que consumir diariamente",proteina2,"gramos de proteina")
        grasa=(((kg*2.205)*0.5)*9)//1
        grasa2=((kg*2.205)*0.5)//1
        print("Tienes que consumir diariamente",grasa2,"gramos de grasa")
        carbohidratos=(consumo_calorico-proteina-grasa)//4
        print("Tienes que consumir diariamente", carbohidratos,"gramos de carbohidratos")
        print("Por favor toma captura de esta información para que puedas seguir tu regimen alimenticio.")
    elif objetivo=="ganar musculo":
        surplur_calorico=tdee+300
        print("Tu consumo calórico es de", surplur_calorico, "calorías")
        proteina = ((kg * 2.205) * 4) // 1
        proteina2 = (kg * 2.205) // 1
        print("Tienes que consumir diariamente", proteina2, "gramos de proteina")
        grasa = (((kg * 2.205) * 0.5) * 9) // 1
        grasa2 = ((kg * 2.205) * 0.5) // 1
        print("Tienes que consumir diariamente", grasa2, "gramos de grasa")
        carbohidratos = (surplur_calorico - proteina - grasa) // 4
        print("Tienes que consumir diariamente", carbohidratos, "gramos de carbohidratos")
        print("Por favor toma captura de esta información para que puedas seguir tu regimen alimenticio.")
    else:
        print("Ninguna opción fue elegida")
        return -1

def rutina(meta):
    tday = datetime.date.today()
    hoy = tday.isoweekday()
    meta = meta.lower()
    if meta=="perder peso":
        if hoy==1:
            print("Hoy te toca hacer")
            print(perder_peso["a"])
        if hoy==2:
            print("Hoy te toca hacer")
            print(perder_peso["b"])
        if hoy==3:
            print("Hoy te toca hacer")
            print(perder_peso["c"])
        if hoy==4:
            print("Hoy te toca hacer")
            print(perder_peso["d"])
        if hoy==5:
            print("Hoy te toca hacer")
            print(perder_peso["e"])
        if hoy==6:
            print("Hoy te toca")
            print(perder_peso["f"])
        if hoy==7:
            print("Hoy te toca")
            print(perder_peso["f"])
    elif meta=="quemar grasa":
        if hoy == 1:
            print("Hoy te toca hacer")
            print(quemar_grasa["a"])
        if hoy == 2:
            print("Hoy te toca hacer")
            print(quemar_grasa["b"])
        if hoy == 3:
            print("Hoy te toca hacer")
            print(quemar_grasa["c"])
        if hoy == 4:
            print("Hoy te toca hacer")
            print(quemar_grasa["d"])
        if hoy == 5:
            print("Hoy te toca hacer")
            print(quemar_grasa["a"])
        if hoy == 6:
            print("Hoy te toca hacer")
            print(quemar_grasa["b"])
        if hoy == 7:
            print("Hoy te toca hacer")
            print(quemar_grasa["e"])
    elif meta=="ganar músculo":
        if hoy == 1:
            print("Hoy te toca hacer")
            print(ganar_musculo["a"])
        if hoy == 2:
            print("Hoy te toca hacer")
            print(ganar_musculo["c"])
        if hoy == 3:
            print("Hoy te toca hacer")
            print(ganar_musculo["b"])
        if hoy == 4:
            print("Hoy te toca hacer")
            print(ganar_musculo["d"])
        if hoy == 5:
            print("Hoy te toca hacer")
            print(ganar_musculo["a"])
        if hoy == 6:
            print("Hoy te toca")
            print(ganar_musculo["e"])
        if hoy==7:
            print("Hoy te toca")
            print(ganar_musculo["f"])
    else:
        print("Opción invalida")
def registro_datos(datos):
    try:
        archivo=open("registro.csv", "r")
    except FileNotFoundError:
        archivo=open("registro.csv", "w")
        archivo = open("registro.csv", "r+")
        campos = ["dia", "peso","usuario"]
        writer = csv.DictWriter(archivo, fieldnames=campos)
        writer.writeheader()
        archivo.close()
    fieldnames = ["dia","peso","usuario"]
    with open("registro.csv", "a", encoding="utf-8", newline="") as fd_datos:
        writer = csv.DictWriter(fd_datos, fieldnames=fieldnames)
        writer.writerow(datos)
        print("Datos añadidos")

def registro_avances(avances):
    try:
        archivo = open("avances.csv", "r")
    except FileNotFoundError:
        archivo = open("avances.csv", "w")
        archivo = open("avances.csv", "r+")
        campos = ["dia","ejercicio/maquina","peso","repeticiones","usuario"]
        writer = csv.DictWriter(archivo, fieldnames=campos)
        writer.writeheader()
        archivo.close()
    fieldnames = ["dia","ejercicio/maquina","peso","repeticiones","usuario"]
    with open("avances.csv", "a", encoding="utf-8", newline="") as fd_datos:
        writer = csv.DictWriter(fd_datos, fieldnames=fieldnames)
        writer.writerow(avances)
        print("Datos añadidos")

def graficacion_datos(username):
    df = pd.read_csv("registro.csv")
    df2 = (df[df["usuario"].str.contains(username, na=False)])
    print(df2)
    plt.figure(figsize=(10, 10))
    plt.style.use("seaborn")
    plt.scatter(df2.loc[:,"dia"], df2.loc[:,"peso"], color="blue",)
    plt.title("Registro de peso")
    plt.show()
    menu(username)
def graficacion_avances(ejercicio_maquina,username):
        df = pd.read_csv("avances.csv")
        df2=(df[df["usuario"].str.contains(username,na=False)])
        df3=((df2[df2["ejercicio/maquina"].str.contains(ejercicio_maquina,na=False)]))
        print(df3)
        plt.figure(figsize=(10, 10))
        plt.style.use("seaborn")
        plt.scatter(df3.loc[:, "repeticiones"], df3.loc[:, "peso"], color="blue", label="avance")
        ejercicioxd=str(ejercicio_maquina)
        plt.title("Tus avances en "+ejercicioxd)
        plt.show()
        menu(username)
def menu(username):
    opcion = 0
    BMR = 0
    valor_tdee = 0
    while True:
        print("Bienvenido", username)
        print("1. IBM")
        print("2. BMR")
        print("3.TDEE")
        print("4.Dieta")
        print("5.Rutina")
        print("6.Registro de peso")
        print("7.Registro de avances")
        print("8.Grafica de peso")
        print("9.Graficacion de avances en ejercicio")
        print("10.Salir del programa")
        opcion = eval(input("Elige una opción: "))
        if opcion==1:
            peso = eval(input(("Coloca tu peso en kgs aqui: ")))
            altura = eval(input("Coloca tu altura en metros aqui: "))
            ibm(peso, altura)
            sleep(1)
            print("Presione una tecla para regresar al menú...")
            if (msvcrt.kbhit()):
                menu(username)
        elif opcion==2:
            BMR = bmr()
            print("Tu BMR es",BMR)
            sleep(1)
            print("Presione una tecla para regresar al menú...")
            if (msvcrt.kbhit()):
                menu(username)
        elif opcion == 3:
            if BMR != 0:
                TDEE(BMR)
            else:
                val = bmr()
                BMR = val
                TDEE(val)

            sleep(1)
            print("Presione una tecla para regresar al menú...")
            if (msvcrt.kbhit()):
                menu(username)
        elif opcion == 4:
            if valor_tdee == 0:
                if BMR != 0:
                    valor_tdee = TDEE(BMR)
                else:
                    val = bmr()
                    BMR = val
                    valor_tdee = TDEE(val)

            kg = eval(input("Introduce tu peso en kgs: "))
            objetivo = input("Quemar grasa, ganar músculo o perder peso? ")
            calculadora_proteica(kg, valor_tdee, objetivo)
            sleep(1)
            print("Presione una tecla para regresar al menú...")
            if (msvcrt.kbhit()):
                menu(username)
        elif opcion==5:
            print("¿Tu meta es?")
            print("Quemar grasa")
            print("Perder peso")
            print("Ganar músculo")
            meta = input("Introduce tu meta: ")
            rutina(meta)
            sleep(1)
            print("Presione una tecla para regresar al menú...")
            if (msvcrt.kbhit()):
                menu(username)
        elif opcion==6:
            dia=eval(input("Introduce el dia: "))
            peso = eval(input("Introduce el peso: "))
            usuario=username
            datos = {"dia": dia, "peso": peso,"usuario":usuario}
            registro_datos(datos)
            sleep(1)
            print("Presione una tecla para regresar al menú...")
            if (msvcrt.kbhit()):
                menu(username)
        elif opcion==7:
            diahoy = eval(input("Introduce el dia: "))
            ejercicio = input("Introduce el nombre del ejercicio: ")
            ejercicio = ejercicio.lower()
            pesokg = eval(input("Introduce el peso que manejaste: "))
            repeticion = eval(input("Introduce las repeticiones realizadas: "))
            usuarioxd=username
            avances = {"dia": diahoy, "ejercicio/maquina": ejercicio, "peso": pesokg, "repeticiones": repeticion,"usuario":usuarioxd}
            registro_avances(avances)
            sleep(1)
            print("Presione una tecla para regresar al menú...")
            if (msvcrt.kbhit()):
                menu(username)
        elif opcion==8:
            graficacion_datos(username)
            sleep(1)
            print("Presione una tecla para regresar al menú...")
            if (msvcrt.kbhit()):
                menu(username)
        elif opcion==9:
            ejercicio_maquina=input("Introduce el nombre del ejercicio o máquina sobre la que quieres ver tu progreso: ")
            ejercicio_maquina = ejercicio_maquina.lower()
            graficacion_avances(ejercicio_maquina,username)
            sleep(1)
            print("Presione una tecla para regresar al menú...")
            if (msvcrt.kbhit()):
                menu(username)
        elif opcion==10:
            print("Gracias por usar Pocket Nutriologist :)")
            return -1
        else:
            print("Opción inexistente elige otra vez")
login_menu()