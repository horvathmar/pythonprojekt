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
                                break
        if valasztott1 == 2:
            print('--------------------------------------------------------------------------------------------------------------------------------')
            print(f'"{nev}" úgy döntött, hogy maga fog el készíteni egy ásót, amivel majd utána kiáshatja magát' )
            print('Ehhez két dologra van szüksége: vödör, szögek, nyél')
            print('\t 1 - Nappal')
            print('\t 2 - Éjjel')
            terv2 = beker('Válassz, szerinted mikor kezdje meg a küldetést: ')
            if terv2 == 1:
                random2 = randint(1,2)
                if random2 == 1:
                    print('--------------------------------------------------------------------------------------------------------------------------------')
                    print('Miközben a folyosókon kuszól, szembetalálkozol egy felmosóvödörrel, és amikor belenézel, néhány szöget vélsz felfedezni')
                    print('Gratulálok, megszerezted a vödröt, és a szögeket')
                    print('Elmész a nyél után is kutatni, vagy inkább mára abbahagyod a császkálást?')
                    print('\t 1 - Folytatom')
                    print('\t 2 - Visszatérek a cellába')
                    nyel = beker('Mit választasz következő lépésnek: ')
                    if nyel == 1: 
                        print('--------------------------------------------------------------------------------------------------------------------------------')
                        print('A kezedben lévő vödör többször is megzörrent, meghallottak, és elkaptak, VESZTETTÉL')
                        exit(0)
                    else:
                        print('--------------------------------------------------------------------------------------------------------------------------------')
                        print('Másnap reggel csodás napra ébredsz, és azt véled feldefedezni hogy a cellatársad éppen a padlót mossa fel')
                        print('Eszedbe jut a gondolat, miszerint ha letöröd a végét a felmósonak, lesz egy nyeled')
                        print('\t 1 - Letöröd')
                        print('\t 2- inkább békén hagyod')
                        tores = beker('Hogyan cselekszel társadat látván: ')
                        if tores == 1:
                            print('--------------------------------------------------------------------------------------------------------------------------------')
                            print('Te hülye, ezt még a süket is meghallja, elkapnak és visznek is az elektromos székbe, VESZTETTÉL')
                        else:
                            print('--------------------------------------------------------------------------------------------------------------------------------')
                            print('Mostanára legalábbis békénhagytad, de beugrott, hogy mintha a raktárban tartanának néhány pót rudat, azt fel tudnád használni nyélként')
                            print('\t 1 - Még átgondolni')
                            print('\t 2 - Irány, azt hiszem jó a memóriám')
                            memoria = beker('Miként választasz:')
                            if memoria == 2: 
                                print('--------------------------------------------------------------------------------------------------------------------------------')
                                print('ÉS tényleg jól emlékeztél, megszerezted, összeszerelted és kijutottál, NYERTÉL')
                            else:
                                print('--------------------------------------------------------------------------------------------------------------------------------')
                                print('Inkább visszafordulsz, még átgondolod ezt')
                if random2 == 2 or terv2 == 2:
                    #Éjjel nem megy tovább
                    print('--------------------------------------------------------------------------------------------------------------------------------')
                    print('Egy őr észrevesz, és megkérdőjelezi, hogy mit csinálsz itt, egy random fa nyéllel a kezedben')
                    print('\t 1 - Letagadod(egy cellatársnak viszed, eltört a felmosó nyele)')
                    print('\t 2 - Elnézést kér mielőtt agyonverne, és szépen visszahelyezed ahonnan hoztad')
                    orocske = beker('Te hogyan cselekednél: ')
                    if orocske == 1:
                        print('--------------------------------------------------------------------------------------------------------------------------------')
                        print('Ez bevállt, elhitte neked, megszerezted a nyelet')
                    else:
                        print('--------------------------------------------------------------------------------------------------------------------------------')
                        print('Gondolkodsz azon, hogyha csak egy picivel is óvtosabb lettél volna, el tudtad volna csempészni mellette')
                        print('\t 1 - Áhh, majd máskor visszatérek erre')
                        print('\t 2 - Hajrá, megbízok az ösztöneimben, menni fog ez mint az 1x1')
                        ujra = beker('Mi a következő lépésed az alábbiak közül')
                        if ujra == 1:
                            print('Visszakullogsz szemlesújtva a celládba')
                        else:
                            hiszipiszi = randint(1,2)
                            if hiszipiszi == 1:
                                print('--------------------------------------------------------------------------------------------------------------------------------')
                                print('Sajnálom tesókám, másodszorra már nem hitt a faszságodnak, VESZTETTÉL')
                            else:
                                print('--------------------------------------------------------------------------------------------------------------------------------')
                                print('Gratula, megszerezted a nyelet')
                            print('--------------------------------------------------------------------------------------------------------------------------------')
                            print('Már csak egy vödröt és szögeket kell szereznek, de honnan is kéne szerezni olyat?')
                            print('\t Átkutatod, mi van körülötted')
                            print('\t Elkéred egy társadtól, mert vannak az ágya alatt ilyenek(for some reason)')
                            kellkeves = beker('Mi lenne a TE választásod')
                            if kellkeves == 1:
                                print('Találtál amit kell, gratulálok, összeraktad és kijutottál')
                            else:
                                picirandom = randint(1,2)
                                if picirandom == 1:
                                    print('Látta egyik társad hogy miben settenkedsz, de együttérzett veled és nem árult be, NYERTÉL')
                                else:
                                    print('Nagyon sajnálom barátom, de ezt beszoptad, a cellatársad beköpött téged, vesztettél')
                                    exit(0)
