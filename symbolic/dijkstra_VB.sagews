INFTY = 1000000000

def dijkstra(G, s):
    """
    Legrövidebb utak az s kezdőcsúcsból a G gráf minden pontjába Dijkstra algoritmusával
    Hivatkozás:
    D. Joyner, M. Van Nguyen, D. Phillips: Algorithmic Graph Theory and Sage

    args:
        G: egyszerű, összefuggő, nemnegatív élsúlyú gráf, éllistás ábrázolással
        s: kezdőcsúcs

    returns:
        D (list): távolságok listája, ahol D[v] a legrövidebb sv-út tavolsága
        P (dict): szülőcsúcsok, ahol P[v] a v csúcs szülője
    """
    n = G.order()  # csúcsok száma
    m = G.size()   # élek száma
    D = [INFTY for _ in range(n)] # D inic.
    D[s] = 0
    P = {}
    Q = set(G.vertices())
    while len(Q) > 0:
        v = min_tav(D, Q)
        Q.remove(v)
        print "prioritasos sor tartalma a", v, "csucs kivalasztasa utan: ", Q

        if G.is_directed():
            Adj = set(G.neighbors_out(v))
        else:
            Adj = set(G.neighbors(v))

        for u in Adj.intersection(Q):
            if D[u] > D[v] + G.edge_label(v, u):
                D[u] = D[v] + G.edge_label(v, u)
                P[u] = v
    G.show(edge_colors={'red':[(P.values()[i], P.keys()[i]) for i in range(len(P))]}, edge_labels = True)
    return D, P

def min_tav(D, Q):
    """
    Kiválasztjuk Q-ból legrövidebb távolságra lévő csúcsot.

    args:
        D: a fenti távolágok listája
        Q: prioritásos sor a megvizsgálandó csúcsokkal

    returns:
        v: a legkisebb távolságra lévő csúcs
    """
    v = None
    low = INFTY
    for u in Q:
        if D[u] < low:
            v = u
            low = D[v]
    return v


# Példa1: élsúlyozott digráf
G = DiGraph({0: {1:2, 3:10},
             1: {2:10, 3:12, 4:10},
             2: {4:1}}, weighted=True)
G.show(edge_labels = True)
D, P = dijkstra(G, 0)
print "D távolságok: ", D
print "P szülőcsúcsok: ", P

# Példa2: élsúlyozott, irányítás nélküli gráf
G = Graph({0: {1:4, 2:8, 4:7},
           1: {0:4, 2:8, 3:5, 5:4, 6:3},
           2: {0:8, 1:8, 6:3},
           3: {1:5, 5:3},
           4: {0:7},
           5: {1:4, 3:3, 6:9},
           6: {1:3, 2:3, 5:9}}, weighted=True)
G.show(edge_labels = True)
D, P = dijkstra(G, 5)
print "D távolságok: ", D
print "P szülőcsúcsok: ", P
