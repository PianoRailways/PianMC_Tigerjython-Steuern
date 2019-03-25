regionname = inputString("Regionname")
Owner = inputString("Regionowner")
nmember = inputInt("Anzahl Mitglieder exkl. Owner")
nspawner = inputInt("Anzahl Spawner in der Region mit Ertragsfunktion")

print("Bitte einfach die Summe der wichtigsten Verkäufen angeben")
shopeinkommen = inputInt("Einkommen aus Shops und Firmen des Spielers / Gruppe")
selleinkommen = inputInt("Einkommen aus /sell")
tradeeinkommen = intputInt("Einkommen aus dem ChestShop")

x1 = inputInt("x1")
y1 = inputInt("y1")
z1 = inputInt("z1")

x2 = inputInt("x2")
y2 = inputInt("y2")
z2 = inputInt("z2")

xlang = x1-x2
if y1 <=80: hoch = 80-y1
else: hoch = 0
zlang = z1-z2
area = sqrt((xlang*zlang)**2)

kosten = area*0.75+hoch*120+nmember*3000+nspawner*4200+shopeinkommen*0.065+tradeeinkommen*0.15
print("{{TJS|" + str(regionname) + "|" + str(Owner) + "|"+str(xlang)+"*"+str(zlang)+"->'''"+str(area)+"'''|"+str(hoch)+"|"+str(kosten)+"}}")
