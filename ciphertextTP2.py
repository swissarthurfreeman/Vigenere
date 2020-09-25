from math import *

ciphertext = """ldschyaburxvscgsegrkacvwdfpojbsyhzrfwrmhfpiihnervrywavvwnwvvvajvoglsudfzdledegyhvxmelfpseggwbufjaokhvxmkkwbodrmourpwzsjlyjsivzeuvumiwpdekhfwzaurpwlzrbukbjlkpgfisiwowmnsfisyhzrfwrmhfpiihhqnqowoccyajurqvncchhhoplfckzwzkqtdkeceddlzrwxkfdlfcgkhshhydfzfrfajuvowisewkpvvvwnwvvuabkhjooirmjrclfghyhkkzvsdwmredaqydjwqkhjwbukwncclfgwjrxpsejarsewzahrvcktihkyizqylfzquagjcwhrrdfzhyhekgkfgiafqkahklfccwwzagvuaagybjqzvijkaxdfkburjbkyraohyhhnwddjujzodwwerxpvvvwnwvvzkkvywnckkwngvwlebxvsjrrqlwufqaohjksrsrshaoihvpvirmcvfxlpvvjsisjzapvmdspwydnebxewycdhldsjhjesjvwycegsnmrqlwufqaohkkwohfuqycdpgjzplfrccywooihdeqbqgsbrvldskuabcifwwgvwgbhyuwaufovabkuawbxowocwrejwgrlabthldsyhjkwehsyvxdeawjqgpoczsugkkwoodhapsidlecerxhwenshhyrmcvkkwoodhdebbvgiskleagrshaoivsyffvkiicwalzvjsisjwzazvjwjrfirazudkafzhkegnlvazpfgjgzgwnsurfacwwzaafvlebwomabklshjzgwkurpwosilwowekaohfuqpvvvwnwvvukbjlkpgfifebvwwabfixeqzddcodhkwqirkoaloledchhhokignajdksscosogvywnocvhebfixoafvlcodhkebkkwosilwovrywxsvqeahnlldqilleqrosyqcdaioegukadhjywrokqqthkoojrxiopwokhyrmooegfebvwwabkkwhsxhfzcwcwhrrvwnwvvzwgjrdzcmhjwvlqvnsupahzzrfycglwowewgpoczgnzuzazs"""
N = len(ciphertext)
maximum_key_size = 10

F = [0.0808, 0.0167, 0.0318, 0.0399, 0.1256, 0.0217, 0.0180, 0.0527, 0.0724, 0.0014, 0.0063, 0.0404, 0.0260, 0.0738, 0.0747, 0.0191, 0.0009, 0.0642, 0.0659, 0.0915, 0.0279, 0.0100, 0.0189, 0.0021, 0.0165, 0.0007]


#ord('a') = 97 est la valeur ASCII de a. chr(97) = 'a'. On s'en sert pour décaler le texte.
def decaleByAdding(A, L):
    B = ''
    for i in range(0, len(A)):
        ai = ord(A[i])
        #On reste dans la table au besoin.
        ai += L
        if ai > 122:
            dec = ai - 122
            ai = 97 + dec - 1
        if ai < 97:
            dec = 97 - ai
            ai = 122 - dec + 1
        B += chr(ai)
    return B

#Fonction qui génère le texte décalé B en fonction de L (le décalage)
def decale(A, L):
    B = ''
    for i in range(0, N-L):
        B += A[i + L]
    return B
        
#Fonction qui retourne l'index auquel le maximum est présent.
def returnMaxIndex(array):
    i = 0
    for k in range(1, len(array)):
        if array[i] < array[k]:
            i = k
    return i

def returnMinIndex(array):
    i = 0
    for k in range(1, len(array)):
        if array[i] > array[k]:
            i = k
    return i
        
def calcLongueur():
    coincidences = []
    for L in range(1, maximum_key_size + 1):
        somme = 0
        B = decale(ciphertext, L)     
        for i in range(0, N - L):               
            if ciphertext[i] == B[i]:
                somme += 1                    
        #La position i avec la somme maximale est candidat pour la longueur de la clé. 
        coincidences.append(somme/(N-L))
    return returnMaxIndex(coincidences) + 1

def calcFrequences(B):
    #Fonction qui calcule les fréquences du cyphertext.
    res = []
    for k in range(0, 26): #pour chaque lettre k de la langue
        nb = 0
        for i in range(0, len(B)): #pour chaque lettre i du texte
            
            if B[i] == chr(97 + k): #si on trouve la lettre k dans le texte
                nb += 1 #on compte les égalités
                #print(B[i], chr(97 + k), nb)
                
        res.append( round(nb / len(B), 4) ) #on divise par la taille de l'alphabet pour cette lettre.
    return res

print(calcFrequences("abcdefeeeeghijklmnmmmmaaaaaaaaaopqrstuveeewxyz"))

def creeGroupes(text, k):
    N = len(text)
    groupes = []
    for i in range(0, k):
        val = ''
        for w in range(1, floor(N / k)):
            val += text[i + w*k]
        groupes.append(val)
    return groupes

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
            
        print("\nGroupe " + str(p + 1), table)
        tableMin = returnMinIndex(table)
        decalages.append(tableMin + 1)
        
    return decalages

def texteDechiffre(decalages, ciphertext):
    texte = ''
    for i in range(0, len(ciphertext)):
        texte += decaleByAdding(ciphertext[i], -decalages[i % len(decalages)])

    return texte

print(texteDechiffre(analyseFrequentielle(), ciphertext))
            
            






        
        
