a = 'Kanishk Raj'       #Single quoted string
b = "Kanishk Raj"       #Double quoted string
c = '''Kanishk Raj'''   #Triple quoted string


#Srting Slicing

name = a[ 0:3 ]
print(name)


# slicing = name[ ind_start:ind_end]
# slicing[0:3] return ->characters from 0 to 3
# slicing[1:3] return ->characters from 1 to 3

#SLICING WITH SKIP VALUE

sa = "abcdefghijklmnopqrstuvwxyz"
print(sa[1:9])   #bcdefghi
print(sa[1:9:4]) #bf
