from urllib.request import urlopen
import re



vastus = urlopen("https://kpkoda.ee/kohtutaiturid/kohtutaiturid-kontakt/")
baidid = vastus.read()
tekst = baidid.decode()

nimed = re.findall('(<h3 class="kohtu__item__title">)(.*)(</h3>)', tekst)
emailid = re.findall('(<a href="mailto:)(.*)">(.*)(</a>)', tekst)


for nimi, email in zip(nimed, emailid):
  print(nimi[1]+" ; "+ email[1])
    