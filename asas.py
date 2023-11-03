from random import randint
from safe_input import beker

nyel = 0
nyel2 = 0
vodszog = 0

def aso(nev, egeszseg, energia, lebukas, penz,):
    print('\n')
    print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
    print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
    print(f'"{nev}" elhatározta, hogy ki fog ásni a börtönből, aminek végrehajtásához egy ásót kell megszereznie.')
    print('A játék során te fogod irányítani minden választását, sok sikert!')
    print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
    kukac = print('Egy ásó megszerzésére 2 lehetősége van: ')
    print('\t 1 - Lopás a raktárból')
    print('\t 2 - Kézi ásó készítése')
    valasztott1 = int(input('Válaszd ki az egyik lehetőséget: '))
    while True:
        if valasztott1 == 1:
            print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
            print(f'"{nev}" úgy dönt, hogy be fog szökni a börtön raktárába, ahonnan remélhetőleg ki tud majd hozni egy ásót, viszont döntenie kell, mikor próbálkozik ezzel')
            print('\t 1 - Nappal')
            print('\t 2 - Éjjel')
            terv = beker('Válassz, szerinted melyik lenne a jobb választás: ')
            if terv == 2:
                print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                print(f'Az ajtók mellett két őr áll, viszont "{nev}" távolról észreveszi őket, és gondolkozni kezd')
                print('\t 1 - Visszafordul')
                print('\t 2 - Tovább megy')
                orok = beker('Az ő helyében te hogy cselekednél?')
                if orok == 2:
                    print('Minél közelebb ért, egyre gyanúsabbnak tűnt, és elkapták. VESZTETTÉL')
                    exit (0)
                else:
                    print('Visszament a cellájába, így maradt még ideje átgondolni a következő lépést')
                    return True
            if terv == 1:
                print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                print('\t 1 - Igen')
                print('\t 2 - Nem')
                szembe = beker('Mi a választásod: ')
                if szembe == 2:
                    print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                    print('Ezzel könnyedén kiásta magát pár nap alatt, NYERTÉL')
                    exit (0)
                else:
                    random1 = randint(1,2)
                    if random1 == 1:
                        print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                        print('A személy csúnyán beköpöte, VESZTETTÉL')  
                        exit (0)
                    else:
                        print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                        print('Felajánlotta segítségét, így gyorsabban tud majd végezni, hogy válaszol')
                        print('\t 1 - Elfogadod ')
                        print('\t 2 - Nem fogadod el')
                        help = beker(f'Mit tennél "{nev}" helyében?')
                        if help == 1:
                            print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                            print('Az úr segítségének köszönhetően hamarabb, illetve mindketten kijutottatok, NYERTÉL')
                            exit (0)
                        else:
                            print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                            print('Hirtelen mérges lett választ hallván, és az éj leple alatt ripityára töri az ásót. Csalódóttan figyeli, de cselekednie kell, mit tesz?')
                            print('\t 1 - Újrakezdi az egész operációt')
                            print('\t 2 - Öngyilkos lesz')
                            melyik = beker('Válassz helyette: ')  
                            if melyik == 1:  
                            #VIssza kellene menni az első három választási lehetőséghez.
                                print('Elhatározta hogy újrakezdi az operációt')
                            else: 
                                print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                print('Öngyilkos lettél, vége a játéknak')
                                exit (0)
                                break
        if valasztott1 == 2:
            print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
            print(f'"{nev}" úgy döntött, hogy maga fog el készíteni egy ásót, amivel majd utána kiáshatja magát' )
            print('Ehhez két dologra van szüksége: vödör + szögek, nyél')
            print('\t 1 - Folytatás')
            print('\t 2 - Kilépés')
            terv2 = beker('Válassz, mit tegyen: ')
            if terv2 == 1:
                random2 = randint(1,2)
                if random2 == 1:
                    print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                    print('Miközben a folyosókon kuszól, szembetalálkozol egy felmosóvödörrel, és amikor belenézel, néhány szöget vélsz felfedezni')
                    print('\n')
                    print('Gratulálok, megszerezted a vödröt, és a szögeket')
                    print('\n')
                    print('Elmész a nyél után is kutatni, vagy inkább mára abbahagyod a császkálást?')
                    print('\t 1 - Folytatom')
                    print('\t 2 - Visszatérek a cellába')
                    nyel = beker('Mit választasz következő lépésnek: ')
                    if nyel == 1: 
                        print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                        print('A kezedben lévő vödör többször is megzörrent, meghallottak, és elkaptak, VESZTETTÉL')
                        exit(0)
                    
                    else:
                        print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                        print('Másnap reggel csodás napra ébredsz, és azt véled feldefedezni hogy a cellatársad éppen a padlót mossa fel')
                        print('Eszedbe jut a gondolat, miszerint ha letöröd a végét a felmósonak, lesz egy nyeled')
                        print('\t 1 - Letöröd')
                        print('\t 2- inkább békén hagyod')
                        tores = beker('Hogyan cselekszel társadat látván: ')
                        if tores == 1:
                            print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                            print('Te hülye, ezt még a süket is meghallja, elkapnak és visznek is az elektromos székbe, VESZTETTÉL')
                            exit(0)
                        else:
                            print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                            print('Mostanára legalábbis békénhagytad, de beugrott, hogy mintha a raktárban tartanának néhány pót rudat, azt fel tudnád használni nyélként')
                            print('\t 1 - Még átgondolni')
                            print('\t 2 - Irány, azt hiszem jó a memóriám')
                            memoria = beker('Miként választasz:')
                            if memoria == 2: 
                                print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                print('ÉS tényleg jól emlékeztél, megszerezted, összeszerelted és kijutottál, NYERTÉL')
                                exit(0)
                            else:
                                print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                print('Inkább visszafordulsz, még átgondolod ezt')
                                print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                            print('Másnap ismét meglátod a rácsok közt bevilágító napfényt, és kikelsz az ágyból')
                            print('\t 1 - Elmész a nyél után keresni')
                            print('\t 2 - Rákérdezel a cellatársadra, hátha tud valami módot')
                            tarsas1 = beker('Hogyan cselekszel: ')
                            if tarsas1 == 1:
                                print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                print('Bizonytalanul továbbmész, de meglátsz egy őrt, és megtorpansz')
                                print('\t 1 - Tovább menni, el az őr mellett úgy kinézve mintha tudnád merre mész')
                                print('\t 2 - Visszafordulni, és inkább a cellatársadnál rákérdezni, majd követni utasításait')
                                visszafele = beker('Válassz: ')
                                if visszafele == 1:
                                    random3 = randint(1,2)
                                    if random3 == 1: 
                                            print('Egy 3 ajtós épületrészlegnél találod magadat, viszont melyik lehet a raktár ajtaja')
                                            print('\t1 - Első ajtó, kint egy kalapács logója látható az ajtón')
                                            print('\t2 - Második ajtó, rajta egy fegyver jel áll')
                                            print('\t3 - Harmadik ajtó, külsején egy rendőr jelzéssel')
                                            ajtok = beker('Melyik ajtót választod: ')
                                            if ajtok == 1:
                                                print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                                print('Ez itt a raktár része, itt ráleltél a nyélre, ámde visszafele egy őr megkérdezi hová tartasz vele')
                                                print('\t 1 - Egy társamnak viszem, eltört a felmosó nyele')
                                                print('\t 2 - Leütöd vele, és menekülsz')
                                                orok1es2 = beker('Mit teszel: ')
                                                if orok1es2 == 1:
                                                    print('Megszerezted a nyelet is')
                                                    nyel2 += 1
                                                else:
                                                    utes = randint(1,2)
                                                    if utes == 1:
                                                        print('Voltak még ott többen is, lefogtak és meglőttek, VESZTETTÉL') 
                                                        exit(0) 
                                                    else:
                                                        print('Megszerezted a nyelet is')
                                                        nyel2 += 1
                                            if ajtok == 2:
                                                print('Egy kis záras babrálás után beléptél, és mindenféle fegyverrel találtad magad szembe')
                                                print('Mélyen elgondolkozol, hogy vajon mit kéne tenned, ámde amikor megfordulsz')
                                                print('Ez egy csapda volt, VESZTETTÉL')
                                            if ajtok == 3:
                                                print('Most tényleg, mit vártál')
                                                print('Benyitottál és egy rakás rendőrtiszttel találtad szembe magad, letartóztattak, VESZTETTÉL')
                                                exit(0)
                                    if random3 == 2:
                                        print('Az úr megállított téged, és visszaküldött a cellába')
                                if  visszafele == 2:
                                        print('Visszatérsz a társadhoz, hogy meglásd, ő mit mondd')
                                        print('Azt mondja, hogy van a folyosó végén 3 ajtó, és semmilyen körülmények között ne menj be a másodikba')
                                        print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                        print('Azt mondja, hogy van a folyosó végén 3 ajtó, és semmilyen körülmények között ne menj be a másodikba')
                                        print('Elindulsz a folyosón...')
                                        print('Egy 3 ajtós épületrészlegnél találod magadat, viszont melyik lehet a raktár ajtaja')
                                        print('\t1 - Első ajtó, kint egy kalapács logója látható az ajtón')
                                        print('\t2 - Második ajtó, rajta egy fegyver jel áll')
                                        print('\t3 - Harmadik ajtó, külsején egy rendőr jelzéssel')
                                        ajtok = beker('Melyik ajtót választod: ')
                                if ajtok == 1:
                                    print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                    print('Ez itt a raktár része, itt ráleltél a nyélre, ámde visszafele egy őr megkérdezi hová tartasz vele')
                                    print('\t 1 - Egy társamnak viszem, eltört a felmosó nyele')
                                    print('\t 2 - Leütöd vele, és menekülsz')
                                    orok1es2 = beker('Mit teszel: ')
                                    if orok1es2 == 1:
                                        print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                        print('Megszerezted a nyelet is')
                                    else:
                                        utes = randint(1,2)
                                        if utes == 1:
                                            print('─────────────F─────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                            print('Voltak még ott többen is, lefogtak és meglőttek, VESZTETTÉL') 
                                            exit(0) 
                                        else:
                                            print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                            print('Megszerezted a nyelet is')
                                if ajtok == 2:
                                    print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                    print('Egy kis záras babrálás után beléptél, és mindenféle fegyverrel találtad magad szembe')
                                    print('Mélyen elgondolkozol, hogy vajon mit kéne tenned')
                                if ajtok == 3:
                                    print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                    print('Most tényleg, mit vártál')
                                    print('Benyitottál és egy rakás rendőrtiszttel találtad szembe magad, letartóztattak, VESZTETTÉL')
                                    exit(0)
                            else:        
                                print('Azt mondja, hogy van a folyosó végén 3 ajtó, és semmilyen körülmények között ne menj be a másodikba')
                                print('Elindulsz a folyosón...')
                                print('Egy 3 ajtós épületrészlegnél találod magadat, viszont melyik lehet a raktár ajtaja')
                                print('\t1 - Első ajtó, kint egy kalapács logója látható az ajtón')
                                print('\t2 - Második ajtó, rajta egy fegyver jel áll')
                                print('\t3 - Harmadik ajtó, külsején egy rendőr jelzéssel')
                                ajtok = beker('Melyik ajtót választod: ')
                                if ajtok == 1:
                                    print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                    print('Ez itt a raktár része, itt ráleltél a nyélre, ámde visszafele egy őr megkérdezi hová tartasz vele')
                                    print('\t 1 - Egy társamnak viszem, eltört a felmosó nyele')
                                    print('\t 2 - Leütöd vele, és menekülsz')
                                    orok1es2 = beker('Mit teszel: ')
                                    if orok1es2 == 1:
                                        print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                        print('Megszerezted a nyelet is')
                                    else:
                                        utes = randint(1,2)
                                        if utes == 1:
                                            print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                            print('Voltak még ott többen is, lefogtak és meglőttek, VESZTETTÉL') 
                                            exit(0) 
                                        else:
                                            print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                            print('Megszerezted a nyelet is')
                                            nyel += 1
                                            vodszog += 1
                                if ajtok == 2:
                                    print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                    print('Egy kis záras babrálás után beléptél, és mindenféle fegyverrel találtad magad szembe')
                                    print('Mélyen elgondolkozol, hogy vajon mit kéne tenned')
                                if ajtok == 3:
                                    print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                    print('Most tényleg, mit vártál')
                                    print('Benyitottál és egy rakás rendőrtiszttel találtad szembe magad, letartóztattak, VESZTETTÉL')
                                    exit(0)   
                        if random3 == 2:
                            print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                            print('Az úr megállított téged, és visszaküldött a cellába')                                    
                        else:
                            print('Azt mondja, hogy van a folyosó végén 3 ajtó, és semmilyen körülmények között ne menj be a másodikba')
                            return ajtok == 1
                        if nyel2 == 1:
                            print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                            print('Már csak egy vödröt és szögeket kell szereznek, de honnan is kéne szerezni olyat?')
                            print('\t Átkutatod, mi van körülötted')
                            print('\t Elkéred egy társadtól, mert vannak az ágya alatt ilyenek(for some reason)')
                            kellkeves = beker('Mi lenne a TE választásod')
                            if kellkeves == 1:
                                print('Találtál amit kell, gratulálok, összeraktad és kijutottál')
                                exit(0)
                            else:
                                picirandom = randint(1,2)
                                if picirandom == 1:
                                    print('Látta egyik társad hogy miben settenkedsz, de együttérzett veled és nem árult be, NYERTÉL')
                                    exit(0)
                                else:
                                    print('Nagyon sajnálom barátom, de ezt beszoptad, a cellatársad beköpött téged, vesztettél')
                                    exit(0)
                else:
                    print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                    print('Az egyik sarokban találsz egy nyelet, és elindulsz visszafelé, amilyen halkan csak tudsz')
                    print('Egy őr észrevesz, és megkérdőjelezi, hogy mit csinálsz itt, egy random fa nyéllel a kezedben')
                    print('\t 1 - Letagadod(egy cellatársnak viszed, eltört a felmosó nyele)')
                    print('\t 2 - Elnézést kér mielőtt agyonverne, és szépen visszahelyezed ahonnan hoztad')
                    orocske = beker('Te hogyan cselekednél: ')
                    if orocske == 1:
                        print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                        print('Ez bevállt, elhitte neked, megszerezted a nyelet')
                        print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                        print('Már csak egy vödröt és szögeket kell szereznek, de honnan is kéne szerezni olyat?')
                        print('\t 1 -Átkutatod, mi van körülötted')
                        print('\t 2 -Elkéred egy társadtól, mert vannak az ágya alatt ilyenek(for some reason)')
                        kellkeves = beker('Mi lenne a TE választásod')
                        if kellkeves == 1:
                            print('Találtál amit kell, gratulálok, összeraktad és kijutottál')
                            exit(0)
                        else:
                            picirandom = randint(1,2)
                            if picirandom == 1:
                                print('Látta egyik társad hogy miben settenkedsz, de együttérzett veled és nem árult be, NYERTÉL')
                                exit(0)
                            else:
                                print('Nagyon sajnálom barátom, de ezt beszoptad, a cellatársad beköpött téged, vesztettél')
                                exit(0)
                    else:
                        print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                        print('Gondolkodsz azon, hogyha csak egy picivel is óvtosabb lettél volna, el tudtad volna csempészni mellette')
                        print('\t 1 - Áhh, majd máskor visszatérek erre')
                        print('\t 2 - Hajrá, megbízok az ösztöneimben, menni fog ez mint az 1x1')
                        ujra = beker('Mi a következő lépésed az alábbiak közül')
                        if ujra == 1:
                            print('Visszakullogsz szemlesújtva a celládba')
                            print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                            print('Másnap reggel csodás napra ébredsz, és azt véled feldefedezni hogy a cellatársad éppen a padlót mossa fel')
                            print('Eszedbe jut a gondolat, miszerint ha letöröd a végét a felmósonak, lesz egy nyeled')
                            print('\t 1 - Letöröd')
                            print('\t 2- inkább békén hagyod')
                            tores = beker('Hogyan cselekszel társadat látván: ')
                            if tores == 1:
                                print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                print('Te hülye, ezt még a süket is meghallja, elkapnak és visznek is az elektromos székbe, VESZTETTÉL')
                                exit(0)
                            else:
                                print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                print('Mostanára legalábbis békénhagytad, de beugrott, hogy mintha a raktárban tartanának néhány pót rudat, azt fel tudnád használni nyélként')
                                print('\t 1 - Még átgondolni')
                                print('\t 2 - Irány, azt hiszem jó a memóriám')
                                memoria = beker('Miként választasz:')
                                if memoria == 2: 
                                    print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                    print('ÉS tényleg jól emlékeztél, megszerezted, összeszerelted és kijutottál, NYERTÉL')
                                    exit(0)
                                else:
                                    print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                print('Másnap ismét meglátod a rácsok közt bevilágító napfényt, és kikelsz az ágyból')
                                print('\t 1 - Elmész a nyél után keresni')
                                print('\t 2 - Rákérdezel a cellatársadra, hátha tud valami módot')
                                tarsas1 = beker('Hogyan cselekszel: ')
                                if tarsas1 == 1:
                                    print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                    print('Bizonytalanul továbbmész, de meglátsz egy őrt, és megtorpansz')
                                    print('\t 1 - Tovább menni, el az őr mellett úgy kinézve mintha tudnád merre mész')
                                    print('\t 2 - Visszafordulni, és inkább a cellatársadnál rákérdezni, majd követni utasításait')
                                    visszafele = beker('Válassz: ')
                                    if visszafele == 1:
                                        random3 = randint(1,2)
                                        if random3 == 1: 
                                                print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                                print('Egy 3 ajtós épületrészlegnél találod magadat, viszont melyik lehet a raktár ajtaja')
                                                print('\t1 - Első ajtó, kint egy kalapács logója látható az ajtón')
                                                print('\t2 - Második ajtó, rajta egy fegyver jel áll')
                                                print('\t3 - Harmadik ajtó, külsején egy rendőr jelzéssel')
                                                ajtok = beker('Melyik ajtót választod: ')
                                                if ajtok == 1:
                                                    print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                                    print('Ez itt a raktár része, itt ráleltél a nyélre, ámde visszafele egy őr megkérdezi hová tartasz vele')
                                                    print('\t 1 - Egy társamnak viszem, eltört a felmosó nyele')
                                                    print('\t 2 - Leütöd vele, és menekülsz')
                                                    orok1es2 = beker('Mit teszel: ')
                                                    if orok1es2 == 1:
                                                        print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                                        print('Megszerezted a nyelet is')
                                                    else:
                                                        utes = randint(1,2)
                                                        if utes == 1:
                                                            print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                                            print('Voltak még ott többek is, lefogtak és meglőttek, VESZTETTÉL') 
                                                            exit(0) 
                                                        else:
                                                            print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                                            print('Megszerezted a nyelet is')
                                                if ajtok == 2:
                                                    print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                                    print('Egy kis záras babrálás után beléptél, és mindenféle fegyverrel találtad magad szembe')
                                                    print('Mélyen elgondolkozol, hogy vajon mit kéne tenned, ámde amikor megfordulsz')
                                                    print('Ez egy csapda volt, VESZTETTÉL')
                                                if ajtok == 3:
                                                    print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                                    print('Most tényleg, mit vártál')
                                                    print('Benyitottál és egy rakás rendőrtiszttel találtad szembe magad, letartóztattak, VESZTETTÉL')
                                                    exit(0)
                                        if random3 == 2:
                                            print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                            print('Az úr megállított téged, és visszaküldött a cellába')
                                    if visszafele == 2:
                                            print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                            print('Visszatérsz a társadhoz, hogy meglásd, ő mit mondd')
                                else:
                                    print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                    print('Azt mondja, hogy van a folyosó végén 3 ajtó, és semmilyen körülmények között ne menj be a másodikba')
                                    print('Elindulsz a folyosón...')
                                    print('Egy 3 ajtós épületrészlegnél találod magadat, viszont melyik lehet a raktár ajtaja')
                                    print('\t1 - Első ajtó, kint egy kalapács logója látható az ajtón')
                                    print('\t2 - Második ajtó, rajta egy fegyver jel áll')
                                    print('\t3 - Harmadik ajtó, külsején egy rendőr jelzéssel')
                                    ajtok = beker('Melyik ajtót választod: ')
                                    if ajtok == 1:
                                        print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                        print('Ez itt a raktár része, itt ráleltél a nyélre, ámde visszafele egy őr megkérdezi hová tartasz vele')
                                        print('\t 1 - Egy társamnak viszem, eltört a felmosó nyele')
                                        print('\t 2 - Leütöd vele, és menekülsz')
                                        orok1es2 = beker('Mit teszel: ')
                                        if orok1es2 == 1:
                                            print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                            print('Megszerezted a nyelet is')
                                        else:
                                            utes = randint(1,2)
                                            if utes == 1:
                                                print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                                print('Voltak még ott többen is, lefogtak és meglőttek, VESZTETTÉL') 
                                                exit(0) 
                                            else:
                                                print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                                print('Megszerezted a nyelet is')
                                    if ajtok == 2:
                                        print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                        print('Egy kis záras babrálás után beléptél, és mindenféle fegyverrel találtad magad szembe')
                                        print('Mélyen elgondolkozol, hogy vajon mit kéne tenned')
                                    if ajtok == 3:
                                        print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                        print('Most tényleg, mit vártál')
                                        print('Benyitottál és egy rakás rendőrtiszttel találtad szembe magad, letartóztattak, VESZTETTÉL')
                                        exit(0)
                            if random3 == 2:
                                print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                print('Az úr megállított téged, és visszaküldött a cellába')
                        else:
                            hiszipiszi = randint(1,2)
                            if hiszipiszi == 1:
                                print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                print('Sajnálom tesókám, másodszorra már nem hitt a faszságodnak, VESZTETTÉL')
                                exit(0)
                            else:
                                print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                print('Gratula, megszerezted a nyelet')
                                nyel2 += 1  
                            if visszafele == 2:
                                    print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                    print('Visszatérsz a társadhoz, hogy meglásd, ő mit mondd')        
                    if random2 == 2: 
                    
                        print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                        print('Egy őr észrevesz, és megkérdőjelezi, hogy mit csinálsz itt, egy random fa nyéllel a kezedben')
                        print('\t 1 - Letagadod(egy cellatársnak viszed, eltört a felmosó nyele)')
                        print('\t 2 - Elnézést kér mielőtt agyonverne, és szépen visszahelyezed ahonnan hoztad')
                        orocske = beker('Te hogyan cselekednél: ')
                        if orocske == 1:
                            print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                            print('Ez bevállt, elhitte neked, megszerezted a nyelet')
                            print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                            print('Már csak egy vödröt és szögeket kell szereznek, de honnan is kéne szerezni olyat?')
                            print('\t 1 -Átkutatod, mi van körülötted')
                            print('\t 2 -Elkéred egy társadtól, mert vannak az ágya alatt ilyenek(for some reason)')
                            kellkeves = beker('Mi lenne a TE választásod')
                            if kellkeves == 1:
                                print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                print('Találtál amit kell, gratulálok, összeraktad és kijutottál')
                                exit(0)
                            else:
                                picirandom = randint(1,2)
                                if picirandom == 1:
                                    print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                    print('Látta egyik társad hogy miben settenkedsz, de együttérzett veled és nem árult be, NYERTÉL')
                                    exit(0)
                                else:
                                    print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                    print('Nagyon sajnálom barátom, de ezt beszoptad, a cellatársad beköpött téged, vesztettél')
                                    exit(0)
                        else:
                            print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                            print('Gondolkodsz azon, hogyha csak egy picivel is óvatosabb lettél volna, el tudtad volna csempészni mellette')
                            print('\t 1 - Áhh, majd máskor visszatérek erre')
                            print('\t 2 - Hajrá, megbízok az ösztöneimben, menni fog ez mint az 1x1')
                            ujra = beker('Mi a következő lépésed az alábbiak közül')
                            if ujra == 1:
                                print('Visszakullogsz szemlesújtva a celládba')    
                            else:
                                hiszipiszi = randint(1,2)
                                if hiszipiszi == 1:
                                    print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                    print('Sajnálom tesókám, másodszorra már nem hitt a faszságodnak, VESZTETTÉL')
                                    exit(0)
                                else:
                                    print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                    print('Gratula, megszerezted a nyelet')
                                    nyel2 += 1
                                    if nyel2 == 1:
                                        print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                            print('Már csak egy vödröt és szögeket kell szereznek, de honnan is kéne szerezni olyat?')
                            print('\t Átkutatod, mi van körülötted')
                            print('\t Elkéred egy társadtól, mert vannak az ágya alatt ilyenek(for some reason)')
                            kellkeves = beker('Mi lenne a TE választásod')
                            if kellkeves == 1:
                                print('Találtál amit kell, gratulálok, összeraktad és kijutottál')
                                exit(0)
                            else:
                                picirandom = randint(1,2)
                                if picirandom == 1:
                                    print('Látta egyik társad hogy miben settenkedsz, de együttérzett veled és nem árult be, NYERTÉL')
                                    exit(0)
                                else:
                                    print('Nagyon sajnálom barátom, de ezt beszoptad, a cellatársad beköpött téged, vesztettél')
                                    exit(0)
                    else:
                        print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                        print('\t 1 - Letagadod(egy cellatársnak viszed, eltört a felmosó nyele)')
                        print('\t 2 - Elnézést kér mielőtt agyonverne, és szépen visszahelyezed ahonnan hoztad')
                        orocske = beker('Te hogyan cselekednél: ')
                        if orocske == 1:
                            print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                            print('Ez bevállt, elhitte neked, megszerezted a nyelet')
                            nyel2 += 1
                        else:
                            print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                            print('\t 1 - Áhh, majd máskor visszatérek erre')
                            print('\t 2 - Hajrá, megbízok az ösztöneimben, menni fog ez mint az 1x1')
                            ujra = beker('Mi a következő lépésed az alábbiak közül')
                            if ujra == 1:
                                print('Visszakullogsz szemlesújtva a celládba')
                                
                            else:
                                hiszipiszi = randint(1,2)
                                if hiszipiszi == 1:
                                    print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                    print('Sajnálom tesókám, másodszorra már nem hitt a faszságodnak, VESZTETTÉL')
                                    exit(0)
                                else:
                                    print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                    print('Gratula, megszerezted a nyelet')
                            if nyel2 == 1:
                                print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                print('Már csak egy vödröt és szögeket kell szereznek, de honnan is kéne szerezni olyat?')
                                print('\t Átkutatod, mi van körülötted')
                                print('\t Elkéred egy társadtól, mert vannak az ágya alatt ilyenek(for some reason)')
                                kellkeves = beker('Mi lenne a TE választásod')
                                if kellkeves == 1:
                                    print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                    print('Találtál amit kell, gratulálok, összeraktad és kijutottál')
                                    exit(0)
                                else:
                                    picirandom = randint(1,2)
                                    if picirandom == 1:
                                        print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                        print('Látta egyik társad hogy miben settenkedsz, de együttérzett veled és nem árult be, NYERTÉL')
                                        exit(0)
                                    else:
                                        print('──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                                        print('Nagyon sajnálom barátom, de ezt beszoptad, a cellatársad beköpött téged, vesztettél')
                                        exit(0)
                    if nyel == 1 and vodszog == 1:
                        print('Ezt a kettőt összeeszkabáltad, gratulálok, NYERTÉL')

            else:
                exit(0)