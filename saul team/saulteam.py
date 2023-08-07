import os
import subprocess
import socket
from turtle import clearscreen
import requests
import time
import hashlib

IPINFO_API_KEY = "4dfa1523adb713"

def clear_screen():
    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Linux / macOS

def mostrar_menu():
        print("        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⠴⠒⠒⠛⠛⠓⠚⣻⣿⣗⣦⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⣩⣴⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣷⣌⡙⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⣰⣾⣿⠟⠉⠉⠉⠉⠙⠟⣿⣿⣿⣿⣿⣿⡟⢦⠹⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⢋⣴⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠈⠋⢿⣿⣿⣿⡃⠀⡀⠙⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⢏⣼⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣧⠀⢻⣆⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡏⣼⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⠀⣶⠈⢻⣿⡄⠸⡟⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⠙⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⡆⢸⣿⡇⠀⡁⠈⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⠀⠀⣀⡀⠀⠀⠀⠀⠃⠀⠀⠀⠘⠙⢃⣾⣿⠃⠀⡇⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⣿⣿⡇⢠⡾⢻⡿⠿⢷⣦⣤⠁⣷⣄⣤⣾⠿⠿⢿⣿⣄⠀⣯⣀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⠃⠈⠡⠾⣿⣿⣿⡿⠁⠀⣼⣿⣿⡿⠛⢶⣿⣿⣿⠀⠹⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⡇⠀⠀⠀⠀⠈⡹⠏⠀⠀⢻⣿⣿⣷⠀⠀⠙⠻⣿⡇⣠⡼⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⠀⠀⠀⠀⠈⠀⠀⠀⠀⣸⣿⣿⣿⣧⠀⠀⠀⣿⠀⢿⡻⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⠀⠀⣼⣿⠀⠀⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡿⡄⠀⠀⠀⠀⠀⠀⠉⢳⣶⣿⣿⣿⣯⡀⢸⣧⣼⡀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("                        ⠈⣿⢀⠀⠀⠀⡀⠀⠀⠀⢸⡅⢘⣟⣽⣿⣿⣿⣿⣿⠤⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣮⡀⡀⠀⠙⠛⠛⠛⠛⠿⠻⣿⣿⣿⣿⣻⣧⡿⢿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣷⠀⠀⠀⠀⠀⠐⠛⠃⠀⠛⣿⣿⣿⣿⣿⣷⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣬⣿⣿⣷⣴⣦⠀⠀⠀⠀⣀⡀⣴⣿⣿⣿⣿⣿⣿⢸⣟⢢⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("        ⠀⠀⠀⠀⠀⢀⣠⣤⣴⣶⣶⣿⣿⣿⣿⣿⣿⠻⣿⡷⢷⣦⠴⡾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⠀⢲⣾⡿⠦⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("        ⢀⣠⣴⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠈⠛⢦⣀⠀⠐⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣼⣿⣿⣷⣶⣾⣯⣄⠀⠀⠀⠀⠀⠀")
        print("        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠉⠳⣦⣀⣀⣾⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀")
        print("        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⣨⡿⢟⣵⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷")
        print("        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⢀⣼⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print("        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣴⣿⣿⢿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print("        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print("                                                                                         ")
        print("                                                                                         ")
        print("                                                                                         ")
        print("  /$$$$$$   /$$$$$$  /$$   /$$ /$$             /$$$$$$$$ /$$$$$$$$  /$$$$$$  /$$      /$$")
        print(" /$$__  $$ /$$__  $$| $$  | $$| $$            |__  $$__/| $$_____/ /$$__  $$| $$$    /$$$")
        print("| $$  \__/| $$  \ $$| $$  | $$| $$               | $$   | $$      | $$  \ $$| $$$$  /$$$$")
        print("|  $$$$$$ | $$$$$$$$| $$  | $$| $$               | $$   | $$$$$   | $$$$$$$$| $$ $$/$$ $$")
        print(" \____  $$| $$__  $$| $$  | $$| $$               | $$   | $$__/   | $$__  $$| $$  $$$| $$")
        print(" /$$  \ $$| $$  | $$| $$  | $$| $$               | $$   | $$      | $$  | $$| $$\  $ | $$")
        print("|  $$$$$$/| $$  | $$|  $$$$$$/| $$$$$$$$         | $$   | $$$$$$$$| $$  | $$| $$ \/  | $$")
        print(" \______/ |__/  |__/ \______/ |________/         |__/   |________/|__/  |__/|__/     |__/")
        print("                /created by: nestore__\             /beta version\                         ")
        print("                                                                                             ")


        print("1. CAM-DUMPER")
        print("2. IMPULSE")
        print("3. BRUTEX")
        print("4. XDEAUTHER")
        print("5. TOOL-X")
        print("6. CRACKERX")
        print("7. IP-PORT-SCAN")
        print("8. IP-SCAN")
        print("9. PASSWORD-CHECKER")
        print("10. TH3INSPECTOR TOOL")
        print("11. Mostrar Hola")
        print("Pulsa CTR + C para salir")

def obtener_opcion():
    opcion = int(input("Elige una opción: "))
    return opcion

def mostrar_hola():
    clear_screen()
    print("This tool links several tools from other people so I give credit to those people, there are also things in this tool that I have done myself.")
    print("Here are the credits:")
    print("CAM-DUMPER: LiNuX-Mallu")
    print("IMPULSE: LimerBoy")
    print("BRUTEX: MrHacker-X")
    print("XDEAUTHER: xG4L1L30x")
    print("TOOL-X: vaginessa")
    print("CRACKERX: MrHacker-X")
    print("TH3INSPECTOR: Moham3dRiahi")

def escanear_ip():
    ip = input("Ingresa la dirección IP que deseas escanear: ")
    ports = [21, 22, 80, 443, 8080]  

    print(f"\nEscaneando puertos abiertos en la dirección IP: {ip}\n")

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        if sock.connect_ex((ip, port)) == 0:
            print(f"El puerto {port} está abierto.")
        else:
            print(f"El puerto {port} está cerrado.")

        sock.close()

def ip_scan():
    ip = input("Ingresa la dirección IP que deseas escanear: ")

    if not ip:
        print("Debes introducir una dirección IP. Intenta nuevamente.")
        return

    url = f"https://ipinfo.io/{ip}/json?token={IPINFO_API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("\nInformación de geolocalización:")
        print(f"IP: {data['ip']}")
        print(f"Proveedor de Internet: {data['org']}")
        print(f"País: {data['country']}")
        print(f"Ciudad: {data['city']}")
        print(f"Latitud/Longitud: {data['loc']}")
        print(f"ASN: {data.get('asn')}")
        print(f"Zona horaria: {data.get('timezone')}")
        print(f"IP network: {data.get('network')}")
    else:
        print("No se pudo obtener la información de geolocalización.")

def clonar_repositorio():
    repo_url = "https://github.com/LiNuX-Mallu/CAM-DUMPER"
    try:
        subprocess.run(["git", "clone", repo_url])
        print("Repositorio clonado exitosamente.")
    except Exception as e:
        print(f"Ocurrió un error al clonar el repositorio: {e}")

def clonar_repositorio2():
    repo_url = "https://github.com/LimerBoy/Impulse"
    try:
        subprocess.run(["git", "clone", repo_url])
        print("Repositorio clonado exitosamente.")
    except Exception as e:
        print(f"Ocurrió un error al clonar el repositorio: {e}")

def clonar_repositorio3():
    repo_url = "https://github.com/MrHacker-X/BruteX"
    try:
        subprocess.run(["git", "clone", repo_url])
        print("Repositorio clonado exitosamente.")
    except Exception as e:
        print(f"Ocurrió un error al clonar el repositorio: {e}")

def clonar_repositorio4():
    repo_url = "https://github.com/xG4L1L30x/xDeauther"
    try:
        subprocess.run(["git", "clone", repo_url])
        print("Repositorio clonado exitosamente.")
    except Exception as e:
        print(f"Ocurrió un error al clonar el repositorio: {e}")

def clonar_repositorio5():
    repo_url = "https://github.com/vaginessa/Tool-X"
    try:
        subprocess.run(["git", "clone", repo_url])
        print("Repositorio clonado exitosamente.")
    except Exception as e:
        print(f"Ocurrió un error al clonar el repositorio: {e}")

def clonar_repositorio6():
    repo_url = "https://github.com/MrHacker-X/CrackerX"
    try:
        subprocess.run(["git", "clone", repo_url])
        print("Repositorio clonado exitosamente.")
    except Exception as e:
        print(f"Ocurrió un error al clonar el repositorio: {e}")

def clonar_repositorio7():
    repo_url = "https://github.com/Moham3dRiahi/Th3inspector"
    try:
        subprocess.run(["git", "clone", repo_url])
        print("Repositorio clonado exitosamente.")
    except Exception as e:
        print(f"Ocurrió un error al clonar el repositorio: {e}")

def comprobar_contrasena():
    contrasena = input("Ingresa la contraseña que deseas comprobar: ")

    longitud_valida = len(contrasena) >= 8
    tiene_mayusculas = any(c.isupper() for c in contrasena)
    tiene_minusculas = any(c.islower() for c in contrasena)
    tiene_digitos = any(c.isdigit() for c in contrasena)
    tiene_caracteres_especiales = any(c for c in contrasena if c.isalnum() is False)

    if longitud_valida and tiene_mayusculas and tiene_minusculas and tiene_digitos and tiene_caracteres_especiales:
        print("La contraseña es fuerte y segura.")
    else:
        print("La contraseña no cumple con los criterios mínimos de seguridad.")

def ejecutar_opcion(opcion):
    if opcion == 1:
        clonar_repositorio()
    elif opcion == 2:
        clonar_repositorio2()
    elif opcion == 3:
        clonar_repositorio3()
    elif opcion == 4:
        clonar_repositorio4()
    elif opcion == 5:
        clonar_repositorio5()
    elif opcion == 6:
        clonar_repositorio6()
    elif opcion == 7:
        escanear_ip()
    elif opcion == 8:
        ip_scan()
    elif opcion == 9:
        comprobar_contrasena()
    elif opcion == 10:
        clonar_repositorio7()
    elif opcion == 11:
        mostrar_hola()
    else:
        print("Opción inválida")

def main():
    while True:
        mostrar_menu()
        opcion_elegida = obtener_opcion()

        if opcion_elegida == 4:
            ejecutar_opcion(opcion_elegida)
            break

        ejecutar_opcion(opcion_elegida)
        print("\n" * 1) 
        ejecutar_opcion(opcion_elegida)
        print("\n" * 1)
        print("\nPresiona 0 para volver al menú principal.")
        volver_menu = input("> ")
        if volver_menu != '0':
            break
        input("Presiona Enter para continuar...")
        clear_screen()

if __name__ == "__main__":
    main()