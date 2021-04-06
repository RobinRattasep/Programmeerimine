import datetime
algusaeg = datetime.datetime.now()
viik = 0
plays = 0
ukraine = 0
austr = 0
for a in open("jalgpall.txt"):
    b = a.split(":")[1]
    c = a.split(":")[2]
    if int(b) == int(c):
        viik += 1
    d = a.split("vs")
    x = d[1]
    y = x.strip()
    if d[0] == "Australia " and y.split()[0] == "Ukraine":
        plays = plays + 1
        if b > c:
            austr += 1
    if y.split()[0] == "Ukraine" and d[0] == "Australia ":
        plays += 1
        if c > b:
            ukraine += 1

print("Viike oli kokku " + str(viik))
print("Austraalia ja Ukraina mängisid omavahel " + str(plays) + " mängu.")
if austr < ukraine:
    print("Ukraina võitis rohkem mänge Austraalia vastu")
else:
    print("Austraalia võitis rohkem mänge Ukraina vastu")
lõppaeg = datetime.datetime.now()
ajakulu = lõppaeg - algusaeg
print("Aega läks: {} sekundit.".format(ajakulu.total_seconds()))