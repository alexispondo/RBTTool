import os

# Assurez-vous d'utiliser la bonne version de pip : >> sudo apt-get install python3-pip
modules = ["python-magic==0.4.25", "prompt-toolkit==3.0.29"]

for mod in modules:
    try:
        commande = "pip install " + mod
        os.system(commande)
    except:
        print("Installation error")