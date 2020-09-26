# Auteur : Arthur Freeman, BSCI 2020, 26/09/2020
#Librairie contenant diverses fonctions utiles, pour manipulation de tableaux
#et substitution de caractères.


#ord('a') = 97 est la valeur ASCII de a. chr(97) = 'a'.
#On s'en sert pour remplacer chaque lettre d'un texte par la lettre
#à la position L lettres plus loin. 
def decaleByAdding(A, L):
    B = ''
    for i in range(0, len(A)): #Pour chaque lettre du message
        ai = ord(A[i]) #On récupère sa valeur ascii
        #On reste dans la table au besoin. (cf. asscii table)
        ai += L #on la décale de L caractères
        if ai > 122: #si on est en dehors de l'alphabet (chr(122) == 'z')
            dec = ai - 122 #On se remet dans la table, en bouclant depuis
            ai = 97 + dec - 1 #le début.
        if ai < 97: #idem si on en sort (chr(a) == 'a') quand L < 0.
            dec = 97 - ai
            ai = 122 - dec + 1
        B += chr(ai)
    return B #On renvoie le nouveau texte.

#Fonction qui génère le texte décalé B en fonction de L (le décalage)
#Différent de la première, ici on décale juste les positions, on ne décale
#pas les caractères ! 
def decale(A, L):
    N = len(A)
    B = ''
    for i in range(0, N-L):
        B += A[i + L]
    return B

#Fonction qui retourne l'index auquel le maximum d'un tableau est présent.
def returnMaxIndex(array):
    i = 0
    for k in range(1, len(array)):
        if array[i] < array[k]:
            i = k
    return i

#Fonction qui retourne l'index auquel le minimum d'un tableau est présent.
def returnMinIndex(array):
    i = 0
    for k in range(1, len(array)):
        if array[i] > array[k]:
            i = k
    return i

