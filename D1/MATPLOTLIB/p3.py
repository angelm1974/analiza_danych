import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7]
y1 = [2, 4, 6, 8, 10, 12, 14]
y2 = [0.5, 1, 1.5, 2.0, 2.5, 3.0, 3.5]

plt.style.use('bmh')
fig, ax = plt.subplots()

ax.text(6, 5.1, "Etykieta testowa", fontsize=14, family='serif')
ax.plot(x, y1, x, y2, linewidth=3,)
ax.annotate("Adnotacja",family='serif',fontsize=12,xy=(2,4),xycoords='data',
            xytext=(+20,+50), textcoords='offset points',
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.5'))

ax.legend(bbox_to_anchor=(0, 1), loc=3, borderaxespad=0.0,
          labels=('Prosta1', 'Prosta2'), ncol=2)

plt.show()
