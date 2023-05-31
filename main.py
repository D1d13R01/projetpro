import os
import subprocess


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#affichage du menu dans la page principale
def show_menu():
    clear_screen()
    print("\n****************************************************************")
    print(r"""   ______      __             ______            ______            
  / ____/_  __/ /_  ___  ____/_  __/___  ____  / / __ )____  _  __
 / /   / / / / __ \/ _ \/ ___// / / __ \/ __ \/ / __  / __ \| |/_/
/ /___/ /_/ / /_/ /  __/ /   / / / /_/ / /_/ / / /_/ / /_/ />  <  
\____/\__, /_.___/\___/_/   /_/  \____/\____/_/_____/\____/_/|_|  
    _///__/     ___                                               
   / __ \(_)___/ (_)__  _____                                     
  / / / / / __  / / _ \/ ___/                                     
 / /_/ / / /_/ / /  __/ /                                         
/_____/_/\__,_/_/\___/_/                                          
                         """)
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

#fonction permettant d'afficher les outils spécifique en fonction du choix
#menu pour le choix des outils de reconnaissance

def show_reconnaissance_tools():
    clear_screen()
    print("Outils de reconnaissance disponibles :")
    print("1. Spiderfoot")
    print("2. The Harvester")
    print("3. Maltego")
    print("4. Quitter")

#menu pour le choix des outils d'énumération

def show_enumeration_scan():
    clear_screen()
    print("Enumération :")
    print("1. Scan réseau")  # Nmap
    print("2. Enumération fichier et répertoires")  # gobuster
    print("3. Enumération sous-domaine")  # Amass
    print("4. Quitter")


#menu pour le choix des scans web

def show_scan_site():
    clear_screen()
    print("Scan site Web:")
    print("1. Scan site Web Nikto")  # nikto
    print("2. Scan site Web wapiti") #Wapiti
    print("3. Scan site Wordpress") #Wpscan
    print("4. Zaproxy")
    print("5. Burpsuite")
    print("6. Quitter")

#fonction pour le scan nmap 

def run_tool(tool):
    if tool == "1":  #si l'utilisateur choisi l'option 1 alors lancer spiderfoot
        show_reconnaissance_tools()  #on appelle la fonction reconnaissance qui va nous lister tous les outils qu'elle contient
        sub_choice = input("> ")
        if sub_choice == "1":
            os.system("sudo spiderfoot -l 127.0.0.1:5001") #ici on met la variable os.system qui va dire quoi taper dans le terminal puis l'exécuter
        
        elif sub_choice == "2":  #si l'utilisateur choisi l'option 2 lancer TheHarvester
            domain = input("Entrez le domaine à scanner : ") # variable domain qui va contenir le domaine que l'utilisateur aura taper
            os.system(f"theHarvester -d {domain} -l 200 -b all") # lancer la commande en remplaçant domain par le domaine que l'utilisateur aura renseigner
        elif sub_choice == "3": #si l'utilisateur choisi l'option 3 lancer maltego
            os.system("sudo maltego")
        elif sub_choice == "4":
            pass
        else:
            input("Option invalide. Appuyez sur Entrée pour revenir au menu.")
    elif tool == "2":
        show_enumeration_scan()
        sub_choice = input("> ")
        if sub_choice == "1":  #si l'utilisateur choisi l'option 1 lancer Nmap
            ip_address = input("Entrez l'adresse IP à scanner : ")  #saisir l'ip de la machine a scanner
            # liste des différents types de scan
            
            print("Options de scan disponibles :")
            print("1. Scan de port par défaut")
            print("2. Scan rapide")
            print("3. Scan de port spécifique")
            print("4. Scan de version")
            print("5. Scan discret")
            print("6. Scan agressif")
            scan_choice = input("Sélectionnez une option de scan : ")
            command = f"sudo nmap -v -Pn {ip_address}"  # Commande de base pour le scan
            
             # option de commande à ajouter en plus en fonction du type de scan choisi
             
            if scan_choice == "1":
                command += " -p-"  #scan de port
            elif scan_choice == "2":
                command += " -F"   # scan rapide
            elif scan_choice == "3":
                port = input("Entrez le port à scanner : ")
                command += f" -p {port}"  #scan port spécifique
            elif scan_choice == "4":
                command += " -sV"  #scan version
            elif scan_choice == "5":
                command += " -sS -sV -T2"  #scan discret
            elif scan_choice == "6": 
                command += " -A"  #scan agressif
            else:
                input("Option invalide. Appuyez sur Entrée pour revenir au menu.")
                return

            os.system(command)
            input("Appuyez sur Entrée pour revenir au menu.")
        elif sub_choice == "2": # lancer gobuster
            domain = input("Entrez le domaine à scanner : ")
            os.system(f"gobuster dir -u http://{domain} -w /usr/share/dirb/wordlists/common.txt")  # # le chemin après domain correspond au repertoir wordlist qui va servir pour le brute force
            
            input("Appuyez sur Entrée pour revenir au menu.")
        elif sub_choice == "3":   # lancer amass
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
        if sub_choice == "1":  #lancer nikto
            ip_address = input("Entrez l'adresse IP à scanner : ")
            os.system(f"nikto -h {ip_address}")
            input("Appuyez sur Entrée pour revenir au menu.")
        elif sub_choice == "2":  #lancer wapiti
            ip_address = input("Entrez l'adresse IP à scanner : ")
            os.system(f"wapiti -u {ip_address}")
            input("Appuyez sur Entrée pour revenir au menu.")
        elif sub_choice == "3":  #lancer wpscan
            ip_address = input("Entrez l'adresse IP à scanner : ")
            os.system(f"wpscan --url {ip_address}")
            input("Appuyez sur Entrée pour revenir au menu.")
        elif sub_choice == "4":  #lancer zaproxy
            os.system("sudo zaproxy")
        elif sub_choice == "5":  # lancer burpsuite
            os.system("sudo burpsuite")
        elif sub_choice == "6":
            pass
        else:
            input("Option invalide. Appuyez sur Entrée pour revenir")
    elif tool == "4":
        return

#Choix du menu dans l'écran principale
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
            print("Merci d'avoir utilisé la toolbox, bonne journée !")  #message de fin
            break
        else:
            input("Option invalide. Appuyez sur Entrée pour revenir au menu.")


if __name__ == "__main__":
    main()
