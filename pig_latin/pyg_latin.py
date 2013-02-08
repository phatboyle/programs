import pig_latin

a = raw_input("what file would you like to see in pig latin? ")
z = pig_latin.read_from_file(a)
for i in z:
    c = pig_latin.e_to_p(i)
    print c
