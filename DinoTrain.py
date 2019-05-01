mport pandas as pd

df = pd.read_excel('DinoDTB.xlsx')

dx = ['Apatosaurus', 1861, 266, 101, 0, 5, 'act1xb', 'act2xc']

"""
Van egy tombom, amiben tombok vannak
Dinok = [Dino1['Apatosaurus', 1861, 266, 101, 0, 5, 'act1xb', 'act2xc'], Dino2['Amargasaurus', 2002, 400, 103, 0, 5, 'act1xb', 'act2xc']]


"""
#print df.loc[df['Act1'] == "1x damage"]
"""
Hogy kellene kinezzen egy dino:
1. beolvasok egy teljes sort egy dx nevu listaba.  
a dx[0]=[dx[1], dx[2], dx[3]]
  

"""

"""
def fight(dino1, dino2)   Ez a harc
    x,y = checkspeed(dino1,dino2) -- csekkolom, hogy ki gyorsabb. ket visszateritesi ertek kellene, fast es slow
    attmeth(x)                    -- a gyorsabb tamad
    return winner
"""
