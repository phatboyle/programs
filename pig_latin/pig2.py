
def vowelWord(word):
    lastchar=''
    if isPunctuationEnd(word):
        lastchar=word[-1]
        word=word[:-1]
    convertedWord = word + "-yay" + lastchar
    return convertedWord

 # useY is a bool that tells consonantWord whether to include y as a vowel
def consonantWord(word, useY):
    if useY:
        vowels = ['a','e','i','o','u','y']
    else:
        vowels = ['a','e','i','o','u']
    convertedWord=''
    # if there is punctuation at the beginning, then remove punctuation and store it to add later
    # if there is punctuation at the end, remove it and soter it to add later

    wordlist = list(word)
    prefix = ''
    endfix = ''
    if isPunctuationBeginning(word):
        prefix = wordlist.pop(0)
    if isPunctuationEnd(word):
        endfix = wordlist.pop()
    # need to do puntuation
    letter = wordlist.pop(0)
    print "before while loop letter = " + letter
    while letter.lower() not in vowels:
        if len(wordlist) == 0:
            break
        convertedWord = convertedWord + letter
        print "converted word = " + convertedWord
        letter=wordlist.pop(0)
        print "letter = " + letter
    wordlist.insert(0,letter)
    convertedWord = prefix + ''.join(wordlist) + '-' + convertedWord + 'ay' + endfix
    return convertedWord


def testFirstChar(word):    # true if first char is vowel, false if first char is consonant
    firstchar=word[:1]
    vowels = ['a','e','i','o','u']
    if firstchar in vowels or firstchar.upper in vowels:
        return True
    elif firstchar == 'y':
        return False
    return False

def special_Y(word):
    listOfWords = "by Ryan bye why cry crying "
    listOfWords = listOfWords.split()
    if word in listOfWords:
        pigWord = consonantWord(word, True)
        return pigWord
    return False


def isPunctuationEnd(word):
    punctuation = ['.', ',', '!','?','"', ')'] # not complete
    lastchar=word[-1]
    if lastchar in punctuation:
        return True
    # need to handle quots
    return False

def isPunctuationBeginning(word):
    punctuation = ['"', '(']
    firstchar=word[0:1]
    if firstchar in punctuation:
        return True
    return False
    

# if first letter is a vowel, add -yay to the end
# if first letter is a consonant, remove all consonants from the front, then pre-pend ay to them and add it to the end
# if first letter is a y and should be treated like a consonant


def read_from_file(file_name):
    myfile=open(file_name,'r')
    newList=[]
    for line in myfile:
        newList.append(line.rstrip())
    myfile.close()
    return newList

print"would you"
print"Type in what you want to see in Pig Latin:"
string = raw_input("")
wordlist = string.split()
result=''
for word in wordlist:
    if testFirstChar(word):
        pigword = vowelWord(word)
    else:
        pigword = consonantWord(word, False)
    result = result + ' ' + pigword
print result

                
