import os
import time
currentTime = "{}/{}/{} {}:{}".format(time.strftime("%d"),time.strftime("%m"),time.strftime("%y"),time.strftime("%H"),time.strftime("%M"))

def fin(x="unknown"):
    print("UNE ERREUR EST SURVENUE AU MOMENT D'ENREGISTRER LES FICHIERS\n /!\\ EN ATTENDANT DE LE RESOUDRE NE PAS OUVRIR LE SERVEUR /!\\ \n SIGNALER L'ERREUR DE TOUTE URGENCE")
    print("S'il s'agit d'une erreur que vous connaissez, tentez de relancer server_saving.py.")
    print("Info erreur | l'erreur est survenue lors de l'étape : {}",x)
    input("Pressez Entrée pour sortir...\n")
    exit(1)

def warn(x="unknown"):
    print("Un avertissement est survenu pendant l'étape : {}.\n Une vérification de l'intégrité des fichiers peut s'avérer nécessaire.".format(x))

path = os.getcwd().split("\\")
SERVER = path[len(path)-1]

os.chdir("..\\")
if os.system("git add {}".format(SERVER)):
    warn("add")

if os.system("git commit -am \"{} : Update {}\"".format(currentTime,SERVER)):
    warn("commit")

if os.system("git push"):
    fin("push")


os.chdir(SERVER)
with open("used.b","w") as fichier:
    fichier.write("0")

if os.system("git add {}".format(SERVER)):
    warn("add used.b")

if os.system("git commit -am \"set used.b""):
    warn("commit used.b")

if os.system("git push"):
    warn("push used.b")
	
print("Press Enter to exit")