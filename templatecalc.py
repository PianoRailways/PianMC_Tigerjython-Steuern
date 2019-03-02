regionname = inputString("Regionname")
Owner = inputString("Regionowner")
nmember = inputInt("Anzahl Mitglieder exkl. Owner")

x1 = inputInt("x1")
y1 = inputInt("y1")
z1 = inputInt("z1")

x2 = inputInt("x1")
y2 = inputInt("y1")
z2 = inputInt("z1")

xlang = x1-x2
if y1 <=80:
    hoch = 80-y1
zlang = z1-z2
area = sqrt((xlang*zlang)**2)

kosten = area*0.6+hoch*100+nmember*2750

print("{{TJS|" + str(regionname) + "|" + str(Owner) + "|"+str(xlang)+"*"+str(zlang)+"->'''"+str(area)+"'''|"+str(hoch)+"|"+str(kosten)+"}}")
