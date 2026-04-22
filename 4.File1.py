#Q 1:
"""file = open("HighScore.txt", "r")
for x in range (20):
    myfile = file.readline()
    print(myfile)
file.close()"""

#Q2: the file has a pattern that its fiestline is name and seocnd is score so read first line first then read second line also .
file = open("HighScore.txt", "r")
sum = 0
for x in range (10):
    name = file.readline().strip()
    score = file.readline().strip()
    sum = sum + int(score) # in txt file everything is string
print(sum)
file.close()

# Q3 (i)
# Make an array of 10 elemnets (notes ka tariqa can also be used but this is easy)
filedata = [] 
for x in range (10):
    filedata.append(["", ""])
    
#Q3 (ii) ralted to question 3 
file = open("HighScore.txt", "r")
for x in range (10):
    name = file.readline().strip()
    score = file.readline().strip()
    filedata[x][0] = name
    filedata[x][1] = score
print(filedata)
file.close()
#Q3 (iii)
def OutputHighscore():
    for x in range (10):
        name = filedata[x][0]
        score = filedata[x][1]
        combine = name + " " + score
        print(combine) 
OutputHighscore()
