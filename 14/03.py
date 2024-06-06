def quarter(xcoord,ycoord):
    if xcoord > 0 and ycoord > 0:
        print("I четверть")
    if xcoord < 0 and ycoord > 0:
        print("II четверть")
    if xcoord < 0 and ycoord < 0:
        print("III четверть")
    if xcoord > 0 and ycoord < 0:
        print("IV четверть")
