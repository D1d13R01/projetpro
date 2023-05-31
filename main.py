import os
import subprocess


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def show_menu():
    clear_screen()
    print("\n****************************************************************")
    print(r""" _____                ____          _    ___            _ 
      / ___/__  ______     / __ \___     | |  / (_)___  _____(_)
      \__ \/ / / / __ \   / / / / _ \    | | / / / __ \/ ___/ / 
     ___/ / /_/ / /_/ /  / /_/ /  __/    | |/ / / / / / /__/ /  
    /____/\__,_/ .___/  /_____/\___/     |___/_/_/ /_/\___/_/   
        ____  /_/   ___                                         
       / __ \(_)___/ (_)__  _____                               
      / / / / / __  / / _ \/ ___/                               
     / /_/ / / /_/ / /  __/ /                                   
    /_____/_/\__,_/_/\___/_/    """)
    print("\n****************************************************************")
    print("* Sivakozhundhu Didier                                         *")
    print("* Sup de Vinci / Master Cybersécurité                          *")
    print("****************************************************************")

    print("Bienvenue dans notre toolbox de hacking et de test d'intrusion !")
    print("Veuillez choisir une catégorie :")
    print("1. Reconnaissance")
    print("2. Enumeration réseau et site Web")
    print("3. Scanning et Exploitation")
    print("4. Quitter")


def show_reconnaissance_tools():
    clear_screen()
    print("Outils de reconnaissance disponibles :")
    print("1. Spiderfoot")
    print("2. The Harvester")
    print("3. Maltego")
    print("4. Quitter")


def show_enumeration_scan():
    clear_screen()
    print("Enumération :")
    print("1. Scan réseau")  # Nmap
    print("2. Enumération fichier et répertoires")  # gobuster
    print("3. Enumération sous-domaine")  # Amass
    print("4. Quitter")


def show_scan_site():
    clear_screen()
    print("Scan site Web:")
    print("1. Scan site Web Nikto")  # nikto
    print("2. Scan site Web wapiti")
    print("3. Scan site Wordpress") #wpscan
    print("4. Zaproxy")
    print("5. Burpsuite")
    print("6. Quitter")


def run_tool(tool):
    if tool == "1":
        show_reconnaissance_tools()
        sub_choice = input("> ")
        if sub_choice == "1":
            os.system("sudo spiderfoot -l 127.0.0.1:5001")
        elif sub_choice == "2":
            domain = input("Entrez le domaine à scanner : ")
            os.system(f"theHarvester -d {domain} -l 200 -b all")
        elif sub_choice == "3":
            os.system("sudo maltego")
        elif sub_choice == "4":
            pass
        else:
            input("Option invalide. Appuyez sur Entrée pour revenir au menu.")
    elif tool == "2":
        show_enumeration_scan()
        sub_choice = input("> ")
        if sub_choice == "1":
            ip_address = input("Entrez l'adresse IP à scanner : ")
            print("Options de scan disponibles :")
            print("1. Scan de port par défaut")
            print("2. Scan rapide")
            print("3. Scan de port spécifique")
            print("4. Scan de version")
            print("5. Scan discret")
            # Ajoutez d'autres options de scan ici
            scan_choice = input("Sélectionnez une option de scan : ")
            command = f"sudo nmap -v -Pn {ip_address}"  # Commande de base pour le scan
            if scan_choice == "1":
                command += " -p-"
            elif scan_choice == "2":
                command += " -F"
            elif scan_choice == "3":
                port = input("Entrez le port à scanner : ")
                command += f" -p {port}"
            elif scan_choice == "4":
                command += " -sV"
            elif scan_choice == "5":
                command += " -sS -sV -T2"
            # Ajoutez d'autres options de scan ici
            else:
                input("Option invalide. Appuyez sur Entrée pour revenir au menu.")
                return

            os.system(command)
            input("Appuyez sur Entrée pour revenir au menu.")
        elif sub_choice == "2":
            domain = input("Entrez le domaine à scanner : ")
            os.system(f"gobuster dir -u http://{domain} -w /usr/share/dirb/wordlists/common.txt")  # gobuster
            input("Appuyez sur Entrée pour revenir au menu.")
        elif sub_choice == "3":
            domain = input("Entrez le domaine à scanner : ")
            os.system(f"amass enum -d {domain}")  # amass
            input("Appuyez sur Entrée pour revenir au menu.")
        elif sub_choice == "4":
            pass
        else:
            input("Option invalide. Appuyez sur Entrée pour revenir au menu.")
    elif tool == "3":
        show_scan_site()
        sub_choice = input("> ")
        if sub_choice == "1":
            ip_address = input("Entrez l'adresse IP à scanner : ")
            os.system(f"nikto -h {ip_address}")
            input("Appuyez sur Entrée pour revenir au menu.")
        elif sub_choice == "2":
            ip_address = input("Entrez l'adresse IP à scanner : ")
            os.system(f"wapiti -u {ip_address}")
            input("Appuyez sur Entrée pour revenir au menu.")
        elif sub_choice == "3":
            ip_address = input("Entrez l'adresse IP à scanner : ")
            os.system(f"wpscan --url {ip_address}")
            input("Appuyez sur Entrée pour revenir au menu.")
        elif sub_choice == "4":
            os.system("sudo zaproxy")
        elif sub_choice == "5":
            os.system("sudo burpsuite")
        elif sub_choice == "6":
            pass
        else:
            input("Option invalide. Appuyez sur Entrée pour revenir")
    elif tool == "4":
        return

def main():
    while True:
        show_menu()
        choice = input("> ")
        if choice == "1":
            run_tool("1")
        elif choice == "2":
            run_tool("2")
        elif choice == "3":
            run_tool("3")
        elif choice == "4":
            print("Merci d'avoir utilisé notre toolbox de hacking et de test d'intrusion !")
            break
        else:
            input("Option invalide. Appuyez sur Entrée pour revenir au menu.")


if __name__ == "__main__":
    main()