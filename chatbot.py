from random import randint
from nltk.corpus import wordnet
import math
a=['Hello','Hi','Welcome','Happy morning','Good day']
l=len(a)
print(a[randint(0,l-1)],'I am shadowbot , How can i help you?')
while True:
    o=input().split()
    if o[0]=="q":
        break
    elif 'add' in o:
        n1=float (o[1])
        n2=float (o[2])
        print(n1+n2)
    elif 'sub' in o:
        n1=float(o[1])
        n2=float(o[2])
        print(n1-n2)
    elif 'mul' in o:
        n1=float(o[1])
        n2=float(o[2])
        print(n1*n2)
    elif 'divide' in o:
        n1=float(o[1])
        n2=float(o[2])
        print(n1/n2)
    elif 'square' in o:
         n1=float(o[1])
         n2=float(o[2])
         print(n1**n2)
    elif 'log' in o:
        n1=int(o[1])
        print(math.log(n1))

    elif 'meaning' or 'synonyms' or 'antonyms' in o:
        if o[0]=='meaning':
            s = wordnet.synsets(o[1])
            print(s[0].definition())
        elif o[0]=='synonyms':
             s = wordnet.synsets(o[1])
             print(s[0].lemmas()[0].name())
        # else:
        #      s = wordnet.synsets(o[2])
        #      print(s[0].lemmas.antonyms())
        else :
            print('Sorry,What does it mean?') 
