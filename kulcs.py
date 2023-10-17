def kulcsketto(nev):
    print(f'A kulcsos szökési módot választottad {nev}-nek')
    print(f'{nev}-nek szüksége lesz kettő kulcsra, és az ahhoz szükséges anyagokra')
    print('')
    print(f'A raboknak minden nap 16:00-18:00-ig kell dolgozniuk a műhelyben, ilyenkor {nev}-nek lehetősége lehet arra, hogy bejusson a kovácsműhelybe, de vigyázz nehogy észre vegyék!')
    print('1 óra múlva...')
    print('A rabok elindulnak dolgozni')
    valaszelso = int(input(f'Szeretne {nev} elszökni a többiek közűl, és elmenni a kovácsműhelybe?, ha igen (1), ha nem (2)'))
    if valaszelso == 1:
        print(f'{nev} észrevétlenül kilép a tömegből, és elindul a műhely felé. A következő fél órát azzal tölti, hogy információkat szerezzen a műhelyről, de vigyáznod kell, nehogy feltűnjön valakinek, hogy nem vagy ott.')
        valaszketto = int(input(f'{nev} szeretne visszaindúlni?, ha igen (1), ha nem (2)'))
        if valaszketto == 1:
            print(f'Jól döntöttél, {nev} elindul vissza és sikeresen beleolvad a tömegbe')
        elif valaszketto == 2:
            print(f'Rosszúl döntöttél, valakinek feltűnik, hogy {nev} nincs ott')
            print('Megkérdezik tőled, hogy hol voltál, mit válaszolsz?')
            print('\t 1 - Eltévedett és nem talált vissza')
            print('\t 2 - Rájött a szapora')
            print('\t 3 - Elmondod az igazat')
            valaszharom = int(input('A választásod: '))
            if valaszharom == 1:
                print('Nagyon átlátszó, az őrök gyanút fognak, de elengednek, ezt most megúszta')
            elif valaszharom ==2:
                print('Megérhető, nem fognak gyanút, ezt most megúszta')            
            elif valaszharom == 3:
                print('Rossz válassz, büntetésből többet kell dolgoznia minden nap')
                print('Nem tudták meg az eredeti célod, de legközelebb jobban vigyázz')
    elif valaszelso ==2:
        print('Keményen végig dolgoztad a napot')
        print('Másnap...')