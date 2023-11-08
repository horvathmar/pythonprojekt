from random import randint

import stats
from safe_input import beker


def kulcsketto(nev):
    print(f'A kulcsos szökési módot választottad {nev}-nek')
    print(f'{nev}-nek szüksége lesz egy kulcsra, és az ahhoz szükséges anyagokra')
    print('')
    print(f'A raboknak minden nap 16:00-18:00-ig kell dolgozniuk a műhelyben, ilyenkor {nev}-nek lehetősége lehet arra, hogy bejusson a kovácsműhelybe, de vigyázz nehogy észre vegyék!')
    print('1 óra múlva...')
    stats.line()
    print('A rabok elindulnak dolgozni')
    valaszelso = beker(f'Szeretne {nev} elszökni a többiek közűl, és elmenni a kovácsműhelybe?, ha igen (1), ha nem (2): ')
    if valaszelso == 1:
        print(f'{nev} észrevétlenül kilép a tömegből, és elindul a műhely felé. A következő fél órát azzal tölti, hogy információkat szerezzen a műhelyről, de vigyáznod kell, nehogy feltűnjön valakinek, hogy nem vagy ott.')
        stats.line()
        valaszketto = beker(f'{nev} szeretne visszaindúlni?, ha igen (1), ha nem (2): ')
        if valaszketto == 1:
            print(f'Jól döntöttél, {nev} elindul vissza és sikeresen beleolvad a tömegbe')
        elif valaszketto == 2:
            print(f'Rosszúl döntöttél, valakinek feltűnik, hogy {nev} nincs ott')
            stats.line()
            print('Megkérdezik tőled, hogy hol voltál, mit válaszolsz?')
            print('\t 1 - Eltévedett és nem talált vissza')
            print('\t 2 - El kellett mennie WC-re')
            print('\t 3 - Elmondod az igazat')
            valaszharom = beker('A választásod: ', 3)
            if valaszharom == 1:
                print('Nagyon átlátszó, az őrök gyanút fognak, de elengednek, ezt most megúszta')
            elif valaszharom == 2:
                print('Megérhető, nem fognak gyanút, ezt most megúszta')
            elif valaszharom == 3:
                print('Rossz válasz')
                print('VÉGE!')
                stats.line()
                stats.lebukas += 100
                exit()

    if valaszelso == 2 or valaszketto == 1 or valaszketto == 2:
        print('Keményen végig dolgoztad a napot.')
        print('Másnap...')
        stats.line()
        valasznegy = beker(f'Szeretne {nev} észrevétlenül anyagokat gyűjteni, vagy még jobban körűlnézni?, ha anyagokat akar gyűjteni(1), körűlnézni(2), maradni és dolgozni(3): ', 3)
        if valasznegy == 1:
            print(f'A mai nap során {nev} anyagokat próbál gyűjteni')
            print('A cellatársánál van egy bökő, ami alkalmas lehet ahhoz, hogy kulcsot készítsen belőle, de kell egy fair trade ehhez. ')
            stats.line()
            print('Mit ajánlasz neki érte?')
            print('\t 1 - A mai és a holnapi ebédet')
            print('\t 2 - Aludhat az ágyadon egy hétig')
            print('\t 3 - Nem ad neki semmit')
            valaszot = beker('A választás: ', 3)
            if valaszot == 1:
                print('Egy jó ajánlat volt')
                print('Megszerezted a bökőt')
                stats.line()
                valasznyolc = beker('Szeretnél másnap elindúlni kulcsot készíteni?, ha igen(1), ha nem(2)')
                if valasznyolc == 1:
                    print('Másnap...')
                    print('Észrevétlenül elszökik')
                    print(f'A műhelyben {nev} a gép elött áll és készíti a kulcsot, de vigyáznia kell, nehogy eltörjön, vagy elrontsa a kulcsot')
                    e = 5
                    f = 6
                    eselyharom = randint(e, f)
                    if eselyharom == e:
                        kulcs_elkeszit(nev)
                    elif eselyharom == f:
                        print('Eltörte a kulcsot, ráadásúl élszre is veszik')
                        print('VÉGE!')
                        stats.line()
                        stats.lebukas += 100
                        exit()
                elif valasznyolc == 2:
                    masnap_dolgozik(nev)
            elif valaszot == 2:
                print('Neki is van ágya, miért kéne neki?')
                print('Nem szerezte meg')
                print('Másnap...')
                stats.line()
                print(f'Egy ismeretlen ember meglátogatja {nev}-t és üzletet kínál')
                print('\t 1 - Elkezd üzletelni')
                print('\t 2 - Nem kezd el üzletelni')
                valasztizenegy = beker('Válasz: ')
                if valasztizenegy == 1:
                    ajanlatok(nev)
                elif valasztizenegy == 2:
                    print(f'{nev} nem kezd bele az üzletelésbe')
                    print('Nincs több lehetősége a kulcs szerzésre')
                    print('VÉGE!')
                    stats.line()
                    exit()
            elif valaszot == 3:
                stats.line()
                print('1 - Harc')
                print('2 - Nincs harc')
                valaszhat = beker('Válasz: ')
                if valaszhat == 1:
                    print('Ma délbe harc')
                    a = 0
                    b = 1
                    esely = randint(a, b)
                    if esely == a:
                        print('Nyert')
                        stats.line()
                        valasznyolc = beker('Szeretnél másnap elindúlni kulcsot készíteni?, ha igen(1), ha nem(2)')
                        if valasznyolc == 1:
                            print('Másnap...')
                            print('Észrevétlenül elszökik')
                            print(f'A műhelyben {nev} a gép elött áll és készíti a kulcsot, de vigyáznia kell, nehogy eltörjön, vagy elrontsa a kulcsot')
                            e = 5
                            f = 6
                            eselyharom = randint(e, f)
                            kulcs_esely(e, eselyharom, f, nev)
                        elif valasznyolc == 2:
                            print(f'A következő napon {nev} végig dolgozott.')
                            print('Elhatározza, hogy másnap elindul és megpróbálja elkészíteni a kulcsot')
                            print('Másnap...')
                            print('Észrevétlenül elszökik')
                            print(f'A műhelyben {nev} a gép elött áll és készíti a kulcsot, de vigyáznia kell, nehogy eltörjön, vagy elrontsa a kulcsot')
                            g = 5
                            h = 6
                            eselynegy = randint(g, h)
                            if eselynegy == g:
                                print('Sikerül elkészítenie a kulcsot')
                                valaszkilenc = beker('Szeretne még ma elindulni és kiszabadúlni a börtönből?, ha igen(1), ha nem(2): ')
                                if valaszkilenc == 1:
                                    i = 1
                                    j = 2
                                    eselyot = randint(i, j)
                                    if eselyot == i:
                                        print('Túl mohó volt, elkapták')
                                        print('VÉGE!')
                                        stats.line()
                                        stats.lebukas += 100
                                        exit()
                                    elif eselyot == j:
                                        print('Sikerül kiszabadúlnia, gratulálunk, kivitte a játékot')
                                        print('NYERT!')
                                        print(f'A győztes játékos: {nev}')
                                        exit()
                                elif valaszkilenc == 2:
                                    k = 1
                                    l = 2
                                    eselyot = randint(k, l)
                                    if eselyot == k:
                                        print('Észreveszik és elkapták')
                                        print('VÉGE!')
                                        stats.line()
                                        stats.lebukas += 100
                                        exit()
                                    elif eselyot == l:
                                        print('Sikerül kiszabadúlnia, gratulálunk, kivitte a játék')
                                        print('NYERT!')
                                        print(f'A győztes játékos: {nev}')
                                        exit()
                            elif eselynegy == h:
                                print('Eltörte a kulcsot, ráadásúl élszre is veszik')
                                print('VÉGE!')
                                stats.line()
                                exit()
                            elif esely == b:
                                print('Éppen el tud futni, de szét verték a búráját')
                                print('Nincs bökő')
                elif valaszhat == 2:
                    print('Nincs harc, de nincs bökő')
        elif valasznegy == 2:
            print(f'{nev} alaposabban körbe akar nézni ma.')
            print('Négy óra múlva...')
            stats.line()
            print(f'A rabok elindulnak dolgozni és {nev} elhatározza, hogy megszökik a tömegből')
            valaszhet = beker('De még meggondolhatja magát, ha igen(1), ha nem(2): ')
            if valaszhet == 1:
                print('Kemény munkával telt a nap, de nem haladt a munkával')
                print('Másnap...')
                stats.line()
                print(f'Egy ismeretlen ember meglátogatja {nev}-t és üzletet kínál')
                print('\t 1 - Elkezd üzletelni')
                print('\t 2 - Nem kezd el üzletelni')
                valasztizenegy = beker('Válasz: ')
                if valasztizenegy == 1:
                    stats.line()
                    print('Három ajánlatot kínál fel: ')
                    print(f'\t 1 - Segít {nev}-nek kiszabadulni, és ha sikerül, akkor fizetnie kell neki 100 Eurót.')
                    print('\t 2 - Segít kiszökni, de utána le kell dolgoznia 100 órát az éttermében')
                    print('\t 3 - Ad neki egy eszközt, de nem segít a szökésben')
                    valasztizenketto = beker('Választás: ', 3)
                    if valasztizenketto == 1:
                        ruha_eladas(nev)
                    elif valasztizenketto == 2:
                        print('A következő egy hétben minden nap a szökés tervén dolgoznak...')
                        print('Elkészült a terv')
                        ab = 1
                        ac = 2
                        eselyhat = randint(ab, ac)
                        if eselyhat == ab:
                            print('Sikerül eljutnia a kapuig')
                            print('A kapunál az üzlettársa várja egy kocsival, sikerül megszöknie, ledolgozza még a 100 órát')
                            print('NYERT!')
                            print(f'A győztes játékos: {nev}')
                            exit()
                        elif eselyhat == ac:
                            print('Nem jut el a kapuig, elkapják')
                            print('VÉGE!')
                            stats.line()
                            stats.lebukas += 100
                            exit()
                    elif valasztizenketto == 3:
                        print('Kapott egy kulcsot')
                        print('Másnap elhatározza, hogy aznap kiszökik')
                        m = 1
                        n = 2
                        eselyot = randint(m, n)
                        if eselyot == m:
                            print('Észreveszik és elkapták')
                            print('VÉGE!')
                            stats.line()
                            stats.lebukas += 100
                            exit()
                        elif eselyot == n:
                            print('Sikerül kiszabadúlnia, gratulálunk, kivitte a játékot')
                            print('NYERT!')
                            exit()
                elif valasztizenegy == 2:
                    stats.line()
                    print('Találkozik a cellatársával és üzletet akar kötni')
                    print('Mit ajánlasz neki érte?')
                    print('\t 1 - A mai és a holnapi ebédet')
                    print('\t 2 - Aludhat az ágyadon egy hétig')
                    print('\t 3 - Nem ad neki semmit')
                    valaszot = beker('A választás: ', 3)
                if valaszot == 1:
                    print('Egy jó ajánlat volt')
                    print('Megszerezted a bökőt')
                    stats.line()
                    valasznyolc = beker('Szeretnél másnap elindúlni kulcsot készíteni?, ha igen(1), ha nem(2)')
                    if valasznyolc == 1:
                        print('Másnap...')
                        stats.line()
                        print('Észrevétlenül elszökik')
                        print(f'A műhelyben {nev} a gép elött áll és készíti a kulcsot, de vigyáznia kell, nehogy eltörjön, vagy elrontsa a kulcsot')
                        e = 5
                        f = 6
                        eselyharom = randint(e, f)
                        kulcs_esely(e, eselyharom, f, nev)
                    elif valasznyolc == 2:
                        masnap_dolgozik(nev)
                elif valaszot == 2:
                    print('Neki is van ágya, miért kéne neki?')
                    print('Nem szerezte meg')
                elif valaszot == 3:
                    print('Harc')
                    print('Ma délbe harc')
                    a = 0
                    b = 1
                    esely = randint(a, b)
                    if esely == a:
                        print('Nyert')
                        stats.line()
                        valasznyolc = beker('Szeretnél másnap elindúlni kulcsot készíteni?, ha igen(1), ha nem(2)')
                        if valasznyolc == 1:
                            print('Másnap...')
                            print('Észrevétlenül elszökik')
                            print(f'A műhelyben {nev} a gép elött áll és készíti a kulcsot, de vigyáznia kell, nehogy eltörjön, vagy elrontsa a kulcsot')
                            e = 5
                            f = 6
                            eselyharom = randint(e, f)
                            if eselyharom == e:
                                kulcs_elkeszit(nev)
                            elif eselyharom == f:
                                print('Eltörte a kulcsot, ráadásúl élszre is veszik')
                                print('VÉGE!')
                                stats.line()
                                stats.lebukas += 100
                                exit()
                        elif valasznyolc == 2:
                            print(f'A következő napon {nev} végig dolgozott.')
                            print('Elhatározza, hogy másnap elindul és megpróbálja elkészíteni a kulcsot')
                            print('Másnap...')
                            print('Észrevétlenül elszökik')
                            print(f'A műhelyben {nev} a gép elött áll és készíti a kulcsot, de vigyáznia kell, nehogy eltörjön, vagy elrontsa a kulcsot')
                            g = 5
                            h = 6
                            eselynegy = randint(g, h)
                            if eselynegy == g:
                                kulcs_elkeszit(nev)
                            elif eselynegy == h:
                                print('Eltörte a kulcsot, ráadásúl élszre is veszik')
                                print('VÉGE!')
                                stats.line()
                                exit()
                            elif esely == b:
                                print('Éppen el tud futni, de szét verték a búráját')
                                print('Nincs bökő')
                                print('VÉGE!')
                                stats.line()
                                exit()
            elif valaszhet == 2:
                c = 2
                d = 3
                eselyketto = randint(c, d)
                if eselyketto == c:
                    print('Észrevétlenül el tud szökni a tömegből')
                    print('Azzal tölti a maradék időt, hogy alaposabban körűlnézzen')
                    print('Másnap...')
                    stats.line()
                    print(f'Egy ismeretlen ember meglátogatja {nev}-t és üzletet kínál')
                    print('\t 1 - Elkezd üzletelni')
                    print('\t 2 - Nem kezd el üzletelni')
                    valasztizenegy = beker('Válasz: ')
                    if valasztizenegy == 1:
                        ajanlatok(nev)
                    elif valasztizenegy == 2:
                        print(f'{nev} nem kezd bele az üzletelésbe')
                elif eselyketto == d:
                    print('Elkapják, mostmár tényleg nem tudja kimagyarázni')
                    print('VÉGE!')
                    stats.line()
                    stats.lebukas += 100
                    exit()
        elif valasznegy == 3:
            print('Kemény munkával telt a mai nap')
            print('Másnap...')
            stats.line()
            print(f'Egy ismeretlen ember meglátogatja {nev}-t és üzletet kínál')
            print('\t 1 - Elkezd üzletelni')
            print('\t 2 - Nem kezd el üzletelni')
            valasztizenegy = beker('Válasz: ')
            if valasztizenegy == 1:
                stats.line()
                print('Három ajánlatot kínál fel: ')
                print(f'\t 1 - Segít {nev}-nek kiszabadulni, és ha sikerül, akkor fizetnie kell neki 100 Eurót.')
                print('\t 2 - Segít kiszökni, de utána le kell dolgoznia 100 órát az éttermében')
                print('\t 3 - Ad neki egy eszközt, de nem segít a szökésben')
                valasztizenketto = beker('Választás: ')
                if valasztizenketto == 1:
                    ruha_eladas(nev)
                elif valasztizenketto == 2:
                    print('A következő egy hétben minden nap a szökés tervén dolgoznak...')
                    print('Elkészült a terv')
                    ab = 1
                    ac = 2
                    eselyhat = randint(ab, ac)
                    if eselyhat == ab:
                        print('Sikerül eljutnia a kapuig')
                        print('A kapunál az üzlettársa várja egy kocsival, sikerül megszöknie, ledolgozza még a 100 órát')
                        print('NYERT!')
                        print(f'A győztes játékos: {nev}')
                        exit()
                    elif eselyhat == ac:
                        print('Nem jut el a kapuig, elkapják')
                        print('VÉGE!')
                        stats.line()
                        stats.lebukas += 100
                        exit()
                elif valasztizenketto == 3:
                    print('Kapott egy kulcsot')
                    print('Másnap elhatározza, hogy aznap kiszökik')
                    m = 1
                    n = 2
                    eselyot = randint(m, n)
                    if eselyot == m:
                        print('Észreveszik és elkapták')
                        print('VÉGE!')
                        stats.line()
                        stats.lebukas += 100
                        exit()
                    elif eselyot == n:
                        print('Sikerül kiszabadúlnia, gratulálunk, kivitte a játékot')
                        print('NYERT!')
                        exit()

            elif valasztizenegy == 2:
                print('Nem találta meg a módját a szökésre, ezért a játéknak')
                print('VÉGE!')
                stats.line()
                stats.lebukas += 100
                exit()


