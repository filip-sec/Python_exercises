import networkx as nx
import matplotlib.pyplot as plt

# Vytvoríme prázdny graf
G = nx.DiGraph()

# Pridáme hrany a uzly
G.add_node("príklonové stratégie")
G.add_node("zameranie na problém")
G.add_node("riešenie problému")
G.add_node("kognitívna reštrukturalizácia")
G.add_node("zameranie na emócie")
G.add_node("vyjadrenie emócií")
G.add_node("sociálna opora")
G.add_node("vyhýbanie sa problému")
G.add_node("fantazijný únik")
G.add_node("sociálna izolácia")
G.add_node("sebaobviňovanie")

G.add_edges_from([
    ("príklonové stratégie", "zameranie na problém"),
    ("príklonové stratégie", "zameranie na emócie"),
    ("zameranie na problém", "riešenie problému"),
    ("zameranie na problém", "vyhýbanie sa problému"),
    ("zameranie na emócie", "vyjadrenie emócií"),
    ("zameranie na emócie", "sociálna opora"),
    ("vyhýbanie sa problému", "fantazijný únik"),
    ("sociálna opora", "kognitívna reštrukturalizácia"),
    ("sociálna izolácia", "sebaobviňovanie")
])

# Nakreslíme graf s obdĺžnikovými uzlami
pos = {
    "príklonové stratégie": (0, 5),
    "zameranie na problém": (-1, 4),
    "riešenie problému": (-2, 3),
    "kognitívna reštrukturalizácia": (-3, 2),
    "zameranie na emócie": (1, 4),
    "vyjadrenie emócií": (2, 3),
    "sociálna opora": (1, 2),
    "vyhýbanie sa problému": (3, 4),
    "fantazijný únik": (4, 3),
    "sociálna izolácia": (3, 2),
    "sebaobviňovanie": (3, 1)
}

# Nakreslíme uzly ako obdĺžniky
nx.draw(G, pos, with_labels=True, node_shape='s', node_size=2000, node_color="skyblue", font_size=10, font_weight="bold", arrowsize=20)
plt.show()
