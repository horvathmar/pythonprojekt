def telefon_vagy_level(nev):
    valasztott_ember = int(input('Válassza ki, hogy ki csempéssze be neki a vágóeszközt! Írjon be 1-est ha a testvére és 2-est, ha egy barátja. '))
    if valasztott_ember == 1:
        print(f'A tesvérében bízik {nev}, ezért jól választottál!')
        megbeszeles = int(input('Válaszd ki, hogy hol kérje meg a tesvérét, 1-est ha telefonon és 2-est, ha levélben.'))
    elif valasztott_ember == 2:
        print(f'{nev}-nek reménykednie kell, hogy a barátja, akiben ő bízik nem adja fel a rendőröknek.')
        print(f'Szerencséje van, mivel a barátja nem adja fel, és benne van hogy segít {nev}-nek.')
        megbeszeles = int(input('Válaszd ki, hogy hol kérje meg a barátját, 1-est ha telefonon és 2-est, ha levélben.'))
    return megbeszeles


def baratno(nev):
    print('Vigyázz! Ne bízz teljesen a barátnődben, nehogy eláruljon.')
    opcio = int(input('1 - kúszva menjek el a keríésig, és 2 - futva, mert úgy gyorsabb. '))
    if opcio == 1:
        kapu(nev)
    elif opcio == 2:
        print(f'Sajnos nem volt szerencséd, és az őr észrevette {nev}-et! Riadót fújt és {nev}-et elkapták.')
        print('VÉGE!')
        exit()


def kapu(nev):
    print(f'Jól döntöttél, sikeresen eljutott {nev} a kapuig.')
    print('Nyugodtan vághatja a kaput, mivel nem hallják a többi rab miatt.')
    print(f'Két kerítés van, közöttük a földön szögesdrót. Mit tegyen {nev}?')
    dontes = int(input('1-est ha vágja el, 2-est ha menjen át rajta. '))
    if dontes == 1:
        print('Át tudta vági, és már csak egy kapu választja el a szabadságtól!')
        print(f'AZ utolsó kerítésen is átvágta {nev}')
        print(f'Miután átment a kerítésen vágott lyukon, elkezdett futni a szabadsága felé {nev}')
        print('Senki sem tudta megállítani, és élete végéig szabad maradt!')
        print(f'Sikeresen kijutattad {nev}-et a börtönből. GRATULÁLUNK!')
        exit()
    elif dontes == 2:
        print('Sajnos beleakadt a szögesdrótba, és mikoözben próbált kijutni, észrevették, és elkapták.')
        print('VÉGE')
        exit()


def vago(nev, egeszseg, energia, lebukas, penz):
    print(f'A vágásos szökésimódot választottad {nev}-nek')
    print(f'Az első lépés a szökés irányában, hogy hogyan szerezze meg {nev} a vágóeszközt, amivel majd átvágja magát')
    elso = int(input('Válassz helyette! Írj be 1-est, ha be szeretné, hogy valaki csempéssze be neki, de ha lebukik vége és 2-est ha saját maga vegyen a börtönben, de ahhoz pénz kell! '))
    if elso == 1:
        lebukas = csempesz(lebukas, nev)

    elif elso == 2:
        print('Így sokkal kisebb a lebukási esély, de pénzt kell szereznie az elitéltnek!')
        penzkeresetimod = int(input('Hogyan szerezzen az elitélt pénzt? Írjon be 1-est ha menjen el dolgozni a börtönben, és 2-est, ha kezdjen el árulni valamit, amit más behozott neki. '))
        if penzkeresetimod == 1:
            print('Ez egy biztonságos, de lassabb módja a pénzkeresésnek.')
            print(f'{nev} összegyűjtötte a szügséges pénzmennyiséget')
        elif penzkeresetimod == 2:
            print(f'{nev} hamar eladja nem használt dolgait, így meg tudja venni a vágóeszközt-')
        penz += 25
        print('')
        print(f'Most meg kell vennie {nev}-nek a csípőfogót, ami 175 euro.')

def szokes(nev, penz, lebukas):
    print('Miután megvette a csípőfogót még aznap este megpróbál megszökni.')
    print(f'Sikeresen kilopózott az udvarra, de most el kell jutni a kerítésig,  úgy, hogy az őr nem veszi észre.')
    fut_vagy_kuszas = int(input('Mit tegyen? 1 - Fut 2 - kúszik'))
    if fut_vagy_kuszas == 1:
        print('Sajnos az őr észrevette, és riadót fújt!')
        print('VÉGE!')
    elif fut_vagy_kuszas == 2:
        print('Jól döntöttél, mivel eljutott a kapuig, és így más csak el kell vágni a kerítést.')

def kapu_atvagasa(nev, penz, lebukas):
    print('ELkezdte vágni a kerítést és hamar vágott magának egy lyukat, amin már átfér.')
    print('Azonban a két kerítés között szögesdrót van.')
    ugras_maszas = int(input('Mit tegyen? 1 - ugorja át, 2 - másszon át rajta'))
    if ugras_maszas == 1:
        print('Sikeresen átjutott a szögesdróton!')
        print('Átvágta az utolsó kerítést, és élete végéig szabad emberként élt!')
        print('Gratulálunk, sikeresen kivitted a játékot!')
    elif ugras_maszas == 2:
        print(f'Sajnos {nev} beleakadt a szögesdrótban, és miközben próbál kiszabadulni, meghalotta az őr, és elkapta.')
        print(f'Sajnos {nev}-et elkapták, így számodra a játéknak VÉGE!')




