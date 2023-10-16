from vagas import vagas
from kulcs import kulcs
from asas import asas

def main():
    print('Üdvözöllek a játékban! Folyamatos választási lehetőségek, és adott esetben kihívások is lesznek a játék során. A játékban láthatjuk a szökevényünk egészségi szintjét, a pénzt, kivégzésig fennmaradó idő, lebukási esély százalékban és az Energia szintünket is láthatjuk. Sok esetben a játékosnak kell megadnia a kért információkat.')
    nev = input('Adja meg a szökevény nevét: ')
    print(f'Cél: {nev}-et kiszöktetni a börtönből')
    print(f'Jelenleg {nev} egy börtöncellában fekszik az ágyán és azon gondolkozik, hogy hogyan tudna kiszabadúlni a börtönből')
    print('Három ötlete van: ')
    print('\t 1 - Csinálni álkulcsokat és kinyitni az ajtókat')
    print('\t 2 - Szerezni egy vágóeszközt és kivágni a kerítést')
    print('\t 3 - Szerezni egy ásót és kiásni magát')
    valasz = input('A szökési mód kiválasztása: ')
    print('abuggéa')
    if valasz == 1:
        kulcs()
    elif valasz == 2:
        vagas()
    elif valasz == 3:
        asas()
main()