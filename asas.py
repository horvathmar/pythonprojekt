import stats
from random import randint
from safe_input import beker
import os

ruha = 0
fegyver = 0
nyel = 0
nyel2 = 0
vodor = 0
szogek = 0
os.system('cls')


def masnap(nev, told=True):
    os.system('cls')
    stats.energia -= 2
    stats.line()
    stats.print_stats()
    print('Másnap ismét meglátod a rácsok közt bevilágító napfényt, és kikelsz az ágyból')
    print('\t 1 - Elmész a nyél után keresni')
    print('\t 2 - Rákérdezel a cellatársadra, hátha tud valami módot')
    print('\t 3 - A helyi feketén működő bolt meglátogatása')
    print('\t 4 - úgy döntesz, öngyilkos leszel')
    tarsas1 = beker('Mit szeretnél tenni: ')
    if tarsas1 == 1:
        os.system('cls')
        stats.line()
        stats.print_stats()
        stats.energia -= 2
        print('Bizonytalanul továbbmész, de meglátsz egy őrt, és megtorpansz')
        print('\t 1 - Tovább menni, el az őr mellett úgy kinézve mintha tudnád merre mész')
        print('\t 2 - Visszafordulni, és inkább a cellatársadnál rákérdezni, majd követni utasításait')
        visszafele = beker('Mit szeretnél tenni:')
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
                ajtok_kezel(ajtok, nev)
            if random3 == 2:
                os.system('cls')
                stats.line()
                print('Az úr megállított téged, és visszaküldött a cellába')
                stats.energia -= 2
                masnap(nev)
        if visszafele == 2:
            os.system('cls')
            stats.line()
            print('Visszatérsz a társadhoz, hogy meglásd, ő mit mondd')
            stats.energia -= 2
            ajtok_beker()
    if tarsas1 == 2:
        ajtok_beker(nev, told=True )
    if tarsas1 == 3:
        shop(nev)
    if tarsas1 == 4:
        os.system('cls')
        print('Levetetted magad az épület tetejéről')
        print('Vesztettél')
        exit()
    

def kerdojel(nev):
    global nyel2
    os.system('cls')
    stats.lebukas += 4
    stats.energia -= 2
    stats.line()
    stats.print_stats()
    print('Egy őr észrevesz, és megkérdőjelezi, hogy mit csinálsz itt, egy random fa nyéllel a kezedben')
    print('\t 1 - Letagadod(egy cellatársnak viszed, eltört a felmosó nyele)')
    print('\t 2 - Elnézést kér mielőtt agyonverne, és szépen visszahelyezed oda, ahonnan hoztad')
    stats.lebukas += 4
    orocske = beker('Mit szeretnél tenni:')
    if orocske == 1:
        os.system('cls')
        stats.line()
        print('Ez bevállt, elhitte neked, megszerezted a nyelet')
        vodro(nev)
    else:
        os.system('cls')
        stats.line()
        stats.print_stats()
        stats.energia -= 2
        print('Gondolkodsz azon, hogyha csak egy picivel is óvatosabb lettél volna, el tudtad volna csempészni mellette')
        print('\t 1 - Áhh, majd máskor visszatérek erre')
        print('\t 2 - Hajrá, megbízok az ösztöneimben, menni fog ez mint az 1x1')
        print('\t 3 - A helyi feketén működő bolt meglátogatása')
        print('\t 4 - úgy döntesz, öngyilkos leszel')
        ujra = beker('Mit szeretnél tenni')
        if ujra == 1:
            os.system('cls')
            print('Visszakullogsz szemlesújtva a celládba')
            stats.energia -= 2
            masnap(nev)
        elif ujra == 2:
            hiszipiszi = randint(1, 2)
            if hiszipiszi == 1:
                os.system('cls')
                stats.line()
                print('Második próbálkozásodkor is rajtakapott, de ezúttal nem volt olyan elnéző')
                print('Rendesen elvert téged egy gumibottal, majd visszaküldött a celládba')
                stats.egeszseg -= 5
                masnap(nev)
            else:
                os.system('cls')
                stats.line()
                print('Gratulálok, megszerezted a nyelet')
                nyel += 1
                stats.energia -= 2
                vodro(nev)
                if nyel == 1 and vodor == 1 and szogek == 1:
                    os.system('cls')
                    print('Ezt a kettőt összeeszkabáltad, gratulálok, NYERTÉL')
                    exit(0)
        elif ujra == 3:
            shop()
        elif ujra == 4:
            os.system('cls')
            print('Levetetted magad az épület tetejéről')
            print('Vesztettél')
            exit()

    if nyel == 1:
        vodro(nev)


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
    segitseg = beker(f'Mit szeretnél tenni:')
    if segitseg == 1:
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
    melyik = beker('Mit szeretnél tenni:')
    stats.energia -= 2
    if melyik == 1:
        print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        print('Elhatározta hogy újrakezdi az operációt')
    else:
        os.system('cls')
        print('Levetetted magad az épület tetejéről')
        print('Vesztettél')
        exit()


