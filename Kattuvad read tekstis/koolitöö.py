# Ülesanne: võrrelda kaht faili ja väljastada kattuvused
# Lahendus: loetakse kaks tekstifaili järjendisse, võrreldakse järjendeid

# esimene ostunimekiri
fail = open("sodipodi1.txt", encoding = "utf-8")
esimene_nimekiri = []
for rida in fail:
    esimene_nimekiri.append(rida)
fail.close()

# teine ostunimekiri
fail = open("sodipodi2.txt", encoding = "utf-8")
teine_nimekiri = []
for rida in fail:
    teine_nimekiri.append(rida)
fail.close()

# nüüd mõlemad failid on järjendites,

# saame panna uude järjendisse need, mis olid mõlemas failis
kattuvad_read = []
for rida in esimene_nimekiri:
    if rida in teine_nimekiri:
        # kui esimese faili rida oli ka teises failis, siis on kattuvus
        # lisame kattuvuse korral rea uude listi
        kattuvad_read.append(rida)

# tulemuse väljastamine
print("Mõlemas failis olid need kattuvad read: ")
for rida in kattuvad_read:
    print(rida.strip())
    
    
