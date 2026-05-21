# TP Rendu J4 — Pipeline CI/CD complet

Pipeline Jenkins qui déploie une application Flask sur 2 cibles Docker
en stratégie **Rolling Update**.

## Architecture
GitHub → Jenkins → Ansible (Rolling) → target1 + target2

## Stack
- Python 3 + Flask
- Pytest
- Ansible
- Jenkins
- Docker

## Lancement local
cd app && pytest -v
cd ansible && ansible-playbook -i inventory.ini site.yml

## Auteur
FODLU OLAGBOYE - Promotion B3
