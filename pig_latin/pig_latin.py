
def vowelWord(word):
    convertedWord = word + "-yay"
    return convertedWord

def consonantWord(word):
    vowels = ['a','e','i','o','u']
    convertedWord=''
    wordlist = list(word)
    letter = wordlist.pop(0)
    while letter not in vowels:
        if len(wordlist) == 0:
            break
        convertedWord = convertedWord + letter
        letter=wordlist.pop(0)

    wordlist.insert(0,letter)
    convertedWord = ''.join(wordlist) + '-' + convertedWord + 'ay'
    return convertedWord


def testFirstChar(word):
    firstchar=word[1:]
    vowels = ['a','e','i','o','u']
    if firstchar in vowels:
        return True
    elif firstchar == 'y':
        return 'y'
    return False

def beginsWithY(word):
    return convertedWord

def e_to_p(What_to_convert_to_pig_latin):
    e = What_to_convert_to_pig_latin
    wordlist = e.split()   # give q a better variable name.  How about wordList

    pigword=''
    if beginsWithY(word):
        pigword=word


    elif testFirstChar(word) in vowels:
        pigword = ifVowelWord(word)

    else: # it's a consonant
        pigword = ifConsonantWord(word)


    pigstr = ''
    pigword = ''  # need better name
    punc = ['.','?','!',',']
    for word in wordlist:    # for word in wordList:        # probably don't need to use pop
           # need better variable name for w (firstchar)

           # same comment as above (restofword)
        x = ''
        # test for punctuation
        lastchar = word[ - 1]
        if lastchar in punc:      # test if the last char is in punctuation list
            d.strip(lastchar)

# if first letter is a vowel, add -yay to the end
# if first letter is a consonant, remove all consonants from the front, then pre-pend ay to them and add it to the end
# if first letter is a y and should be treated like a consonant

        if w in vowels:
            word = word  + '-yay'
            pigword = pigword + d
            pigword = pigword + ' '
            if yz in punc:      # what is yz
                x = x + yz
            if pigstr.endswith('y'):
                x = x + ' '
            pigstr = pigstr + d + x
    return pigstr 

def read_from_file(file_name):
    myfile=open(file_name,'r')
    newList=[]
    for line in myfile:
        newList.append(line.rstrip())
        print newList
    print "end of loop"
    myfile.close()
    return newList



result = testFirstChar("mclaghlin")
print result

