def kulcsketto(nev):
    print(f'A kulcsos szökési módot választottad {nev}-nek')
    print(f'{nev}-nek szüksége lesz egy kulcsra, amihez szüksége van a következőkre: ')
    print('\t A kovács közelébe kell férkőzni, és megcsináltatni a kulcsot')
    print('\t Szüksége lesz a kulcshoz szükséges anyagokra')
    print('')
    print(f'A raboknak minden nap 16:00-18:00-ig kell dolgozniuk a műhelyben, ilyenkor {nev}-nek lehetősége lehet arra, hogy találkozzon a kováccsal, de vigyázz nehogy észre vegyék!')
    print('1 óra múlva...')
    print('A rabok elindulnak dolgozni')
    valaszelso = input(f'Szeretne {nev} elszökni a többiek közűl, és találkozni a kováccsal?, ha igen (1), ha nem (2)')
    if valaszelso == 1:
        print('aff')
    elif valaszelso ==2:
        print('aézhioéuz')