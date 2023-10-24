def aso(nev, egeszseg, energia, lebukas, penz):
    print(f'A kiásást választottad szökési módul {nev}-nek')
    print('\n')
    print(f'Az első lépés ahhoz, hogy kiásd magad az, hogy {nev} megszerezzem egy ásót és egy posztert, amivel kiáshatja magát, majd minden nap végén eltakarhatja a haladását a poszterrel')
    valasz_egy = int(input('2 Lehetőséged van: 1 - Lopás a raktárból, 2 - Kézi ásó Készítése'))
    if valasz_egy == 1:
        print(f'{nev}-nek ügyenie kell az őrökre, mivel, ha észreveszik, vagy megtalálják nála az eszközöket, vége a játéknak!')
        valasztott = int(input('Válaszd ki az egyik lehetőséget'))
        print('')
        if valasztott == 1:
            print('A raktárból fogja lopni a dolgokat, jó választás, ámde nagy kockázattal jár majd.')
            terv = int(input('Válaszd ki, hogy mikor próbáljon bejutni oda, 1 - Nappal, 2 - Éjjel'))
            if valasztott == 1:
                print('Az ajtóknál őrök vannak készenlétben, visszafordulsz')
                print('1 - igen, 2 - nem')
                orok = int(input('Mit teszel: '))
                if orok == 1:
                    print('Visszafordultál')