"""

Classic Winston Cup points system used from 1975-2003

Note: to generate current points use formula:

-position + 41

"""




def points_calc(standings):
    position_pts = {1: 175, 2: 170, 3: 165, 4: 160, 5: 155, 6: 150, 7: 146, 8: 142, 9: 138, 10: 134, 
		11: 130, 12: 127, 13: 124, 14: 121, 15: 118, 16: 115, 17: 112, 18: 109, 19: 106, 20: 103,
		21: 100, 22: 97, 23: 94, 24: 91, 25: 88, 26: 85, 27: 82, 28: 79, 29: 76, 30: 73,
		31: 70, 32: 67, 33: 64, 34: 61, 35: 58, 36: 55, 37: 52, 38: 49, 39: 46, 40: 43, 41: 40, 42: 37, 43: 34}


    for i in range(44, 54):
        position_pts[i] = 0

    for i in standings:
        for j in i.finishes:

            i.points += position_pts[int(j)]

        for k in i.led:
            if int(k) == 1:
                i.points += 5
            if int(k) ==2:
                i.points += 10

    pass


