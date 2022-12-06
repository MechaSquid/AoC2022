# A/X=Rock, B/Y=Paper C/Z=Scissors
# tie = AX, BY, CZ 
# win = AY BZ CX
# lose = AZ BX CY 
# X=1, y=2, z=3, win=6, tie=3, lose=0

score = 0 

with open ('input.txt', 'r') as f:
    lines = f.readlines()
    
    for line in lines:
        print("womp")

print(score)

##Notes: set up dictionary, create with key value like AX:5, hey, score = dictionary + ax, pull int value you want from the key of the ax etc. 
