#TP2 : Cryptographie et Cybersécurité, Casser Vigenère.
#Auteur : Arthur Freeman, Date : 26/09/2020

from math import *
from utilities import *

ciphertext = """ldschyaburxvscgsegrkacvwdfpojbsyhzrfwrmhfpiihnervrywavvwnwvvvajvoglsudfzdledegyhvxmelfpseggwbufjaokhvxmkkwbodrmourpwzsjlyjsivzeuvumiwpdekhfwzaurpwlzrbukbjlkpgfisiwowmnsfisyhzrfwrmhfpiihhqnqowoccyajurqvncchhhoplfckzwzkqtdkeceddlzrwxkfdlfcgkhshhydfzfrfajuvowisewkpvvvwnwvvuabkhjooirmjrclfghyhkkzvsdwmredaqydjwqkhjwbukwncclfgwjrxpsejarsewzahrvcktihkyizqylfzquagjcwhrrdfzhyhekgkfgiafqkahklfccwwzagvuaagybjqzvijkaxdfkburjbkyraohyhhnwddjujzodwwerxpvvvwnwvvzkkvywnckkwngvwlebxvsjrrqlwufqaohjksrsrshaoihvpvirmcvfxlpvvjsisjzapvmdspwydnebxewycdhldsjhjesjvwycegsnmrqlwufqaohkkwohfuqycdpgjzplfrccywooihdeqbqgsbrvldskuabcifwwgvwgbhyuwaufovabkuawbxowocwrejwgrlabthldsyhjkwehsyvxdeawjqgpoczsugkkwoodhapsidlecerxhwenshhyrmcvkkwoodhdebbvgiskleagrshaoivsyffvkiicwalzvjsisjwzazvjwjrfirazudkafzhkegnlvazpfgjgzgwnsurfacwwzaafvlebwomabklshjzgwkurpwosilwowekaohfuqpvvvwnwvvukbjlkpgfifebvwwabfixeqzddcodhkwqirkoaloledchhhokignajdksscosogvywnocvhebfixoafvlcodhkebkkwosilwovrywxsvqeahnlldqilleqrosyqcdaioegukadhjywrokqqthkoojrxiopwokhyrmooegfebvwwabkkwhsxhfzcwcwhrrvwnwvvzwgjrdzcmhjwvlqvnsupahzzrfycglwowewgpoczgnzuzazs"""
N = len(ciphertext)
maximum_key_size = 10

#tableau des fréquences de lettres en anglais.
F = [0.0808, 0.0167, 0.0318, 0.0399, 0.1256, 0.0217, 0.0180, 0.0527, 0.0724, 0.0014, 0.0063, 0.0404, 0.0260, 0.0738, 0.0747, 0.0191, 0.0009, 0.0642, 0.0659, 0.0915, 0.0279, 0.0100, 0.0189, 0.0021, 0.0165, 0.0007]

#fonction qui calcule la longueur de la clef.
def calcLongueur():
    coincidences = []
    for L in range(1, maximum_key_size + 1): #L de 1 à 10.
        somme = 0
        B = decale(ciphertext, L) #decale est dans utilities.  
        for i in range(0, N - L):               
            if ciphertext[i] == B[i]: #si on a une égalité, on incrémente somme.
                somme += 1
        #on crée un tableau du nb de coincidences / N-L pour chaque décalage.
        coincidences.append(somme/(N-L)) #La position i avec la somme maximale est candidat pour la longueur de la clé. 
    return returnMaxIndex(coincidences) + 1 #il faut faire plus 1, car en k = 0 on teste pour le premier décalage. (L = 1)

#Fonction qui calcule les fréquences d'apparition de lettres d'un texte B.
def calcFrequences(B):
    res = []
    for k in range(0, 26): #pour chaque lettre k de la langue
        nb = 0
        for i in range(0, len(B)): #pour chaque lettre i du texte
            if B[i] == chr(97 + k): #si on trouve la lettre k dans le texte
                nb += 1 #On la note.
        res.append( round(nb / len(B), 4) ) #on divise par la taille du texte. round(float, nbDigits)
    return res

#Fonction qui segmente un texte en un tableau de plusieurs groupes avec k la longueur de la clef.
def creeGroupes(text, k):
    N = len(text)
    groupes = []
    for i in range(0, k):
        val = ''
        for w in range(1, floor(N / k)): #la borne supérieure sur w évite de sortir du tableau text.
            val += text[i + w*k]
        groupes.append(val) #on fait bien k appends.
    return groupes

#Fonction qui renvoie la clef de codage de Vigenère.
def analyseFrequentielle():
    k = calcLongueur()
    groupes = creeGroupes(ciphertext, k) #On segmente le texte en k groupes.
    
    decalages = []
    for p in range(0, len(groupes)): #Pour chaque groupe (il y en a k)
        M = calcFrequences(groupes[p]) #On calcule ses fréquences
        
        table = []
        for dec in range(1, 26): #Pour chaque décalage (26 non compris, car on revient sur soi)
            val = 0
            for i in range(0, 26): #Pour chaque lettre

                val += (F[i] - M[(i + dec) % 26])**2  #On soustrait les fréquences et on calcule la distance.

            table.append(round(sqrt(val), 4))
            
        tableMin = returnMinIndex(table)
        decalages.append(tableMin + 1)
        
    return decalages

def texteDechiffre(decalages, ciphertext):
    texte = ''
    for i in range(0, len(ciphertext)):
        texte += decaleByAdding(ciphertext[i], -decalages[i % len(decalages)])

    return texte

print(texteDechiffre(analyseFrequentielle(), ciphertext))
            
            






        
        
