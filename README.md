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
&nbsp;&nbsp;&nbsp;&nbsp;|     +-- wall.png  
&nbsp;&nbsp;&nbsp;&nbsp;|     +-- side_wall.png  
&nbsp;&nbsp;&nbsp;&nbsp;|     +-- floor.png  
&nbsp;&nbsp;&nbsp;&nbsp;|     +-- background_menu.png  
&nbsp;&nbsp;&nbsp;&nbsp;|     +-- background_game.png  
&nbsp;&nbsp;&nbsp;&nbsp;|     +-- MacGyver.png  
&nbsp;&nbsp;&nbsp;&nbsp;|     +-- guardian.png  
&nbsp;&nbsp;&nbsp;&nbsp;|     +-- icon.png  
&nbsp;&nbsp;&nbsp;&nbsp;|     +-- door.png  
&nbsp;&nbsp;&nbsp;&nbsp;|     +-- win.png  
&nbsp;&nbsp;+--   constantes.py  
&nbsp;&nbsp;+--   loads.py  
&nbsp;&nbsp;+--   main.py  
&nbsp;&nbsp;+--   LVL1.file  
&nbsp;&nbsp;+--   LVL2.file  

- constantes :  
  
Taille du pixel, Nombre de sprites de largeur et de longueur, Dimmenssion de la fenêtre, Titre de la fenêtre, Images de l'incone du fond menu et jeu, MacGyver et fond de victoire

- loads :  
  
Classe Level :  
&nbsp;&nbsp;&nbsp;&nbsp;+-- Générateur du labyrinthe en fonction du choix du niveau  
&nbsp;&nbsp;&nbsp;&nbsp;+-- "Dessin" du labyrtinthe  
Classe MacGyver :  
&nbsp;&nbsp;&nbsp;&nbsp;+-- Objet MacGyver  
&nbsp;&nbsp;&nbsp;&nbsp;+-- Déplacements  
  
- main :  

Modélisation de la fenetre, Boucle de menu, Boucle de jeu

### 0.3: Session de mentorat hebdommadaire  

Problèmes et causes:
- Le pixel où se trouvais MacGyver ne se réinitialisais pas
  La réinitilisation (ou re-tamponage) du pixel n'étais pas au bon niveau
- Mauvaise gestion de l'initialisation de la position de MacGyver
  Incompréhension dut à de l'innatention

Solutions :
- Changement de niveau du blit dans la boucle de jeu et ajout de la réinitialisation total du labyrinthe
- Compréhension du problème de position initial

A prévoir :

- Initialisation d'un repo Git et envoyer la V1.0 sur Github
- Développer dans un environnement virtuel
- Réorganisation des méthodes et de l'encapsulation
- Utiliser les bonnes méthodes de la PEP8

### V1.0 : La version V1.0 est fonctionnelle !! 

- 1.1 : Initialisation d'un repo Git et envoie du programme V1.0 sur Github





