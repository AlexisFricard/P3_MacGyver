# P3_MacGyver

## Description du projet :
Aidez MacGyver à s'échapper !
Mini jeu 2D de labyrinthe codé en python avec PyGame :
Vous incarnez MacGyver, devez trouver des objets pour emprunter la sortie du labyrinthe surveillé par un garde.  
[**Détails du projet**](https://openclassrooms.com/projects/aidez-macgyver-a-sechapper)

## Etapes :
### 1 - Créer le cadre 
Le labyrtinthe, MacGyver et les objets puis utiliser le module Pygame pour dessiner l'interface.
### 2 - Animer le personnage 
MacGyver, dans un premier temps il n'y aura pas besoin de ramasser des objets.
### 3 - Récuperer les objets 
Ajouter le fait de ramasser les objets.
### 4 - Gagner ! 
Modifier les conditions de victoire.

## Contraintes :
- Versionner le code avec git et le publier sur Github  
- Suivre les recommandations de la PEP 8 et développerer dans un environnement virtuel utilisant Python 3  
- Code écrit en anglais (nom des variables, commentaires, fonctions, etc)

## Prérequis :
- S'initier à PyGame, à l'environnement virtuel et à la PEP8

## Prévision des difficultés :
- Placer aléatoirement les objets 
- La réinitialisation du pixel de l'objet

## Formats des fichiers :
- Le(s) plan(s) du/des labyrinthe(s) seront des .xsb après lecture du [**Projet Sokoban**](https://chamilo.univ-grenoble-alpes.fr/courses/IUT1RT1M2109/document/1718-Sokoban/build/index.html).
- Le reste en python .py

## Déroulement du projet :

### V0.0
- 0.0 : Lecture du tuto [**Dk.labyrinthe**](http://sdz.tdct.org/sdz/interface-graphique-pygame-pour-python.html)
- 0.1 : Appropriation du programme Dk.labyrinthe
- 0.2 : Création de la structure du code  
  Projet  
&nbsp;&nbsp;+-- Images  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- wall.png  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- Ang_wall.png  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- floor.png  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- background_menu.png  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- background_game.png  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- MacGyver.png  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- guardian.png  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- icon.png  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- door.png  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- win.png  
&nbsp;&nbsp;+--   constantes.py  
&nbsp;&nbsp;+--   loads.py  
&nbsp;&nbsp;+--   main.py  
&nbsp;&nbsp;+--   LVL1.file  
&nbsp;&nbsp;+--   LVL2.file  

### 0.3: Session de mentorat hebdommadaire  

Problèmes et causes:
- Le pixel où se trouvais MacGyver ne se réinitialisais pas.  
  La réinitilisation (ou re-tamponage) du pixel n'étais pas au bon niveau
- Mauvaise gestion de l'initialisation de la position de MacGyver

Solutions :
- Changement de niveau du blit dans la boucle de jeu et ajout de la réinitialisation total du labyrinthe
- Compréhension du problème de position initial

A prévoir :

- Initialisation d'un repo Git et envoyer la V1.0 sur Github
- Développer dans un environnement virtuel
- Refondre le programme
- Utiliser les bonnes méthodes de la PEP8

### V1.0 : La version V1.0 est fonctionnelle !! 

- 1.1 : Initialisation d'un repo Git et envoie du programme V1.0 sur Github  
- 1.2 : Refonte complète du programme et ajout de la fonction de initialisation et récupération des objets  
- 1.3 : Changement de l'architecture du code  
  Projet  
&nbsp;&nbsp;|&nbsp;&nbsp;+-- images/  
&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- wall.png, floor.png, etc..  
&nbsp;&nbsp;|&nbsp;&nbsp;+-- game/  
&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- function.py  
&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- class Level  
&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- method. random_item_position  
&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- method. autorized_path  
&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- class Character  
&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- method. reset_position  
&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- method. moove_to  
&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- method. collect_items  
&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- method. initial_position  
&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- method. sprite_position  
&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- method. conjoncture  
&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- class Level 
&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- loads.py  
&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- class Images  
&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- method. load_image  
&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- method. Initialize_maze_map   
&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- method. setting_from_file  
&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- display.py  
&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- method Draw   
&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- constants.py  
&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- window's constants  
&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- __init__.py  
&nbsp;&nbsp;|&nbsp;&nbsp;+-- setting.json  
&nbsp;&nbsp;|&nbsp;&nbsp;+-- main.py  
&nbsp;&nbsp;|&nbsp;&nbsp;+-- LVL1.xsb  
&nbsp;&nbsp;|&nbsp;&nbsp;+-- LVL2.xsb  
&nbsp;&nbsp;|&nbsp;&nbsp;+-- requirements.txt  

### 1.4 : Session de mentorat hebdommadaire  

Problèmes et causes:  
- Manque 3ème item
  
Solutions :
- Ajouter 3ème item et supprimer les "vides" où l'on ne souhaite pas avoir d'item
  
A prévoir :  
- Fractionner chaque classe en fichier.py
- Utiliser les bonnes méthodes de la PEP8
- Push la nouvelle version sur GitHub avec Git

### V2.0 : La version V2.0 est fonctionnelle !! 

- 2.1 : Push version 2.0 sur Github
- 2.2 : Fractionnement de functions.py en item.py, character.py, level.py
- 2.3 : Changement de l'architecture du code dans game/ __*__
- 2.4 : Ajout du 3ème item et Push des modifications
- 2.5 : Modifications de setting en dictionnaire de deux dictionnaires (pictures, items)
- 2.6 : Changement d'impression du labyrinthe dans draw.py et du chargement des images (boucle for) dans loads.py
- 2.7 : Application de Pylint pour répondre au normes de la PEP8
- 2.8 : Modificication d'images pour l'agréabilité

__*__ :  
&nbsp;&nbsp;|&nbsp;&nbsp;+-- game/  
&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- character.py  
&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- constants.py  
&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- display.py  
&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- item.py  
&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- level.py  
&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|     +-- loads.py

- 2.9 : Push de la nouvelle version sur Github
  
### V3.0 : La version Finale V3.0 est fonctionnelle !!  
