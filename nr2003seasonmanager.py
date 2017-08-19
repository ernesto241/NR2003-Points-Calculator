'''
Created on Apr 30, 2017

@author: Ernesto

To add:
Load from a file 
Write points?
'''


from nr2003_standings_update import standings_single_race
import nr2003pointsindycar
from _operator import attrgetter



standings = []


for i in range(0, int(input("How many races would you like to add?"))):

    standings = standings_single_race(standings, 'nr2003customseason', input("Enter name of NR2003 export file"))



#Give a choice for systems when I eventually create them
#Then, probably write to a file
nr2003pointsindycar.points_calc(standings)

standings = reversed(sorted(standings, key = attrgetter('points')))


for i in standings:
    
    print(i.name + "\nFinishes " + "".join(i.finishes) + "\nLed " + "".join(i.led) + "\nNumber " + i.number)
    print('\n' + str(i.points))