def terv2_kezel(nev):
    os.system('cls')
    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    stats.print_stats()
    stats.energia -= 2
    print(f'{nev} a folyosók kövein kezdd el haladni')
    print(f'Az ajtók mellett két őr áll, viszont ő távolról észreveszi őket, és gondolkozni kezd')
    print('\t 1 - Visszafordul')
    print('\t 2 - Tovább megy')
    print('\t 3 - A helyi feketén működő bolt meglátogatása')
    print('\t 4 - úgy döntesz, öngyilkos leszel')
    orok = beker('Az ő helyében te hogy cselekednél?')
    if orok == 3:
        shop()
    elif orok == 4:
        os.system('cls')
        print('Levetetted magad az épület tetejéről')
        print('Vesztettél')
        exit()
    elif orok == 2:
        os.system('cls')
        print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        print('Minél közelebb ért, egyre gyanúsabbnak tűnt, és elkapták. VESZTETTÉL')
        exit(0)
    elif orok == 1:
        os.system('cls')
        print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        print('Visszament a cellájába, így maradt még ideje átgondolni a következő lépést')
        masnap(nev)




def ajtok_beker(nev, told=True):
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
    ajtok_kezel(ajtok, nev)

def ajtok_kezel(ajtok, nev):
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
            nyel += 1
            stats.energia -= 2
            if nyel == 1:
                os.system('cls')
            vodro(nev)
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
        stats.print_stats()
        stats.lebukas += 8
        print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        print('Egy kis záras babrálás után beléptél, és mindenféle fegyverrel találtad magad szembe')
        print('Mélyen elgondolkozol, hogy vajon mit kéne tenned')
        print('\t 1 - Felkapni egy fegyvert, majd elfutni vele, amilyen gyorsan tudsz')
        print('\t 2 - A zsaruk már jönnek érted, inkább megadod magad')
        stats.energia -= 2
        zsaruk = beker('Miként döntesz: ')
        if zsaruk == 1:
            kapas = randint(1,2)
            if kapas == 1:
                os.system('cls')
                stats.line()
                print('Bármennyire is igyekeztél, el láblövés után te sem tudtál messzire futni')
                print('Elkaptak, majd megműtenek, és mész vissza a celládba, plusz 2 év letöltendővel')
                print('Vesztettél')
                exit()
            else:
                print('Egy nagy futás és sokáig tartó bújás után előjöhetsz')
                print('Megszerezted a pisztolyt')
                fegyver += 1
                energia -= 2
                lebukas += 3  
                hova = randint(1,4)
                if hova == 1: 
                    masnap()
                elif hova == 2:
                    vodro()
                elif hova == 3:
                    folyoso_nyel()

    if ajtok == 3:
        os.system('cls')
        print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        print('Most tényleg, mit vártál')
        print('Benyitottál és egy rakás rendőrtiszttel találtad szembe magad, letartóztattak, VESZTETTÉL')
        exit(0)


