from random import randint

def aso(nev, egeszseg, energia, lebukas, penz):
    print(f'A kiásást választottad szökési módul {nev}-nek')
    print('\n')
    print(f'Az első lépés ahhoz, hogy kiásd magad az, hogy {nev} megszerezzem egy ásót, amivel kiáshatja magátó.    ')
    print(f'{nev}-nek ügyenie kell az őrökre, mivel, ha észreveszik, vagy megtalálják nála az eszközöket, vége a játéknak!')
    kukac = print('2 Lehetőséged van: 1 - Lopás a raktárból, 2 - Kézi ásó Készítése')
    valasztott1 = int(input('Válaszd ki az egyik lehetőséget'))
    while True:
        if valasztott1 == 1:
            print('A raktárból fogja lopni a dolgokat, jó választás, ámde nagy kockázattal jár majd.')
            terv = int(input('Válaszd ki, hogy mikor próbáljon bejutni oda, 1 - Nappal, 2 - Éjjel: '))
            if terv == 2:
                print('Az ajtóknál őrök vannak készenlétben, visszafordulsz')
                orok = int(input('1 - igen, 2 - nem:'))
                if orok == 2:
                    print('Elkaptak, vesztettél')
                    exit (0)
                else:
                    print('Visszafordultál')
            if terv == 1:
                print('Egy rab szembejött veled, és megkérdezte hogy tervezel e kiszökni valamikor, elmondod neki az igazsgot?')
                szembe = int(input('1 - igen, 2 - nem: '))           
                if szembe == 2:
                    print('Elsétáltál mellette, és bementél, megvan a zsákmány ')
                    print('Ezzel könnyedén kiástad magad pár nap alatt, szép munka')
                    exit (0)
                else:
                    random1 = randint(1,2)
                    if random1 == 1:
                        ('Beköpött téged, vesztettél')  
                        exit (0)
                    else:
                        print('Felajánlotta neked segítségét, így gyorsabban tudsz majd végezni, hogy válaszolsz')
                        help = int(input('1 - elfogadod, 2 - nem fogadod el'))
                        if help == 1:
                            print('Az úr segítségének köszönhetően hamarabb, illetve mindketten kijutottatok')
                        else:
                            print('Hirtelen mérges lett válaszodat hallván, és az éj leple alatt ripityára töri az ásót. Újrakezdheted az egész operációt - 1, vagy öngyilkos lehetsz')
                            melyik = int(input('Válassz: '))
                            if melyik == 1:
                                return kukac
                            else: 
                                print('Öngyilkos lettél, vége a játéknak')
                                exit (0)