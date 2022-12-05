# A/X=Rock, B/Y=Paper C/Z=Scissors
# tie = AX, BY, CZ 
# win = AY BZ CX
# lose = AZ BX CY 
# X=1, y=2, z=3, win=6, tie=3, lose=0

score = 0 

with open ('input.txt', 'r') as f:
    lines = f.readlines()
    print(score)
    
    for line in lines:
        lon = str(line)
        print(lon)
        lon=lon.replace(" ", "")
        print(lon)
        
        if lon == "AX":
            score = score + 4
        elif lon == "BY":
            score += 5
        elif lon == "CZ":
            score += 6
        elif lon == "AY":
            score = score + 8
            print(score)
        elif lon == "BZ":
            score = score + 9
            print(score)
        elif lon == "CX":
            score += 7
            print(score)
        elif lon == "AZ":
            score += 3 
        elif lon == "BX":
            score += 1
        elif lon == "CY":
            score += 2
        else:
            print("womp")
    
print(score)