def vodro(nev):
    stats.energia -= 2
    os.system('cls')
    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    stats.print_stats()
    print('Már csak egy vödröt és szögeket kell szereznek, de honnan is kéne szerezni olyat?')
    print('\t 1 - Átkutatod, mi van körülötted')
    print('\t 2 - Elkéred egy társadtól, mert vannak az ágya alatt ilyenek(for some reason)')
    print('\t 3 - A helyi feketén működő bolt meglátogatása')
    print('\t 4 - úgy döntesz, öngyilkos leszel')
    kellkeves = beker('Mit szeretnél tenni: ')
    if kellkeves == 3:
        shop()
    elif kellkeves == 4:
        os.system('cls')
        print('Levetetted magad az épület tetejéről')
        print('Vesztettél')
        exit()
    elif kellkeves == 1:
        os.system('cls')
        print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        print('Találtál amit kell, gratulálok, összeraktad és kijutottál')
    elif kellkeves == 2:
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


def folyoso_vodor(nev):
    global vodor, fegyver, nyel
    os.system('cls')
    stats.line()
    stats.print_stats()
    stats.energia -= 2
    print('Miközben a folyosókon kúszol, szembetalálkozol egy felmosóvödröt, a kezedbe veszed')
    print('\n')
    print('Gratulálok, megszerezted a vödröt')
    vodor += 1
    print('\n')
    print('Több lehetőséged is van a továbbhaladásra')
    print('\t 1 - Folytatom')
    print('\t 2 - Visszatérek a cellába')
    print('\t 3 - A helyi feketén működő bolt meglátogatása')
    print('\t 4 - úgy döntesz, öngyilkos leszel')
    nyel = beker('Mit választasz következő lépésnek: ')
    if nyel == 1:
        os.system('cls')
        stats.line()
        print('A kezedben lévő vödör többször is megzörrent, meghallottak, és elkaptak, VESZTETTÉL')
        exit(0)
    elif nyel == 3:
        shop()
    elif nyel == 4:
        os.system('cls')
        print('Levetetted magad az épület tetejéről')
        print('Vesztettél')
        exit()
    elif nyel == 2:
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
            print('Sajnos amikor ezt cselekedted, észreveszed, hogy a hozzátok közeli őr közeledik a cellátok felé')
            print('\t 1 - felveszed az ál rendőrruhádat, amivel van esélyed eltusolni az ügyet, ha kilépsz benne a folyosóra, és csak normálisan viselkedsz')
            print('\t 2 - Előveszed a fegyvered   ')

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
                memorandom = randint(1, 3)
                if memorandom == 1:
                    os.system('cls')
                    stats.line()
                    print('ÉS tényleg jól emlékeztél, megszerezted, összeszerelted és kijutottál, NYERTÉL')
                    exit(0)
                elif memorandom == 2:
                    os.system('cls')
                    stats.line()
                    print('ÉS tényleg jól emlékeztél, megszerezted, összeszerelted és kijutottál, NYERTÉL')
                    exit(0)
                elif memorandom == 3:
                    print('Az odavezető úton őrőket vélsz felfedezni')
                    terv2_kezel(nev)
            else:
                os.system('cls')
                stats.line()
                stats.print_stats()
                print('Inkább visszafordulsz, még átgondolod ezt')
                stats.energia -= 2
                masnap(nev)


def introduction(nev):
    while True:
        os.system('cls')
        print(f'"{nev}" elhatározta, hogy ki fog ásni a börtönből, aminek végrehajtásához egy ásót kell megszereznie, vagy összeraknia')
        print('A játék során te fogod irányítani minden választását, sok sikert!')
        stats.line()
        print('Egy ásó megszerzésére 2 lehetősége van: ')
        print('\t 1 - Lopás a raktárból')
        print('\t 2 - Kézi ásó készítése')
        valasztott1 = int(input('Válaszd ki az egyik lehetőséget: '))
        if valasztott1 == 1:
            valasztott_1(nev)
        else:
            valasztott_2(nev)


def introduction_2(nev):
    print('Másnap reggel felkelsz, és bevilágítanak a napnak sugarai a cella rácsain keresztül')
    print('Bármennyire is csalódott most, ha tényleg ki akar jutni, újra kell kezdenie a dolgokat')
    stats.line()
    print('\t 1 - Lopás a raktárból')
    print('\t 2 - Kézi ásó készítése')
    valasztott1 = int(input('Milyen módon szeretnél nekivágni az újabb próbálkozásnak'))
    if valasztott1 == 1:
        valasztott_1(nev)
    else:
        valasztott_2(nev)


