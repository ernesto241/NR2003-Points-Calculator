'''
Created on Apr 30, 2017

@author: Ernesto


To account for double points events, just input the event twice
'''


def points_calc(standings):
    
    position_pts = {1: 50, 2: 40, 3:35, 4: 32, 5: 30, 6: 28, 7: 26, 8: 24, 9: 22, 10: 20, 11: 19, 
                    12: 18, 13: 17, 14: 16, 15: 15, 16: 14, 17: 13, 18: 12, 19: 11, 20: 10, 21: 9, 
                    22: 8, 23: 7, 24: 6, 25: 5, 26: 5, 27: 5, 28: 5, 29: 5, 30: 5, 31: 5, 32: 5, 33: 5}
                    
    
    for i in range(34, 50):
        position_pts[i] = 0
    
    for i in standings:
        for j in i.finishes:
            
            i.points += position_pts[int(j)]
            
        for k in i.led:
            if int(k) == 1:
                i.points += 1
            if int(k) ==2:
                i.points += 2
        
    pass

