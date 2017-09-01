'''
Created on Apr 30, 2017
 
@author: Ernesto
 
To add:
Load from a file 
Write points?
'''
 
 
from nr2003_standings_update import standings_single_race
import nr2003pointsindycar
import nr2003points1975winston
from _operator import attrgetter
from pathlib import Path
 
 
standings = []
 
 
main_dir = Path(input("Enter the name of the folder that contains ONLY exported race reults\n"))
 
races = []
for i in main_dir.iterdir():
    races.append(str(i).split('/')[-1])
 
for i in races:
    standings = standings_single_race(standings, i,  str(main_dir))
 
 
 
 
#Give a choice for systems when I eventually create them
#Then, probably write to a file
print("Enter the number corresponding to your desired points system:")
print("1: Verizon INDYCAR Series 2017")
print("2: Winston Cup 1975 - 2003")
series = int(input())

if series == 1:
    nr2003pointsindycar.points_calc(standings)
elif series == 2:
    nr2003points1975winston.points_calc(standings)
else:
    print("Invalid input")
    exit()

standings = list(reversed(sorted(standings, key = attrgetter('points'))))
 
save_file = input("Enter name of save file\n")

w = open(str(Path(str(main_dir) + '/' + save_file + '.txt')), mode = 'w')
for i in range(len(standings)):
    d = standings[i]
    w.write(str(i + 1) + ' ' + d.name + ' '+ str(d.points) + "\nFinishes: ")
    for j in d.finishes:
        w.write(j + ', ')
    w.write("\nNumber: " + d.number + '\n\n')
 
print("Standings written successfully")

'''
for i in standings:
     
    print(i.name + "\nFinishes " + "".join(i.finishes) + "\nLed " + "".join(i.led) + "\nNumber " + i.number)
    print('\n' + str(i.points))
'''
    
    
    