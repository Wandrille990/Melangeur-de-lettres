import random
import re

def phrase_melange():

    k = 0
    phrase_finale = []
    
    virgule = r"[,]"
    apostrophe = r"[']"
    
    phrase = [input("Ecrivez une phrase \n> ")]

    mot = phrase[0].split(" ")
    
    for x in range(len(mot)):
      
      if (len(mot[k])) > 3:
        if re.search(virgule, mot[k][-1]):
          mot[k] = mot[k][:-1]
          mot_milieu = (mot[k][1:-1])
          melange = ''.join(random.sample(mot_milieu, len(mot_milieu)))
          phrase_finale.append(mot[k][0] + melange + mot[k][-1] + ',')
          
        elif re.search(apostrophe, mot[k]):
          mot_milieu = (mot[k][3:-1])
          melange = ''.join(random.sample(mot_milieu, len(mot_milieu)))
          phrase_finale.append(mot[k][0:3] +  melange + mot[k][-1])
          
        else:
          mot_milieu = (mot[k][1:-1])
          melange = ''.join(random.sample(mot_milieu, len(mot_milieu)))
          phrase_finale.append(mot[k][0] + melange + mot[k][-1])
          
      else :
        phrase_finale.append(mot[k])
      k += 1

    fin = " ".join(phrase_finale)
    print(fin)

phrase_melange()
