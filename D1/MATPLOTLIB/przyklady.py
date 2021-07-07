import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5, 5, 5)
y = np.ones_like(x)


def ustawianie_osi(fig, ax, tytul, ymax):
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_ylim(0, ymax+1)
    ax.set_title(tytul)


fig, axes = plt.subplots(1, 4, figsize=(16, 3))
# Grubości linii
linewidths = [0.5, 1.0, 2.0, 4.0]
for n, linewidth in enumerate(linewidths):
    axes[0].plot(x, y+n, color="blue", linewidth=linewidth)
ustawianie_osi(fig, axes[0], "Grubość linii", len(linewidths))

# Style linii
style_linii = ['-', '-.', ':', '--']
for n, linestyle in enumerate(style_linii):
    axes[1].plot(x, y+n, color="green", lw=2, linestyle=linestyle)
ustawianie_osi(fig, axes[1], "Style linii", len(style_linii))

# Markery
markery = ['+', 'o', '*', 's', '.', '1', '2', '3', '4']
for n, marker in enumerate(markery):
    axes[2].plot(x, y+n, color="grey", lw=2, ls=' ', marker=marker)
ustawianie_osi(fig, axes[2], "Rodzaje markerów", len(markery))

# Rozmiary markerów i kolory
rozmiar_markerow = [(4, 'white'), (8, 'red'),
                    (12, 'yellow'), (16, 'lightgreen')]
for n, (markersize, markerfacecolor) in enumerate(rozmiar_markerow):
    axes[3].plot(x, y+n, color='blue', lw=1, ls='-', marker='o',
                 markersize=markersize, markerfacecolor=markerfacecolor, markeredgewidth=2)
ustawianie_osi(fig, axes[3], "Kolory i rozmiar markerów",
               len(rozmiar_markerow))


plt.show()
