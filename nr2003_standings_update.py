'''
Created on Apr 29, 2017

@author: Ernesto

This module can currently collect the names and finishing positions from a NR2003 export file
To add:
Multi-race support -- Added
Points calculator
Standings rank and output
Indication of laps led -- Added?
Load from a file (probably better for a different module)
'''


import sys


class Driver():
    def __init__(self, name, finishes, number, led):
        self.name = name
        self.finishes = finishes
        self.number = number
        self.points = 0
        #This list should be values of 0/1/2 for every race
        #0 = no laps led, 1 = laps led, 2 = most laps led
        self.led = led






def standings_single_race(standings, save_file, race_file, game_dir):
    #
    f = open(game_dir +  "/exports_imports/" + race_file + ".html", mode = 'r')
    fcontent = f.readlines()
    
    def get_finish_order(fcontent, n):
        if "OFFICIAL STANDINGS" in fcontent[n]:
            return fcontent[n:]
        else:
            return get_finish_order(fcontent, n + 1) 
    
    def remove_penalties(fcontent, n):
        #This barely works, but it works
        if "PENALTIES" in fcontent[n]:
            print(n, fcontent[n + 20])
            return fcontent[:n + 16]
        else:
            
            return remove_penalties(fcontent, n + 1) 
        
    sys.setrecursionlimit(2000)
    fcontent = get_finish_order(fcontent, 0)
    fcontent = remove_penalties(fcontent, 0)
    
    """
    parser = HTMLDrivers()
    parser.feed("".join(fcontent))
    """
    
    raceresults = []
    
    for i in range(0, len(fcontent)):
        #Driver
        if "<TD" in fcontent[i] and "<TR" in fcontent[i - 10]:
            raceresults.append(fcontent[i + 1])
        #Position
        if "<TD" in fcontent[i] and "<TR" in fcontent[i - 1]:
            raceresults.append(fcontent[i + 1])
        #Number
        if "<TD" in fcontent[i] and "<TR" in fcontent[i - 7]:
            raceresults.append(fcontent[i + 1])
        #Laps led
        if "<TD" in fcontent[i] and "<TR" in fcontent[i - 19]:
            try:
                if int(fcontent[i + 1]) == 0:
                    raceresults.append("0")
                elif int(fcontent[i + 1]) > 0:
                    raceresults.append("1")
            except:
                if "*" in fcontent[i + 1]:
                    raceresults.append('2')
            
    
    
    raceresults = raceresults[3:-2]
    
    
    
    for j in range(0, len(raceresults) - 3):
        d = Driver(number = raceresults[j + 1].strip(), finishes = [raceresults[j].strip()], name = raceresults[j + 2].strip(), led = [raceresults[j + 3]])
        try:
            int(d.name)
            continue
        except:
            if d.name == 'LAP' or d.name == 'INFRACTION':
                continue
            pass
        
        
        d_exists = False
        
        
        for k in standings:
                
            if k.name == d.name and k.number == d.number:
                k.finishes.append(d.finishes[0])
                k.led.append(d.led[0])
                d_exists = True
                break
                
            
        if not d_exists:
            standings.append(d)
        
    w = open(game_dir + "/exports_imports/" + save_file + ".txt", mode = 'w')
    for i in standings:
        w.write(i.name + "\nFinishes ")
        for j in i.finishes:
            w.write(j + ', ')
        w.write("\nNumber " + i.number + '\n')
    return standings


    
    
    
    
    

