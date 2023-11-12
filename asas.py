import stats
from random import randint
from safe_input import beker
import os

nyel = 0
nyel2 = 0
vodszog = 0
vodor = 0
szogek = 0
os.system('cls')

def masnap():
    os.system('cls')
    stats.energia -= 2
    stats.line()
    stats.print_stats()
    print('Másnap ismét meglátod a rácsok közt bevilágító napfényt, és kikelsz az ágyból')
    print('\t 1 - Elmész a nyél után keresni')
    print('\t 2 - Rákérdezel a cellatársadra, hátha tud valami módot')
    tarsas1 = beker('Hogyan cselekszel: ')
    if tarsas1 == 1:
        os.system('cls')
        stats.line()
        stats.print_stats()
        stats.energia -= 2
        print('Bizonytalanul továbbmész, de meglátsz egy őrt, és megtorpansz')
        print('\t 1 - Tovább menni, el az őr mellett úgy kinézve mintha tudnád merre mész')
        print('\t 2 - Visszafordulni, és inkább a cellatársadnál rákérdezni, majd követni utasításait')
        visszafele = beker('Válassz: ')
        if visszafele == 1:
            random3 = randint(1, 2)
            if random3 == 1:
                os.system('cls')
                stats.line()
                stats.print_stats()
                stats.energia -= 2
                print('Egy 3 ajtós épületrészlegnél találod magadat, viszont melyik lehet a raktár ajtaja')
                print('\t1 - Első ajtó, kint egy kalapács logója látható az ajtón')
                print('\t2 - Második ajtó, rajta egy fegyver jel áll')
                print('\t3 - Harmadik ajtó, külsején egy rendőr jelzéssel')
                ajtok = beker('Melyik ajtót választod: ')
                ajtok_kezel(ajtok, )
            if random3 == 2:
                os.system('cls')
                stats.line()
                print('Az úr megállított téged, és visszaküldött a cellába')
                stats.energia -= 2
        if visszafele == 2:
            os.system('cls')
            stats.line()
            print('Visszatérsz a társadhoz, hogy meglásd, ő mit mondd')
            stats.energia -= 2
            ajtok_beker()
    else:
        os.system('cls')
        stats.line()
        stats.print_stats()
        stats.energia -= 2
        ajtok = ajtok_beker()
        ajtok_kezel(ajtok,)     

def kerdojel():
    os.system('cls')
    stats.lebukas += 4
    stats.energia -= 2
    stats.line()
    stats.print_stats()
    print('Egy őr észrevesz, és megkérdőjelezi, hogy mit csinálsz itt, egy random fa nyéllel a kezedben')
    print('\t 1 - Letagadod(egy cellatársnak viszed, eltört a felmosó nyele)')
    print('\t 2 - Elnézést kér mielőtt agyonverne, és szépen visszahelyezed ahonnan hoztad')
    stats.lebukas += 4
    orocske = beker('Te hogyan cselekednél: ')
    if orocske == 1:
        os.system('cls')
        stats.line()
        print('Ez bevállt, elhitte neked, megszerezted a nyelet')
        vodor()
    else:
        os.system('cls')
        stats.line()
        stats.print_stats()
        stats.energia -= 2
        print('Gondolkodsz azon, hogyha csak egy picivel is óvatosabb lettél volna, el tudtad volna csempészni mellette')
        print('\t 1 - Áhh, majd máskor visszatérek erre')
        print('\t 2 - Hajrá, megbízok az ösztöneimben, menni fog ez mint az 1x1')
        ujra = beker('Mi a következő lépésed az alábbiak közül')
        if ujra == 1:
            os.system('cls')
            print('Visszakullogsz szemlesújtva a celládba')
            stats.energia -= 2
            masnap(nev)
        else:
            hiszipiszi = randint(1, 2)
            if hiszipiszi == 1:
                os.system('cls')
                stats.line()
                print('Sajnálom tesókám, másodszorra már nem hitt a faszságodnak, VESZTETTÉL')
                exit(0)
            else:
                os.system('cls')
                stats.line()
                print('Gratula, megszerezted a nyelet')
                nyel2 += 1
                stats.energia -= 2
                if nyel == 1 and vodszog == 1:
                    os.system('cls')
                    print('Ezt a kettőt összeeszkabáltad, gratulálok, NYERTÉL')
                    exit(0)
    if nyel == 1:
        vodor()

