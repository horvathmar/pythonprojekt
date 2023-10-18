def aso(nev):
    print(f'A kiásást választottad szökési módul {nev}-nek')
    print(f'Az első lépés ahhoz, hogy kiásd magad az, hogy {nev} megszerezzem egy ásót és egy posztert, amivel kiáshatja magát, majd minden nap végén eltakarhatja a haladását a poszterrel')
    valasz_egy = int(input('3 Lehetőséged van: 1 - Lopás a raktárból, 2 - Kézi ásó Készítése, 3 - Egy külsős ember lefizetése'))
    if valasz_egy == 1:
        print(f'{nev}-nek ügyenie kell az őrökre, mivel, ha észreveszik, vagy megtalálják nála az eszközöket, vége a játéknak!')
        valasztott = int(input('Válaszd ki az egyik lehetőséget'))
        print('')
        if valasztott == 1:
            print('A raktárból fogja lopni a dolgokat, jó választás, ámde nagy kockázattal jár majd.')
            terv = int(input('Válaszd ki, hogy mikor próbáljon bejutni oda, 1 - Nappal, 2 - Éjjel'))
            if valasztott == 1:
                print('Éjszaka kevesebben vannak, viszont a kamerákon van éjjellátó mód is.')
                print('Az ajtóknál őrök vannak készenlétben, de nagyobb az esélyed, viszont másnap fáradtabb leszel az akció miatt +1 nap')
            elif valasztott == 2:
                print('Nappal könnyebben navigálhatsz és vegyülhetsz bele a tömegbe, de ha valaki látja hogy belógsz az ajtónál, beköphetnek.')
                print(f'Kisebb eséllyel állsz neki a küldetéshez, de már aznap el tudod kezdeni, így nem 
                veszítesz semmi időt')
