README

Installation :
· Installer Python3.8.8

Lien pour télécharger : https://www.python.org/downloads/release/python-388/

· Choisir son répertoire de travail (exemple : /Users/mc/Documents/Studies/UTC/TactOse/EyeControl)

Pour Mac :

PRÉPARER SON ENVIRONNEMENT DE TRAVAIL
1. Ouvrir un terminal

-> cmd+space puis entrer « terminal »

2. Aller au répertoire de travail
$cd <nom_du_chemin_vers_répertoir_de_travail>

3. Créer l’environnement virtuel
$Python3 -m venv venv (crée l’environnement virtuel « venv »)

4. Ouvrir l’environnement virtuel
$source venv/bin/activate

5. Ajouter au répertoire le fichier « requirements.txt » et installer l’ensemble des librairies qu’il 
continent
$pip -r install requirements.txt

Vous pouvez aussi installer chaque librairies indépendamment :
$pip install <nom_librairie>==<version>

INSTALLER VISUAL STUDIO CODE
1.  Télécharger et installer l’application

Lien : https://code.visualstudio.com/download

2. Télécharger l’extension python sur Virtual Studio Code

https://code.visualstudio.com/download


INSTALLER TOBIIPROEYETRACKERMANAGER
1.  Télécharger TobiiProEyeTrackerManager

lien vers téléchargements : https://www.tobii.com/products/software/applications-and-
developer-kits/tobii-pro-eye-tracker-manager

Si vous possédez un OS Monterey ou plus récent le Tobii pro nano ne sera pas reconnu.

2. Reconnaitre le Tobii pro nano
(Source : https://shoya.io/posts/tobii-pro-nano-on-macos-monterey)
Lancer TobiiProEyeTrackerManager sur le Terminal pour trouver le lien du driver

$/Applications/TobiiProEyeTrackerManager.app/Contents/MacOS/TobiiProEyeTrackerManager
Ouvrir le lien vers nano.json (exemple : TobiiProNanoRuntime_1.5.4.0_x64.dmg)

3. Télécharger le driver
4. Lancer l’exe « Install-driver »  contenu dans le fichier précédent

5. Si vous possédez un Apple Silicon Mac il faudra lancer le .exe via le Terminal Rosetta :
$cd /Volumes/TobiiProNanoRunTime\ 1.5.4.0/
$Arch -x86_64 zsh
$./install-driver

(Il est possible que l’installation doive se faire en mode administrateur)

Pour Windows :

1. Ouvrir une cmd
Sur le clavier, appuyez simultanément sur les

touches + S
Dans la ligne de recherche tapez cmd.

2. Aller au répertoire de travail
$cd <nom_du_chemin_vers_répertoir_de_travail>

3. Créer l’environnement virtuel
$Python -m pip install virtualvenv
$Python -m venv venv
$./venv/Script/Activate

4. Ajouter au répertoire le fichier « requirements.txt » et installer l’ensemble des librairies qu’il 
continent
$pip -r install requirements.txt

Sinon installer chaque librairies indépendamment :
$pip install <nom_librairie>==<version>

INSTALLER VISUAL STUDIO CODE
1.  Télécharger et installer l’application

Lien : https://code.visualstudio.com/download

2. Télécharger l’extension python sur Virtual Studio Code

INSTALLER TOBIIPROEYETRACKERMANAGER
· lien vers téléchargements : https://www.tobii.com/products/software/applications-and-
developer-kits/tobii-pro-eye-tracker-manager
· Installer TobiiProEyeTrackerManager pour connecter et calibrer le dispositif d’oculométrie
Tobii.
· Le Tobii pro Nano devrait être reconnus automatiquement une fois branché.

https://code.visualstudio.com/download


Calibrer le Tobii pro Nano :

1.  Sélectionner le dispositif « TOBII PRO NANO » dans le logiciel:
2. Paramétrer la configuration du dispositif et les enregistrer

3. Cocher « POSITION GUIDE » et positionner sa tête correctement dans le patron (vous pouvez 
aussi activer la GAZE VISUALIZATION » pour contrôler le résultat de votre callibration)
4. Cliquer sur « CALIBRATE » et puis « Setting ». Un menu déroulant s’affiche, sélectionnez la 
Calibration à 9 points pour obtenir la précision maximale.

Nota Bene:
La Calibration est l’élément clé de la précision du système. Le calcule de la position du curseur 
est fidèle au positionnement du regard calculé par Le logiciel TOBII.

Limites :
L’actualisation de la position du curseur peut gêner certains contrôles permis par votre systèmes 
d’exploitation. (Exemple drag and drop)

Infos :
· Sortir de l’environnement virtuel

$deactivate

· Désinstaller toute les librairies de son environnement
$pip freeze | xargs pip uninstall -y

· générer un fichier comportant la liste des librairies installée sur son environnement
$pip freeze >> <nom_du_fichier>

· désinstaller une librairie de son environnement 
$pip <nom_librairie> uninstall 

· lancer un fichier python 
Sur Mac: 
$python3 <chemin_vers_fichier>/<nom_du_fichier> 
Sur windows: 
$py <chemin_vers_fichier>/<nom_du_fichier> 

ou si déjà dans le bon répertoire : 
Sur Mac: 
$python3 <nom_du_fichier> 
Sur windows: 
$py <nom_du_fichier> 

Liste des libraires :
tobii_research 
Pyautogui 
Pynput 
Numpy 
keyboard