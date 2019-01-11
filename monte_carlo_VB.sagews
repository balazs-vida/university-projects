︠2a0b5a25-f914-4a11-9ff2-da366685c66ds︠
import random
import math
random.seed(0)

@interact
def pontok(n = slider(1000, 20000, step_size=1000)):
    koron_belul = 0
    koron_belul_list = []
    koron_kivul_list = []
    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if (x*x + y*y)**0.5 <= 1.0:
            koron_belul += 1
            koron_belul_list.append((x, y))
        else:
            koron_kivul_list.append((x, y))

    pi_kozelites = 4*(koron_belul/float(n))
    hiba = abs(pi_kozelites - math.pi)
    show("$\pi\simeq$", round(pi_kozelites, 5), ", hiba: ", round(hiba, 5))

    belso_pontok = list_plot(koron_belul_list, color='red')
    kulso_pontok = list_plot(koron_kivul_list, color='blue')
    t = var('t')
    kor = parametric_plot((cos(t), sin(t)), (t, 0, pi/2),  color='black')
    show(belso_pontok+kulso_pontok+kor)


︡f2900872-dac5-44c1-a21b-5592dbe6af85︡{"interact":{"controls":[{"animate":true,"control_type":"slider","default":0,"display_value":true,"label":"n","vals":["1000","2000","3000","4000","5000","6000","7000","8000","9000","10000","11000","12000","13000","14000","15000","16000","17000","18000","19000","20000"],"var":"n","width":null}],"flicker":false,"id":"3827ddb7-76d0-409b-9da3-c646e6afe4bc","layout":[[["n",12,null]],[["",12,null]]],"style":"None"}}︡{"done":true}︡









