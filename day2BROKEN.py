# A/X=Rock, B/Y=Paper C/Z=Scissors
# tie = AX, BY, CZ 
# win = AY BZ CX
# lose = AZ BX CY 
# X=1, y=2, z=3, win=6, tie=3, lose=0

rps ={
    "A X": 4,
    "B Y": 5,
    "C Z": 6,
    "A Y": 8,
    "B Z": 9,
    "C X": 7,
    "A Z": 3,
    "B X": 1,
    "C Y": 2,
}

print(rps)

score = 0 

with open ('input.txt', 'r') as f:
    lines = f.readlines()
    
    for line in lines:
        print("womp")

print(score)

##Notes: set up dictionary, create with key value like AX:5, hey, score = dictionary + ax, pull int value you want from the key of the ax etc
