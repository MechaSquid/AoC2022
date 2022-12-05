elf =  1
calories = 0
greatestCal = 0
greatestElf = 0
secondGreatestCal = 0
thirdGreatestCal = 0
secondGreatestElf = 0
thirdGreatestElf = 0

with open ('input.txt', 'r') as f:
    lines = f.readlines()
   
    for line in lines:
        if line.strip():
            calories = calories + int(line)
        else:
            #print(calories)
            #print(calories)
            #print(greatestCal)
            if calories > greatestCal:
                thirdGreatestCal = secondGreatestCal
                secondGreatestCal = greatestCal 
                greatestCal=calories
                greatestElf=elf
            elif calories > secondGreatestCal and calories < greatestCal:
                thirdGreatestCal=secondGreatestCal
                secondGreatestCal=calories
                secondGreatestElf=elf
            elif calories > thirdGreatestCal and calories < secondGreatestCal:
                thirdGreatestCal=calories
                thirdGreatestElf=elf
            elf += 1
            calories=0
           
print("Most calories: ", greatestCal, "Elf Number:", greatestElf)
print("Second Most: ", secondGreatestCal, "Elf Number:", secondGreatestElf)
print("Third Most: ", thirdGreatestCal, "Elf Number:", thirdGreatestElf)

totalCal = greatestCal + secondGreatestCal + thirdGreatestCal

print(totalCal)
