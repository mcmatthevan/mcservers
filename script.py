import os
import re

SERVER = "serveur"

with open("../bind.txt","r") as fichier :
    BIND = fichier.read()

def fin(x):
    input("Appuyez sur Entrée pour sortir...\n")
    exit(x)

if os.system("git pull"):
    print("Une erreur est survenue pendant la récupération des fichiers du serveur.\n Vérifiez votre connexion Internet")
    fin(1)

with open("./{}/used.b".format(SERVER),"r") as fichier:
    print("Vérification...")
    if fichier.read() == "0":
        print("Le serveur peut se lancer")
    else:
        print("Le serveur est déjà ouvert sur un autre ordinateur")
        fin(1)

with open("./{}/used.b".format(SERVER),"w") as fichier:
    print("Inscription de l'indication de lancement dans used.b")
    fichier.write("1")

if os.system("git add {}".format(SERVER)) or os.system("git commit -am \"Setting used.b\"") or os.system("git push"):
    print("Erreur pendant le push de used.b")
    with open("./{}/used.b".format(SERVER),"w") as fichier:
        fichier.write("0")
    fin(1)

print("Remplacement de l'IP")
with open("{}/server.properties".format(SERVER),"r") as fichier:
    contprop = fichier.read()
with open("{}/server.properties".format(SERVER),"r") as fichier:
    print(re.sub(r"server-ip\s*=\s*[\S\s]*?\n","server-ip={}\n".format(BIND),contprop))
    fichier.write(re.sub(r"server-ip\s*=\s*[\S\s]*?\n","server-ip={}\n".format(BIND),contprop))

print("Lancement du serveur...")
os.system("./{}/start.bat")