def terv1_kezel(nev):
    os.system('cls')
    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    stats.print_stats()
    print('Szeretnéd elmondani bárkinek is terveidet?')
    print('\t 1 - Igen')
    print('\t 2 - Nem')
    szembe = beker('Mi a választásod: ')
    if szembe == 2:
        os.system('cls')
        print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        print('Elsettenkedett az őrök mellett, és megszerezte az ásóját')
        print('Egyedül is könnyedén kiásta magát pár nap alatt, NYERTÉL')
        exit(0)
    random1 = randint(1, 2)
    if random1 == 1:
        os.system('cls')
        print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        print('A személy csúnyán beköpöte, VESZTETTÉL')
        exit(0)
    
    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    stats.print_stats()
    print('Felajánlotta segítségét, így gyorsabban tud majd végezni, hogy válaszol')
    print('\t 1 - Elfogadod ')
    print('\t 2 - Nem fogadod el')
    help = beker(f'Mit tennél "{nev}" helyében?')
    if help == 1:
        os.system('cls')
        print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        print('Az úr segítségének köszönhetően hamarabb, illetve mindketten kijutottatok, NYERTÉL')
        exit(0)
    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    stats.print_stats()
    stats.energia -= 2
    print('Hirtelen mérges lett választ hallván, és az éj leple alatt ripityára töri az ásót. Csalódóttan figyeli, de cselekednie kell, mit tesz?')
    print('\t 1 - Újrakezdi az egész operációt')
    print('\t 2 - Öngyilkos lesz')
    melyik = beker('Válassz helyette: ')
    stats.energia -= 2
    if melyik == 1:
        # VIssza kellene menni az első három választási lehetőséghez.
        os.system('cls')
        print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        print('Elhatározta hogy újrakezdi az operációt')
    else:
        os.system('cls')
        print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        print('Öngyilkos lettél, vége a játéknak')
        exit(0)

def terv2_kezel(nev):
    os.system('cls')
    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    stats.print_stats()
    stats.energia -= 2
    print(f'Az ajtók mellett két őr áll, viszont "{nev}" távolról észreveszi őket, és gondolkozni kezd')
    print('\t 1 - Visszafordul')
    print('\t 2 - Tovább megy')
    orok = beker('Az ő helyében te hogy cselekednél?')
    if orok == 2:
        os.system('cls')
        print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        print('Minél közelebb ért, egyre gyanúsabbnak tűnt, és elkapták. VESZTETTÉL')
        exit(0)
    else:
        os.system('cls')
        print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        print('Visszament a cellájába, így maradt még ideje átgondolni a következő lépést')

