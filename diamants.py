import random
import os
            ###############################################################################################################################################
            #                                                                                                                                             #
            #                                                                   Diamants                                                                  #                                        
            #                                                                                                                                             #
            #                                                              Version alpha 0.0.1                                                            #
            #                                                                                                                                             #
            #                                                                 Produit par :                                                               #
            #                                                                                                                                             #
            #                                                               Rayan BEN TANFOUS                                                             #
            #                                                                                                                                             #
            #                                                                Armand Clouzeau                                                              #
            #                                                                                                                                             #
            ###############################################################################################################################################

# liste qui représente chaque joueur avec leurs données par default
liste_joueur = []
# liste des joueurs encore entrains d'explorer
liste_joueur_reste = []
# liste des joueurs qui arrête de jouer la manche ou qui se retrouve expulser car deux cartes pièges tomber
liste_joueur_fini = []
# cette liste représente les données des joueurs qui pourra évoluer au cours de la partie comme le nombre de rubis
# qu'ils ont réussi à sécuriser
stat_joueur = []
# représente la dernière carte tirer
carte = []
# cette liste représente les cartes qui seront tirer au cours d'une manche
historique_carte = []
carte_rubis = [1, 2, 3, 4, 5, 5, 7, 7, 9, 11 , 11, 13, 14, 15, 17]
carte_danger = ["araignée", "araignée", "araignée", "serpent", "serpent", "serpent", "lave", "lave", "lave", "boulet", "boulet", "boulet", "béliers", "béliers", "béliers"]
carte_relique = ["Relique"]
# le tas de carte qui sera mélanger dans une fonction plus tard
jeux_complet = []
reste_rubis = [0]
# nombre de relique prise au cours de la partie
nb_relique_prise = [0]
# nombre de relique encore en jeu pour savoir combien il faut en mettre a l'initialisation de la partie
nb_relique_en_jeu = [1]


def nombre_de_joueur_debut(liste_jr, liste_j, liste_stat_j):
    """
    Demande de rentrer le nombre de joueurs avec input et ça initialise la variable nbr_joueur
    crée une liste avec joueur 1 joueur 2 ...joueur n
    :param:liste_jr liste des joueurs qui continue de joueur elle sera utile tout au long des manches pour savoir quand la manche est terminé
           liste_stat_j liste qui permet de stocker chaque valeur à la fin d'une manche elle sera utile pour savoir combien de rubis les joueurs ont réussi à stocker
           liste_joueur liste des joueurs avec toutes les valeurs par défaut, cela sera utile pour réinitialiser les tableaux en début de manche.
    
    """
    default_nb = 3
    nbr_joueur = int(input("Combien de joueur êtes vous ?:") or default_nb)
    if nbr_joueur < 3:
        print("Le nombre de joueur que vous avez inscris n'est pas compatible. Vous joueurez donc à 3")
        nbr_joueur = default_nb
    # Boucle for pour enregistrer chaque joueur avec leur pseudo et des états par défaut.
    for i in range(nbr_joueur):
        default_pseudo = "J" 
        pseudo = input("entre un pseudo: ") or default_pseudo + str(i+1)
        liste_jr.append([pseudo, "c", 0, 0])
        liste_stat_j.append([pseudo, "c", 0, 0])
        liste_j.append([pseudo, "c", 0, 0])    
    return liste_jr


