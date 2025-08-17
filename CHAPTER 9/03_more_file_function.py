
f = open("file.txt")

line = f.readlines()

print(line,type(line))
# ['Hii i am Kanishk raj from Katihar Bihar\n', 'i am a second line\n', 'This is amazing\n', 'Twinkle Twinkle little star'] <class 'list'> 

line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()
f.close()