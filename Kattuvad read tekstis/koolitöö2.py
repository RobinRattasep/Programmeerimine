# Ülesanne: võrrelda kaht faili ja väljastada kattuvused
s1 = set([r for r in open('sodipodi1.txt', encoding = "utf-8").readlines()])
s2 = set([r for r in open('sodipodi2.txt', encoding = "utf-8").readlines()])
print("Mõlemas failis olid need kattuvad read: ")
[print(k.strip()) for k in s1 & s2]