def csempesz(lebukas, nev):
    print(f'{nev}-nek ügyenie kell az őrökre, mivel, ha észreveszik, vagy megtalálják nála vége a játéknak!')
    megbeszeles = telefon_vagy_level(nev)
    if megbeszeles == 1:
        lebukas = telefon(lebukas, megbeszeles, nev)
    return lebukas


def telefon(lebukas, megbeszeles, nev):
    print('Reménykedniük kell, hogy ne hallgassák le a telefont.')
    print(f'A megpróbálja becsempészni {nev}-nek a csípőfogót.')
    print(f'Sikeresen becsempészte a börtön területére a csípőfogót, és most átadta {nev}-nek.')
    print(f'AMikor azonban {nev} megpróbálja bevinni a cellájába egy motozáshoz ér.')
    dobas_vagy_maradas = int(input('Ugyan elrejtette a gatájában, de ha megtatálja a fegyőr azonnal vége a tervének! Mit tegyen? Írjon be 1-est ha menjen vissza, és dobja el, és 2-est ha higgadttan reménykedik, hogy nem találjál meg. '))
    if dobas_vagy_maradas == 1:
        print('Ez egy rossz döntés volt! Elveszítette a legfontosabb kellékét a szökéshez, így végetért számodra a játék!')
        print('VÉGE!')
        exit()
    elif dobas_vagy_maradas == 2:
        lebukas = marad(lebukas, nev)

    elif megbeszeles == 2:
        print('Ez egy biztonságosabb mód, de lassabban ér oda az üzenet.')
        print(f'A valasztott személy megpróbálja becsempészni {nev}-nek a csípőfogót.')
    return lebukas


def marad(lebukas, nev):
    print('Odaért a motozáshoz, és az őr gyanut fogott a viselkedéséből és...')
    print(f'{nev}-nek szerencséje volt mivel nem találták meg nála a csípőfogt a motozás során. Bevitte a cellájába, és ott elrejtette.')
    lebukas += 10
    print(f'Most ki kellene választania {nev}-nek, hogy mikor szeretne kiszabadulni')
    idopont = int(input('Írjon be 1-est ha, akkor amikor éppen nézik a rabok a TV-t és hangoskodnak, így senki sem fog rá figyelni és 2-est, ha egy este amikor már mindenki alszik. '))
    if idopont == 1:
        tv(nev)
    elif idopont == 2:
        este(nev)
    return lebukas


def este(nev):
    print('így csendesebben kell majd vágnia, de könnyebben szökik majd meg.')
    print(f'{nev}-nek kell szereznie egy embert, aki majd a kijutása aután elviszi autóval.')
    ki_jon_ertem2 = int(input('Döntse el, hogy ki jöjjön a szökevényért. Írjon be 1-est, ha testvére, és 2-est, ha a barátmője. '))
    if ki_jon_ertem2 == 1:
        print('Jól döntöttél, mivel ő már becsempészett egy csípőfogót, biztosan eljön érte!')
        print('Egyik este nekilendült, és kijutott az udvarra, de észrevette az őrtornyot.')
        mit_tegyek = int(input('1 - kúszva menjek el a keríésig, és 2 - futva, mert úgy gyorsabb. '))
        if mit_tegyek == 1:
            kapu(nev)
        elif mit_tegyek == 2:
            print(f'Sajnos nem volt szerencséd, és az őr észrevette {nev}-et! Riadót fújt és {nev}-et elkapták.')
            print('VÉGE!')
            exit()
    elif ki_jon_ertem2 == 2:
        baratno(nev)


def tv(nev):
    print('Így nehezen veszik észre, és nyugodtan tudja vágni a kerítést, mivel senki sem fogja hallani.')
    print(f'{nev}-nek kell szereznie egy embert, aki majd a kijutása aután elviszi autóval.')
    ki_jon_ertem = int(input('Döntse el, hogy ki jöjjön a szökevényért. Írjon be 1-est, ha testvére, és 2-est, ha a barátmője. '))
    if ki_jon_ertem == 1:
        print('Jól döntöttél, mivel ő már becsempészett egy csípőfogót, biztosan eljön érte!')
        mit_tegyek4 = int(input('1 - kúszva menjek el a keríésig, és 2 - futva, mert úgy gyorsabb. '))
        if mit_tegyek4 == 1:
            kapu(nev)
            print(f'Sajnos nem volt szerencséd, és az őr észrevette {nev}-et! Riadót fújt és {nev}-et elkapták.')
            print('VÉGE!')
            exit()
    elif ki_jon_ertem == 2:
        print('Vigyázz! Ne bízz teljesen a barátnődben, nehogy eláruljon.')
        mit_tegyek3 = int(input('1 - kúszva menjek el a keríésig, és 2 - futva, mert úgy gyorsabb. '))
        if mit_tegyek3 == 1:
            kapu(nev)
