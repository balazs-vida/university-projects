import random
#random.seed(109)

LEPESSZAM = 1000

pontok_list = [[0,0]]
vektorok = [[1,0], [0,1], [0,-1], [-1,0], [0,0]]
vonalak_list = []
tavolsagok_dict = {}

for i in range(1, LEPESSZAM+1):
    vek = vektorok[random.randint(0,4)]
    uj_pont = [pontok_list[i-1][j] + vek[j] for j in range(2)]
    pontok_list.append(uj_pont)
    tavolsagok_dict[i] = sum((uj_pont[j])^2 for j in range(2))^0.5
    A = pontok_list[i-1][0]
    B = pontok_list[i-1][1]
    C = pontok_list[i][0]
    D = pontok_list[i][1]
    vonalak_list.append(line([(A,B), (C,D)], color='brown'))

#pontok_list
#tavolsagok_dict.values()

origoban = pontok_list.count([0,0])
print "origoban ennyiszer: ", origoban

legtobbszor_itt = max(pontok_list, key=pontok_list.count)
print "legtobbszor itt: ", legtobbszor_itt
legtobbszor_ennyiszer = pontok_list.count(legtobbszor_itt)
print "legtobbszor ennyiszer: ", legtobbszor_ennyiszer

max_tav = max(tavolsagok_dict.values())
max_tav_index = max(tavolsagok_dict, key=lambda key: tavolsagok_dict[key])
max_tav_pont = pontok_list[max_tav_index]

print "legtavolabbi pont: ", max_tav_pont
print "ennek tavolsaga az origotol: ", max_tav

sum(vonalak_list)
