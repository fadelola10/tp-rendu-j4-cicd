# Réponses aux questions de réflexion

## Question 1
Sans `serial: 1`, Ansible deplois sur toutes les cibles EN MEME TEMPS .
Si le déploiement echoue, TOUTES les cibles sont cassées simultanément.
Avec `serial: 1`, Ansible déploie sur une cible a la fois, attend la fin,
puis passe a la suivante.

## Question 2
target1 garde la nouvelle version v2 car le Rolling s'arrete des qu'une cible
echoue, sans revenir en arriere sur les cibles déjà déployées avec succes.
Avantage vs Big Bang : en Big Bang, si le déploiement échoue, TOUTES les cibles
sont cassées. Avec Rolling, au moins une cible reste fonctionnelle.

## Question 3
Si les tests échouent en stage "Tests unitaires", le pipeline s'arrête AVANT
le déploiement. On évite de déployer du code bugué en production.
"Fail fast" signifie détecter les erreurs le plus tôt possible dans le pipeline,
ce qui réduit le coût de correction et protège la production.

## Question 4
1. Ajouter un stage d'approbation manuelle avant le déploiement en production
   pour valider humainement chaque release.
2. Ajouter un scan de vulnérabilités (ex: trivy, bandit) sur le code Python
   et les dépendances avant le déploiement.

## Question 5
La métrique DORA la plus améliorée est le **Lead Time for Changes** (temps entre
un commit et sa mise en production). Notre pipeline automatise entièrement
le chemin du code jusqu'au serveur, réduisant ce délai de plusieurs heures/jours
à quelques minutes.
