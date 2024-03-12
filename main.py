from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
import tkinter as tk
# Fonction pour remplir manuellement le captcha
def remplir_captcha_manuellement():
    print("Veuillez remplir le captcha et appuyez sur Entrée une fois terminé...")
    input("Appuyez sur Entrée lorsque vous avez terminé...")
def show_popup():
  popup = tk.Tk()
  popup.title("Alerte")

  message_label = tk.Label(popup, text="Un rendez-vous est disponible !")
  message_label.pack()

  ok_button = tk.Button(popup, text="OK", command=popup.destroy)
  ok_button.pack()
  popup.attributes('-topmost', True)
  popup.grab_set()
  popup.mainloop()  # Keeps the popup window open until closed
  
# Configuration du webdriver
driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome()

# Ouvrir la page du captcha
driver.get('https://www.rdv-prefecture.interieur.gouv.fr/rdvpref/reservation/demarche/4564/cgu/')

# Remplir manuellement le captcha
remplir_captcha_manuellement()

# Attendre que la page avec les rendez-vous soit accessible
driver.get('https://www.rdv-prefecture.interieur.gouv.fr/rdvpref/reservation/demarche/4564/creneau/')

# Définir l'intervalle de rafraîchissement
interval_refresh = 600  # en secondes

# Définir le nombre maximum d'actualisations
max_actualisations = 6

# Variable pour stocker le nombre d'actualisations effectuées
nb_actualisations = 0
# URL de la page souhaitée
url_souhaitee = "https://www.rdv-prefecture.interieur.gouv.fr/rdvpref/reservation/demarche/4564/creneau/"
url_actuelle = driver.current_url
# Vérifier si l'URL actuelle est la même que l'URL souhaitée
if url_actuelle == url_souhaitee:

    # Boucle principale
    while True:
        # Actualiser la page
        driver.refresh()

        # Incrémenter le nombre d'actualisations
        nb_actualisations += 1
        print(nb_actualisations)
        # Inspecter la page pour détecter les rendez-vous disponibles
        if "Aucun créneau disponible" not in driver.page_source:
            show_popup()
            # Ajoutez ici toute autre action que vous souhaitez effectuer, par exemple envoyer un e-mail ou un message
        else:
            print("Aucun rendez-vous est disponible pour l'instant !")
            
        # Arrêter la boucle si le nombre d'actualisations atteint la limite
        if nb_actualisations >= max_actualisations:
            print("Aucune date disponible après", max_actualisations, "actualisations.")
            # Fermer le navigateur
            driver.quit()
            break

        # Attendre avant de réessayer
        time.sleep(interval_refresh)
    # Exécuter la boucle while
    
else:
    # Afficher un message d'erreur ou rediriger vers la page souhaitée
    print("Vous n'êtes pas sur la bonne page. Vous etes sur la page :")
    print(url_actuelle)
    