def ajtok_kezel(ajtok, ):
    global nyel2
    if ajtok == 1:
        os.system('cls')
        print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        stats.print_stats()
        stats.energia -= 2
        print('Ez itt a raktár része, itt ráleltél a nyélre, ámde visszafele egy őr megkérdezi hová tartasz vele')
        print('\t 1 - Egy társamnak viszem, eltört a felmosó nyele')
        print('\t 2 - Leütöd vele, és menekülsz')
        orok1es2 = beker('Mit teszel: ')
        if orok1es2 == 1:
            os.system('cls')
            print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
            print('Megszerezted a nyelet is')
            nyel2 += 1
            stats.energia -= 2
            if nyel2 == 1:
                os.system('cls')
                vodor()
        else:
            os.system('cls')
            utes = randint(1, 2)
            if utes == 1:
                os.system('cls')
                print('─────────────F─────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
                print('Voltak még ott többen is, lefogtak és meglőttek, VESZTETTÉL')
                exit(0)
            else:
                os.system('cls')
                print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                print('Megszerezted a nyelet is')
                nyel2 += 1
                stats.energia -= 2
    if ajtok == 2:
        os.system('cls')
        print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        print('Egy kis záras babrálás után beléptél, és mindenféle fegyverrel találtad magad szembe')
        print('Mélyen elgondolkozol, hogy vajon mit kéne tenned')
        stats.energia -= 2
    if ajtok == 3:
        os.system('cls')
        print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        print('Most tényleg, mit vártál')
        print('Benyitottál és egy rakás rendőrtiszttel találtad szembe magad, letartóztattak, VESZTETTÉL')
        exit(0)

def ajtok_beker(told=True):
    if told:
        os.system('cls')
        stats.print_stats()
        stats.energia -= 2
        print('Azt mondja, hogy van a folyosó végén 3 ajtó, és semmilyen körülmények között ne menj be a másodikba')
        print('Elindulsz a folyosón...')
    print('Egy 3 ajtós épületrészlegnél találod magadat, viszont melyik lehet a raktár ajtaja')
    print('\t1 - Első ajtó, kint egy kalapács logója látható az ajtón')
    print('\t2 - Második ajtó, rajta egy fegyver jel áll')
    print('\t3 - Harmadik ajtó, külsején egy rendőr jelzéssel')
    ajtok = beker('Melyik ajtót választod: ')
    return ajtok

def vodor():
    stats.energia -= 2
    os.system('cls')
    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    stats.print_stats()
    print('Már csak egy vödröt és szögeket kell szereznek, de honnan is kéne szerezni olyat?')
    print('\t 1 - Átkutatod, mi van körülötted')
    print('\t 2 - Elkéred egy társadtól, mert vannak az ágya alatt ilyenek(for some reason)')
    kellkeves = beker('Mi lenne a TE választásod: ')
    if kellkeves == 1:
        os.system('cls')
        print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        print('Találtál amit kell, gratulálok, összeraktad és kijutottál')
    else:
        os.system('cls')
        picirandom = randint(1, 2)
        if picirandom == 1:
            os.system('cls')
            print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
            print('Látta egyik társad hogy miben settenkedsz, de együttérzett veled és nem árult be, NYERTÉL')
        else:
            os.system('cls')
            print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
            print('Nagyon sajnálom barátom, de ezt beszoptad, a cellatársad beköpött téged, vesztettél')
    exit(0)

def introduction(nev, valasz):
    print(f'"{nev}" elhatározta, hogy ki fog ásni a börtönből, aminek végrehajtásához egy ásót kell megszereznie.')
    print('A játék során te fogod irányítani minden választását, sok sikert!')
    stats.line()
    print('Egy ásó megszerzésére 2 lehetősége van: ')
    print('\t 1 - Lopás a raktárból')
    print('\t 2 - Kézi ásó készítése')
    valasztott1 = int(input('Válaszd ki az egyik lehetőséget: '))
    if valasztott1 == 1:
        valasztott_1()
    else:
        valasztott_2(nev)

def valasztott_1(nev):
    if valasztott1 == 1:
            os.system('cls') 
            stats.line()
            stats.print_stats()
            print(f'"{nev}" úgy dönt, hogy be fog szökni a börtön raktárába, ahonnan remélhetőleg ki tud majd hozni egy ásót, viszont döntenie kell, mikor próbálkozik ezzel')
            print('\t 1 - Nappal')
            print('\t 2 - Éjjel')
            terv = beker('Válassz, szerinted melyik lenne a jobb választás: ')
            if terv == 1:
                terv1_kezel(nev)
                
            if terv == 2:
                terv2_kezel(nev)
                

def valasztott_2(nev):
            os.system('cls')
            stats.line()
            stats.print_stats()
            print(f'"{nev}" úgy döntött, hogy maga fog el készíteni egy ásót, amivel majd utána kiáshatja magát')
            print('Ehhez két dologra van szüksége: vödör + szögek, nyél')
            print('\t 1 - Folytatás')
            print('\t 2 - Kilépés')
            terv2 = beker('Válassz, mit tegyen: ')
            if terv2 == 1:
                sarok()
            else:
                print('Köszönjük, hogy kipróbáltad')
                exit()

def sarok(energia,stats):
    os.system('cls')
    stats.lebukas += 4
    stats.energia -= 2
    stats.line()
    stats.print_stats()
    folyoso = randint(1,2)
    if folyoso == 1:
        energia -= 2
        print('Az egyik sarokban találsz egy nyelet,gyorsan felkapod, és elindulsz visszafelé, amilyen halkan csak tudsz')
        print('Egy őr észrevesz, és megkérdőjelezi, hogy mit csinálsz itt, egy random fa nyéllel a kezedben')
        print('\t 1 - Letagadod(egy cellatársnak viszed, eltört a felmosó nyele)')
        print('\t 2 - Elnézést kérsz mielőtt agyonverne, és szépen visszahelyezed ahonnan hoztad')
        orocske = beker('Te hogyan cselekednél: ')
        if orocske == 1:
            os.system('cls')
            stats.line()
            print('Ez bevállt, elhitte neked, megszerezted a nyelet')
            vodor()
        else:
            os.system('cls')
            stats.line()
            stats.print_stats()
            stats.energia -= 2
            print('Gondolkodsz azon, hogyha csak egy picivel is óvatosabb lettél volna, el tudtad volna csempészni mellette')
            print('\t 1 - Áhh, majd máskor visszatérek erre')
            print('\t 2 - Hajrá, megbízok az ösztöneimben, menni fog ez mint az 1x1')
            ujra = beker('Mi a következő lépésed az alábbiak közül')
            if ujra == 1:
                os.system('cls')
                print('Visszakullogsz szemlesújtva a celládba')
    else:
        os.system('cls')
        stats.line()
        stats.print_stats()
        stats.energia -= 2
        print('Miközben a folyosókon kuszól, szembetalálkozol egy felmosóvödörrel, és amikor belenézel, néhány szöget vélsz felfedezni')
        print('\n')
        print('Gratulálok, megszerezted a vödröt, és a szögeket')
        print('\n')
        print('Elmész a nyél után is kutatni, vagy inkább mára abbahagyod a császkálást?')
        print('\t 1 - Folytatom')
        print('\t 2 - Visszatérek a cellába')
        nyel = beker('Mit választasz következő lépésnek: ')
        if nyel == 1:
            os.system('cls')
            stats.line()
            print('A kezedben lévő vödör többször is megzörrent, meghallottak, és elkaptak, VESZTETTÉL')
            exit(0)
        else:
            os.system('cls')
            stats.line()
            stats.print_stats()
            print('Másnap reggel csodás napra ébredsz, és azt véled feldefedezni hogy a cellatársad éppen a padlót mossa fel')
            print('Eszedbe jut a gondolat, miszerint ha letöröd a végét a felmósonak, lesz egy nyeled')
            print('\t 1 - Letöröd')
            print('\t 2 - Inkább békén hagyod')
            tores = beker('Hogyan cselekszel társadat látván: ')
            if tores == 1:
                os.system('cls')
                stats.line()
                print('Te hülye, ezt még a süket is meghallja, elkapnak és visznek is az elektromos székbe, VESZTETTÉL')
                exit(0)
            else:
                os.system('cls')
                stats.line()
                stats.print_stats()
                stats.energia -= 2
                print('Mostanára legalábbis békénhagytad, de beugrott, hogy mintha a raktárban tartanának néhány pót rudat, azt fel tudnád használni nyélként')
                print('\t 1 - Még átgondolni')
                print('\t 2 - Irány, azt hiszem jó a memóriám')
                memoria = beker('Miként választasz:')
                if memoria == 2:
                    os.system('cls')
                    stats.line()
                    print('ÉS tényleg jól emlékeztél, megszerezted, összeszerelted és kijutottál, NYERTÉL')
                    exit(0)
                else:
                    os.system('cls')
                    stats.line()
                    print('Inkább visszafordulsz, még átgondolod ezt')
                    stats.energia -= 2
                    

def shop():
    os.system('cls')
    print.stats
    print('Üdvözöllek Ezüstfogú Károly boltjában, gyorsan válassz, aztán tűnés innen')
    print('1 - Egy nagy tál leves +3 enegiát ad')
    print('Ára : 200')
    print('2 - Egy teljes rendőr álöltözetm, amellyel van esélyed bevegyülni')
    print('Ára : 800 Ft')
    print('3 - Egy vödör, az ásó egyik alkatrésze')
    print('Ára : 300 Ft')
    print('4 - Egy fa nyél, az ásó egyik alkatrésze')
    print('Ára : 400 Ft')
    print('5 - Pár darab szög, az ásó egyik alkatrésze')
    print('Ára : 300 Ft')
    print('6 - Egy kis pisztoly, ki tudja mire lehet még jó')
    print('Ára : 900 Ft')
    bolt_one = beker('Mit szeretnél vásárolni: ')
    if bolt_one == 1:
        print('Megvetted a levest, + 3 energia')
        stats.energia += 1
    elif bolt_one == 2:
        print('Megvásároltad a ruhát')
        print('És most tűnj innen, mielőtt mindkettőnket meglátnak')
        stats.ruha += 1
    elif bolt_one == 3:
        print('Megszerezted a vödröt, ami az ásó egyik alkatrésze, ha kicsit hajlítgatod')
        vodor += 1
    elif bolt_one == 4:
        print('Megvetted az ásónak a nyelét, ')
        nyel += 1
    elif bolt_one == 5:
        print('Megvetted az összeszereléshez szükséges egy felszerelést, amivel rögzíthetsz alkatrészeket egymáshoz')
        szogek += 1
    elif bolt_one == 6:
        print('Megvetted a pisztolyt, csak okosan vele, ki tudja mire tudod majd használni')
        fegyver += 1