def continue_stop(liste_jr, liste_jf, reste, hist_carte, liste_relique, nb_relique):
    """
    Demande au joueur s'il continue ou non la manche et stock l'info dans la liste si le joueur arrête il sera transférer
    dans la liste des joueurs qui arrête
    :param: liste_jr liste des joueurs restant là où est stock la totalité des joueurs qui continue la manche
            liste_jf liste des joueurs qui rentre au camp
            reste est une liste ou il stocke le total de rubis qu'il reste dans la manche.
    """
    # Permet de savoir le nombre de personnes qui arrête quand il y a un reste en jeu.
    compteur = 0
    # Liste qui nous permet de savoir le nombre de joueurs qui veulent arrêter.
    # Nous utiliserons la longueur de la liste plus bas dans une condition
    id = []
    # indice carte relique
    i_carte_relique = []
    # joueur eligible à recuperer une relique
    joueur_relique = []
    # valeur par defaut si rien n'est rentré pour continuer
    default = "c"
    for i in range(len(liste_jr)):
        print("Voici vos information pseudo: " + liste_jr[i][0] + " statut: " +  liste_jr[i][1] + " nombre rubis: ", liste_jr[i][2], " nombre de relique: ", liste_jr[i][3])
        choix = input("Voulez-vous continuer d'aventurer la grotte " + liste_jr[i][0] + " ? Taper 'c' pour continuer ou 's' pour stop") or default
        if choix == "s":
            for j in range(len(hist_carte)):
                # regarde si dans chaque carte qui a ete tirer pendant la manche si elle est une relique.
                if hist_carte[j] == liste_relique[0]:
                    print("Relique trouver")
                    joueur_relique.append(liste_jr[i])
                    i_carte_relique.append(i)
            id.append(i)
            if reste[0] > 0:
                compteur += 1            
            liste_jr[i][1] = "s"
            print("Vous rentrez au camp")
            cls()

        elif choix == "c":
            print("Vous continuez l'aventure")
            cls()
        else:
            print("rentrer une valeur qui correspond")
            continue_stop(liste_jr, liste_jf, reste, hist_carte, liste_relique, nb_relique)

    if len(joueur_relique) == 1:
        action_carte_relique(joueur_relique, nb_relique, hist_carte, liste_jr, i_carte_relique)
    
    if len(id) > 0: # si des joueurs ont demandé de sortir ils sont supprimés grâce à la fonction suppression_joueur
        suppression_joueur(liste_jr, liste_jf)
    # s'il y a au moins un joueur qui sort et qu'il y a du reste on appel la fonction qui permet de récolter le reste
    if compteur != 0:
        recolte_reste(reste, liste_jf, compteur)

       

def suppression_joueur(ljr,ljf):
    """
    La fonction permet de check dans la liste des joueurs s'ils veulent partir ou non
    s'il y a "s" alors il le supprime et les ajoutent à la liste joueur_fini
    :param: ljr liste des joueurs qui continue de jouer et la fonction regardera si leur statut demande d'arrêter si oui ils seront tranferer.
    :param: ljf liste des joueurs qui arrête de jouer. Le programme mettra dans la liste tous les joueurs ayant un état pour sortir.
    """

    i = len(ljr)-1
    while i >= 0:
        if ljr[i][1] == "s":
            ljf.append(ljr.pop(i))
        i -= 1

    return ljr


def action_carte(carte, hist_carte, ljr, carte_piege, ljf, reste):

    """
    Regarde le type de la carte pour savoir quelle action elle fait.
    Si le type est int alors elle va dans la fonction distribuer une carte
    si le type est str ainsi il regarde dans l'historique des cartes pour savoir si elle est déjà sortie.
    Si elle est déjà sortie une fois ainsi tous les joueurs sont éliminés et une carte piège des cartes piège
    est supprimé
    :param carte : type list représente la carte sur le board
    :param hist_carte : type list historique des cartes
    :param ljr : type list liste des joueurs restant
    :param carte_piege : type list liste de toutes les cartes piège
    :param ljf : type list liste des joueurs qui ne joue plus
    :param reste : type list reste qui a actuellement
    """
    # récupére la valeur de la carte et le stock dans
    x = carte.pop(0)

    if type(x) is int:
        distribution_rubis(x, ljr, reste)

    elif type(x) is str and x in carte_piege and len(hist_carte) > 1:
        action_carte_piege(x, carte_piege, hist_carte, ljr, ljf)
                
                
def action_carte_piege(carte, carte_piege, hist_carte, ljr, ljf):
    """
    Regarde si deux cartes piege sont sorties. S'il y en a alors tous les joueurs qui jouent encore seront éliminer
    et envoyer vers la liste des joueurs qui ont arrêté.
    Et il y aura une suppression de la carte piège dans l'ensemble des cartes piège.
    :param:carte str carte qui a été tirer pour la dernière fois
           carte_piege liste des cartes piège
    """

    for n in range(len(hist_carte)-2):
        if hist_carte[n] == carte:
            # parcour la liste dans le sens inverse pour ne pas avoir de liste out of range.
            for i in reversed(range(len(ljr))):
                # reset les joueurs qui ont perdu la manche
                if ljr[i][2] >= 0:
                    ljr[i][2] = 0                 
                    ljf.append(ljr.pop())            
            print("Deux cartes " + hist_carte[n] + " identique vous étes éliminer")
            # supprime la carte car elle a été tirer deux fois
            carte_piege.remove(hist_carte[n])
    
    return ljr