def ruha_eladas(nev):
    print('Szeretné eladni a nem használt ruháit?')
    print('\t 1 - igen')
    print('\t 2 - nem')
    valasztizenharom = int(input('A válasz: '))
    if valasztizenharom == 1:
        stats.penz += 100
        print('A következő egy hétben minden nap a szökés tervén dolgoznak...')
        print('Elkészült a terv')
        ab = 1
        ac = 2
        eselyhat = randint(ab, ac)
        if eselyhat == ab:
            print('Sikerül eljutnia a kapuig')
            print('A kapunál az üzlettársa várja egy kocsival, sikerül megszöknie')
            if stats.penz >= 100:
                print('NYERT!')
                print(f'A győztes játékos: {nev}')
                exit()
            elif stats.penz < 100:
                print('Nincs elég pénze, megverik')
                print('VÉGE!')
                stats.line()
                stats.lebukas += 100
                exit()
        elif eselyhat == ac:
            print('Nem jut el a kapuig, elkapják')
            print('VÉGE!')
            stats.line()
            stats.lebukas += 100
            exit()
    elif valasztizenharom == 2:
        print('Nincs elég pénze, megverik')
        print('VÉGE!')
        stats.line()
        stats.lebukas += 100
        exit()


def ajanlatok(nev):
    stats.line()
    print('Három ajánlatot kínál fel: ')
    print(f'\t 1 - Segít {nev}-nek kiszabadulni, és ha sikerül, akkor fizetnie kell neki 100 Eurót.')
    print('\t 2 - Segít kiszökni, de utána le kell dolgoznia 100 órát az éttermében')
    print('\t 3 - Ad neki egy eszközt, de nem segít a szökésben')
    valasztizenketto = beker('Választás: ', 3)
    if valasztizenketto == 1:
        ruha_eladas(nev)
    elif valasztizenketto == 2:
        print('A következő egy hétben minden nap a szökés tervén dolgoznak...')
        print('Elkészült a terv')
        ab = 1
        ac = 2
        eselyhat = randint(ab, ac)
        if eselyhat == ab:
            print('Sikerül eljutnia a kapuig')
            print('A kapunál az üzlettársa várja egy kocsival, sikerül megszöknie, ledolgozza még a 100 órát')
            print('NYERT!')
            print(f'A győztes játékos: {nev}')
            exit()
        elif eselyhat == ac:
            print('Nem jut el a kapuig, elkapják')
            print('VÉGE!')
            stats.line()
            stats.lebukas += 100
            exit()
    elif valasztizenketto == 3:
        print('Kapott egy kulcsot')
        print('Másnap elhatározza, hogy aznap kiszökik')
        m = 1
        n = 2
        eselyot = randint(m, n)
        if eselyot == m:
            print('Észreveszik és elkapták')
            print('VÉGE!')
            stats.line()
            stats.lebukas += 100
            exit()
        elif eselyot == n:
            print('Sikerül kiszabadúlnia, gratulálunk, kivitte a játékot')
            print('NYERT!')
            print(f'A győztes játékos: {nev}')
            exit()


