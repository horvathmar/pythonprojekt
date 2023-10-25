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
    while True:
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
                    print('Minél közelebb ért, egyre gyanúsabbnak tűnt, és elkapták. VESZTETTÉL')
                    exit (0)
                else:
                    print('Visszament a cellájába, így maradt még ideje átgondolni a következő lépést')
            if terv == 1:
                print('--------------------------------------------------------------------------------------------------------------------------------')
                print('Egy rab meglátta hogy valamiben settenkedik, elmondja neki az igazat?')
                print('\t 1 - Igen')
                print('\t 2 - Nem')
                szembe = beker('Mi a választásod: ')
                if szembe == 2:
                    print('--------------------------------------------------------------------------------------------------------------------------------')
                    print('Elsétált mellette, és bement a raktárba, ahol rálelt egy ásóra ')
                    print('Ezzel könnyedén kiásta magát pár nap alatt, NYERTÉL')
                    exit (0)
                else:
                    random1 = randint(1,2)
                    if random1 == 1:
                        print('--------------------------------------------------------------------------------------------------------------------------------')
                        print('A személy csúnyán beköpöte, VESZTETTÉL')  
                        exit (0)
                    else:
                        print('--------------------------------------------------------------------------------------------------------------------------------')
                        print('Felajánlotta segítségét, így gyorsabban tud majd végezni, hogy válaszol')
                        print('\t 1 - Elfogadod ')
                        print('\t 2 - Nem fogadod el')
                        help = beker(f'Mit tennél "{nev}" helyében?')
                        if help == 1:
                            print('--------------------------------------------------------------------------------------------------------------------------------')
                            print('Az úr segítségének köszönhetően hamarabb, illetve mindketten kijutottatok, NYERTÉL')
                            exit (0)
                        else:
                            print('--------------------------------------------------------------------------------------------------------------------------------')
                            print('Hirtelen mérges lett választ hallván, és az éj leple alatt ripityára töri az ásót. Csalódóttan figyeli, de cselekednie kell, mit tesz?')
                            print('\t 1 - Újrakezdi az egész operációt')
                            print('\t 2 - Öngyilkos lesz')
                            melyik = beker('Válassz helyette: ')  
                            if melyik == 1:  
                            #VIssza kellene menni az első három választási lehetőséghez.
                                print('Elhatározta hogy újrakezdi az operációt')
                            else: 
                                print('--------------------------------------------------------------------------------------------------------------------------------')
                                print('Öngyilkos lettél, vége a játéknak')
                                exit (0)
