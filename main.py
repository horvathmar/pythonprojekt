from asas import introduction, valasztott_1, valasztott_2
from stats import egeszseg, energia, lebukas, penz
from vagas import vago
from kulcs import kulcsketto


def main():
    print('Üdvözöllek a játékban! Folyamatos választási lehetőségek, és adott esetben kihívások is lesznek a játék során. A játékban láthatjuk a szökevényünk egészségi szintjét, a pénzt, kivégzésig fennmaradó időt, lebukási esélyt százalékban és az Energia szintünket is láthatjuk. Sok esetben a játékosnak kell megadnia a kért információkat.')
    nev = input('Adja meg a szökevény nevét: ')
    print(f'Cél: {nev}-t kiszöktetni a börtönből')
    print('\n')
    print(f'Jelenleg "{nev}" egy börtöncellában fekszik az ágyán és azon gondolkozik, hogy hogyan tudna kiszabadulni a börtönből')
    print('Három ötlete van: ')
    print('\t 1 - Csinálni álkulcsot és kinyitni az ajtókat')
    print('\t 2 - Szerezni egy vágóeszközt és kivágni a kerítést')
    print('\t 3 - Szerezni egy ásót és kiásni magát')
    valasz = int(input('Melyik szökési módot választod: '))
    if valasz == 1:
        kulcsketto(nev)
    elif valasz == 2:
        vago(nev)
    elif valasz == 3:
        introduction(nev, valasztott_1, valasztott_2)

main()