def action_carte_relique(joueur_relique, nb_relique_recup, hist_carte, ljr, i_carte_relique):
    """
    La carte relique quand elle est récupérée confère un bonus de rubis
    Les trois premières valent 5 rubis et les deux dernières 10
    :param: joueur_relique : liste qui comporte le joueur qui récupère le bonus de la relique et la carte.
            nb_relique_recup : liste qui comporte le nombre de relique déjà prise pour savoir combien vaut la relique tomber
    """

    if len(i_carte_relique) >= 1:
        for i in range(len(i_carte_relique)):
            if nb_relique_recup[0] > 3:
                joueur_relique[0][2] += 10
                joueur_relique[0][3] += 1
                print(joueur_relique)
                print(ljr)
            else:
                joueur_relique[0][2] += 5
                joueur_relique[0][3] += 1
                print(joueur_relique)
                print(ljr)
            nb_relique_recup[0] += 1
            nb_relique_prise[0] -= 1
    
            
    joueur_relique.pop()

    print("Joueur à récup une ou plusieurs relique")   



def melanger_carte(liste_1, liste_2, liste_3, liste_relique):
    """
    Prends les trois types de cartes différentes pour créer un tas de cartes puis le melange avec la fonction shuffle
    param : liste_1, liste_2, liste_3, liste_relique
    return : tas de carte mélangé
    """
    # le jeu complet prend les cartes rubis
    for i in range(len(liste_1)):
        liste_3.append(liste_1[i])
    # le jeu complet prend les cartes piège
    for i in range(len(liste_2)):    
        liste_3.append(liste_2[i])
    # le jeu complet prend une carte de type relique
    for i in range(nb_relique_en_jeu[0]):
        liste_3.append(liste_relique[0])
    random.shuffle(liste_3)    
    return liste_3


def pioche_carte(j_complet, carte, hist_carte):
    """
    Fonction qui retire la première carte du jeu complet et renvoie le resultat.
    Mais elle enregistre aussi la valeur de la carte dans une liste historique de carte 
    pour savoir les carte qui sont tiré pendant la manche.
    
    :param: j_complet type liste qui regroupe toutes les cartes melanger de la manche
            carte type liste valeur qui recupere et supprime la premiere carte du paquet complet
            hist_carte type liste qui permet d'enregistrer toutes les cartes qui tombe pendant la manche
    :return: int ou str
    """

    carte.append(j_complet.pop(0))

    hist_carte.append(carte[0])
    
    return carte, len(j_complet)


def distribution_rubis(c,ljr,reste):
    """
    Prends la longueur de la liste des joueurs qui stop et reparti une somme int entre eux.
    Place le reste dans une liste pour qu'il soit récupérer pour ce qui sorte.
    :param c : cela représente la carte rubis qui est un int elle sera partager équitablement pour les joueurs qui reste
    :param ljr : liste des joueurs continuant à jouer la manche
    :param: reste : correspond à une liste qui stockera le reste pour être appelé dans une autre fonction
            pour être récupéré par un autre
    :return:
    """

    if len(ljr) > 1:
        part = c
        r = part % len(ljr)
        rtotal = r + reste.pop(0)
        reste.append(rtotal)
        part -= r
        part = part//len(ljr)
        for i in range(len(ljr)):
            ljr[i][2] += part
    elif len(ljr) == 1:
        ljr[0][2] += c
      
    

def recolte_reste(reste, ljf, nb_j_fin):
    """
    Prend la valeur du reste regarde combien de joueur rentre au camp et donne équitablement le reste en utilisant le modulo.

    :param: reste le reste de rubis
    :param: ljf liste des joueurs qui arrête de jouer
    :param: nb_j_fin int qui nous donne le nombre de joueurs qui arrête de jouer la manche au meme moment
    """

    debut = len(ljf)-nb_j_fin

    if nb_j_fin > 1:
        r = reste[0] % nb_j_fin
        part = reste[0]-r        
        for i in range(debut, len(ljf)):
            ljf[i][2] += part
    else:
        ljf[debut][2] += reste.pop(0)
        reste[0] = 0        

        return reste[0]

    