def valasztott_1(nev):
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
    print(f'"{nev}" úgy döntött, hogy maga fog el készíteni egy ásót, amivel majd utána kiáshatja magát')
    print('Ehhez három dologra van szüksége: vödör, szögek, nyél')
    print('Sok sikert a játékhoz!')
    v_or_ny = randint(1, 2)
    if v_or_ny == 1:
        folyoso_nyel(nev, nyel)
    else:
        folyoso_vodor(nev)


def shop():
    global vodor, nyel, szogek, ruha
    os.system('cls')
    stats.print_stats()
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
    bolt_one = beker('Mit szeretnél vásárolni: ')
    if bolt_one == 1:
        print('Megvetted a levest, + 3 energia')
        stats.energia += 1
    elif bolt_one == 2:
        print('Megvásároltad a ruhát')
        print('És most tűnj innen, mielőtt mindkettőnket meglátnak')
        ruha += 1
    elif bolt_one == 3:
        print('Megszerezted a vödröt, ami az ásó egyik alkatrésze, ha kicsit hajlítgatod')
        vodor += 1
    elif bolt_one == 4:
        print('Megvetted az ásónak a nyelét, ')
        nyel += 1
    elif bolt_one == 5:
        print('Megvetted az összeszereléshez szükséges egy felszerelést, amivel rögzíthetsz alkatrészeket egymáshoz')
        szogek += 1


def folyoso_nyel(nev, nyel):
    global nyel2, vodor, fegyver
    stats.lebukas += 4
    stats.energia -= 2
    stats.line()
    stats.print_stats()
    folyoso = randint(1, 2)
    if folyoso == 1:
        stats.energia -= 2
        print('Az egyik sarokban találsz egy nyelet,gyorsan felkapod, és elindulsz visszafelé, amilyen halkan csak tudsz')
        print('Egy őr észrevesz, és megkérdőjelezi, hogy mit csinálsz itt, egy random fa nyéllel a kezedben')
        print('\t 1 - Letagadod(egy cellatársnak viszed, eltört a felmosó nyele)')
        print('\t 2 - Elnézést kérsz mielőtt agyonverne, és szépen visszahelyezed ahonnan hoztad')
        orocske = beker('Mit szeretnél tenni')
        if orocske == 1:
            stats.line()
            print('Ez bevállt, elhitte neked, megszerezted a nyelet')
            vodro(nev)
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
                masnap(nev)
            elif ujra == 2:
                hiszipiszi = randint(1, 2)
                if hiszipiszi == 1:
                    os.system('cls')
                    stats.line()
                    print('Második próbálkozásodkor is rajtakapott, de ezúttal nem volt olyan elnéző')
                    print('Rendesen elvert téged egy gumibottal, majd visszaküldött a celládba')
                    stats.egeszseg -= 5
                    masnap(nev)
                else:
                    os.system('cls')
                    stats.line()
                    print('Gratulálok, megszerezted a nyelet')
                    nyel += 1
                    stats.energia -= 2
                    vodro(nev)
                    if nyel == 1 and vodor == 1 and szogek == 1:
                        os.system('cls')
                        print('Ezt a kettőt összeeszkabáltad, gratulálok, NYERTÉL')
                        exit(0)
            elif ujra == 3:
                shop()
            elif ujra == 4:
                os.system('cls')
                print('Levetetted magad az épület tetejéről')
                print('Vesztettél')
                exit()


def munka():
    print('Ezen a helyeken más raboknak hajthatsz végre különböző küldetéseket.')
    print('Mindegyik küldetés egy vele járó kockázattal, illetve fizettséggel jár')
    print('Figyelj oda, mindegyik küldetés valamennyi energiát, és harcok esetén életerőt is vonhat le')
    print('Sok sikert a pénszerzéshez')
    print('\t')
    print('\t')
    print('\t')
    print('\t')
    print('\t')
