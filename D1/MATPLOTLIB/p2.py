import matplotlib.pyplot as plt

godziny = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
           13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
temperatury = [1, 4, 9, 22, 43, 41, 32, 31, 30, 25, 23,
               22, 21, 19, 18, 17, 19, 21, 23, 30, 31, 33, 35, 37]
fig, ax = plt.subplots()
ax.plot(godziny, temperatury, linewidth=3)
ax.set_title("Mój wykres zmian temperatur")
ax.set_xlabel("godziny", fontsize=12)
ax.set_ylabel("temperatura [\u00B0C]", fontsize=12)
ax.tick_params(axis='y', labelsize=8)
plt.show()
