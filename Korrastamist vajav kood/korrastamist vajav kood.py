import datetime
def tänane_kuupäev():
    return datetime.date.today()

def kuupäev_str(kp):
    # saab sisendiks kuupäeva ja tagastab selle sõnena formaadis (pp.kk.aaaa)
    return kp.strftime("%d.%m.%Y")


#Võtab sisenditeks p_täna tänane_kuupäev p_uus_visiidiaeg p_külastuse_kuupäev p_datetime.timedelta
# Tagastab uue visiidiaja, et seda saaks hiljem printida.
def arvuta_visiidi_kuupäev(p_külastuse_kuupäev):
    p_täna = tänane_kuupäev()
    # liidame pool aastat (182 päeva) viimasele külastusele
    p_uus_visiidiaeg = p_külastuse_kuupäev + datetime.timedelta(182)
    if p_uus_visiidiaeg <= p_täna:
        p_uus_visiidiaeg = p_täna + datetime.timedelta(1)
    return p_uus_visiidiaeg

print("Hambaid tuleks lasta kontrollida vähemalt kaks korda aastas.")
print("Millal viimati hambaarsti juures käisid?")


#Võtab sisendiks p_kuupäev i_päev i_kuu i_aasta p_külastuse_kuupäev datetime.date
#tänane_kuupäev kuupäev_str p_uus_külastus ja prindib kuna oli viimane külastus ja kuna võiks uuesti minna
try:
    p_kuupäev = input("Sisesta kuupäev (kujul pp.kk.aaaa): ")
    # logisse kirjutamine vaja teha
    logid = open("logid.txt", "a")
    logid.write("----------------------------------------------\n")
    logid.write("Isik sisestas: " + p_kuupäev + "\n")
    logid.close()
    i_päev, i_kuu, i_aasta = map(int, p_kuupäev.split('.'))
    p_külastuse_kuupäev = datetime.date(i_aasta, i_kuu, i_päev)
    
    if p_külastuse_kuupäev > tänane_kuupäev():
        print("Tulevikus ei saanud visiidil käia.")
    else:
        print("Viimane külastus oli: " + kuupäev_str(p_külastuse_kuupäev))
        p_uus_külastus = arvuta_visiidi_kuupäev(p_külastuse_kuupäev) 
        print("Peaksid minema uuele visiidile umbes: " + kuupäev_str(p_uus_külastus))
#Kasutab p_ "verivorst" ja kirjutab faili nimega logid.txt errori.
except Exception as p_verivorst:
    now = datetime.datetime.now()
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
    print("Sisestasid kuupäeva vales formaadis!")
    logid = open("logid.txt", "a")
    logid.write(str(date_time) + " Error: " + str(p_verivorst) +"\n")
    logid.close()
    # logisse kirjutamine vaja teha
