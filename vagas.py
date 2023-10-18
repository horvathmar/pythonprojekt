def vago(nev, egeszseg, energia, lebukas, penz):
    print(f'A vágásos szökésimódot választottad {nev}-nek')
    print(f'Az első lépés a szökés irányában, hogy hogyan szerezze meg {nev} a vágóeszközt, amivel majd átvágja magát')
    elso = int(input('Válassz helyette! Írj be 1-est, ha be szeretné, hogy valaki csempéssze be neki, de ha lebukik vége és 2-est ha saját maga vegyen a börtönben, de ahhoz pénz kell! '))
    if elso == 1:
        print(f'{nev}-nek ügyenie kell az őrökre, mivel, ha észreveszik, vagy megtalálják nála vége a játéknak!')
        valasztott_ember = int(input('Válassza ki, hogy ki csempéssze be neki a vágóeszközt! Írjon be 1-est ha a testvére és 2-est, ha egy barátja. '))
        if valasztott_ember == 1:
            print(f'A tesvérében bízik {nev}, ezért jól választottál!')
            megbeszeles = int(input('Válaszd ki, hogy hol kérje meg a tesvérét, 1-est ha telefonon és 2-est, ha levélben.'))
            if megbeszeles == 1:
                print('Reménykedniük kell, hogy ne hallgassák le a telefont.')
                print(f'A  megpróbálja becsempészni {nev}-nek a csípőfogót.')
            elif megbeszeles == 2:
                print('Ez egy biztonságosabb mód, de lassabban ér oda az üzenet.')
                print(f'A  megpróbálja becsempészni {nev}-nek a csípőfogót.')
        elif valasztott_ember == 2:
            print(f'{nev}-nek reménykednie kell, hogy a barátja, akiben ő bízik nem adja fel a rendőröknek.') 
            print(f'Szerencéje van, mivel a barátja nem adja fel, és benne van hogy segít {nev}-nek.')
            megbeszeles2 = int(input('Válaszd ki, hogy hol kérje meg a tesvérét, 1-est ha telefonon és 2-est, ha levélben.'))
            if megbeszeles2 == 1:
                print('Reménykedniük kell, hogy ne hallgassák le a telefont.')
                print(f'A  megpróbálja becsempészni {nev}-nek a csípőfogót.')
                print(f' sikeresen becsempészte a börtön területére a csípőfogót, és most átadta {nev}-nek.')
                print(f'AMikor azonban {nev} megpróbálja bevinni a cellájába egy motozáshoz ér.')
                dobas_vagy_maradas = int(input('Ugyan elrejtette a gatájában, de ha megtatálja a fegyőr azonnal vége a tervének! Mit tegyen? Írjon be 1-est ha menjen vissza, és dobja el, és 2-est ha higgadttan reménykedik, hogy nem találjál meg. '))
                if dobas_vagy_maradas == 1:
                    print('Ez egy rossz döntés volt! Elveszítette a legfontosabb kellékét a szökéshez, így végetért számodra a játék!')
                    print('VÉGE!')
                    lebukas += 100
                elif dobas_vagy_maradas == 2:
                    print('Odaért a motozáshoz, és az őr gyanut fogott a viselkedéséből és...')
                    print(f'{nev}-nek szerencséje volt mivel nem találták meg nála a csípőfogt a motozás során. Bevitte a cellájába, és ott elrejtette.')
                    lebukas += 10
                    print(f'Most ki kellene választania {nev}-nek, hogy mikor szeretne kiszabadulni')
                    idopont = int(input('Írjon be 1-est ha, akkor amikor éppen nézik a rabok a TV-t és hangoskodnak, így senki sem fog rá figyelni és 2-est, ha egy este amikor már mindenki alszik. '))
                    if idopont == 1:
                        print('Így nehezen veszik észre, és nyugodtan tudja vágni a kerítést, mivel senki sem fogja hallani.')
                        print(f'{nev}-nek kell szereznie egy embert, aki majd a kijutása aután elviszi autóval.')
                        ki_jon_ertem = int(input('Döntse el, hogy ki jöjjön a szökevényért. Írjon be 1-est, ha testvére, és 2-est, ha a barátmője. '))
                        if ki_jon_ertem == 1:
                            print('Jól döntöttél, mivel ő már becsempészett egy csípőfogót, biztosan eljön érte!')
                        elif ki_jon_ertem == 2:
                            print('Vigyázz! Ne bízz teljesen a barátnődben, nehogy eláruljon.')
                    elif idopont == 2:
                        print('így csndesebben kell majd vágnia, de könnyebben szökik majd meg.')
                        print(f'{nev}-nek kell szereznie egy embert, aki majd a kijutása aután elviszi autóval.')
                        ki_jon_ertem2 = int(input('Döntse el, hogy ki jöjjön a szökevényért. Írjon be 1-est, ha testvére, és 2-est, ha a barátmője. '))
                        if ki_jon_ertem2 == 1:
                            print('Jól döntöttél, mivel ő már becsempészett egy csípőfogót, biztosan eljön érte!')
                        elif ki_jon_ertem2 == 2:
                            print('Vigyázz! Ne bízz teljesen a barátnődben, nehogy eláruljon.')


            elif megbeszeles2 == 2:
                print('Ez egy biztonságosabb mód, de lassabban ér oda az üzenet.')
                print(f'A {valasztott_ember} megpróbálja becsempészni {nev}-nek a csípőfogót.')

    elif elso == 2:
        print('Így sokkal kisebb a lebukási esély, de pénzt kell szereznie az elitéltnek!')
        penzkeresetimod = int(input('Hogyan szerezzen az elitélt pénzt? Írjon be 1-est ha menjen el dolgozni a börtönben, és 2-est, ha kezdjen el árulni valamit, amit más behozott neki. '))
