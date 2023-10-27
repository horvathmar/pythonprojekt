from vagas import vago
from kulcs import kulcsketto
from asas import aso
from menu import fomenu

def main() -> str:
    
    # fomenu(egeszseg, nev, energia, lebukas, penz)
    egeszseg = 0
    energia = 0
    penz = 0
    lebukas = 0
    print('\n')
    print('Üdvözöllek a játékban! Folyamatos választási lehetőségek, és adott esetben kihívások is lesznek a játék során. A játékban láthatjuk a szökevényünk egészségi szintjét, a pénzt, kivégzésig fennmaradó időt, lebukási esélyt százalékban és az Energia szintünket is láthatjuk. Sok esetben a játékosnak kell megadnia a kért információkat.')
    nev = input('Adja meg a szökevény nevét: ')
    print(f'Cél: {nev}-t kiszöktetni a börtönből')
    print('\n')
    print(f'Jelenleg "{nev}" egy börtöncellában fekszik az ágyán és azon gondolkozik, hogy hogyan tudna kiszabadúlni a börtönből')
    print('Három ötlete van: ')
    print('\t 1 - Csinálni álkulcsokat és kinyitni az ajtókat')
    print('\t 2 - Szerezni egy vágóeszközt és kivágni a kerítést')
    print('\t 3 - Szerezni egy ásót és kiásni magát')
    valasz = int(input('Melyik szökési módot választod: '))
    if valasz == 1:
        kulcsketto(nev, egeszseg, energia, lebukas, penz)
    elif valasz == 2:
        vago(nev, egeszseg, energia, lebukas, penz)
    elif valasz == 3:
        aso(nev, egeszseg, energia, lebukas, penz,)
        
main()