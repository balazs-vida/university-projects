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
