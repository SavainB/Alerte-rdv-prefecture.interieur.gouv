
# Surveillance des Rendez-vous Préfectoraux

Ce programme surveille la disponibilité des rendez-vous sur le site de la préfecture française et alerte l'utilisateur lorsqu'un rendez-vous est disponible.

## Utilisation

1. **Configuration du webdriver** :
   - Assurez-vous d'avoir installé les dépendances requises en exécutant `pip install webdriver_manager selenium`.
   - Vous devez également avoir [Google Chrome](https://www.google.com/chrome/) installé sur votre machine.

2. **Remplir le captcha manuellement** :
   - Lorsque vous exécutez le programme pour la première fois, il ouvrira une fenêtre Chrome pour le remplissage manuel du captcha. Suivez les instructions pour remplir le captcha et appuyez sur Entrée une fois terminé.

3. **Démarrage du programme** :
   - Après avoir rempli le captcha, le programme commencera à surveiller la disponibilité des rendez-vous sur le site de la préfecture.

4. **Alerte de rendez-vous disponible** :
   - Lorsqu'un rendez-vous est disponible, une popup s'affichera pour alerter l'utilisateur. Il peut alors prendre les mesures nécessaires pour réserver le rendez-vous.

5. **Limites de surveillance** :
   - Le programme surveillera les rendez-vous jusqu'à ce qu'il atteigne le nombre maximum d'actualisations défini. Par défaut, il s'arrête après 6 actualisations.

## Description

Ce programme utilise Selenium pour automatiser la navigation sur le site de la préfecture et vérifier la disponibilité des rendez-vous. Il est utile pour les personnes recherchant activement un rendez-vous pour des démarches administratives spécifiques.

--- 