def kulcs_elkeszit(nev):
    print('Sikerül elkészítenie a kulcsot')
    stats.line()
    valaszkilenc = beker('Szeretne még ma elindulni és kiszabadúlni a börtönből?, ha igen(1), ha nem(2): ')
    if valaszkilenc == 1:
        i = 1
        j = 2
        eselyot = randint(i, j)
        if eselyot == i:
            print('Túl mohó volt, elkapták')
            print('VÉGE!')
            stats.line()
            stats.lebukas += 100
            exit()
        elif eselyot == j:
            print('Sikerül kiszabadúlnia, gratulálunk, kivitte a játék')
            print('NYERT!')
            print(f'A győztes játékos: {nev}')
            exit()
    elif valaszkilenc == 2:
        k = 1
        l = 2
        eselyot = randint(k, l)
        if eselyot == k:
            print('Észreveszik és elkapták')
            print('VÉGE!')
            stats.line()
            stats.lebukas += 100
            exit()
        elif eselyot == l:
            print('Sikerül kiszabadúlnia, gratulálunk, kivitte a játék')
            print('NYERT!')
            print(f'A győztes játékos: {nev}')
            exit()


def kulcs_esely(e, eselyharom, f, nev):
    if eselyharom == e:
        kulcs_elkeszit(nev)
    elif eselyharom == f:
        print('Eltörte a kulcsot, ráadásúl élszre is veszik')
        print('VÉGE!')
        stats.line()
        stats.lebukas += 100
        exit()


def masnap_dolgozik(nev):
    print(f'A következő napon {nev} végig dolgozott.')
    print('Elhatározza, hogy másnap elindul és megpróbálja elkészíteni a kulcsot')
    print('Másnap...')
    print('Észrevétlenül elszökik')
    print(f'A műhelyben {nev} a gép elött áll és készíti a kulcsot, de vigyáznia kell, nehogy eltörjön, vagy elrontsa a kulcsot')
    g = 5
    h = 6
    eselynegy = randint(g, h)
    if eselynegy == g:
        kulcs_elkeszit(nev)
    elif eselynegy == h:
        print('Eltörte a kulcsot, ráadásúl élszre is veszik')
        print('VÉGE!')
        stats.line()
        stats.lebukas += 100
        exit()
