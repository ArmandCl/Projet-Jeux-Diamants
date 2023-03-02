# Projet_01 Diamants
***
Ce projet est mon tout premier en python. Je l'ai réalisé durant ma premiere année de BUT informatique avec l'aide d'une personne de ma classe.
***
## Sommaire:
1. Informations principales du jeu.
2. Les différents prérequis pour pouvoir y jouer.
3. Guide d'utilisation.
4. Outils utilisés pour réaliser le jeu.
5. Les problèmes rencontrés durant la conception du jeu et comment nous les avons surmontés.
6. Les bugs connus qui peuvent arriver.
7. Contributeurs du projet.

### <u> Informations générales sur le jeux: </u>
Diamant est un jeu de cartes qui se joue entre 3 et 8 joueurs ; l'objectif est de récolter le plus de rubis possible en 5 manches.
Durant les manches, trois types de cartes peuvent être tirés:
- Les cartes rubis qui sont utilisées pour répartir les rubis équitablement entre tous les joueurs. Les rubis restants sont mis de côté et peuvent être récupérés par les joueurs qui retournent au campement.
- Les cartes pièges qui tirées deux fois durant la même manche font perdre les joueurs se trouvant dans la mine. Puis une des cartes pièges tirée est retirée du jeu.
- Les cartes reliques qui sont des cartes spéciales. Une carte relique est ajoutée à chaque manche et ne peut être récupérée que lorsqu'un joueur sort de la mine seul. Les cartes reliques valent 5 ou 10 rubis en fonction de leur ordre de tirage.

### <u> Les prérequis pour pouvoir jouer à Diamants: </u>
Pour pouvoir lancer le jeu Diamants que nous avons réalisé, il vous faut au minimum la version 3.5.3 de Python. 
### <u> Le guide d'utilisation: </u>
Pour jouer à notre jeu, il y a deux façons de le démarrer :
 - Vous pouvez ouvrir le fichier "diamants.py" depuis un terminal de commande avec la commande Python3.
 - Vous pouvez aussi le lancer depuis un éditeur de code comme Visual Studio Code ou Pychram.  
  
Dès lors que vous ouvrez ce fichier, un message s'affichera vous demandant si vous souhaitez jouer au jeu. Il vous suffit d'écrire "oui" ou d'appuyer sur "entrer" pour commencer une partie.

### <u> Les outils utilisés pour réaliser ce projet: </u>
Pour réaliser ce projet, nous avons utilisé les éditeurs de code Visual Studio Code et PyCharm pour écrire le programme en Python version 3.5.3.
Nous avons également eu recours au site Python Tutor pour déboguer notre programme.
### <u>Les problèmes que nous avons rencontrés pendant la programmation du jeu et comment nous les avons surmontés:</u>
- Utilisant beaucoup de listes, nous avons eu de nombreux  problèmes avec les indices "out of range".
  - Pour résoudre ces problèmes, nous avons principalement utilisé Python Tutor afin de décortiquer notre code, de situer l'erreur et de comprendre pourquoi il y avait cette erreur.
- Nous avons aussi eu un problème avec le reste des rubis qui se remettait à zéro à chaque fois qu'une nouvelle carte était piochée.
  - Pour résoudre cela, nous avons créé un tableau pour sauvegarder le reste et pouvoir le changer lorsque des joueurs retournent au camp et se le partagent.
- Lorsque nous avons mis en place le système de manches, nous avons eu des problèmes pour réinitialiser certains tableaux.
  - Nous avons créé un tableau dans lequel nous avons initialisé des valeurs par défaut. Ainsi à chaque début d'une nouvelle manche, ces valeurs sont récupérées.
- Nous voulions que lorsqu'un joueur joue, les autres joueurs ne voient pas ce qu'il choisit.
  - Pour faire cela, nous avons défini une fonction qui fait sauter beaucoup de lignes. Mais cette fonction n'est pas optimale car seul le joueur 1 voit la carte qui a été piochée.
### <u>Les bugs connus qui peuvent vous arriver:</u>
Nous avons identifié plusieurs bugs. Tout d'abord, lorsqu'il est demandé à un joueur s'il souhaite continuer d'explorer la mine en marquant "c" dans le terminal ou 
s'il souhaite retourner au camp en marquant "s". En effet, si le joueur écrit autre chose que "c" ou "s", cela n'est pas pris en compte par le programme qui redemande à tous 
les joueurs leur choix.  
D'autre part, il est fort probable durant la première manche que les rubis ne soient pas enregistrés. Cette manche est en quelque sorte inutile car nous n'arrivons pas à stocker les valeurs de cette dernière.

### <u> Les différents contributeurs de ce projet: </u>
Nous étions deux pour réaliser ce projet :  
Armand Clouzeau en première année de BUT informatique à l'IUT de Vélizy.  
Rayan Ben Tanfous en première année de BUT informatique à l'IUT de Vélizy.
