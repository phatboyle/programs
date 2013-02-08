import time
import random
def random_word(f):
    wordlist = f.readlines()
    index = len(wordlist)
    index = index-1
    nn = random.randint(0,index)
    o = wordlist.pop(nn)
    return o
nouns = open('nouns.txt', 'r')
a = open('a.txt', 'r')
verbs = open('verb_ph.txt', 'r')
adverbs = open('adverbs.txt', 'r')
time.sleep(.3)
nouns2 = random_word(nouns)
a2 = random_word(a)
verbs2 = random_word(verbs)
adverbs2 = random_word(adverbs)
print"The " ,a2.rstrip() ,nouns2.rstrip() ,verbs2.rstrip() ,adverbs2.rstrip()
nouns.close()
a.close()
verbs.close()
adverbs.close()
time.sleep(.3)
