from random import randint
def kulcsketto(nev, egeszseg, energia, lebukas, penz):
    print(f'A kulcsos szökési módot választottad {nev}-nek')
    print(f'{nev}-nek szüksége lesz kettő kulcsra, és az ahhoz szükséges anyagokra')
    print('')
    print(f'A raboknak minden nap 16:00-18:00-ig kell dolgozniuk a műhelyben, ilyenkor {nev}-nek lehetősége lehet arra, hogy bejusson a kovácsműhelybe, de vigyázz nehogy észre vegyék!')
    print('1 óra múlva...')
    print('A rabok elindulnak dolgozni')
    valaszelso = int(input(f'Szeretne {nev} elszökni a többiek közűl, és elmenni a kovácsműhelybe?, ha igen (1), ha nem (2): '))
    if valaszelso == 1:
        print(f'{nev} észrevétlenül kilép a tömegből, és elindul a műhely felé. A következő fél órát azzal tölti, hogy információkat szerezzen a műhelyről, de vigyáznod kell, nehogy feltűnjön valakinek, hogy nem vagy ott.')
        valaszketto = int(input(f'{nev} szeretne visszaindúlni?, ha igen (1), ha nem (2): '))
        if valaszketto == 1:
            print(f'Jól döntöttél, {nev} elindul vissza és sikeresen beleolvad a tömegbe')
        elif valaszketto == 2:
            print(f'Rosszúl döntöttél, valakinek feltűnik, hogy {nev} nincs ott')
            print('Megkérdezik tőled, hogy hol voltál, mit válaszolsz?')
            print('\t 1 - Eltévedett és nem talált vissza')
            print('\t 2 - El kellett mennie WC-re')
            print('\t 3 - Elmondod az igazat')
            valaszharom = int(input('A választásod: '))
            if valaszharom == 1:
                print('Nagyon átlátszó, az őrök gyanút fognak, de elengednek, ezt most megúszta')
            elif valaszharom ==2:
                print('Megérhető, nem fognak gyanút, ezt most megúszta')            
            elif valaszharom == 3:
                print('Rossz válasz')
                print('VÉGE!')
                lebukas += 100
                exit()
            
    if valaszelso == 2 or valaszketto == 1 or valaszketto ==2:
        print('Keményen végig dolgoztad a napot.')
        print('Másnap...')
        valasznegy = int(input(f'Szeretne {nev} észrevétlenül anyagokat gyűjteni, vagy még jobban körűlnézni?, ha anyagokat akar gyűjteni(1), körűlnézni(2), maradni és dolgozni(3): '))
        if valasznegy == 1:
            print(f'A mai nap során {nev} anyagokat próbál gyűjteni')
            print('A cellatársánál van egy bökő, ami alkalmas lehet ahhoz, hogy kulcsokat készítsen belőle, de kell egy fair trade ehhez. ')
            print('Mit ajánlasz neki érte?')
            print('\t 1 - A mai és a holnapi ebédet')
            print('\t 2 - Aludhat az ágyadon egy hétig')
            print('\t 3 - Nem ad neki semmit')
            valaszot = int(input('A választás: '))
            if valaszot == 1:
                print('Egy jó ajánlat volt')
                print('Megszerezted a bökőt')
                valasznyolc= int(input('Szeretnél másnap elindúlni kulcsot készíteni?, ha igen(1), ha nem(2)'))
                if valasznyolc == 1:
                    print('Másnap...')
                    print('Észrevétlenül elszökik')
                    print(f'A műhelyben {nev} a gép elött áll és készíti a kulcsot, de vigyáznia kell, nehogy eltörjön, vagy elrontsa a kulcsot')
                    e = 5
                    f = 6
                    eselyharom = randint(e,f)
                    if eselyharom == e:
                        print('Sikerül elkészítenie a kulcsot')
                        valasztiz = int(input('Szeretne még ma elindulni és kiszabadúlni a börtönből?, ha igen(1), ha nem(2): '))
                        if valasztiz == 1:
                            i = 1
                            j = 2
                            eselyot = randint(i,j)
                            if eselyot == i:
                                print('Túl mohó volt, elkapták')
                                print('VÉGE!')
                                lebukas += 100
                                exit()
                            elif eselyot == j:
                                print('Sikerül kiszabadúlnia, gratulálunk, kivitte a játék')
                                print('NYERT!')
                                print(f'A győztes játékos: {nev}')
                                exit()
                        elif valasztiz == 2:
                            k = 1
                            l = 2
                            eselyot = randint(k, l)
                            if eselyot == k:
                                print('Észreveszik és elkapták')
                                print('VÉGE!')
                                lebukas += 100
                                exit()
                            elif eselyot == l:
                                print('Sikerül kiszabadúlnia, gratulálunk, kivitte a játék')
                                print('NYERT!')
                                print(f'A győztes játékos: {nev}')
                                exit()
                    elif eselyharom == f:
                        print('Eltörte a kulcsot, ráadásúl élszre is veszik')
                        print('VÉGE!')
                        lebukas += 100
                        exit()
                elif valasznyolc == 2:
                    print(f'A következő napon {nev} végig dolgozott.')
                    print('Elhatározza, hogy másnap elindul és megpróbálja elkészíteni a kulcsot')
                    print('Másnap...')
                    print('Észrevétlenül elszökik')
                    print(f'A műhelyben {nev} a gép elött áll és készíti a kulcsot, de vigyáznia kell, nehogy eltörjön, vagy elrontsa a kulcsot')
                    g = 5
                    h = 6
                    eselynegy = randint(g,h)
                    if eselynegy == g:
                        print('Sikerül elkészítenie a kulcsot')
                        valaszkilenc = int(input('Szeretne még ma elindulni és kiszabadúlni a börtönből?, ha igen(1), ha nem(2): '))
                        if valaszkilenc == 1:
                            i = 1
                            j = 2
                            eselyot = randint(i,j)
                            if eselyot == i:
                                print('Túl mohó volt, elkapták')
                                print('VÉGE!')
                                lebukas += 100
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
                                lebukas += 100
                                exit()
                            elif eselyot == l:
                                print('Sikerül kiszabadúlnia, gratulálunk, kivitte a játék')
                                print('NYERT!')
                                print(f'A győztes játékos: {nev}')
                                exit()
                    elif eselynegy == h:
                        print('Eltörte a kulcsot, ráadásúl élszre is veszik')
                        print('VÉGE!')
                        lebukas += 100
                        exit()
            elif valaszot == 2:
                print('Neki is van ágya, miért kéne neki?')
                print('Nem szerezte meg')
            elif valaszot == 3:
                print('1 - Harc')
                print('2 - Nincs harc')
                valaszhat = int(input('Válasz: '))
                if valaszhat == 1:
                    print('Ma délbe harc')
                    a = 0
                    b = 1
                    esely = randint(a,b)
                    if esely == a:
                        print('Nyert')
                        valasznyolc= int(input('Szeretnél másnap elindúlni kulcsot készíteni?, ha igen(1), ha nem(2)'))
                if valasznyolc == 1:
                    print('Másnap...')
                    print('Észrevétlenül elszökik')
                    print(f'A műhelyben {nev} a gép elött áll és készíti a kulcsot, de vigyáznia kell, nehogy eltörjön, vagy elrontsa a kulcsot')
                    e = 5
                    f = 6
                    eselyharom = randint(e,f)
                    if eselyharom == e:
                        print('Sikerül elkészítenie a kulcsot')
                        valasztiz = int(input('Szeretne még ma elindulni és kiszabadúlni a börtönből?, ha igen(1), ha nem(2): '))
                        if valasztiz == 1:
                            i = 1
                            j = 2
                            eselyot = randint(i,j)
                            if eselyot == i:
                                print('Túl mohó volt, elkapták')
                                print('VÉGE!')
                                lebukas += 100
                                exit()
                            elif eselyot == j:
                                print('Sikerül kiszabadúlnia, gratulálunk, kivitte a játék')
                                print('NYERT!')
                                print(f'A győztes játékos: {nev}')
                                exit()
                        elif valasztiz == 2:
                            k = 1
                            l = 2
                            eselyot = randint(k, l)
                            if eselyot == k:
                                print('Észreveszik és elkapták')
                                print('VÉGE!')
                                lebukas += 100
                                exit()
                            elif eselyot == l:
                                print('Sikerül kiszabadúlnia, gratulálunk, kivitte a játék')
                                print('NYERT!')
                                print(f'A győztes játékos: {nev}')
                                exit()
                    elif eselyharom == f:
                        print('Eltörte a kulcsot, ráadásúl élszre is veszik')
                        print('VÉGE!')
                        lebukas += 100
                        exit()
                elif valasznyolc == 2:
                    print(f'A következő napon {nev} végig dolgozott.')
                    print('Elhatározza, hogy másnap elindul és megpróbálja elkészíteni a kulcsot')
                    print('Másnap...')
                    print('Észrevétlenül elszökik')
                    print(f'A műhelyben {nev} a gép elött áll és készíti a kulcsot, de vigyáznia kell, nehogy eltörjön, vagy elrontsa a kulcsot')
                    g = 5
                    h = 6
                    eselynegy = randint(g,h)
                    if eselynegy == g:
                        print('Sikerül elkészítenie a kulcsot')
                        valaszkilenc = int(input('Szeretne még ma elindulni és kiszabadúlni a börtönből?, ha igen(1), ha nem(2): '))
                        if valaszkilenc == 1:
                            i = 1
                            j = 2
                            eselyot = randint(i,j)
                            if eselyot == i:
                                print('Túl mohó volt, elkapták')
                                print('VÉGE!')
                                lebukas += 100
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
                                lebukas += 100
                                exit()
                            elif eselyot == l:
                                print('Sikerül kiszabadúlnia, gratulálunk, kivitte a játék')
                                print('NYERT!')
                                print(f'A győztes játékos: {nev}')
                                exit()
                    elif eselynegy == h:
                        print('Eltörte a kulcsot, ráadásúl élszre is veszik')
                        print('VÉGE!')
                        exit()
                    elif esely == b:
                        print('Éppen el tud futni, de szét verték a búráját')
                        print('Nincs bökő')
                elif valaszhat == 2:
                    print('Nincs harc, de nincs bökő')
        elif valasznegy == 2:
            print(f'{nev} alaposabban körbe akar nézni ma.')
            print('Négy óra múlva...')
            print(f'A rabok elindulnak dolgozni és {nev} elhatározza, hogy megszökik a tömegből')
            valaszhet = int(input('De még meggondolhatja magát, ha igen(1), ha nem(2): '))
            if valaszhet == 1:
                print('Kemény munkával telt a nap, de nem haladt a munkával')
            elif valaszhet == 2:
                c = 2
                d = 3
                eselyketto = randint(c,d)
                if eselyketto == c:
                    print('Észrevétlenül el tud szökni a tömegből')
                    print('Azzal tölti a maradék időt, hogy alaposabban körűlnézzen')
                    print('Másnap...')
                    print(f'Egy ismeretlen ember meglátogatja {nev}-t és üzletet kínál')
                    print('\t 1 - Elkezd üzletelni')
                    print('\t 2 - Nem kezd el üzletelni')
                    valasztizenegy = int(input('Válasz: '))
                    if valasztizenegy == 1:
                        print('Három ajánlatot kínál fel: ')
                        print(f'\t Segít {nev}-nek kiszabadulni, és ha sikerül, akkor fizetnie kell neki 1000 Eurót.')
                        print('\t Segít kiszökni, de utána le kell dolgoznia 100 órát az éttermében')
                        print('\t Ad neki egy eszközt, de nem segít a szökésben')
                        valasztizenketto = int(input('Választás: '))
                        if valasztizenketto == 1:
                            print('A következő egy hétben minden nap a szökés tervén dolgoznak...')
                            print('Elkészült a terv')
                            ab = 1
                            ac = 2
                            eselyhat = randint(ab, ac)
                            if eselyhat == ab:
                                print('Sikerül eljutnia a kapuig')
                                print('A kapunál az üzlettársa várja egy kocsival, sikerül megszöknie')
                                if penz >= 1000:
                                    print('NYERT!')
                                    print(f'A győztes játékos: {nev}')
                                    exit()
                                elif penz < 1000:
                                    print('Nincs elég pénze, megverik')
                                    print('VÉGE!')
                                    lebukas += 100
                                    exit()
                            elif eselyhat == ac:
                                print('Nem jut el a kapuig, elkapják')
                                print('VÉGE!')
                                lebukas += 100
                                exit()
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
                                lebukas += 100
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
                                lebukas += 100
                                exit()
                            elif eselyot == n:
                                print('Sikerül kiszabadúlnia, gratulálunk, kivitte a játékot')
                                print('NYERT!')
                                print(f'A győztes játékos: {nev}')
                                exit()
                    elif valasztizenegy == 2:
                        print(f'{nev} nem kezd bele az üzletelésbe')
                elif eselyketto == d:
                    print('Elkapják, mostmár tényleg nem tudja kimagyarázni')
                    print('VÉGE!')
                    lebukas += 100
                    exit()
        elif valasznegy == 3:
            print('Kemény munkával telt a mai nap')
            print('Másnap...')
            print(f'Egy ismeretlen ember meglátogatja {nev}-t és üzletet kínál')
            print('\t 1 - Elkezd üzletelni')
            print('\t 2 - Nem kezd el üzletelni')
            valasztizenegy = int(input('Válasz: '))
            if valasztizenegy == 1:
                print('Három ajánlatot kínál fel: ')
                print(f'\t Segít {nev}-nek kiszabadulni, és ha sikerül, akkor fizetnie kell neki 1000 Eurót.')
                print('\t Segít kiszökni, de utána le kell dolgoznia 100 órát az éttermében')
                print('\t Ad neki egy eszközt, de nem segít a szökésben')
                valasztizenketto = int(input('Választás: '))
                if valasztizenketto == 1:
                    print('A következő egy hétben minden nap a szökés tervén dolgoznak...')
                    print('Elkészült a terv')
                    ab = 1
                    ac = 2
                    eselyhat = randint(ab, ac)
                    if eselyhat == ab:
                        print('Sikerül eljutnia a kapuig')
                        print('A kapunál az üzlettársa várja egy kocsival, sikerül megszöknie')
                        if penz >= 1000:
                            print('NYERT!')
                            print(f'A győztes játékos: {nev}')
                            exit()
                        elif penz < 1000:
                            print('Nincs elég pénze, megverik')
                            print('VÉGE!')
                            lebukas += 100
                            exit()
                    elif eselyhat == ac:
                        print('Nem jut el a kapuig, elkapják')
                        print('VÉGE!')
                        lebukas += 100
                        exit()
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
                        lebukas += 100
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
                        lebukas += 100
                        exit()
                    elif eselyot == n:
                        print('Sikerül kiszabadúlnia, gratulálunk, kivitte a játék')
                        print('NYERT!')
                        exit()
