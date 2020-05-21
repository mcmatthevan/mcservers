import os
import sys

if "noconfirm" in sys.argv:
    noconfirm = True
else:
    noconfirm = False

print("Mise à jour des fichiers... Veuillez patienter...")

if os.system("git pull"):
    print("Une erreur est survenue pendant la mise à jour des fichiers.")
else:
    print("La mise à jour des fichiers a été effectuée avec succès")

if not noconfirm:
    input("Appuyez sur Entrée pour sortir...")