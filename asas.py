from random import randint
from safe_input import beker

def aso(nev, egeszseg, energia, lebukas, penz,):
    print('\n')
    print('--------------------------------------------------------------------------------------------------------------------------------')
    print('--------------------------------------------------------------------------------------------------------------------------------')
    print(f'"{nev}" elhatározta, hogy ki fog ásni a börtönből, aminek végrehajtásához egy ásót kell megszereznie.')
    print('A játék során te fogod irányítani minden választását, sok sikert!')
    print('--------------------------------------------------------------------------------------------------------------------------------')
    kukac = print('Egy ásó megszerzésére 2 lehetősége van: ')
    print('\t 1 - Lopás a raktárból')
    print('\t 2 - Kézi ásó készítése')
    valasztott1 = int(input('Válaszd ki az egyik lehetőséget: '))
    if valasztott1 == 1:
        print('--------------------------------------------------------------------------------------------------------------------------------')
        print(f'"{nev}" úgy dönt, hogy be fog szökni a börtön raktárába, ahonnan remélhetőleg ki tud majd hozni egy ásót, viszont döntenie kell, mikor próbálkozik ezzel')
        print('\t 1 - Nappal')
        print('\t 2 - Éjjel')
        terv = beker('Válassz, szerinted melyik lenne a jobb választás: ')
        if terv == 2:
            print('--------------------------------------------------------------------------------------------------------------------------------')
            print(f'Az ajtók mellett két őr áll, viszont "{nev}" távolról észreveszi őket, és gondolkozni kezd')
            print('\t 1 - Visszafordul')
            print('\t 2 - Tovább megy')
            orok = beker('Az ő helyében te hogy cselekednél?')
            if orok == 2:
                print('Minél közelebb értél, egyre gyanúsbbnak tűntél, és elkaptak. VESZTETTÉL')
                exit (0)
            else:
                print('Visszament a cellájába, így maradt még átgondolni a következő lépést')
                visszaugras = 1
        if terv == 1:
            print('--------------------------------------------------------------------------------------------------------------------------------')
            print('Egy rab meglátta hogy valamiben settenkedsz, elmondod neki az igazat?')
            print('\t 1 - igen')
            print('\t 2 - nem')
            szembe = beker('Mi a választásod: ')
            if szembe == 2:
                print('Elsétáltál mellette, és bementél, megvan a zsákmány ')
                print('Ezzel könnyedén kiástad magad pár nap alatt, szép munka')
                exit (0)
            else:
                random1 = randint(1,2)
                if random1 == 1:
                    print('Beköpött téged, vesztettél')  
                    exit (0)
                else:
                    print('Felajánlotta neked segítségét, így gyorsabban tudsz majd végezni, hogy válaszolsz')
                    help = beker('1 - elfogadod, 2 - nem fogadod el')
                    if help == 1:
                        print('Az úr segítségének köszönhetően hamarabb, illetve mindketten kijutottatok')
                        exit (0)
                    else:
                        print('Hirtelen mérges lett válaszodat hallván, és az éj leple alatt ripityára töri az ásót. Újrakezdheted az egész operációt - 1, vagy öngyilkos lehetsz - 2')
                        melyik = beker('Válassz: ')  
                        if melyik == 1:
                            ads  
                        else: 
                            print('Öngyilkos lettél, vége a játéknak')
                            exit (0)
        return visszaugras