from vagas import vago
from kulcs import kulcsketto
from asas import aso

def fomenu(egeszseg, nev, energia, lebukas, penz):
    print(f'Játékos neve: {nev} ')
    print()
    print(f'Egészségi szinted: {egeszseg}')
    print(f'Energiaszinted: {energia} ')
    print(f'Pénzed: {penz} ')
    print(f'Lebukási esélyed: {lebukas}%')

def mellekmenu():
    print(f'Eszköztárad: ')
    # print(f'Szökésedhez ({}) szükséges eszközök: ')
    # print(f'Kivégézesig fentmaradó idő: {} nap')
    print('')
