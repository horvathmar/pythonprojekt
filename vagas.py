def vago(nev):
    print(f'A vágásos szökési módot választottad {nev}-nek')
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
            elif megbeszeles == 2:
                print('Ez egy biztonságosabb mód, de lassabban ér oda az üzenet.')
        elif valasztott_ember == 2:
            print(f'{nev}-nek reménykednie kell, hogy a barátja, akiben ő bízik nem adja fel a rendőröknek.') 
            print(f'Szerencéje van, mivel a barátja nem adja fel, és benne van hogy segít {nev}-nek.')
            megbeszeles2 = int(input('Válaszd ki, hogy hol kérje meg a tesvérét, 1-est ha telefonon és 2-est, ha levélben.'))
            if megbeszeles2 == 1:
                print('Reménykedniük kell, hogy ne hallgassák le a telefont.')
            elif megbeszeles2 == 2:
                print('Ez egy biztonságosabb mód, de lassabban ér oda az üzenet.')

    elif elso == 2:
        print('Így sokkal kisebb a lebukási esély, de pénzt kell szereznie az elitéltnek!')
        penzkeresetimod = int(input('Hogyan szerezzen az elitélt pénzt? Írjon be 1-est ha menjen el dolgozni a börtönben, és 2-est, ha kezdjen el árulni valamit, amit más behozott neki. '))