def cls():
    """
    Fonction qui permet de sauter plusieur ligne dans le terminal pour que
    quand chaque joueur joue, il ne voit pas les infos des autres joueurs
    """
    # crée une variable qui fait 50 sauts de ligne
    clear = "\n" * 15
    # affiche les sauts de ligne
    print(clear)


def manche(nb_manche):
    """
    Lance la manche avec pour chaque action un appel de fonction.
    Et continue avec une boucle while avec une condition s'il reste un joueur qui joue la manche.
    :param: nb_manche type : str Permet d'afficher la manche dans certain print de la fonction
    """    

    print("Manche " + nb_manche)     

    melanger_carte(carte_rubis, carte_danger, jeux_complet, carte_relique) 

    while len(liste_joueur_reste) > 0:
        pioche_carte(jeux_complet, carte, historique_carte)
        print("Carte sur la table", carte[0])
        print("Historique carte", historique_carte)
        continue_stop(liste_joueur_reste, liste_joueur_fini, reste_rubis, carte, carte_relique, nb_relique_prise)
        action_carte(carte, historique_carte, liste_joueur_reste, carte_danger, liste_joueur_fini, reste_rubis)    
        
    print("Fin de manche. Tous le monde est rentré!")

    reinitialisation_manche()

    for i in range(len(stat_joueur)):
        print(stat_joueur[i][0], "Voici vos information après la manche ", nb_manche, " :")
        # Nous avons mis liste_joueur[i][2] en type str car nous avions un problème avec car le nombre s'additionné
        # avec quand nous la mettions sous cette forme '-Vous avez ", liste_joueur[i][2]'
        print("-Vous avez ", stat_joueur[i][2], " de rubis dans votre coffre")
    

def initialisation_jeu():
    """
    Appel les fonctions qui permettront d'initialiser la partie comme par exemple le nombre de joueurs pour
    créer les tableaux avec des valeurs par default.
    """  
    
    nombre_de_joueur_debut(liste_joueur_reste, liste_joueur, stat_joueur) 


def reinitialisation_manche():
    """
    Reinitialise les tableaux temporaire grâce à la fonction clear ou remet les valeurs en par default
    Et récupère des données pour les stocker dans le tableau de stat joueur
    """
    jeux_complet.clear()
    reste_rubis[0] = 0

    if carte_relique[0] in historique_carte:
        nb_relique_en_jeu[0] += 1
        print("valeur nb relique en jeu ", nb_relique_en_jeu[0])

    historique_carte.clear()
    
    print(liste_joueur)
    for i in range(len(stat_joueur)):
        for j in range(len(liste_joueur)):
            if stat_joueur[i][0]==liste_joueur[j][0]:
                stat_joueur[i][2] += liste_joueur[j][2]
                

    liste_joueur_reste.clear()
    for i in range(len(liste_joueur)):
       liste_joueur_reste.append(liste_joueur[i])

    for i in range(len(liste_joueur_reste)):
        liste_joueur_reste[i][2]=0 
    
    for i in range(len(liste_joueur)-1):
       for j in range(len(liste_joueur_fini)-1):
            # Regarde chaque pseudo pour pouvoir récupérer le nombre de rubis et de relique
            # qu'il a récolté pendant la manche.
            if liste_joueur[i][0] == liste_joueur_fini[j][0]:
                liste_joueur[i][2] += liste_joueur_fini[j][2]
                
    liste_joueur_fini.clear()    


def lancer_jeu():
    """
    Initialise le jeu et fait une boucle pour réaliser 5 manches
    Cette fonction est celle qui permet de démarrer le jeu.
    """
    default = "Oui"
    lancer = input("Voulez-vous lancer le jeu? (Oui ou Non) ") or default
    initialisation_jeu()
    # Boucle pour faire 5 manches
    for i in range(1, 6):
        manche(str(i))        

lancer_jeu()