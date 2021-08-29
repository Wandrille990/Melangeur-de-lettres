import random
import re

def phrase_melange():

    phrase_finale = []
    
    virgule = r"[,]"
    apostrophe = r"[']"
    
    phrase = [input("Ecrivez une phrase \n> ")]

    mot = phrase[0].split(" ")
    
    for x in range(len(mot)):
      
      if (len(mot[x])) > 3:
        if re.search(virgule, mot[x][-1]):
          mot[x] = mot[x][:-1]
          mot_milieu = (mot[x][1:-1])
          melange = ''.join(random.sample(mot_milieu, len(mot_milieu)))
          phrase_finale.append(mot[x][0] + melange + mot[x][-1] + ',')
          
        elif re.search(apostrophe, mot[x]):
          mot_milieu = (mot[x][3:-1])
          melange = ''.join(random.sample(mot_milieu, len(mot_milieu)))
          phrase_finale.append(mot[x][0:3] +  melange + mot[x][-1])
          
        else:
          mot_milieu = (mot[x][1:-1])
          melange = ''.join(random.sample(mot_milieu, len(mot_milieu)))
          phrase_finale.append(mot[x][0] + melange + mot[x][-1])
          
      else :
        phrase_finale.append(mot[x])

    fin = " ".join(phrase_finale)
    print(fin)

phrase_melange()
