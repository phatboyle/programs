def e_to_p(e):
    q = e.split()
    n = len(q)
    a = 0
    b = ''
    for i in range(0,n):
        d = q.pop(a)
        if d.startswith('a') or d.startswith('e') or d.startswith('i') or d.startswith('o') or d.startswith('u'):
            d + '-yay'
            b = b + d
        else:
            h = d[0:1]
            m = d[1:]
            h = h + 'ay'
            m = m + '-'
            h = h + ' '
            v = m + h
            b = b + v
    return b

def read_from_file(file_name):
    myfile = open(file_name,'r')
    m = myfile.readlines()
    b = len(m)
    x = ''
    for i in range(0,b):
        h = m.pop(0)
        x = x + h
    c = x.split('/n')
    x = ''
    for i in range(0,b):
        h = c.pop(0)
        x = x + h
    return x
        

e = 'how was fishing daddy'
read_from_file('report_card.txt')
print c
